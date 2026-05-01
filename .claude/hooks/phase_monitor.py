#!/usr/bin/env python3
"""Stop hook — Sustained Research Cycle phase monitor.

매 응답 종료 후 transcript 의 마지막 assistant message 를 읽어
Phase 상태 token 을 검출, 다음 Phase 의 prompt 를 주입하여
Claude 가 자동으로 다음 turn 에 진입하게 한다.

Token → continuation prompt 매핑:
- [Phase 1 complete] → Phase 2 turn 1 시작
- [Phase 2 turn N in progress] → Phase 2 turn N+1 진행
- [Phase 2 complete] → Phase 3 시작
- [Phase 3 complete] 또는 [Cycle complete, next ideation ready] → 다음 cycle Phase 1
- 토큰 없음 → continue X (자연 종료)

stop_hook_active 는 hook system enabled 신호 (항상 true) — 루프 방지 X.
무한 루프 방지: token 미명시 응답 = 자연 종료. 또한 turn 카운터 안전장치.

매 실행 /tmp/phase_monitor.log 에 logging.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("/tmp/phase_monitor.log")
STATE_PATH = Path("/tmp/phase_monitor_state.json")
DEDUPE_WINDOW_SEC = 90  # 동일 token 90초 내 재emit 방지 (race condition)


def log(msg: str) -> None:
    """Append timestamped line to log."""
    ts = datetime.now().isoformat(timespec="seconds")
    try:
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(f"[{ts}] {msg}\n")
    except OSError:
        pass


SYSTEM_USER_MARKERS = (
    "<task-notification>",
    "<system-reminder>",
    "[SYSTEM NOTIFICATION",
    "tool_result",
    "Stop hook feedback",  # hook 자기 주입 prompt
    "Stop hook blocking error",
    "UserPromptSubmit hook",
)


def is_real_user_message(msg: dict) -> bool:
    """task-notification / system-reminder / tool_result 는 진짜 user 가 아님."""
    content = msg.get("content")
    text = ""
    if isinstance(content, str):
        text = content
    elif isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "tool_result":
                    return False  # tool result is not a real user message
                if block.get("type") == "text":
                    parts.append(block.get("text", ""))
        text = "\n".join(parts)
    if not text.strip():
        return False
    return not any(marker in text for marker in SYSTEM_USER_MARKERS)


def read_last_assistant_text(transcript_path: str, lookback: int = 50) -> str:
    """Transcript JSONL 의 마지막 *진짜* user message 이후의 모든 assistant text.

    Claude Code 가 한 응답을 여러 entry 로 split 기록.
    또한 task-notification / system-reminder user entries 는 *boundary* 로 인정 X
    (그것은 monitor event 또는 system 알림이지 사용자 응답 아님).
    """
    path = Path(transcript_path)
    if not path.exists():
        return ""

    entries = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    texts = []
    for entry in reversed(entries):
        msg = entry.get("message")
        if not isinstance(msg, dict):
            continue
        role = msg.get("role")
        if role == "user":
            if is_real_user_message(msg) and texts:
                break  # 진짜 user message 만나면 stop
            continue  # task-notification / system-reminder / tool_result 는 무시
        if role != "assistant":
            continue

        content = msg.get("content")
        block_text = ""
        if isinstance(content, str):
            block_text = content
        elif isinstance(content, list):
            parts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    parts.append(block.get("text", ""))
            block_text = "\n".join(parts)
        if block_text:
            texts.append(block_text)
        if len(texts) >= lookback:
            break

    return "\n".join(reversed(texts))


def detect_phase_token(text: str) -> str:
    """*마지막* phase token 검출 — 본문에 여러 token 있으면 가장 끝쪽이 진짜.

    역순 line 검사 + 최초 발견 token return (그게 응답 마지막 token).
    """
    # 역순 line 별 검사
    lines = text.split("\n")
    for line in reversed(lines):
        line = line.strip()
        if re.search(r"\[Cycle complete[^\]]*\]", line):
            return "cycle_complete"
        if re.fullmatch(r"\[Phase 3 complete\]", line):
            return "phase3_complete"
        if re.fullmatch(r"\[Phase 2 complete\]", line):
            return "phase2_complete"
        m = re.fullmatch(r"\[Phase 2 turn (\d+) in progress\]", line)
        if m:
            return f"phase2_turn_{m.group(1)}"
        if re.fullmatch(r"\[Phase 1 complete\]", line):
            return "phase1_complete"
    return ""


CONTINUATION_PROMPTS = {
    "phase1_complete": (
        "Cycle Phase 2 turn 1 진입.\n\n"
        "직전 Phase 1 의 planning.md 가설 검증 시작.\n"
        "본 turn 의무:\n"
        "1. 가설에 필요한 자료 (paper sections, lemmas, candidates) enumeration.\n"
        "2. Specialist blind round (Tier 1 + 관련 Tier 2 최소 4명) — SPECIALISTS.md Blind Round Protocol.\n"
        "3. 검증/audit 작업 시작 (work.md 누적).\n\n"
        "응답 끝에 [Phase 2 turn 1 in progress] 또는 진전 X 시 [Phase 2 turn 1 stuck] 명시.\n"
        "honest scope 유지. paper-direct anchor. NOVEL spree 거부."
    ),
    "phase2_turn_N": (
        "Cycle Phase 2 turn N+1 진입.\n\n"
        "직전 turn 의 work.md 진전 검토 + 다음 step:\n"
        "- DoD 항목 추가 검증 / specialist cross-examination / 새 sub-claim.\n"
        "- 막혔으면 우회 후보 또는 다른 specialist 시각.\n"
        "- 진전 X 3 turns 연속 시 Phase 2 종결 (안전장치).\n\n"
        "응답 끝에 [Phase 2 turn N+1 in progress] 또는 [Phase 2 complete] 명시.\n"
        "honest scope 유지."
    ),
    "phase2_complete": (
        "Cycle Phase 3 진입 — Conclusion + Meta-learning.\n\n"
        "본 turn 의무:\n"
        "1. attempt 폴더에 postmortem.md 작성 (표준 양식).\n"
        "2. learnings/sustained_research_log.md 갱신 — 본 cycle meta 교훈.\n"
        "3. learnings/intuition_calibration.md 갱신 — Phase 1 직관 score vs 결과 비교.\n"
        "4. lemmas/walls.md 갱신 (해당 시).\n"
        "5. *novel content N/10* 정직 평가.\n\n"
        "응답 끝에 [Phase 3 complete] 명시."
    ),
    "phase3_complete": (
        "Cycle 종료 → 다음 cycle Phase 1 Ideation 진입.\n\n"
        "본 turn 의무 (HARNESS §Sustained Research Cycle Phase 1):\n"
        "1. 직전 5-10 attempts postmortem 검토 + sustained_research_log.md + intuition_calibration.md 직접 인용.\n"
        "2. 새 attempt 폴더 NNN_cycleN_ideation_phase1 생성.\n"
        "3. planning.md 작성 — *직관 훈련 섹션 의무* (후보별 first-impression score + 근거).\n"
        "4. Cross-domain pass §6 + Specialist 패널 §7 (blind round Phase 2 에서).\n"
        "5. 1개 narrow hypothesis 선택 + DoD + 막힘 예측 + 진전/stuck 판정 기준.\n"
        "6. lemmas/dont_try_directions.md Cut 1-7 self-check.\n\n"
        "응답 끝에 [Phase 1 complete] 명시.\n"
        "honest scope 유지. paper-direct stamp 외 야심 가설 우선."
    ),
    "cycle_complete": None,  # phase3_complete 와 동일 — 아래 매핑
}


def get_continuation(token: str) -> str:
    """Token → continuation prompt. phase2_turn_N 의 N 추출하여 N+1 명시 prompt."""
    if token == "cycle_complete":
        return CONTINUATION_PROMPTS["phase3_complete"]
    if token.startswith("phase2_turn_"):
        try:
            n = int(token.split("_")[-1])
        except ValueError:
            n = 0
        next_n = n + 1
        return CONTINUATION_PROMPTS["phase2_turn_N"].replace(
            "turn N+1", f"turn {next_n}"
        ).replace("turn N+1 in progress", f"turn {next_n} in progress")
    return CONTINUATION_PROMPTS.get(token, "")


def load_state() -> dict:
    """직전 emit state 읽기 — race condition dedupe 용."""
    if not STATE_PATH.exists():
        return {}
    try:
        with STATE_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    try:
        with STATE_PATH.open("w", encoding="utf-8") as f:
            json.dump(state, f)
    except OSError:
        pass


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        log("ERROR: invalid JSON stdin")
        return 0

    transcript_path = payload.get("transcript_path", "")
    log(f"fired: cwd={payload.get('cwd', '?')} transcript={transcript_path}")

    text = read_last_assistant_text(transcript_path)
    text_tail = text[-300:] if text else "(empty)"
    log(f"last assistant tail: {text_tail!r}")

    token = detect_phase_token(text)
    log(f"token detected: {token or '(none)'}")
    if not token:
        return 0

    # Dedupe: 같은 token 을 최근에 emit 했으면 skip (race condition 방지)
    import time
    now = time.time()
    state = load_state()
    last_token = state.get("last_token")
    last_emit_ts = state.get("last_emit_ts", 0)
    last_transcript = state.get("last_transcript", "")
    if (
        last_token == token
        and last_transcript == transcript_path
        and now - last_emit_ts < DEDUPE_WINDOW_SEC
    ):
        log(
            f"DEDUPE: same token={token} within {now - last_emit_ts:.1f}s, skip "
            "(race condition — transcript flush 대기)"
        )
        return 0

    prompt = get_continuation(token)
    if not prompt:
        log("no continuation prompt mapped")
        return 0

    output = {"decision": "block", "reason": prompt}
    log(f"emitting decision=block, reason length={len(prompt)}")
    save_state({"last_token": token, "last_emit_ts": now, "last_transcript": transcript_path})
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
