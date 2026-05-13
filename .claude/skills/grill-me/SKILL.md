---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when the user wants to stress-test a plan, get grilled on their design, or says "grill me".
---

Interview the user relentlessly about every aspect of their plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, give your recommended answer with reasoning.

Ask one question at a time. No batching, no lists of questions.

If a question can be answered by exploring the codebase or sibling projects, explore instead of asking. For `audit-hq`, the relevant reference projects already on disk are:
- `~/workspace/client/Johnson` — BCQT pipeline for one DN (SAP MB51/MB5B + BCCT → Mẫu 15/15a/16). Phase 3 audit tests + Phase 4 anomaly investigation are directly relevant.
- `~/workspace/client/BCQT-System` — productized BCQT system. Architecture, adapter pattern, findings/CheckSpec, data model.
- `~/workspace/client/barry-CO-main` — CO (Certificate of Origin) tooling. Only archive ingestion + Data Hub adapter pattern are relevant.

Recommendations must be grounded in concrete evidence — cite a file/line, a regulation (TT 38/2015, TT 39/2018, TT 121/2025, QĐ 1357/QĐ-TCHQ), or a lesson from a prior project. Avoid generic-principle recommendations when project evidence exists.

When the user gives a vague answer ("we'll figure it out", "probably fine", "tuỳ"), push back once. If they still can't sharpen it, note as an open question and move on — don't let it bluff.

Stop when major branches of the decision tree are resolved or the user says enough. End with a short summary:
- **Decided** — what's settled, with the user's answers
- **Open** — what's deferred, and what's needed to close it
- **Next step** — the smallest concrete thing to do next
