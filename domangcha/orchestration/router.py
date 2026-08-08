from __future__ import annotations

from typing import Any, Dict, Optional

from .contracts import Route, RouteDecision


class TaskRouter:
    """Single deterministic routing authority for DIRECT, LOOP, and GRAPH."""

    GRAPH_SIGNALS = {"security", "destructive", "architecture", "parallel", "resume"}
    SCORE = {
        "mutation": 2, "database": 4, "api": 2, "frontend": 2,
        "security": 5, "destructive": 5, "architecture": 5,
        "parallel": 4, "resume": 5, "external": 3, "iterative": 2,
    }

    def route(
        self,
        intent: Dict[str, Any],
        proposed: Optional[Dict[str, Any]] = None,
        minimum: Optional[Route] = None,
    ) -> RouteDecision:
        signals = set(intent.get("signals", []))
        reasons = []
        approval = "destructive" in signals

        if intent.get("read_only") and "mutation" not in signals:
            decision = RouteDecision(Route.DIRECT, -5, ["read-only deterministic task"])
            return self._apply_minimum(decision, minimum)

        if {"database", "api", "frontend"}.issubset(signals):
            reasons.append("database + API + frontend invariant")
            decision = RouteDecision(Route.GRAPH, 11, reasons, approval)
            return self._validated_proposal(decision, proposed, minimum)

        hard = signals.intersection(self.GRAPH_SIGNALS)
        if hard:
            reasons.append("hard graph invariant: " + ", ".join(sorted(hard)))
            decision = RouteDecision(Route.GRAPH, sum(self.SCORE[x] for x in signals), reasons, approval)
            return self._validated_proposal(decision, proposed, minimum)

        score = sum(self.SCORE.get(signal, 0) for signal in signals)
        files = int(intent.get("estimated_files", 0) or 0)
        if files == 1 and signals == {"mutation"}:
            score -= 2
            reasons.append("isolated one-file deterministic mutation")
        elif 2 <= files <= 3:
            score += 1
        elif 4 <= files <= 7:
            score += 3
        elif files >= 8:
            score += 5
        if score <= 1:
            route = Route.DIRECT
        elif score <= 6:
            route = Route.LOOP
        else:
            route = Route.GRAPH
        reasons.append("deterministic complexity score=%d" % score)
        ambiguous = score in {1, 2, 6, 7}
        decision = RouteDecision(route, score, reasons, approval, ambiguous)
        return self._validated_proposal(decision, proposed, minimum)

    def escalate(self, current: Route, reason: str) -> RouteDecision:
        target = Route.LOOP if current == Route.DIRECT else Route.GRAPH
        if current == Route.GRAPH:
            target = Route.GRAPH
        return RouteDecision(target, 0, ["escalated: " + reason])

    def _validated_proposal(self, decision, proposed, minimum):
        if proposed and decision.ambiguous:
            try:
                candidate = Route(proposed.get("proposed_route", ""))
                decision.proposed_route = candidate
                if self._rank(candidate) >= self._rank(decision.route):
                    decision.route = candidate
                    decision.reasons.append("validated semantic proposal")
            except (TypeError, ValueError):
                decision.reasons.append("invalid semantic proposal ignored")
        return self._apply_minimum(decision, minimum)

    def _apply_minimum(self, decision, minimum):
        if minimum and self._rank(minimum) > self._rank(decision.route):
            decision.route = minimum
            decision.reasons.append("command minimum route")
        return decision

    @staticmethod
    def _rank(route: Route) -> int:
        return {Route.DIRECT: 1, Route.LOOP: 2, Route.GRAPH: 3}[route]
