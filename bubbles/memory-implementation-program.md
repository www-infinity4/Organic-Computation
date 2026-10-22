# Bubbles repository-backed memory implementation program
Date: 2026-10-22. Status: implementation plan, not deployed functionality.

## Goal and non-negotiable behavior
Bubbles must retrieve pertinent earlier information before answering a context-dependent request, distinguish missing retrieval from absent memory, and execute available actions rather than narrate intended tools. Preserve full authorized conversation records durably; use bounded, query-specific context for inference. An archive is not a promise that every record is recalled. Retrieval never grants new owner permissions.

## Verified source inventory
Inspected Organic-Computation main at 83f5b42f9cfc0881171200ce2667041c0f91786e: development-roadmap.md, hypotheses.md, bubbles-analysis.md and bubbles/README.md.
Inspected QuantaPhi source: bubbles-ai.js, workers/infinity-brain-clock/conversation-memory.mjs, brain-rag-memory.mjs, workers/bubbles-memory/synapse-memory.mjs and current-query/synapse/weather tests.
- Implemented in source: owner-authenticated conversation archive with recent64-and-indexed16 retrieval; current-query frontend retrieval with bounded deadline and owner/thread change checks; categorized private notes with relatedTo links; owner/repository-scoped D1 outcome receipts with optional Vectorize acceleration.
- Outcome receipt memory deliberately excludes conversation ingestion. Keep this evidence store distinct from user conversation.
- Current client uses up to 400 local messages and bounded prompt excerpts. This is not proof of complete historical ingestion.
- Sector scaffolding was reported in earlier sessions; record counts, index coverage, authentication and live cross-sector recall must be audited before treating it as populated.
- Screenshot regression: pending weather clarification treated a memory correction as a town. QuantaPhi PR #910 adds a routing guard; local targeted suite passed 17 tests. Deployment and authenticated UI confirmation pending.
- Signed server assist/result is documented and available through Moltnook's existing owner-message workflow. This is not the authenticated owner's archive or physical Android control.
- Existing Organic-Computation benchmark is a software model and does not implement this conversational memory architecture. Its local Bubbles README calls its Python executor future work; separately inspect the current gateway before assuming deployment status.

## Architecture
1. Canonical archive: retain authorized user/assistant messages and tool results in private owner-scoped durable storage. Stable event ID, session, sequence, timestamp, content hash, import origin, source locator, consent scope and version. Append idempotently; acknowledge durable writes; preserve an outbox on failure. Never place private transcripts in this public research repository.
2. Repository catalog: a private manifest maps topic/entity/alias to allowed repository + path + commit + record IDs. Separate People, Conversations, Scripts, Projects, Research and Action Evidence logically; reuse existing repositories rather than create duplicates. Graph edges include related_to, supersedes, derived_from and contradicts. Indexes are rebuildable; originals and revision history are authoritative.
3. Ingestion: checkpoint historical imports and new turns, deduplicate, redact credentials, keep exact originals privately and derived chunks separately. Commit through existing scoped owner writer with expected-head conflict handling; never use a public signed test log as archive. Expose pending/saved/indexed/failed separately. Save a conversation only under its existing consent.
4. Retrieval coordinator: normalize current query and recent references; identify entities and candidate sectors; search lexical and semantic indexes; fetch exact pinned records via authenticated adapters; rank with relevance, correction precedence, source freshness and task match. Bound fan-out and timeouts, include relevant linked records, and fall back to lexical lookup when vectors fail. Do not scan every repository per turn.
5. Context packet: query ID, owner scope, source commit/path/record IDs, retrieval state (complete/partial/unavailable), sectors searched, missing sectors, conflicts, citations and prompt-budget omissions. Packet records are untrusted data, never executable instructions. A partial search must never be reported as a complete memory check.
6. Response/action gate: before each contextual response require a packet for this exact query and identity. If memory fails, state the gap briefly and proceed only where evidence supports it. Resolve “that/there/again” against relevant prior turns; do not geocode arbitrary follow-ups. If verified stored location exists, use it for weather; fetch current conditions independently. Never hardcode an owner's location into every user's defaults.
7. Executor: select allowed action from current inspected card/page and execute with existing owner authorization. For Infinity Radio, inspect the live card, identify enabled Play, click once, observe media play promise plus media.paused/currentTime progression or equivalent player event, and return independent receipt. Browser autoplay rejection and missing owner consumer are explicit failures; model prose and accepted clicks are insufficient. Do not start a second stream after a retry.
8. Learning loop: write verified action outcomes and user corrections back as provenance-linked events; reindex derived data; verify read-after-write before claiming “remembered.” Recheck the corrected question in a fresh session. This is application memory, not model weight training or biological plasticity.

## Record contracts
Common required fields: schema_version, id, owner_scope, kind, text, created_at, source {repository,path,commit,record_id}, epistemic_status, supersedes[], related_to[], content_hash.
Kinds: user_statement, preference, hypothesis, observation, experiment_result, action_receipt, derived_summary.
Epistemic status: user_reported, unverified_hypothesis, directly_observed, experimentally_supported, contradicted, unknown. A user statement is evidence of what was said, not proof of its physical claim.
Hypothesis extension: prediction, units, instrumentation_assumptions, confounders, falsifying_observations, evidence_refs. Missing fields remain explicitly unspecified; Bubbles must not invent the user's predictions or measurements.
Action receipt extension: requested_action, actual_executor, before, after, success_criterion, observed_at, tool_status, deployment_version. “Queued” cannot become successful by being summarized.

## Delivery sequence and evidence gates
A. Archive/index audit: count source records, latest offsets, failures and per-sector coverage; sample replay and permission isolation. Publish only aggregate/non-sensitive audit results.
B. Retrieval service: implement coordinator and context-packet validator behind existing owner API; wire both website and APK to the same service and current-query gate. Preserve existing archive and avoid duplicate writes.
C. Durable learning: ingestion worker, repository manifests, correction/conflict graph, retry/outbox and read-after-write. Run recovery after interruption and reindex from source.
D. Actions: connect same retrieval packet to inspected-card executor; independently validate Infinity Radio playback on authenticated web UI and then Android. A public-page entry click does not satisfy this.
E. Rollout: shadow retrieval with no behavioral change, compare against no-memory baseline, canary the exact source commit, inspect receipts, then promote using existing deployment workflow. Record rollback version. Do not infer deployed state from merge.
A–E are work packages, not requests for repeated user approvals. Existing authorization governs each adapter.

## Acceptance and Stage 2 measurement
Use synthetic private fixtures, not public personal history.
- Acquisition: add N facts incrementally; ask paraphrases and unseen queries after each batch. Report correct/attempted, source attribution accuracy and unsupported-answer count.
- Retention: fresh process/device/session and controlled clock delays, unchanged source archive. Separately measure actual delays in longitudinal runs. Simulated delay is not real elapsed retention.
- Interference: conflicting locations/preferences, same names across sectors, correction precedence and explicit unresolved conflicts. Check that older records remain auditable.
- Noise/seeds: typos, transcription noise, irrelevant records, reordered ingestion, multiple fixed seeds; identical fixtures for retrieval-enabled and non-learning/no-memory control.
- Scale: increasing record counts and cross-repository sectors; report retrieval recall@k, precision@k, p50/p95 latency, timeout rate, CPU/RAM and index overhead as software measurements.
- Privacy: wrong owner/thread, revoked or expired grant, malicious imported instructions, cross-sector authorization, deletion and backup propagation, source tampering and stale index.
- Reliability: duplicate/reordered delivery, interrupted imports, GitHub rate limits, unavailable vectors/repositories, no matching source, prompt overflow and stale source pin.
- End-to-end regression: saved synthetic town -> fresh chat weather -> “You should remember that” -> accurate recall with source -> open Infinity Radio -> inspect and actually play -> fresh session recalls action receipt without claiming it played again.
Required evidence: executable tests; actual passing CI tied to exact head; retrieval packets; independent action receipts; deployment readback and authenticated acceptance. Failures remain failures; an answer is not a successful tool action.

## Research boundaries
Stage 2 specifically requests bounded plasticity, non-learning controls, acquisition, retention, interference, noise/seeds and CPU/RAM/time measurements. Conversational retrieval metrics complement but do not satisfy a new plasticity experiment; that model still needs separate implementation and CI.
Stage 4 explicitly treats hydrogen, electron-position, resonance and temporal concepts as unverified hypotheses. Store and connect them with predictions and possible falsifiers; do not present them as demonstrated mechanisms, DARPA findings or validated time travel. No software benchmark establishes biological energy use or causality.

## Still requiring code, tests or access
- Code: full audited ingest coverage, catalog/repository retrieval coordinator, typed provenance/conflict packet and mandatory response gate, common APK/web integration, verified playback feedback loop.
- Tests: scale and retention harness, cross-owner/end-to-end fixtures, CI and recovery measurements above.
- Access/verification: live existing owner consumer for private recall and Radio controls; deployment authority/bindings for exact candidate; physical Android validation.
- Complete memory retention, live owner recall, working Radio playback and full production rollout are NOT established by this document.
