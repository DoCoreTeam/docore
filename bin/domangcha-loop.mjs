#!/usr/bin/env node
// DOMANGCHA v3.0.0  bin/domangcha-loop.mjs
// 경량 설치기: 현재 작업 디렉터리에 자율개발 루프를 설치한다.
// 전역 18 에이전트 설치는 domangcha --full 이 담당하며 이 파일은 ~/.claude 를 건드리지 않는다.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PKG_ROOT = path.join(__dirname, '..');
const TEMPLATES = path.join(PKG_ROOT, 'domangcha', 'loop', 'templates');
const ROOT = process.cwd();
const args = process.argv.slice(2);
const has = (f) => args.includes(f);

const fail = (m) => { console.error(`[DOMANGCHA] ${m}`); process.exit(1); };
const say = (m) => console.log(`[DOMANGCHA] ${m}`);

function readVersion() {
  const f = path.join(PKG_ROOT, 'domangcha', 'VERSION');
  if (!fs.existsSync(f)) fail(`버전 파일 없음: ${f}, 패키지가 손상되었으니 다시 설치할 것`);
  return fs.readFileSync(f, 'utf8').trim();
}
const VERSION = readVersion();

// Node 22.13 이상 필요 (node:sqlite 내장)
{
  const [maj, min] = process.versions.node.split('.').map(Number);
  if (maj < 22 || (maj === 22 && min < 13)) {
    fail(`Node 22.13 이상 필요, 현재 ${process.versions.node}. nvm install 22 로 올린 뒤 다시 실행`);
  }
}
if (!fs.existsSync(TEMPLATES)) fail(`템플릿 없음: ${TEMPLATES}`);

function copyIfMissing(rel) {
  const dest = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  if (fs.existsSync(dest)) return false;
  fs.copyFileSync(path.join(TEMPLATES, rel), dest);
  return true;
}
function copyAlways(rel) {
  const dest = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(path.join(TEMPLATES, rel), dest);
}

console.log('');
console.log(`  DOMANGCHA v${VERSION} — 경량 자율개발 루프 설치`);
console.log(`  대상: ${ROOT}`);
console.log('');

if (!fs.existsSync(path.join(ROOT, '.git'))) {
  execSync('git init -q', { cwd: ROOT, stdio: 'ignore' });
  say('git 저장소 초기화');
}

// 기존 CLAUDE.md 자동 이관 (기본 동작, --no-migrate 로 끔)
const claudeMd = path.join(ROOT, 'CLAUDE.md');
let migrated = null;
if (!has('--no-migrate') && fs.existsSync(claudeMd)) {
  const existing = fs.readFileSync(claudeMd, 'utf8');
  const isLoopKit = existing.includes('@LOOP.md') || /^# DOMANGCHA v3\./m.test(existing);
  if (!isLoopKit) {
    const heavyDir = path.join(ROOT, '.claude', 'heavy');
    fs.mkdirSync(heavyDir, { recursive: true });
    const dest = path.join(heavyDir, 'CEO.md');
    if (fs.existsSync(dest)) fs.rmSync(dest);
    fs.renameSync(claudeMd, dest);
    migrated = path.relative(ROOT, dest);
  }
}

copyAlways(path.join('scripts', 'loop.mjs')); // 항상 최신 CLI 로 갱신
const placed = [];
for (const rel of [
  'LOOP.md',
  'CLAUDE.md',
  path.join('.claude', 'commands', 'plan.md'),
  path.join('.claude', 'commands', 'loop.md'),
  path.join('.claude', 'commands', 'policy.md'),
  path.join('.cursor', 'rules', 'loop.mdc'),
]) if (copyIfMissing(rel)) placed.push(rel);

if (has('--agents')) {
  for (const link of ['AGENTS.md', 'GEMINI.md']) {
    const dest = path.join(ROOT, link);
    if (fs.lstatSync(dest, { throwIfNoEntry: false })) fs.rmSync(dest, { force: true });
    fs.symlinkSync('LOOP.md', dest);
  }
  say('AGENTS.md, GEMINI.md 심볼릭 링크 생성 (Codex, Gemini CLI 용)');
}

say(`scripts/loop.mjs 갱신${placed.length ? `, 신규 ${placed.join(', ')}` : ', 기존 규정 파일 보존'}`);
if (migrated) say(`기존 CLAUDE.md → ${migrated} 자동 이관 (LOOP.md 5절 중량 모드에서 읽음)`);

const name = path.basename(ROOT);
execSync(`node scripts/loop.mjs init --project ${JSON.stringify(name)} --cursor`, { cwd: ROOT, stdio: 'inherit' });

try {
  execSync('git add -A', { cwd: ROOT, stdio: 'ignore' });
  execSync(`git commit -qm "v${VERSION}: DOMANGCHA 경량 루프 설치"`, { cwd: ROOT, stdio: 'ignore' });
} catch { /* 변경 없음 또는 git author 미설정, 무시 */ }

console.log('');
say(`설치 완료 · 프로젝트 ${name}`);
say('다음 단계: Claude Code 를 열고 하고 싶은 일을 자연어로 그냥 말하면 됨 (슬래시 커맨드 불필요)');
say('전체 18 에이전트 설치가 필요하면 npx domangcha --full');
console.log('');
