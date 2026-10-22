# Connecting the Organic Computation benchmark to Bubbles

The `organic_computation.benchmark` contract in [`organic-tool.json`](./organic-tool.json) defines a **future read-only Bubbles tool**. It does **not** register the tool or give the Bubbles runtime a Python interpreter merely by being placed in GitHub.

The existing Bubbles signed owner runner can continue researching this repository, and can show source-backed files. A future executor should take validated integers, start an ephemeral isolated Python 3.12 process with no network or credentials, invoke `python3 -m simulations.benchmark`, validate the JSON result, and return a signed receipt including the pinned source commit and arguments. Only then advertise it as runnable.

**Must pass before enabling:** simulated output JSON schema and provenance; exact seed/trials echoed; repeatability; cross-user separation; intentionally malformed input rejected; revoked tool access rejected; error and timeout surfaced; source commit and deployed version matched; Android and website UI displays scientific limitations. It must not authorize Robot Brain, repository writes, wallet changes or external account operations.

Until that is done, the Bubbles catalog may show a link to the research repository with `source_ready_not_deployed` status and natural-language instructions to interpret the method, but should not show a Run button that falsely promises execution.
