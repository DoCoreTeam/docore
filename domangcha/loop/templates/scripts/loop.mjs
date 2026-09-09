#!/usr/bin/env node
// DOMANGCHA v3.0.0  scripts/loop.mjs
// 프로젝트 자율개발 루프의 기록 CLI 겸 훅 핸들러 (Claude Code, Cursor 공용)
// 이 파일은 npx domangcha 가 프로젝트에 설치하며 재설치 때마다 최신본으로 갱신됨
// 요구 사항: Node 22.13 이상 (node:sqlite 내장, 추가 npm 의존성 없음)
// 사용법: node scripts/loop.mjs <명령> [옵션]   (명령 목록은 하단 usage 참조)

process.removeAllListeners('warning');
process.on('warning', (w) => { if (w.name !== 'ExperimentalWarning') console.error(w.message); });

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { execSync } from 'node:child_process';

let DatabaseSync;
try { ({ DatabaseSync } = await import('node:sqlite')); }
catch { console.error('[DOMANGCHA] node:sqlite unavailable / 사용 불가 — Node 22.13+ required'); process.exit(1); }

const KIT_VERSION = "3.0.0";

// ---------- 경로 ----------
function findRoot(start) {
  let dir = start;
  for (let i = 0; i < 12; i++) {
    if (fs.existsSync(path.join(dir, '.loop'))) return dir;
    if (fs.existsSync(path.join(dir, '.git')) || fs.existsSync(path.join(dir, 'package.json'))) return dir;
    const up = path.dirname(dir);
    if (up === dir) break;
    dir = up;
  }
  return start;
}
const ROOT = process.env.LOOP_ROOT || process.env.CLAUDE_PROJECT_DIR || findRoot(process.cwd());
const LOOP_DIR = path.join(ROOT, '.loop');
const DB_PATH = path.join(LOOP_DIR, 'loop.db');
const PLAN_PATH = path.join(LOOP_DIR, 'PLAN.md');
const TEMPLATE_PATH = path.join(LOOP_DIR, 'PLAN.template.md');
const ARCHIVE_DIR = path.join(LOOP_DIR, 'archive');
const POLICY_PATH = path.join(LOOP_DIR, 'POLICY.md');
const REGISTRY_PATH = path.join(os.homedir(), '.loop', 'registry.json');

// ---------- 유틸 ----------
const now = () => new Date().toISOString();
const today = () => now().slice(0, 10);
const sha = (s) => crypto.createHash('sha256').update(s).digest('hex').slice(0, 16);
const pad = (n) => String(n).padStart(4, '0');
const readStdin = () => { try { return fs.readFileSync(0, 'utf8'); } catch { return ''; } };
const readJsonStdin = () => { try { return JSON.parse(readStdin() || '{}'); } catch { return {}; } };
process.stdout.on('error', (e) => { if (e && e.code === 'EPIPE') process.exit(0); });
const out = (s) => process.stdout.write(s + '\n');
const die = (s) => { console.error('[DOMANGCHA] ' + s); process.exit(1); };

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next !== undefined && !next.startsWith('--')) { args[key] = next; i++; } else args[key] = true;
    } else args._.push(a);
  }
  return args;
}

function sh(cmd, opts = {}) {
  return execSync(cmd, { cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'], encoding: 'utf8', ...opts }).trim();
}
function gitAvailable() { try { sh('git rev-parse --is-inside-work-tree'); return true; } catch { return false; } }
function gitCommit(message) {
  if (!gitAvailable()) return { skipped: L('git 저장소 아님', 'not a git repository') };
  try {
    sh('git add -A');
    const status = sh('git status --porcelain');
    if (!status) return { skipped: L('변경 없음', 'no changes') };
    sh(`git commit -q -m ${JSON.stringify(message)}`);
    return { hash: sh('git rev-parse --short HEAD') };
  } catch (e) { return { skipped: L('커밋 실패 ', 'commit failed ') + String(e.message || e).split('\n')[0] }; }
}
function gitTag(tag) {
  if (!gitAvailable()) return false;
  try { sh(`git tag ${JSON.stringify(tag)}`); return true; } catch { return false; }
}
function changedFiles() {
  if (!gitAvailable()) return [];
  try { return sh('git status --porcelain').split('\n').filter(Boolean).map((l) => l.slice(3).trim()); } catch { return []; }
}

// ---------- DB ----------
const SCHEMA = `
CREATE TABLE IF NOT EXISTS settings (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS instructions (
  id TEXT PRIMARY KEY,
  content TEXT NOT NULL,
  source TEXT NOT NULL,
  session_id TEXT,
  plan_id TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS interventions (
  id TEXT PRIMARY KEY,
  content TEXT NOT NULL,
  source TEXT NOT NULL,
  session_id TEXT,
  plan_id TEXT,
  plan_version TEXT,
  item_id TEXT,
  effect TEXT,
  resulting_plan_version TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS implementations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  plan_id TEXT NOT NULL,
  plan_version TEXT NOT NULL,
  item_id TEXT NOT NULL,
  attempt INTEGER NOT NULL,
  summary TEXT,
  files TEXT,
  audit_result TEXT NOT NULL,
  audit_notes TEXT,
  commit_hash TEXT,
  started_at TEXT NOT NULL,
  finished_at TEXT
);
CREATE TABLE IF NOT EXISTS file_changes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  plan_id TEXT,
  item_id TEXT,
  tool TEXT,
  file_path TEXT NOT NULL,
  session_id TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS plan_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  plan_id TEXT NOT NULL,
  version TEXT NOT NULL,
  status TEXT,
  content TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  trigger TEXT NOT NULL,
  trigger_ref TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  kind TEXT NOT NULL,
  detail TEXT,
  plan_id TEXT,
  plan_version TEXT,
  session_id TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS policies (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  rule TEXT NOT NULL,
  origin TEXT,
  status TEXT NOT NULL,
  created_at TEXT NOT NULL,
  retired_at TEXT,
  retired_reason TEXT
);
CREATE TABLE IF NOT EXISTS policy_hits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  policy_id TEXT NOT NULL,
  plan_id TEXT,
  plan_version TEXT,
  item_id TEXT,
  note TEXT,
  created_at TEXT NOT NULL
);
`;

// ---------- 언어 / language ----------
// 파일 어휘는 두 언어를 모두 파싱하고, 기록할 때만 현재 언어로 쓴다.
// The file vocabulary parses both languages and writes only in the current one.
const LANGS = ['ko', 'en'];
let _lang;
function lang() {
  if (_lang) return _lang;
  try { _lang = getSetting('lang') === 'en' ? 'en' : 'ko'; } catch { _lang = 'ko'; }
  return _lang;
}
const EN = () => lang() === 'en';
const L = (ko, en) => (EN() ? en : ko);

const FIELD = {
  planId: ['플랜 ID', 'Plan ID'],
  planVersion: ['플랜 버전', 'Plan version'],
  written: ['작성', 'Written'],
  startCommit: ['시작 커밋', 'Start commit'],
  status: ['상태', 'Status'],
  instruction: ['지시', 'Instruction'],
  target: ['목표 버전', 'Target version'],
  mode: ['모드', 'Mode'],
  scope: ['범위', 'Scope'],
  criteria: ['감사 기준', 'Audit criteria'],
  depends: ['의존', 'Depends'],
};
const ITEM_STATUS = {
  pending: ['대기', 'pending'],
  active: ['진행중', 'active'],
  passed: ['통과', 'passed'],
  held: ['held', 'held'],
  cancelled: ['취소', 'cancelled'],
};
ITEM_STATUS.held = ['보류', 'held'];
const PLAN_STATUS = {
  draft: ['초안', 'draft'],
  active: ['진행중', 'active'],
  done: ['완료', 'done'],
  aborted: ['중단', 'aborted'],
};
const MODE = { light: ['경량', 'light'], heavy: ['중량', 'heavy'] };
const SECTION = { items: ['## 항목', '## Items'], history: ['## 변경 이력', '## History'] };
// 두 언어판 문서를 모두 열 수 있어야 하므로 섹션은 양쪽을 다 찾는다.
// Both language editions must open, so section lookup tries either spelling.
function sectionIndex(text, name, last) {
  for (const marker of SECTION[name]) {
    const i = last ? text.lastIndexOf(marker) : text.indexOf('\n' + marker);
    if (i >= 0) return i;
  }
  return -1;
}
const SEC = (name) => SECTION[name][EN() ? 1 : 0];
const NONE = ['없음', 'none'];
const isNone = (v) => NONE.includes(String(v || '').trim().toLowerCase()) || NONE.includes(String(v || '').trim());

const W = (table, key) => table[key][EN() ? 1 : 0];
const F = (name) => FIELD[name][EN() ? 1 : 0];
const FRE = (name) => '(?:' + FIELD[name].join('|') + ')';
function keyOf(table, word, fallback) {
  const w = String(word || '').trim();
  for (const k of Object.keys(table)) if (table[k].includes(w)) return k;
  return fallback;
}

const DEFAULT_SETTINGS = {
  project_name: path.basename(ROOT),
  plan_confirm: 'true',
  auto_commit: 'true',
  auto_tag: 'true',
  bump_package_version: 'true',
  checkpoint_every: '3',
  max_audit_retries: '3',
  max_plan_revisions_per_item: '3',
  policy_promote_after: '2',
  policy_rewrite_after: '3',
  lang: 'ko',
  heavy_doc: '.claude/heavy/CEO.md',
  cmd_typecheck: 'pnpm tsc --noEmit',
  cmd_lint: 'pnpm lint',
  cmd_test: 'pnpm test',
  cmd_build: 'pnpm build',
};

let _db;
function db(create = false) {
  if (_db) return _db;
  if (!fs.existsSync(DB_PATH)) {
    if (!create) die(L('.loop/loop.db 없음, 먼저 node scripts/loop.mjs init 실행', '.loop/loop.db is missing; run node scripts/loop.mjs init first'));
    fs.mkdirSync(LOOP_DIR, { recursive: true });
  }
  _db = new DatabaseSync(DB_PATH);
  _db.exec('PRAGMA journal_mode = WAL;');
  _db.exec(SCHEMA);
  return _db;
}
const q = (sql, ...p) => db().prepare(sql).all(...p);
const q1 = (sql, ...p) => db().prepare(sql).get(...p);
const run = (sql, ...p) => db().prepare(sql).run(...p);

function getSetting(key) { const r = q1('SELECT value FROM settings WHERE key = ?', key); return r ? r.value : DEFAULT_SETTINGS[key]; }
function setSetting(key, value) {
  run('INSERT INTO settings(key, value, updated_at) VALUES (?, ?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at', key, String(value), now());
}
const flag = (key) => String(getSetting(key)) === 'true';
const num = (key) => Number(getSetting(key));

function nextId(table, prefix) {
  const r = q1(`SELECT COUNT(*) AS c FROM ${table}`);
  return `${prefix}_${pad(r.c + 1)}`;
}
function addEvent(kind, detail, sessionId) {
  const p = readPlan(false);
  run('INSERT INTO events(kind, detail, plan_id, plan_version, session_id, created_at) VALUES (?,?,?,?,?,?)',
    kind, detail || null, p ? p.header.id : null, p ? p.header.version : null, sessionId || null, now());
}

// ---------- 플랜 파일 ----------
const TEMPLATE_KO = `# PLAN {{project}}: {{title}}
플랜 ID: {{plan_id}}
플랜 버전: v0.1.0
상태: 초안
지시: {{instruction}}
목표 버전: {{target}}
작성: {{date}}

## 목표
- (이 플랜이 끝났을 때 사용자가 얻는 것 1~3줄)

## 범위 밖
- (이번에 하지 않는 것, 없으면 "없음")

## 완료 정의
- {{cmd_typecheck}}, {{cmd_test}}, {{cmd_build}} 통과
- 사용자 노출 문자열은 전부 i18n 키 사용
- 설정값은 env 추가 없이 DB 저장 + UI 관리 (해당 시)

## 참조
- (이 플랜 전체가 따라야 할 문서, UI 항목은 디자인 시스템 INDEX 경로 명시)

## 항목

### I01 (항목 제목)
상태: 대기
모드: 경량
범위: (변경 파일 또는 디렉터리, 신규 파일은 "신규" 표기)
감사 기준:
- (명령과 기대 결과, 예: pnpm test profile 통과)
- (관측 가능한 조건, 예: GET /api/profile 미인증 401)
의존: 없음

## 종합 감사
- (전 항목 통과 후 기록)

## 변경 이력
- v0.1.0 ({{date}}) 최초 작성 ({{instruction}})
`;

const TEMPLATE_EN = `# PLAN {{project}}: {{title}}
Plan ID: {{plan_id}}
Plan version: v0.1.0
Status: draft
Instruction: {{instruction}}
Target version: {{target}}
Written: {{date}}

## Goal
- (what the user gets when this plan is done, 1-3 lines)

## Out of scope
- (what this plan does not do, or "none")

## Definition of done
- {{cmd_typecheck}}, {{cmd_test}}, {{cmd_build}} pass
- every user-facing string goes through an i18n key
- settings live in the database with UI management, not in new env vars (where applicable)

## References
- (documents this whole plan must follow; for UI items name the design system INDEX path)

## Items

### I01 (item title)
Status: pending
Mode: light
Scope: (files or directories to change; mark new files "new")
Audit criteria:
- (a command and its expected result, e.g. pnpm test profile passes)
- (an observable condition, e.g. GET /api/profile returns 401 when unauthenticated)
Depends: none

## Final audit
- (recorded after every item passes)

## History
- v0.1.0 ({{date}}) first written ({{instruction}})
`;

const DEFAULT_TEMPLATE = () => (EN() ? TEMPLATE_EN : TEMPLATE_KO);

// 언어를 바꿀 때, 손대지 않은 기본 템플릿만 새 언어판으로 교체한다.
// Switching language replaces the plan template only while it is still the untouched default.
function retemplate() {
  if (!fs.existsSync(TEMPLATE_PATH)) return '';
  const current = fs.readFileSync(TEMPLATE_PATH, 'utf8');
  if (current === DEFAULT_TEMPLATE()) return '';
  if (current !== TEMPLATE_KO && current !== TEMPLATE_EN) {
    return L(', PLAN.template.md 는 수정본이라 그대로 둠', ', PLAN.template.md is customised and was left alone');
  }
  fs.writeFileSync(TEMPLATE_PATH, DEFAULT_TEMPLATE());
  return L(', PLAN.template.md 교체', ', PLAN.template.md replaced');
}

function readPlanText() { return fs.existsSync(PLAN_PATH) ? fs.readFileSync(PLAN_PATH, 'utf8') : null; }

function parsePlan(text) {
  const itemsStart = sectionIndex(text, 'items');
  const head = itemsStart >= 0 ? text.slice(0, itemsStart) : text;
  const hget = (name) => { const m = head.match(new RegExp('^' + FRE(name) + ':\\s*(.+)$', 'm')); return m ? m[1].trim() : null; };
  const titleLine = text.split('\n').find((l) => l.startsWith('# ')) || '';
  const header = {
    title: titleLine.replace(/^# PLAN\s*[^:]*:\s*/, '').replace(/^# /, '').trim(),
    id: hget('planId'),
    version: hget('planVersion'),
    status: hget('status'),
    instruction: hget('instruction'),
    target: hget('target'),
  };
  const items = [];
  const re = /^### (I\d+[a-z]*)\s+(.*)$/gm;
  const idx = [];
  let m;
  while ((m = re.exec(text))) idx.push({ id: m[1], title: m[2].trim(), start: m.index });
  for (let i = 0; i < idx.length; i++) {
    const nextH2 = text.indexOf('\n## ', idx[i].start + 1);
    let end = i + 1 < idx.length ? idx[i + 1].start : text.length;
    if (nextH2 >= 0 && nextH2 < end) end = nextH2 + 1;
    const block = text.slice(idx[i].start, end);
    const st = block.match(new RegExp('^' + FRE('status') + ':\\s*(.+)$', 'm'));
    const mode = block.match(new RegExp('^' + FRE('mode') + ':\\s*(.+)$', 'm'));
    items.push({ ...idx[i], end, block: block.trimEnd(), status: st ? st[1].trim() : W(ITEM_STATUS, 'pending'), mode: mode ? mode[1].trim() : W(MODE, 'light') });
  }
  return { header, items, text };
}
function readPlan(required = true) {
  const t = readPlanText();
  if (!t) { if (required) die(L('.loop/PLAN.md 없음, 먼저 plan new 실행', '.loop/PLAN.md is missing; run plan new first')); return null; }
  return parsePlan(t);
}
function planStatusKey(s) { return keyOf(PLAN_STATUS, String(s || '').split(' ')[0], null); }
function planActive(p) { return p && p.header.status && !['done', 'aborted'].includes(planStatusKey(p.header.status)); }
function statusKey(s) { return keyOf(ITEM_STATUS, String(s || '').split(' ')[0], 'pending'); }
function modeKey(m) { return keyOf(MODE, m, 'light'); }
function counts(p) {
  const c = { pending: 0, active: 0, passed: 0, held: 0, cancelled: 0 };
  for (const it of p.items) { const k = statusKey(it.status); c[k] = (c[k] || 0) + 1; }
  return c;
}
function nextItem(p) {
  return p.items.find((it) => statusKey(it.status) === 'active') || p.items.find((it) => statusKey(it.status) === 'pending') || null;
}
function writePlan(text) { fs.writeFileSync(PLAN_PATH, text); }

function setItemStatus(p, id, status) {
  const it = p.items.find((x) => x.id === id);
  if (!it) die(L(`항목 ${id} 없음`, `item ${id} does not exist`));
  const before = p.text.slice(0, it.start);
  let block = p.text.slice(it.start, it.end);
  const after = p.text.slice(it.end);
  const stRe = new RegExp('^' + FRE('status') + ':.*$', 'm');
  const line = `${F('status')}: ${status}`;
  if (stRe.test(block)) block = block.replace(stRe, line);
  else block = block.replace(/^(### .*)$/m, `$1\n${line}`);
  writePlan(before + block + after);
}
function setPlanStatus(p, status) {
  const itemsStart = sectionIndex(p.text, 'items');
  const head = itemsStart >= 0 ? p.text.slice(0, itemsStart) : p.text;
  const rest = itemsStart >= 0 ? p.text.slice(itemsStart) : '';
  writePlan(head.replace(new RegExp('^' + FRE('status') + ':.*$', 'm'), `${F('status')}: ${status}`) + rest);
}
function bumpVersion(v, level) {
  const m = /^v(\d+)\.(\d+)\.(\d+)$/.exec(v || 'v0.1.0');
  let [maj, min, pat] = m ? [Number(m[1]), Number(m[2]), Number(m[3])] : [0, 1, 0];
  if (level === 'major') { maj++; min = 0; pat = 0; } else if (level === 'minor') { min++; pat = 0; } else pat++;
  return `v${maj}.${min}.${pat}`;
}
function snapshot(trigger, ref) {
  const p = readPlan(false);
  if (!p) return null;
  const hash = sha(p.text);
  const last = q1('SELECT content_hash FROM plan_versions WHERE plan_id = ? ORDER BY id DESC LIMIT 1', p.header.id || '');
  if (last && last.content_hash === hash) return { skipped: true, version: p.header.version };
  run('INSERT INTO plan_versions(plan_id, version, status, content, content_hash, trigger, trigger_ref, created_at) VALUES (?,?,?,?,?,?,?,?)',
    p.header.id || '', p.header.version || '', p.header.status || '', p.text, hash, trigger, ref || null, now());
  return { skipped: false, version: p.header.version };
}
function currentItem() { return getSetting('current_item') || null; }
function slug(s) { return String(s).replace(/[\\/:*?"<>|\s]+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'plan'; }
function archivePlan(p) {
  fs.mkdirSync(ARCHIVE_DIR, { recursive: true });
  const name = `${p.header.id || 'P0000'}-${p.header.target || 'v0.0.0'}-${slug(p.header.title)}.md`;
  const dest = path.join(ARCHIVE_DIR, name);
  fs.writeFileSync(dest, p.text);
  fs.unlinkSync(PLAN_PATH);
  return path.relative(ROOT, dest);
}

// ---------- 레지스트리 ----------
function readRegistry() { try { return JSON.parse(fs.readFileSync(REGISTRY_PATH, 'utf8')); } catch { return { projects: [] }; } }
function registerProject(name) {
  const reg = readRegistry();
  reg.projects = reg.projects.filter((x) => x.path !== ROOT);
  reg.projects.push({ name, path: ROOT, added_at: now() });
  fs.mkdirSync(path.dirname(REGISTRY_PATH), { recursive: true });
  fs.writeFileSync(REGISTRY_PATH, JSON.stringify(reg, null, 2));
}

// ---------- 훅 설정 병합 ----------
const CLAUDE_HOOKS = {
  SessionStart: [{ hooks: [{ type: 'command', command: 'node', args: ['${CLAUDE_PROJECT_DIR}/scripts/loop.mjs', 'hook', 'session'], timeout: 20 }] }],
  UserPromptSubmit: [{ hooks: [{ type: 'command', command: 'node', args: ['${CLAUDE_PROJECT_DIR}/scripts/loop.mjs', 'hook', 'prompt'], timeout: 10 }] }],
  PostToolUse: [{ matcher: 'Edit|Write|MultiEdit', hooks: [{ type: 'command', command: 'node', args: ['${CLAUDE_PROJECT_DIR}/scripts/loop.mjs', 'hook', 'edit'], timeout: 10 }] }],
  PreCompact: [{ hooks: [{ type: 'command', command: 'node', args: ['${CLAUDE_PROJECT_DIR}/scripts/loop.mjs', 'hook', 'precompact'], timeout: 20 }] }],
};
const CURSOR_HOOKS = {
  version: 1,
  hooks: {
    sessionStart: [{ command: 'node scripts/loop.mjs hook session' }],
    beforeSubmitPrompt: [{ command: 'node scripts/loop.mjs hook prompt' }],
    afterFileEdit: [{ command: 'node scripts/loop.mjs hook edit' }],
    preCompact: [{ command: 'node scripts/loop.mjs hook precompact' }],
  },
};
function mergeClaudeHooks() {
  const file = path.join(ROOT, '.claude', 'settings.json');
  fs.mkdirSync(path.dirname(file), { recursive: true });
  let cfg = {};
  if (fs.existsSync(file)) { try { cfg = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { die(L('.claude/settings.json 파싱 실패, 수동 확인 필요', '.claude/settings.json could not be parsed; fix it by hand')); } }
  cfg.hooks = cfg.hooks || {};
  for (const [event, groups] of Object.entries(CLAUDE_HOOKS)) {
    cfg.hooks[event] = cfg.hooks[event] || [];
    const has = JSON.stringify(cfg.hooks[event]).includes('loop.mjs');
    if (!has) cfg.hooks[event].push(...groups);
  }
  fs.writeFileSync(file, JSON.stringify(cfg, null, 2) + '\n');
  return path.relative(ROOT, file);
}
function mergeCursorHooks() {
  const file = path.join(ROOT, '.cursor', 'hooks.json');
  fs.mkdirSync(path.dirname(file), { recursive: true });
  let cfg = { version: 1, hooks: {} };
  if (fs.existsSync(file)) { try { cfg = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { die(L('.cursor/hooks.json 파싱 실패', '.cursor/hooks.json could not be parsed')); } }
  cfg.hooks = cfg.hooks || {};
  for (const [event, list] of Object.entries(CURSOR_HOOKS.hooks)) {
    cfg.hooks[event] = cfg.hooks[event] || [];
    if (!JSON.stringify(cfg.hooks[event]).includes('loop.mjs')) cfg.hooks[event].push(...list);
  }
  fs.writeFileSync(file, JSON.stringify(cfg, null, 2) + '\n');
  return path.relative(ROOT, file);
}

// ---------- 정책 (자체감사 누적) ----------
function activePolicies() { return q("SELECT * FROM policies WHERE status = 'active' ORDER BY id"); }
function policyHits(id) { return q1('SELECT COUNT(*) AS c FROM policy_hits WHERE policy_id = ?', id).c; }
function renderPolicyFile() {
  const active = activePolicies();
  const retired = q("SELECT * FROM policies WHERE status != 'active' ORDER BY id");
  const lines = [`# DOMANGCHA v${KIT_VERSION} — POLICY ${getSetting('project_name')}`, ''];
  lines.push(L('이 파일은 자체감사로 발견한 반복 실수를 프로젝트 정책으로 누적한 기록',
    'This file accumulates repeated mistakes that self-audit turned into project rules.'));
  lines.push(L('항목 자가감사 3-g 에서 활성 정책 전 줄을 대조하고 위반 시 policy hit 로 기록',
    'Check every active rule during item self-audit 3-g and record a breach with policy hit.'));
  lines.push(L('추가와 폐기는 loop policy add | retire 로 수행하며 이 파일은 그 결과를 렌더링한 것',
    'Add and retire through loop policy add | retire; this file renders the result.'));
  lines.push('');
  lines.push(L('## 활성 정책', '## Active policies'));
  lines.push('');
  if (!active.length) lines.push(L('- 없음 (같은 감사 실패가 반복되면 정책으로 승격됨)',
    '- none (a repeated audit failure gets promoted here)'));
  for (const r of active) {
    lines.push(`### ${r.id} ${r.title}`);
    lines.push(`${L('규칙', 'Rule')}: ${r.rule}`);
    lines.push(`${L('근거', 'Origin')}: ${r.origin || L('없음', 'none')}`);
    lines.push(`${L('위반', 'Breaches')}: ${policyHits(r.id)}${L('회', '')}`);
    lines.push(`${L('추가', 'Added')}: ${r.created_at.slice(0, 10)}`);
    lines.push('');
  }
  if (retired.length) {
    lines.push(L('## 폐기 정책', '## Retired policies'));
    lines.push('');
    for (const r of retired) lines.push(`- ${r.id} ${r.title} (${r.retired_reason || r.status}, ${r.retired_at ? r.retired_at.slice(0, 10) : ''})`);
    lines.push('');
  }
  fs.mkdirSync(LOOP_DIR, { recursive: true });
  fs.writeFileSync(POLICY_PATH, lines.join('\n'));
}
function policyLines(prefix) {
  const active = activePolicies();
  if (!active.length) return [];
  const lines = [`${prefix} ${L(`적용 중인 프로젝트 정책 ${active.length}건 (.loop/POLICY.md), 자가감사 3-g 에서 전 줄 대조 필수`,
    `${active.length} active project ${active.length === 1 ? 'policy' : 'policies'} (.loop/POLICY.md), check every line during self-audit 3-g`)}`];
  for (const r of active.slice(0, 10)) lines.push(`${prefix} ${r.id} ${r.title}: ${r.rule}`);
  if (active.length > 10) lines.push(`${prefix} ${L(`이하 ${active.length - 10}건은 policy list 로 확인`, `${active.length - 10} more, see policy list`)}`);
  return lines;
}

// ---------- /ceo 승격 게이트 / escalation gate ----------
// 기본은 이 루프다. /ceo 는 전체 하네스를 부르며, 없으면 그때 설치를 제안한다.
// This loop is the default. /ceo calls the full harness and offers to install it on demand.
const CEO_RE = /^\s*\/ceo\b/i;
const HARNESS = path.join(os.homedir(), '.domangcha', 'domangcha', 'engine.py');
const HARNESS_INSTALL = 'curl -fsSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash';
function escalationLines() {
  if (fs.existsSync(HARNESS)) {
    // 전역 enforcer 훅이 라우트 카드를 렌더링하므로 여기서는 한 줄만 남긴다.
    return [L('[DOMANGCHA] /ceo 감지: 전체 하네스로 승격, 끝나면 LOOP.md 로 복귀',
      '[DOMANGCHA] /ceo detected: escalating to the full harness, returning to LOOP.md afterwards')];
  }
  return [
    L('[DOMANGCHA] /ceo 는 전체 하네스(18 에이전트 · DIRECT/LOOP/GRAPH · 게이트)를 요구하는데 이 머신에는 아직 없습니다.',
      '[DOMANGCHA] /ceo needs the full harness (18 agents, DIRECT/LOOP/GRAPH, gates) and it is not on this machine yet.'),
    L('[DOMANGCHA] 사용자에게 설치 여부를 묻고 승인받은 뒤에만 아래를 실행할 것:',
      '[DOMANGCHA] Ask the user first and run this only after they approve:'),
    `[DOMANGCHA]   ${HARNESS_INSTALL}`,
    L('[DOMANGCHA] 설치는 ~/.claude 와 ~/.domangcha 에 쓰고 네트워크가 필요합니다 (이 프로젝트는 바뀌지 않음).',
      '[DOMANGCHA] It writes to ~/.claude and ~/.domangcha and needs network access; this project is not modified.'),
    L('[DOMANGCHA] 거절하면 이 요청을 LOOP.md 절차로 그대로 진행할 것 — 루프만으로도 처리 가능합니다.',
      '[DOMANGCHA] If they decline, handle the request through LOOP.md as usual; the loop alone can do it.'),
  ];
}

// ---------- 진행 카드 / progress card ----------
// 저장소 불변식: 반복마다 회차와 진전을 보고한다.
// Repository invariant: report iteration and progress on every pass.
function progressCard(p) {
  if (!p) return null;
  const c = counts(p);
  const total = p.items.length || 1;
  const done = c.passed;
  const pct = Math.round((done / total) * 100);
  const filled = Math.round(pct / 10);
  const bar = '▓'.repeat(filled) + '░'.repeat(10 - filled);
  const nx = nextItem(p);
  const retries = nx ? (latestImpl(p.header.id, nx.id) || {}).attempt || 0 : 0;
  const room = Math.max(0, num('max_audit_retries') - retries);
  const pol = activePolicies().length;
  const parts = [
    `🔁 DOMANGCHA · ${p.header.id} ${p.header.version} ${bar} ${pct}%`,
    `${L('항목', 'items')} ${done}/${p.items.length}`,
    `${L('재시도 여유', 'retries left')} ${room}/${num('max_audit_retries')}`,
  ];
  if (c.held) parts.push(`${L('보류', 'held')} ${c.held}`);
  if (pol) parts.push(`${L('정책', 'policies')} ${pol}`);
  parts.push(nx ? `${L('다음', 'next')} ${nx.id}` : L('종합 감사 단계', 'final audit'));
  return parts.join(' · ');
}

// ---------- 출력 도우미 ----------
function resumeText() {
  const p = readPlan(false);
  const name = getSetting('project_name');
  if (!p) {
    const head = [`[DOMANGCHA v${KIT_VERSION}] ${L('프로젝트', 'project')} ${name}, ${L('활성 플랜 없음 (.loop/PLAN.md 부재), 새 지시는 plan new 로 시작', 'no active plan (.loop/PLAN.md absent); start a new instruction with plan new')}`];
    return head.concat(policyLines('[DOMANGCHA]')).join('\n');
  }
  const c = counts(p);
  const lines = [];
  lines.push(`[DOMANGCHA v${KIT_VERSION}] ${L('프로젝트', 'project')} ${name}, ${L('플랜', 'plan')} ${p.header.id} ${p.header.version} "${p.header.title}", ${L('상태', 'status')} ${p.header.status}, ${L('목표', 'target')} ${p.header.target}`);
  const _card = progressCard(p);
  if (_card) lines.push(_card);
  lines.push(`[DOMANGCHA] ${L('항목 통과', 'items passed')} ${c.passed} / ${L('진행중', 'active')} ${c.active} / ${L('대기', 'pending')} ${c.pending} / ${L('보류', 'held')} ${c.held} / ${L('취소', 'cancelled')} ${c.cancelled}, ${L('전체', 'total')} ${p.items.length}`);
  const cur = currentItem();
  const nx = nextItem(p);
  if (nx && statusKey(nx.status) === 'active') lines.push(`[DOMANGCHA] ${L(`이전 컨텍스트에서 진행중이던 항목 ${nx.id}, 구현 상태 불명이므로 재감사 대상`, `item ${nx.id} was in progress in an earlier context; its state is unknown, so re-audit it`)}`);
  else if (cur) lines.push(`[DOMANGCHA] ${L(`기록상 진행 항목 ${cur} (플랜 상태와 불일치 시 플랜 우선)`, `records show ${cur} in progress (the plan file wins on disagreement)`)}`);
  if (nx) { lines.push(L('[DOMANGCHA] 다음 대상 항목', '[DOMANGCHA] next item')); lines.push(nx.block.slice(0, 1800)); }
  else if (planActive(p)) lines.push(L('[DOMANGCHA] 대기 항목 없음, 종합 감사 단계', '[DOMANGCHA] no pending items; final audit stage'));
  const ivs = q('SELECT id, item_id, content FROM interventions WHERE plan_id = ? AND resulting_plan_version IS NULL AND effect IS NULL ORDER BY id DESC LIMIT 3', p.header.id || '');
  for (const iv of ivs.reverse()) lines.push(`[DOMANGCHA] ${L('최근 개입', 'recent intervention')} ${iv.id}${iv.item_id ? ' (' + iv.item_id + ')' : ''}: ${iv.content.replace(/\s+/g, ' ').slice(0, 160)}`);
  const cmds = ['cmd_typecheck', 'cmd_lint', 'cmd_test', 'cmd_build'].map((k) => `${k.slice(4)}=${getSetting(k)}`).join(', ');
  lines.push(`[DOMANGCHA] ${L('감사 명령', 'audit commands')} ${cmds}`);
  lines.push(...policyLines('[DOMANGCHA]'));
  lines.push(L('[DOMANGCHA] 재개 규칙과 감사 기준은 LOOP.md 기준', '[DOMANGCHA] resume rules and audit criteria come from LOOP.md'));
  return lines.join('\n');
}
function passesThisSession() {
  const last = q1("SELECT created_at FROM events WHERE kind = 'session_start' ORDER BY id DESC LIMIT 1");
  const since = last ? last.created_at : '1970-01-01';
  return q1("SELECT COUNT(*) AS c FROM implementations WHERE audit_result = 'pass' AND finished_at > ?", since).c;
}

// ---------- 명령 ----------
const cmds = {};

cmds.init = (a) => {
  fs.mkdirSync(LOOP_DIR, { recursive: true });
  db(true);
  for (const [k, v] of Object.entries(DEFAULT_SETTINGS)) if (!q1('SELECT 1 FROM settings WHERE key = ?', k)) setSetting(k, v);
  if (a.project) setSetting('project_name', a.project);
  if (a.lang) { if (!LANGS.includes(String(a.lang))) die(`--lang ${LANGS.join('|')}`); setSetting('lang', a.lang); _lang = null; }
  if (!fs.existsSync(TEMPLATE_PATH)) fs.writeFileSync(TEMPLATE_PATH, DEFAULT_TEMPLATE());
  const gi = path.join(LOOP_DIR, '.gitignore');
  if (!fs.existsSync(gi)) fs.writeFileSync(gi, 'loop.db\nloop.db-wal\nloop.db-shm\nexport/\n');
  fs.mkdirSync(ARCHIVE_DIR, { recursive: true });
  if (!fs.existsSync(path.join(ARCHIVE_DIR, '.gitkeep'))) fs.writeFileSync(path.join(ARCHIVE_DIR, '.gitkeep'), '');
  const hooksFile = mergeClaudeHooks();
  const cursorFile = (a.cursor || fs.existsSync(path.join(ROOT, '.cursor'))) ? mergeCursorHooks() : null;
  const pkg = path.join(ROOT, 'package.json');
  if (fs.existsSync(pkg)) {
    try {
      const j = JSON.parse(fs.readFileSync(pkg, 'utf8'));
      j.scripts = j.scripts || {};
      if (!j.scripts.loop) { j.scripts.loop = 'node scripts/loop.mjs'; fs.writeFileSync(pkg, JSON.stringify(j, null, 2) + '\n'); }
    } catch { /* package.json 손상 시 건너뜀 */ }
  }
  registerProject(getSetting('project_name'));
  renderPolicyFile();
  addEvent('init', KIT_VERSION);
  out(`[DOMANGCHA v${KIT_VERSION}] ${L('초기화 완료', 'initialised')}: ${path.relative(ROOT, DB_PATH)}, ${path.relative(ROOT, POLICY_PATH)}, ${hooksFile}${cursorFile ? ', ' + cursorFile : ''}, ${L('레지스트리', 'registry')} ${REGISTRY_PATH}`);
  out(resumeText());
};

cmds.status = (a) => {
  if (a.all) {
    const reg = readRegistry();
    if (!reg.projects.length) return out(L('등록된 프로젝트 없음', 'no registered projects'));
    for (const pr of reg.projects) {
      const planFile = path.join(pr.path, '.loop', 'PLAN.md');
      if (!fs.existsSync(planFile)) {
        const adir = path.join(pr.path, '.loop', 'archive');
        const last = fs.existsSync(adir) ? fs.readdirSync(adir).filter((f) => f.endsWith('.md')).sort().pop() : null;
        out(`${pr.name}  ${L('활성 플랜 없음', 'no active plan')}${last ? '  ' + L('최근 보관', 'last archived') + ' ' + last : ''}  ${pr.path}`);
        continue;
      }
      const p = parsePlan(fs.readFileSync(planFile, 'utf8'));
      const c = counts(p); const nx = nextItem(p);
      out(`${pr.name}  ${p.header.id} ${p.header.version} ${p.header.status}  ${L('통과', 'passed')} ${c.passed}/${p.items.length}  ${L('다음', 'next')} ${nx ? nx.id + ' ' + nx.title : L('없음', 'none')}  ${pr.path}`);
    }
    return;
  }
  out(resumeText());
};

cmds.resume = () => out(resumeText());

cmds.hook = (a) => {
  const event = a._[0];
  const input = readJsonStdin();
  const sessionId = input.session_id || input.conversation_id || null;
  const isCursor = typeof input.hook_event_name === 'string' && /^[a-z]/.test(input.hook_event_name);
  const source = isCursor ? 'cursor' : 'claude_code';
  if (!fs.existsSync(DB_PATH)) { if (event === 'session') out(`[DOMANGCHA v${KIT_VERSION}] ${L('미초기화, node scripts/loop.mjs init 필요', 'not initialised; run node scripts/loop.mjs init')}`); return; }
  if (event === 'prompt') {
    const prompt = String(input.prompt || '').trim();
    if (!prompt) { if (isCursor) out('{"continue":true}'); return; }
    const p = readPlan(false);
    if (planActive(p)) {
      const id = nextId('interventions', 'iv');
      run('INSERT INTO interventions(id, content, source, session_id, plan_id, plan_version, item_id, created_at) VALUES (?,?,?,?,?,?,?,?)',
        id, prompt, source, sessionId, p.header.id, p.header.version, currentItem(), now());
      if (isCursor) { out('{"continue":true}'); return; }
      const msg = [`[DOMANGCHA v${KIT_VERSION}] ${L('개입 기록', 'intervention recorded')} ${id} · ${L('플랜', 'plan')} ${p.header.id} ${p.header.version}${currentItem() ? ' · ' + L('진행 항목', 'current item') + ' ' + currentItem() : ''}`];
      const card = progressCard(p);
      if (card) msg.push(card);
      if (CEO_RE.test(prompt)) { msg.push(...escalationLines()); out(msg.join('\n')); return; }
      msg.push(L('[DOMANGCHA] 다음 행동: 이 개입이 플랜을 바꾸는지 판단 (LOOP.md 2절 개입 처리)',
        '[DOMANGCHA] next: decide whether this intervention changes the plan (LOOP.md section 2)'));
      msg.push(L(`[DOMANGCHA] 바꾸면 plan revise --level patch|minor --note "무엇을 왜" --ref ${id} 후 계속, 안 바꾸면 답변 후 현재 항목 계속`,
        `[DOMANGCHA] if it does: plan revise --level patch|minor --note "what and why" --ref ${id}, then continue; if not, answer and stay on the current item`));
      msg.push(L('[DOMANGCHA] 멈춤·중단 지시면 즉시 hold 또는 plan abort, 현재 플랜과 무관한 새 기능이면 완료 후 새 플랜으로 분리 제안',
        '[DOMANGCHA] on a stop instruction, hold or plan abort at once; for a feature unrelated to this plan, propose a separate plan after this one'));
      msg.push(...policyLines('[DOMANGCHA]'));
      out(msg.join('\n'));
    } else {
      const id = nextId('instructions', 'ins');
      run('INSERT INTO instructions(id, content, source, session_id, created_at) VALUES (?,?,?,?,?)', id, prompt, source, sessionId, now());
      if (isCursor) { out('{"continue":true}'); return; }
      const msg = [`[DOMANGCHA v${KIT_VERSION}] ${L('지시 기록', 'instruction recorded')} ${id} · ${L('활성 플랜 없음', 'no active plan')}`];
      if (CEO_RE.test(prompt)) { msg.push(...escalationLines()); out(msg.join('\n')); return; }
      msg.push(L('[DOMANGCHA] 다음 행동: 구현·수정·추가 지시면 코드에 손대기 전에 LOOP.md 1절대로 플랜부터 작성',
        '[DOMANGCHA] next: for anything that changes the repository, write the plan before touching code (LOOP.md section 1)'));
      msg.push(L(`[DOMANGCHA] plan new --title "제목" --instruction ${id} --target vX.Y.Z → PLAN.md 작성 → plan check 통과 → plan confirm`,
        `[DOMANGCHA] plan new --title "title" --instruction ${id} --target vX.Y.Z → write PLAN.md → plan check → plan confirm`));
      msg.push(L('[DOMANGCHA] 단순 질문·조회·설명 요청이면 플랜 없이 바로 답변 (LOOP.md 1절 예외)',
        '[DOMANGCHA] a question, lookup or explanation is answered directly, with no plan (LOOP.md section 1 exception)'));
      msg.push(...policyLines('[DOMANGCHA]'));
      out(msg.join('\n'));
    }
    return;
  }
  if (event === 'edit') {
    const fp = (input.tool_input && input.tool_input.file_path) || input.file_path || null;
    if (!fp) return;
    const p = readPlan(false);
    run('INSERT INTO file_changes(plan_id, item_id, tool, file_path, session_id, created_at) VALUES (?,?,?,?,?,?)',
      p ? p.header.id : null, currentItem(), input.tool_name || input.hook_event_name || null, path.isAbsolute(fp) ? path.relative(ROOT, fp) : fp, sessionId, now());
    return;
  }
  if (event === 'precompact') {
    snapshot('precompact', input.trigger || null);
    addEvent('precompact', input.trigger || null, sessionId);
    return;
  }
  if (event === 'session') {
    snapshot('session', input.source || null);
    addEvent('session_start', input.source || (isCursor ? 'cursor' : null), sessionId);
    out(resumeText());
    return;
  }
  die(L(`알 수 없는 훅 이벤트 ${event}`, `unknown hook event ${event}`));
};

cmds.plan = (a) => {
  const sub = a._[0];
  if (sub === 'new') {
    const cur = readPlan(false);
    if (planActive(cur) && !a.force) die(L(`활성 플랜 ${cur.header.id} ${cur.header.version} 존재, 완료 후 진행하거나 --force 로 보관 후 생성`, `plan ${cur.header.id} ${cur.header.version} is still active; finish it or pass --force to archive and start a new one`));
    if (cur) { const dest = archivePlan(cur); addEvent('archive', dest); out(`[DOMANGCHA] ${L('기존 플랜 보관', 'archived previous plan')} ${dest}`); }
    const n = q1('SELECT COUNT(DISTINCT plan_id) AS c FROM plan_versions').c;
    const planId = `P${pad(n + 1)}`;
    const tpl = fs.existsSync(TEMPLATE_PATH) ? fs.readFileSync(TEMPLATE_PATH, 'utf8') : DEFAULT_TEMPLATE();
    const vars = {
      project: getSetting('project_name'), title: a.title || L('(제목)', '(title)'), plan_id: planId,
      instruction: a.instruction || '(지시 ID)', target: a.target || '(목표 버전)', date: today(),
      cmd_typecheck: getSetting('cmd_typecheck'), cmd_test: getSetting('cmd_test'), cmd_build: getSetting('cmd_build'),
    };
    writePlan(tpl.replace(/\{\{(\w+)\}\}/g, (_, k) => vars[k] ?? `{{${k}}}`));
    if (a.instruction) run('UPDATE instructions SET plan_id = ? WHERE id = ?', planId, a.instruction);
    setSetting('current_item', '');
    snapshot('instruction', a.instruction || null);
    addEvent('plan_new', planId);
    out(`[DOMANGCHA] ${L(`플랜 ${planId} 생성`, `plan ${planId} created`)} ${path.relative(ROOT, PLAN_PATH)}, ${L('항목 작성 후 plan check 실행', 'write the items then run plan check')}`);
    return;
  }
  const p = readPlan();
  if (sub === 'check') {
    const problems = [];
    if (!p.items.length) problems.push(L('항목 없음', 'no items'));
    if (!/^v\d+\.\d+\.\d+$/.test(p.header.target || '')) problems.push(L('목표 버전 형식 오류 (v0.0.0)', 'target version must look like v0.0.0'));
    if (/\(제목\)|\(지시 ID\)|\(목표 버전\)|\(항목 제목\)/.test(p.text)) problems.push(L('템플릿 자리표시자 잔존', 'template placeholders still present'));
    const seen = new Set();
    for (const it of p.items) {
      if (seen.has(it.id)) problems.push(`${it.id} ${L('중복', 'is duplicated')}`); seen.add(it.id);
      if (!new RegExp('^' + FRE('scope') + ':\\s*\\S', 'm').test(it.block)) problems.push(`${it.id} ${L('범위 없음', 'has no scope')}`);
      const crit = (it.block.split(new RegExp('^' + FRE('criteria') + ':\\s*$', 'm'))[1] || '').split(/^(?![-\s])\S/m)[0];
      const n = (crit.match(/^- \S/gm) || []).length;
      if (n < 1) problems.push(`${it.id} ${L('감사 기준 없음', 'has no audit criteria')}`);
      if (/\(명령과 기대 결과|\(관측 가능한 조건|\(a command and its expected result|\(an observable condition/.test(it.block)) problems.push(`${it.id} ${L('감사 기준 자리표시자 잔존', 'still has audit-criteria placeholders')}`);
      const dep = (it.block.match(new RegExp('^' + FRE('depends') + ':\\s*(.+)$', 'm')) || [])[1];
      if (dep && !isNone(dep)) for (const d of dep.split(/[,\s]+/).filter(Boolean)) if (!p.items.some((x) => x.id === d)) problems.push(`${it.id} ${L(`의존 ${d} 없음`, `depends on ${d}, which does not exist`)}`);
    }
    if (problems.length) { out(L('[DOMANGCHA] 플랜 점검 실패', '[DOMANGCHA] plan check failed')); problems.forEach((x) => out('- ' + x)); process.exit(2); }
    out(`[DOMANGCHA] ${L('플랜 점검 통과, 항목', 'plan check passed, items')} ${p.items.length}${flag('plan_confirm') ? L(', 사용자 확인 후 plan confirm 실행', '; get the user\'s confirmation, then plan confirm') : L(', plan confirm 실행 후 착수', '; run plan confirm and start')}`);
    return;
  }
  if (sub === 'confirm') {
    setPlanStatus(p, W(PLAN_STATUS, 'active'));
    if (gitAvailable() && !new RegExp('^' + FRE('startCommit') + ':', 'm').test(p.text)) {
      try { const h = sh('git rev-parse --short HEAD'); const t = readPlanText(); writePlan(t.replace(new RegExp('^(' + FRE('written') + ':.*)$', 'm'), `$1\n${F('startCommit')}: ${h}`)); } catch { /* 커밋 없음 */ }
    }
    run("UPDATE interventions SET effect = 'plan_review', resulting_plan_version = ? WHERE plan_id = ? AND item_id IS NULL AND effect IS NULL AND resulting_plan_version IS NULL", p.header.version, p.header.id);
    snapshot('confirm', a.ref || null);
    addEvent('plan_confirm', p.header.id);
    out(`[DOMANGCHA] ${L(`플랜 ${p.header.id} ${p.header.version} 진행중, 첫 항목은`, `plan ${p.header.id} ${p.header.version} is active; first item`)} start ${nextItem(readPlan()).id}`);
    return;
  }
  if (sub === 'revise') {
    const level = a.level || 'patch';
    const v = bumpVersion(p.header.version, level);
    const note = a.note || L('(변경 사유 없음)', '(no reason given)');
    const ref = a.ref || null;
    let text = p.text.replace(new RegExp('^' + FRE('planVersion') + ':.*$', 'm'), `${F('planVersion')}: ${v}`);
    const histIdx = sectionIndex(text, 'history', true);
    const line = `- ${v} (${today()}) ${note}${ref ? ' (' + ref + ')' : ''}`;
    if (histIdx >= 0) text = text.trimEnd() + '\n' + line + '\n';
    else text = text.trimEnd() + `\n\n${SEC('history')}\n` + line + '\n';
    writePlan(text);
    const trigger = ref && ref.startsWith('iv_') ? 'intervention' : ref && ref.startsWith('audit:') ? 'audit' : 'manual';
    snapshot(trigger, ref);
    if (ref && ref.startsWith('iv_')) run('UPDATE interventions SET resulting_plan_version = ?, effect = COALESCE(effect, ?) WHERE id = ?', v, 'scope_change', ref);
    if (ref && ref.startsWith('audit:')) {
      const itemId = ref.slice(6);
      const c = q1("SELECT COUNT(*) AS c FROM plan_versions WHERE plan_id = ? AND trigger = 'audit' AND trigger_ref = ?", p.header.id, ref).c;
      if (c >= num('max_plan_revisions_per_item')) out(`[DOMANGCHA] ${L(`주의: ${itemId} 감사 기인 플랜 갱신 ${c}회, 한계 ${num('max_plan_revisions_per_item')}회 도달, 사용자 판단 요청 권고`, `warning: ${c} plan revisions caused by ${itemId}, limit ${num('max_plan_revisions_per_item')} reached; ask the user to decide`)}`);
    }
    out(`[DOMANGCHA] ${L('플랜', 'plan')} ${p.header.id} ${p.header.version} -> ${v} (${trigger})`);
    return;
  }
  if (sub === 'snapshot') { const r = snapshot(a.trigger || 'manual', a.ref || null); out(`[DOMANGCHA] ${L('스냅샷', 'snapshot')} ${r.skipped ? L('변경 없음', 'unchanged') : L('저장', 'saved')} ${r.version}`); return; }
  if (sub === 'next') { const nx = nextItem(p); out(nx ? nx.block : L('[DOMANGCHA] 대기 항목 없음', '[DOMANGCHA] no pending items')); return; }
  if (sub === 'abort') {
    setPlanStatus(p, W(PLAN_STATUS, 'aborted'));
    snapshot('abort', a.ref || null);
    const dest = archivePlan(readPlan());
    setSetting('current_item', '');
    addEvent('archive', dest);
    out(`[DOMANGCHA] ${L('플랜 중단, 보관', 'plan aborted, archived')} ${dest}`);
    return;
  }
  die(L('plan 하위 명령: new | check | confirm | revise | snapshot | next | abort', 'plan subcommands: new | check | confirm | revise | snapshot | next | abort'));
};

cmds.start = (a) => {
  const id = a._[0]; if (!id) die(L('항목 ID 필요', 'item id required'));
  const p = readPlan();
  if (!planActive(p) || planStatusKey(p.header.status) !== 'active') die(L(`플랜 상태 ${p.header.status}, plan confirm 후 착수`, `plan status is ${p.header.status}; run plan confirm before starting`));
  const it = p.items.find((x) => x.id === id); if (!it) die(L(`항목 ${id} 없음`, `item ${id} does not exist`));
  if (statusKey(it.status) === 'passed' && !a.force) die(L(`${id} 이미 통과, 재작업은 --force`, `${id} already passed; pass --force to redo it`));
  const blocked = p.items.filter((x) => statusKey(x.status) === 'active' && x.id !== id);
  if (blocked.length && !a.force) die(L(`진행중 항목 ${blocked.map((x) => x.id).join(',')} 존재, 먼저 pass/fail/hold 처리`, `items ${blocked.map((x) => x.id).join(',')} are still active; pass, fail or hold them first`));
  const dep = (it.block.match(new RegExp('^' + FRE('depends') + ':\\s*(.+)$', 'm')) || [])[1];
  if (dep && !isNone(dep)) {
    const unmet = dep.split(/[,\s]+/).filter(Boolean).filter((d) => { const x = p.items.find((y) => y.id === d); return !x || statusKey(x.status) !== 'passed'; });
    if (unmet.length && !a.force) die(L(`${id} 의존 미충족 ${unmet.join(',')}`, `${id} has unmet dependencies: ${unmet.join(',')}`));
  }
  const attempt = q1('SELECT COUNT(*) AS c FROM implementations WHERE plan_id = ? AND item_id = ?', p.header.id, id).c + 1;
  run('INSERT INTO implementations(plan_id, plan_version, item_id, attempt, audit_result, started_at) VALUES (?,?,?,?,?,?)', p.header.id, p.header.version, id, attempt, 'started', now());
  setItemStatus(p, id, W(ITEM_STATUS, 'active'));
  setSetting('current_item', id);
  run("UPDATE interventions SET effect = 'plan_review' WHERE plan_id = ? AND item_id IS NULL AND effect IS NULL AND resulting_plan_version IS NULL", p.header.id);
  snapshot('status', `start:${id}`);
  out(`[DOMANGCHA] ${id} ${L('착수', 'started')} (${L('시도', 'attempt')} ${attempt}/${num('max_audit_retries')})${modeKey(it.mode) === 'heavy' ? L(', 중량 모드: ' + getSetting('heavy_doc') + ' 규정 적용', ', heavy mode: apply the rules in ' + getSetting('heavy_doc')) : ''}`);
  out(readPlan().items.find((x) => x.id === id).block);
  out(`[DOMANGCHA] ${L('감사 명령', 'audit commands')} typecheck=${getSetting('cmd_typecheck')}, test=${getSetting('cmd_test')}`);
};

function latestImpl(planId, itemId) {
  return q1('SELECT * FROM implementations WHERE plan_id = ? AND item_id = ? ORDER BY id DESC LIMIT 1', planId, itemId);
}

cmds.pass = (a) => {
  const id = a._[0]; if (!id) die(L('항목 ID 필요', 'item id required'));
  if (!a.summary) die(L('--summary "어떻게 구현했는지" 필수', '--summary "what you implemented" is required'));
  const p = readPlan();
  const it = p.items.find((x) => x.id === id); if (!it) die(L(`항목 ${id} 없음`, `item ${id} does not exist`));
  const row = latestImpl(p.header.id, id); if (!row || row.audit_result !== 'started') die(L(`${id} 착수 기록 없음, start ${id} 먼저`, `no start record for ${id}; run start ${id} first`));
  const files = a.files ? String(a.files).split(',').map((s) => s.trim()).filter(Boolean) : changedFiles();
  let commitHash = null; let commitNote = '';
  if (flag('auto_commit') && !a['no-commit']) {
    setItemStatus(p, id, W(ITEM_STATUS, 'passed'));
    const r = gitCommit(`${p.header.target}-${id}: ${it.title}`);
    if (r.hash) { commitHash = r.hash; commitNote = `, ${L('커밋', 'commit')} ${r.hash}`; } else commitNote = `, ${L('커밋 생략', 'commit skipped')} (${r.skipped})`;
  } else setItemStatus(p, id, W(ITEM_STATUS, 'passed'));
  run('UPDATE implementations SET summary = ?, files = ?, audit_result = ?, audit_notes = ?, commit_hash = ?, finished_at = ? WHERE id = ?',
    a.summary, JSON.stringify(files), 'pass', a.notes || null, commitHash, now(), row.id);
  run("UPDATE interventions SET effect = 'absorbed' WHERE plan_id = ? AND item_id = ? AND effect IS NULL AND resulting_plan_version IS NULL", p.header.id, id);
  setSetting('current_item', '');
  snapshot('status', `pass:${id}`);
  const p2 = readPlan(); const c = counts(p2); const nx = nextItem(p2);
  const k = passesThisSession(); const every = num('checkpoint_every');
  out(`[DOMANGCHA] ${id} ${L('통과', 'passed')} (${c.passed}/${p2.items.length})${commitNote}, ${L('이번 컨텍스트 통과', 'passed this context')} ${k}`);
  out(nx ? `[DOMANGCHA] ${L('다음 항목', 'next item')} ${nx.id} ${nx.title}` : L('[DOMANGCHA] 대기 항목 없음, 종합 감사 단계 (final)', '[DOMANGCHA] no pending items; final audit stage (final)'));
  if (k >= every && nx) out(`[DOMANGCHA] ${L(`체크포인트: 플랜 ${p2.header.version} 저장됨, 여기서 /clear 후 재개 권장 (checkpoint_every=${every})`, `checkpoint: plan ${p2.header.version} saved; a /clear here and resume is recommended (checkpoint_every=${every})`)}`);
};

cmds.fail = (a) => {
  const id = a._[0]; if (!id) die(L('항목 ID 필요', 'item id required'));
  if (!a.reason) die(L('--reason 필수', '--reason is required'));
  const p = readPlan();
  const row = latestImpl(p.header.id, id); if (!row || row.audit_result !== 'started') die(L(`${id} 착수 기록 없음`, `no start record for ${id}`));
  run('UPDATE implementations SET audit_result = ?, audit_notes = ?, files = ?, finished_at = ? WHERE id = ?', 'fail', a.reason, JSON.stringify(changedFiles()), now(), row.id);
  const limit = num('max_audit_retries');
  out(`[DOMANGCHA] ${id} ${L('감사 실패 (시도', 'audit failed (attempt')} ${row.attempt}/${limit}): ${a.reason}`);
  if (row.attempt >= limit) out(L(`[DOMANGCHA] 재시도 한계 도달, hold ${id} --reason 로 보류하고 사용자 판단 요청`, `[DOMANGCHA] retry limit reached; hold ${id} --reason and ask the user to decide`));
  else out(L(`[DOMANGCHA] 수정 후 start ${id} 로 재착수 (플랜 갱신이 필요하면 먼저 plan revise --ref audit:${id})`, `[DOMANGCHA] fix it and run start ${id} again (if the plan itself must change, plan revise --ref audit:${id} first)`));
  const fails = q1("SELECT COUNT(*) AS c FROM implementations WHERE plan_id = ? AND item_id = ? AND audit_result = 'fail'", p.header.id || '', id).c;
  const promote = num('policy_promote_after');
  if (fails >= promote) {
    out(`[DOMANGCHA] ${L(`자체감사: ${id} 감사 실패 ${fails}회 누적 (승격 기준 ${promote}회), 같은 실수가 반복되고 있음`, `self-audit: ${id} has failed ${fails} times (promotion threshold ${promote}); the same mistake is repeating`)}`);
    out(`[DOMANGCHA] ${L(`원인이 이 항목 밖에서도 재발할 일반 규칙이면 policy add --title "짧은 제목" --rule "무엇을 하지 말고 무엇을 할 것" --origin audit:${id} 로 정책에 기록할 것`, `if the cause is a general rule that would recur elsewhere, record it: policy add --title "short title" --rule "what not to do and what to do instead" --origin audit:${id}`)}`);
    out(L('[DOMANGCHA] 이 항목 한정 실수면 정책으로 올리지 말고 수정만 할 것', '[DOMANGCHA] if it is specific to this item, just fix it and do not promote a policy'));
  }
};

cmds.hold = (a) => {
  const id = a._[0]; if (!id) die(L('항목 ID 필요', 'item id required'));
  if (!a.reason) die(L('--reason 필수', '--reason is required'));
  const p = readPlan();
  const row = latestImpl(p.header.id, id);
  if (row && row.audit_result === 'started') run('UPDATE implementations SET audit_result = ?, audit_notes = ?, finished_at = ? WHERE id = ?', 'hold', a.reason, now(), row.id);
  setItemStatus(p, id, `${W(ITEM_STATUS, 'held')} (${a.reason})`);
  setSetting('current_item', '');
  snapshot('status', `hold:${id}`);
  out(`[DOMANGCHA] ${id} ${L('보류', 'held')}: ${a.reason}, ${L('사용자 판단 대기', 'waiting on the user')}`);
};

cmds.checkpoint = (a) => {
  const r = snapshot('checkpoint', a.note || null);
  addEvent('checkpoint', a.note || null);
  const p = readPlan(false);
  out(`[DOMANGCHA] ${L('체크포인트', 'checkpoint')} ${r ? r.version : L('(플랜 없음)', '(no plan)')} ${r && !r.skipped ? L('스냅샷 저장', 'snapshot saved') : L('변경 없음', 'unchanged')}, ${L('이번 컨텍스트 통과', 'passed this context')} ${passesThisSession()}${p ? ', ' + L('다음', 'next') + ' ' + (nextItem(p) ? nextItem(p).id : L('없음', 'none')) : ''}`);
};

cmds.final = (a) => {
  const result = a.result; if (!['pass', 'fail'].includes(result)) die(L('--result pass|fail 필수', '--result pass|fail is required'));
  if (!a.summary) die(L('--summary 필수', '--summary is required'));
  const p = readPlan();
  const open = p.items.filter((x) => !['passed', 'cancelled'].includes(statusKey(x.status)));
  if (open.length && result === 'pass') die(L(`미완 항목 ${open.map((x) => x.id).join(',')} 존재, 종합 감사 통과 불가`, `items ${open.map((x) => x.id).join(',')} are unfinished; the final audit cannot pass`));
  if (/\(전 항목 통과 후 기록\)|\(recorded after every item passes\)/.test(p.text)) die(L('PLAN.md 종합 감사 절에 결과 기록 후 실행 (자리표시자 잔존)', 'record the result in the PLAN.md final-audit section first (placeholder still present)'));
  addEvent('final_audit', `${result}: ${a.summary}`);
  if (result === 'fail') { snapshot('final', 'fail'); out(`[DOMANGCHA] ${L(`종합 감사 실패 기록: ${a.summary}, 보완 항목을 plan revise 로 추가 후 계속`, `final audit recorded as failed: ${a.summary}; add the remedial items with plan revise and return to section 2`)}`); return; }
  setPlanStatus(p, W(PLAN_STATUS, 'done'));
  snapshot('final', 'pass');
  const target = p.header.target;
  const pkg = path.join(ROOT, 'package.json');
  if (flag('bump_package_version') && fs.existsSync(pkg) && /^v\d+\.\d+\.\d+$/.test(target || '')) {
    try { const j = JSON.parse(fs.readFileSync(pkg, 'utf8')); j.version = target.slice(1); fs.writeFileSync(pkg, JSON.stringify(j, null, 2) + '\n'); } catch { /* 건너뜀 */ }
  }
  const dest = archivePlan(readPlan());
  setSetting('current_item', '');
  addEvent('archive', dest);
  let note = '';
  if (flag('auto_commit')) {
    const r = gitCommit(`${target}: ${p.header.title}`);
    note = r.hash ? `, 커밋 ${r.hash}` : `, 커밋 생략 (${r.skipped})`;
    if (r.hash && flag('auto_tag')) note += gitTag(target) ? `, ${L('태그', 'tag')} ${target}` : L(', 태그 실패', ', tag failed');
  }
  out(`[DOMANGCHA] ${L('플랜', 'plan')} ${p.header.id} ${L('완료', 'done')} ${target}${note}, ${L('보관', 'archived')} ${dest}`);
};

cmds.mark = (a) => {
  const id = a._[0]; if (!id || !a.effect) die('mark <iv_id> --effect answer|scope_change|order_change|stop|note');
  run('UPDATE interventions SET effect = ? WHERE id = ?', a.effect, id);
  out(`[DOMANGCHA] ${id} effect=${a.effect}`);
};

cmds.history = (a) => {
  const limit = Number(a.limit || 30);
  const rows = q(`
    SELECT created_at, 'instruction' AS kind, id AS ref, substr(content,1,120) AS detail FROM instructions
    UNION ALL SELECT created_at, 'intervention', id || COALESCE(' @' || item_id, ''), substr(content,1,120) FROM interventions
    UNION ALL SELECT COALESCE(finished_at, started_at), 'implementation', item_id || ' #' || attempt || ' ' || audit_result, COALESCE(summary, audit_notes, '') FROM implementations
    UNION ALL SELECT created_at, 'plan', version || ' ' || trigger, COALESCE(trigger_ref, '') FROM plan_versions
    UNION ALL SELECT created_at, 'event', kind, COALESCE(detail, '') FROM events
    ORDER BY 1 DESC LIMIT ?`, limit);
  for (const r of rows.reverse()) out(`${r.created_at}  ${r.kind.padEnd(14)}  ${String(r.ref).padEnd(22)}  ${String(r.detail).replace(/\s+/g, ' ')}`);
};

cmds.config = (a) => {
  const sub = a._[0];
  if (sub === 'set') {
    if (!a._[1] || a._[2] === undefined) die('config set <key> <value>');
    if (a._[1] === 'lang' && !LANGS.includes(String(a._[2]))) die(`lang ${LANGS.join('|')}`);
    setSetting(a._[1], a._[2]);
    if (a._[1] === 'lang') { _lang = null; out(`lang=${a._[2]}${retemplate()}`); return; }
    out(`${a._[1]}=${a._[2]}`);
    return;
  }
  if (sub === 'get') { out(String(getSetting(a._[1]) ?? '')); return; }
  const rows = q('SELECT key, value FROM settings ORDER BY key');
  const merged = { ...DEFAULT_SETTINGS }; for (const r of rows) merged[r.key] = r.value;
  for (const [k, v] of Object.entries(merged)) out(`${k}=${v}`);
};

cmds.export = () => {
  const dir = path.join(LOOP_DIR, 'export');
  fs.mkdirSync(dir, { recursive: true });
  for (const t of ['instructions', 'interventions', 'implementations', 'file_changes', 'plan_versions', 'events', 'settings']) {
    const rows = q(`SELECT * FROM ${t}`);
    fs.writeFileSync(path.join(dir, `${t}.jsonl`), rows.map((r) => JSON.stringify(r)).join('\n') + (rows.length ? '\n' : ''));
  }
  out(`[DOMANGCHA] ${L('내보내기 완료', 'exported')} ${path.relative(ROOT, dir)}`);
};

cmds.policy = (a) => {
  const sub = a._.shift() || 'list';
  const p = readPlan(false);
  if (sub === 'list' || sub === 'check') {
    const active = activePolicies();
    if (!active.length) { out(L('[DOMANGCHA] 활성 정책 없음, 같은 감사 실패가 반복되면 policy add 로 승격', '[DOMANGCHA] no active policies; a repeated audit failure gets promoted with policy add')); return; }
    out(`[DOMANGCHA] ${L(`활성 정책 ${active.length}건 — 자가감사 3-g 대조 목록`, `${active.length} active ${active.length === 1 ? 'policy' : 'policies'} — the self-audit 3-g checklist`)}`);
    for (const r of active) out(`  ${r.id} ${r.title}\n    ${L('규칙', 'rule')}: ${r.rule}\n    ${L('근거', 'origin')}: ${r.origin || L('없음', 'none')} · ${L('위반', 'breaches')} ${policyHits(r.id)}`);
    if (sub === 'check') out(L('[DOMANGCHA] 각 줄을 이번 변경분에 대조하고 위반 시 policy hit P00x --note "무엇을 어겼는지" 기록', '[DOMANGCHA] check every line against this change and record a breach with policy hit P00x --note "what you broke"'));
    return;
  }
  if (sub === 'add') {
    if (!a.title) die(L('--title "정책 제목" 필수', '--title "policy title" is required'));
    if (!a.rule) die(L('--rule "무엇을 하지 말고 무엇을 할 것" 필수', '--rule "what not to do and what to do instead" is required'));
    const id = 'P' + String(q1('SELECT COUNT(*) AS c FROM policies').c + 1).padStart(3, '0');
    run('INSERT INTO policies(id, title, rule, origin, status, created_at) VALUES (?,?,?,?,?,?)',
      id, a.title, a.rule, a.origin || null, 'active', now());
    renderPolicyFile();
    addEvent('policy_add', `${id} ${a.title}`);
    out(`[DOMANGCHA] ${L('정책', 'policy')} ${id} ${L('기록', 'recorded')}: ${a.title}`);
    out(`[DOMANGCHA] ${L('규칙', 'rule')}: ${a.rule}`);
    out(L('[DOMANGCHA] .loop/POLICY.md 갱신됨, 이후 모든 항목 자가감사 3-g 와 프롬프트 훅에서 자동 재주입', '[DOMANGCHA] .loop/POLICY.md updated; it is re-injected in every later self-audit 3-g and prompt hook'));
    return;
  }
  if (sub === 'hit') {
    const id = a._[0]; if (!id) die(L('정책 ID 필요 (예: policy hit P001)', 'policy id required (e.g. policy hit P001)'));
    const row = q1("SELECT * FROM policies WHERE id = ? AND status = 'active'", id);
    if (!row) die(L(`활성 정책 ${id} 없음, policy list 확인`, `no active policy ${id}; check policy list`));
    run('INSERT INTO policy_hits(policy_id, plan_id, plan_version, item_id, note, created_at) VALUES (?,?,?,?,?,?)',
      id, p ? p.header.id : null, p ? p.header.version : null, currentItem() || null, a.note || null, now());
    const c = policyHits(id);
    renderPolicyFile();
    out(`[DOMANGCHA] ${L(`정책 위반 ${id} 기록 (누적 ${c}회)`, `policy breach ${id} recorded (${c} total)`)}: ${row.title}`);
    const limit = num('policy_rewrite_after');
    if (c >= limit) out(`[DOMANGCHA] ${L(`자체감사: ${id} 를 ${c}회 어겼음, 정책 문구가 실행 가능하지 않다는 뜻이므로 policy retire 후 더 구체적인 규칙으로 다시 add 할 것`, `self-audit: ${id} has been broken ${c} times, so it is not written as something you can act on; policy retire it and add a more specific rule`)}`);
    return;
  }
  if (sub === 'retire') {
    const id = a._[0]; if (!id) die(L('정책 ID 필요', 'policy id required'));
    if (!a.reason) die(L('--reason 필수', '--reason is required'));
    const row = q1("SELECT * FROM policies WHERE id = ?", id); if (!row) die(L(`정책 ${id} 없음`, `policy ${id} does not exist`));
    run("UPDATE policies SET status = 'retired', retired_at = ?, retired_reason = ? WHERE id = ?", now(), a.reason, id);
    renderPolicyFile();
    addEvent('policy_retire', `${id} ${a.reason}`);
    out(`[DOMANGCHA] ${L('정책', 'policy')} ${id} ${L('폐기', 'retired')}: ${a.reason}`);
    return;
  }
  die(L(`알 수 없는 policy 하위 명령 ${sub} (list|check|add|hit|retire)`, `unknown policy subcommand ${sub} (list|check|add|hit|retire)`));
};

cmds.help = () => out(EN() ? `DOMANGCHA v${KIT_VERSION} — project autonomous dev loop
  init [--project NAME] [--lang ko|en] [--cursor]   set up .loop, merge hooks, register the project
  status [--all]                          current plan state (--all covers every project)
  resume                                  resume context (the SessionStart hook calls this)
  plan new --title T --instruction ins_x --target vX.Y.Z [--force]
  plan check | confirm | next | snapshot | abort
  plan revise --level patch|minor --note "reason" --ref iv_x|audit:Ixx
  start Ixx [--force]                     begin an item (status active, attempt +1)
  pass Ixx --summary "what you built" [--files a,b] [--notes "audit evidence"] [--no-commit]
  fail Ixx --reason "why it failed"
  hold Ixx --reason "why it is blocked"
  checkpoint [--note]                     snapshot and record a checkpoint
  final --result pass|fail --summary "final audit summary"
  mark iv_x --effect answer|scope_change|order_change|stop|note
  policy list | check                     active policies (check is the self-audit 3-g list)
  policy add --title T --rule R [--origin audit:Ixx|iv_x]   promote a repeated mistake
  policy hit P00x [--note]                record a breach (repeats suggest a rewrite)
  policy retire P00x --reason "reason"
  history [--limit N] | config [set k v | get k] | export
  hook session|prompt|edit|precompact     hook handlers (stdin JSON)
  config set lang ko|en                   switch the language of every message and template` : `DOMANGCHA v${KIT_VERSION} — 프로젝트 자율개발 루프
  init [--project 이름] [--lang ko|en] [--cursor]   .loop 초기화, 훅 병합, 레지스트리 등록
  status [--all]                          현재 플랜 상태 (--all 은 전 프로젝트)
  resume                                  재개용 컨텍스트 출력 (SessionStart 훅이 호출)
  plan new --title T --instruction ins_x --target vX.Y.Z [--force]
  plan check | confirm | next | snapshot | abort
  plan revise --level patch|minor --note "사유" --ref iv_x|audit:Ixx
  start Ixx [--force]                     항목 착수 (상태 진행중, 시도 +1)
  pass Ixx --summary "구현 요약" [--files a,b] [--notes "감사 근거"] [--no-commit]
  fail Ixx --reason "실패 사유"
  hold Ixx --reason "보류 사유"
  checkpoint [--note]                     스냅샷과 체크포인트 기록
  final --result pass|fail --summary "종합 감사 요약"
  mark iv_x --effect answer|scope_change|order_change|stop|note
  policy list | check                     활성 정책 조회 (check 는 자가감사 3-g 대조용)
  policy add --title T --rule R [--origin audit:Ixx|iv_x]   반복 실수를 정책으로 승격
  policy hit P00x [--note]                정책 위반 기록 (누적되면 정책 재작성 권고)
  policy retire P00x --reason "사유"
  history [--limit N] | config [set k v | get k] | export
  hook session|prompt|edit|precompact     훅 핸들러 (stdin JSON)
  config set lang ko|en                   모든 메시지와 템플릿의 언어 전환`);

// ---------- 진입 ----------
const argv = parseArgs(process.argv.slice(2));
const cmd = argv._.shift() || 'help';
if (!cmds[cmd]) { console.error(`[DOMANGCHA] unknown command / 알 수 없는 명령 ${cmd}`); cmds.help(); process.exit(1); }
try { cmds[cmd](argv); }
catch (e) { console.error('[DOMANGCHA] error / 오류: ' + (e && e.message ? e.message : e)); process.exit(1); }
