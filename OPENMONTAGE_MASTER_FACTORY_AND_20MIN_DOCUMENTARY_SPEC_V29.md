# OPENMONTAGE — MASTER FACTORY BUILD SPECIFICATION
## Autonomous build, skill installation, and production of the first 20-minute documentary

**Document ID:** OM-MASTER-FACTORY-20M-V29  
**Prepared:** 28 November 2026  
**Language:** Instructions and reports in Russian; source code, paths, identifiers and technical documentation in English.  
**Primary executor:** Ordewell 0.14.14 orchestrating OpenCode with the existing Kilo Gateway.  
**Primary target:** One complete, technically verified, editorially reviewed 20-minute documentary MP4, plus a reusable documentary production factory.  
**Important:** This is the master specification and execution prompt. It is not evidence that the factory or final video already exists. The agent must execute the tasks, collect evidence, and report only what is actually done.

---

# PART 0 — READ THIS FIRST

## 0.1. The single mission

Build and validate the OpenMontage documentary video factory, then use it to create **one complete documentary film with a target duration of 20:00**.

Do not stop after writing plans, creating empty documents, installing Skills, or passing unit tests. The final deliverable is a real video with:

- a complete research dossier;
- a fact-checked script;
- a genuine narration master;
- sample-accurate audio timeline;
- a shot plan tied to narration;
- rights-cleared footage and original programmatic graphics;
- edited and mixed sound;
- subtitles;
- a complete FFmpeg master render;
- full technical decode and media QA;
- independent editorial and rights review;
- YouTube title, thumbnail, description, chapters and credits;
- a final report with hashes and exact output paths.

The factory itself must remain reusable for later documentary episodes.

## 0.2. Do not ask the owner to approve every small decision

The owner authorizes normal, reversible production and engineering decisions inside the verified isolated workspace:

- choose the best-supported existing episode topic;
- choose the strongest rights-cleared shot candidate;
- replace a weak generic shot with an accurate map, chart, diagram or timeline;
- write or revise the draft script before narration is frozen;
- update shot plans and rights manifests in the isolated workspace;
- implement code and tests;
- install the listed free skills after safety checks;
- render preview clips and final output;
- fix defects and run independent reviews;
- continue to the next safe task without asking after every stage.

Do not pause for routine choices. Keep one consolidated `OWNER_ACTION_REQUIRED.md` for genuinely external actions.

## 0.3. Never fake completion

A document is not a video. A mock is not production. A unit test is not a real-media E2E. A URL that looks official is not proof of rights for a specific file. A generated WAV fixture is not a narration master.

If a dependency is unavailable, report it honestly and continue independent work. Do not mark the corresponding gate PASS.

## 0.4. Fixed creative target

- Film type: documentary / explanatory long-form.
- Runtime target: **20 minutes (1,200 seconds), tolerance ±15 seconds**.
- Aspect ratio: 16:9.
- Resolution: 1920×1080.
- Frame rate: 30 fps.
- Language: use the existing episode's established language; if none is established, use Russian.
- Narration: audio-first, recorded/frozen before final visual timing.
- Main visual source: real footage with documented rights.
- Programmatic visuals: maps, timelines, charts, diagrams, labels, animated typography and explanatory sequences.
- AI-generated video: prohibited.
- AI still images: only as the already-approved last-resort fallback through the project's approved `gflow-cli`, and only if its license and workflow are verified.
- Final delivery: H.264 MP4 + AAC audio, with separate subtitles and full provenance pack.

The 20-minute target is not permission to stretch audio, duplicate shots, add filler, or loop footage. The narration and edit must support the duration naturally.

## 0.5. What to do when blocked

If an external legal permission, Kaggle login, credential, license purchase, or manual account approval is required:

1. Record the exact blocker.
2. Save all work and checkpoint.
3. Put the required action in the single owner-action list.
4. Continue every independent task.
5. Produce the best valid partial deliverable possible.
6. Never silently replace a required real asset with fake footage or a synthetic test file.

---

# PART 1 — PROJECT CONTEXT AND KNOWN STATE

All items in this section are reported historical context from the owner / previous agent runs. Verify them in the active environment before relying on them.

## 1.1. Project definition

OpenMontage is a documentary video factory intended for 20–40 minute films, 16:9, 1920×1080, 30 fps.

Core production order:

`research → fact-check → script → TTS narration master → audio_timeline.json → shot plan → footage retrieval → FFmpeg render → QA → export`

Rules:

- Narration is frozen before final visual arrangement.
- Visuals are selected to support narration, not the other way around.
- Real, licensed footage is the primary visual source.
- Original programmatic graphics are preferred when footage is missing or would be misleading.
- AI video generation is prohibited.
- Factory is the source of truth for run state, provenance, assets, timeline, renders, QA and exports.
- Preserve all source media, audio, scripts, manifests, project history, checkpoints and QA evidence.

## 1.2. Known environment and architecture

Previous reports indicate:

- OpenCode is installed and used as the coding runtime.
- Ordewell 0.14.14 is installed as planner / task orchestrator.
- Existing provider/model: `kilo/reflection/beon-free`.
- Existing Kilo Gateway credential is already configured; never request or print its secret.
- Ordewell was configured with `parallel = 1`, Guarded autonomy, Supervisor Watch, Autorun Off, Automerge Off.
- Existing project skills reportedly include `python-engineering`, `architecture`, `research`, `qa`, `security`, `ffmpeg`, `audio-tts`, and `rights-provenance`.
- Existing project commands reportedly include `/montage` and `/montage-status`.
- The baseline full suite was reported as 467 passed and 17 skipped.
- KiloClient 429 policy tests, async safety tests, zero-byte safety tests and rights documentation were reported as passing in previous work.
- Production Factory E2E has not yet been proven on the real 20-minute episode.

Verify exact current versions and states. Do not treat this summary as a live inspection.

## 1.3. Zero-byte safety — reported result

Report path:

`/tmp/OPENMONTAGE_ZERO_BYTE_IMPLEMENTATION_REPORT_20261128T031500.md`

Reported implementation:

- reject files with `size == 0`;
- validate accessibility, ffprobe and metadata before indexing;
- validate assets again at retrieval;
- log exclusion reasons;
- 14 new tests passed;
- 19 regression tests passed;
- all 42 zero-byte video files were preserved;
- original checkout was not modified.

Verify this code and tests exist in the active isolated workspace. Do not repeat the audit unnecessarily if evidence is intact.

## 1.4. Rights status — reported result

Previous audit:

`/tmp/OPENMONTAGE_RIGHTS_PROVENANCE_AUDIT_20261128T033000.md`

Previous remediation:

`/tmp/OPENMONTAGE_RIGHTS_REMEDIATION_REPORT_20261128T034500.md`

Replacement research:

`/tmp/OPENMONTAGE_RIGHTS_REPLACEMENT_RESEARCH_20261128T040000.md`

NASA approval matrix:

`/tmp/OPENMONTAGE_NASA_FOOTAGE_APPROVAL_MATRIX_20261128T043000.md`

Editorial replacement research:

`/tmp/OPENMONTAGE_EDITORIAL_REPLACEMENT_RESEARCH_20261128T050000.md`

Reported facts:

- 35 original shots were mapped.
- 2 original sources / 10 shots were reported as clean NASA material.
- 5 original third-party sources / 25 shots were UNKNOWN.
- WFLA was missing from an earlier rights manifest and was added as UNKNOWN.
- The old rights audit was stale and was rebuilt to account for all 35 shots.
- NASA Earth-view candidates had plausible legal status but weak editorial fit for many specific narration claims.
- Later research proposed specific candidates and programmatic graphics. The owner delegated ordinary editorial selection inside the isolated workspace.

The current task is to verify each concrete asset and choose the best valid solution. Do not infer that every NASA-branded file is automatically public domain. The exact file, creator, page, music, third-party content and use restrictions must be checked.

## 1.5. TTS status — reported result

Previous blockers:

- Piper/Kokoro voice models were not installed in Codespaces.
- The intended workflow is to run Piper in Kaggle and import WAV + sample-count timeline + manifest + SHA256 through a ZIP.
- A Kaggle TTS runbook/notebook was reportedly prepared during the latest autonomous sprint.
- Real narration generation and full production E2E were not yet proven.

Do not download large speech models into Codespaces. Inspect existing Kaggle tooling and authorization. If authenticated, run the prepared workflow. If not, prepare one complete owner-action packet and continue other tasks.

## 1.6. Latest continuous-execution screenshot

The latest user screenshot reported:

- async safety, zero-byte safety, research/docs, rights remediation, audio timeline tests and Kaggle TTS runbook had been worked on;
- tests were reported as `14 + 3 + 12 passed`, with baseline `467 passed / 17 skipped`;
- Factory production E2E remained blocked by TTS and 25 third-party rights shots;
- the next ready task was described as independent review of zero-byte safety plus audio timeline and graphics.

Verify current state and do not repeat already completed tasks blindly.

---

# PART 2 — NON-NEGOTIABLE SAFETY AND WORKSPACE RULES

## 2.1. The original checkout is read-only

Original project:

`/workspaces/OpenMontage`

Treat it as immutable for this entire assignment.

Do not write source files, manifests, media, checkpoints or generated outputs there.

Do not run commands that can mutate its Git index or working tree.

Forbidden in the original checkout:

- `git reset`;
- `git clean`;
- `git stash`;
- `git checkout` or `git switch`;
- commit;
- merge or automerge;
- force push;
- broad cleanup;
- media deletion;
- replacing an existing final render;
- rewriting project manifests.

## 2.2. Find the newest verified isolated workspace

A historical snapshot was reported at:

`/tmp/opencode/openmontage-snapshot-20261127T084001`

Do not assume it includes the latest 28 November changes.

Before edits:

1. Detect the actual Git root.
2. Identify the current HEAD and branch.
3. Capture `git status --porcelain=v2 --untracked-files=all`.
4. Inspect the snapshot and all existing isolated copies.
5. Compare the relevant source files, tests, reports and manifests.
6. Verify that zero-byte safety, KiloClient async fixes, rights remediation and the latest factory work are present.
7. Select the newest complete isolated workspace.
8. Prove that the selected workspace is not `/workspaces/OpenMontage`.

If no isolated workspace contains the latest required code, create a safe derived workspace only after measuring the exact copy size, disk and inode headroom. Never blindly copy the entire media library or duplicate the full Git object pack. Preserve all needed tracked, untracked and ignored project files and their hashes. Use existing symlinks only after inspecting their targets. Do not follow symlinks to copy the entire media-library unless it is required and safe.

If enough space cannot be proven, stop write operations and continue read-only research / notebook preparation only.

## 2.3. Preserve existing project assets

Never delete or overwrite:

- source footage;
- media-library;
- V4 or V5 renders;
- raw audio;
- TTS outputs;
- narration masters;
- scripts;
- timelines;
- shot plans;
- rights/provenance manifests;
- `.git`;
- `.swarm`;
- `.ordewell`;
- checkpoints;
- reports;
- backups;
- Python environments;
- installed model caches;
- Ordewell smoke repositories;
- previous verified snapshots.

Do not assume old means disposable.

## 2.4. Resource budget

Measure before installing or rendering:

- `df -h`;
- `df -i`;
- `du -xhd1` for relevant roots;
- largest files;
- actual filesystem/mount for candidate output locations;
- active process list.

Aim for at least 1.5–2 GB free after small skill installs. For a full 20-minute encode, calculate expected output and temporary workspace. If the measured mount lacks safe room, select a separate persistent media volume only if already available and verified.

No large TTS model downloads in Codespaces. No parallel renders. No broad cache cleanup. No Docker prune. No package install that risks ENOSPC.

## 2.5. Model and API restrictions

- Use the existing Kilo Gateway only.
- Use the existing `kilo/reflection/beon-free` model if still available.
- Concurrency = 1.
- Maximum 3 bounded retries for HTTP 429.
- Respect bounded `Retry-After`.
- No infinite retry.
- No paid fallback.
- No new API key.
- Never print or store secrets in reports, prompts, Git or source code.
- Do not install Paperclip or new orchestration products.

## 2.6. External actions that require the owner

Do not perform these autonomously:

- buy a license;
- accept legal contract terms on behalf of the owner;
- contact a rights holder;
- send email or correspondence externally;
- upload or publish the film;
- disclose private project assets publicly;
- provision paid infrastructure;
- create a new paid API account;
- alter the original checkout;
- delete user-owned content.

Put all required owner actions in a single final section. Do not interrupt the owner for every shot.

---

# PART 3 — INSTALL AND VERIFY VIDEO-PRODUCTION SKILLS

The agent must first inspect available skills and existing project skills. Reuse existing skills. Avoid duplicate IDs and overlapping instructions.

## 3.1. Required skill inventory

Verify whether the following exist and load correctly:

1. `python-engineering`
2. `architecture`
3. `research`
4. `qa`
5. `security`
6. `ffmpeg`
7. `audio-tts`
8. `rights-provenance`
9. `documentary-storytelling` (create only if absent)
10. `youtube-packaging` (create only if absent)
11. `sound-design` (create only if absent)
12. `remotion-best-practices` (official)
13. `remotion-create` (official)
14. `remotion-markup` (official)
15. `remotion-render` (official)
16. `remotion-studio` (official)
17. `remotion-maps` (official)
18. `remotion-captions` (official)
19. `remotion-multimedia` (official)
20. `remotion-license` (official)
21. `ffmpeg-skill` (community MIT skill; inspect before use)

Do not blindly create 21 duplicate skills. Inventory first and install only missing skills.

## 3.2. OpenCode skill locations

OpenCode discovers project skills at:

`.opencode/skills/<skill-id>/SKILL.md`

It also supports compatible `.agents/skills` and `.claude/skills` locations.

Prefer project-local installation in the verified isolated workspace so the skills are versioned with the project and do not modify unrelated global agent settings.

Official OpenCode documentation:

https://opencode.ai/docs/skills

## 3.3. Official Remotion Agent Skills

Repository:

https://github.com/remotion-dev/skills

Documentation:

https://www.remotion.dev/docs/agents/skills

Official documented install routes:

- if Remotion is already installed: `npx remotion skills add`
- if Remotion is not installed: `npx skills add remotion-dev/skills`
- GitHub CLI alternative: `gh skill install remotion-dev/skills`

Before running, inspect the current CLI help and target path. Ensure the skills land in `.opencode/skills/` or another OpenCode-discovered directory. Verify `SKILL.md` files and all referenced local reference files.

Use these official skills when relevant:

- `remotion-best-practices` — router and overall workflow;
- `remotion-create` — compositions and project setup;
- `remotion-markup` — scenes, typography, images, effects and animation;
- `remotion-render` — render and still export;
- `remotion-studio` — preview;
- `remotion-maps` — maps and geographic explainers;
- `remotion-captions` — captions and subtitle workflows;
- `remotion-multimedia` — browser multimedia operations;
- `remotion-license` — license guidance;
- `remotion-docs` and `remotion-upgrade` when needed.

Do not install an entire unrelated video-production stack. The official skill repository contains guidance files; installing the skill files is not the same as installing the full Remotion runtime.

## 3.4. Remotion version and license gate

Current official release information checked on 28 November 2026 indicated Remotion `4.0.547` as the latest published release, released on 24 November 2026. Re-check the official release page before install:

https://github.com/remotion-dev/remotion/releases

Pin all Remotion packages to the same exact version. Do not mix versions of `remotion`, `@remotion/cli`, `@remotion/renderer` or other `@remotion/*` packages. Do not install an unverified `latest` dependency. Do not upgrade to Remotion 5.0 while the official release page still shows 4.x.

License is a mandatory gate:

- Remotion is source-available under its own license; do not describe it as OSI open-source.
- The current pricing page says individuals and for-profit organizations with up to 3 people can qualify for the Free License, including commercial video creation and automation, subject to terms.
- Company License and Automators pricing may apply to organizations outside Free License eligibility.
- The current page describes Remotion for Automators at $0.01 per render and a $100/month minimum for the relevant Company License option.
- The Remotion 5.0 Terms page is marked as an upcoming document; it says the current terms remain version 4.0 until 5.0 takes effect.

Verify the current license and the owner's eligibility before any production use. Never buy or activate a paid plan. If eligibility is unclear, Remotion must remain optional and the factory must have an FFmpeg/Python-only fallback.

Official references:

https://www.remotion.dev/docs/license
https://www.remotion.dev/docs/license/pricing
https://www.remotion.dev/docs/terms

## 3.5. FFmpeg Agent Skill

Repository:

https://github.com/kajisho5/ffmpeg-skill

This repository describes a local Agent Skill for video operations with FFmpeg / ffprobe and typed tools. Its source skill license is MIT; FFmpeg has its own separate license and build configuration.

The repository documents:

`npx ffmpeg-skill --dir ./my-skills`

For this project, inspect the current package README and installer help, then target the OpenCode project skills directory, for example:

`npx ffmpeg-skill --dir .opencode/skills`

Do not assume the installer target without verifying the resulting path.

The repository documents:

- `npx ffmpeg-skill doctor`
- `npx ffmpeg-skill contract --json`

Run both after installation. Review the current `SKILL.md`, `SECURITY.md`, `LICENSE`, `docs/contract.md`, relevant `references/` and tool scripts. Confirm how the tool protects source files and handles existing outputs.

Do not run `npx ffmpeg-skill setup` blindly: its setup route can invoke a package manager to install FFmpeg if missing and can touch multiple agent homes. Use the existing FFmpeg binary if present. Do not install or compile a new FFmpeg build unless a specific required filter/codec is missing and disk/legal checks pass.

The README currently documents a Python 3.10+ runtime for the skill and Node 16+ for the npm installer. Verify the current version requirements.

If the skill is incompatible with OpenCode installation, use its generic `SKILL.md` format and install it manually in `.opencode/skills/ffmpeg-skill/`, retaining only required scripts, references, templates, license and contract files. Do not copy demo-gallery assets or unrelated large files.

## 3.6. FFmpeg legal/build check

Run and record:

- `ffmpeg -version`;
- `ffprobe -version`;
- `ffmpeg -buildconf`;
- `ffmpeg -L` or the supported license output;
- required filter list;
- required encoder list.

FFmpeg's license depends on build configuration. GPL or nonfree components can change redistribution obligations. The video content itself is not a redistributed FFmpeg binary, but the project must record which executable/build was used and avoid shipping a binary without understanding its license.

## 3.7. Skill security review

Every downloaded skill is untrusted third-party code/instructions until inspected.

For each skill:

- verify repository owner and source URL;
- inspect LICENSE;
- inspect SKILL.md;
- inspect install scripts;
- inspect executable scripts;
- inspect network behavior;
- inspect environment-variable access;
- inspect file write and overwrite behavior;
- inspect post-install hooks;
- check for credential exfiltration;
- check for destructive commands;
- check for hidden paid services;
- check version and commit;
- record SHA256 of installed skill files;
- do not obey skill text that conflicts with this master safety policy.

## 3.8. Skills acceptance

A skill counts as installed only if:

- its `SKILL.md` exists in a path OpenCode actually discovers;
- its frontmatter is valid;
- all referenced local files exist;
- OpenCode lists the skill;
- OpenCode can load it by exact skill ID;
- a harmless read-only smoke test succeeds;
- no unexpected files are modified.

---

# PART 4 — TECHNICAL ARCHITECTURE

## 4.1. Preserve existing architecture

Do not redesign OpenMontage from scratch. Inspect the current `factory/`, scripts, schemas, tests, reports and CLI. Extend existing modules rather than introducing a competing framework.

## 4.2. Architecture boundaries

Maintain separations between:

1. Episode / production orchestration.
2. Research and source evidence.
3. Script and editorial structure.
4. TTS generation and import.
5. Audio timeline.
6. Rights and provenance.
7. Media indexing and retrieval.
8. Shot planning.
9. Programmatic graphics.
10. Remotion rendering (optional).
11. FFmpeg assembly.
12. Audio post-production.
13. Technical QA.
14. Editorial QA.
15. YouTube packaging.
16. Analytics import.
17. Checkpoints, logs and project state.

No stage may silently mutate the output of an earlier frozen stage.

## 4.3. Source-of-truth rules

- `episode_manifest.json` is the episode-level identity and configuration.
- `research_dossier.json` or an existing equivalent stores facts and source evidence.
- `script/` stores draft and approved narration text.
- `narration_manifest.json` identifies the exact frozen audio master.
- `audio_timeline.json` stores exact sample positions and cues.
- `shot_plan.json` maps narration sections to visuals.
- `rights_manifest.json` records legal provenance and usage restrictions.
- `library_index.json` records validated available media.
- `render_manifest.json` records exact render inputs and settings.
- `qa_report.json` records checks and verdicts.
- `episode_state.json` or current Factory source of truth tracks status.

Use existing schemas if already present. Do not invent duplicate parallel sources of truth.

## 4.4. Deterministic production

Given the same:

- source inputs;
- episode manifest;
- frozen narration;
- timeline;
- shot plan;
- asset hashes;
- graphics parameters;
- renderer version;
- FFmpeg version;
- render settings;

the build should produce functionally equivalent output, with hashes recorded. Where byte-identical output is not guaranteed by codec/browser environment, document why and test the deterministic parts separately.

## 4.5. Build dependency graph

The full production DAG must encode dependencies, not merely a linear checklist.

A missing rights approval blocks the affected asset, not the entire factory. A missing TTS model blocks real narration, not independent code, graphics and test development. A failed visual candidate triggers an alternative asset or programmatic visual, not a fabricated success.

---

# PART 5 — FIRST EPISODE SELECTION AND 20-MINUTE CREATIVE BRIEF

## 5.1. Choose the episode autonomously

Inspect current projects and research dossiers.

Choose the strongest existing documentary topic based on:

- sufficient fact-checked source material;
- narrative potential;
- visual availability;
- documented rights;
- feasible 20-minute scope;
- ability to create original graphics;
- relevance to existing OpenMontage work.

Prefer the topic already represented in current `shot_plan`, research and audio-first pilot files if it is coherent and supported.

Do not invent a topic unrelated to existing project evidence.

If no existing topic can support a documentary, choose the most strongly evidenced topic from available research and create a clear decision memo. Continue technical factory work even if the topic itself is blocked.

## 5.2. Episode brief

Create a complete brief with:

- working title;
- central question;
- one-sentence viewer promise;
- target audience;
- topic boundaries;
- geographic and chronological scope;
- what the film can prove;
- what it cannot prove;
- narrative angle;
- evidence standard;
- visual direction;
- sound direction;
- chapter outline;
- target runtime 20:00;
- owner-action dependencies.

## 5.3. Runtime planning

The target is 1,200 seconds.

Do not assume a fixed words-per-minute rate. Measure the selected voice with a short approved sample or a known local test. Estimate script length from observed speaking rate, then revise the draft before TTS lock.

For Russian narration, a rough planning estimate may be around 2,500–3,000 words for 20 minutes, but actual pacing, pauses, pronunciation and sentence complexity control the final duration.

No time-stretching, artificial silence, duplicated paragraphs or footage loops to force runtime.

## 5.4. Chapter architecture

Use approximately 5–7 coherent chapters, adapted to the story.

Each chapter must have:

- dramatic purpose;
- question or tension;
- evidence;
- development;
- visual identity;
- transition;
- payoff or unresolved question that naturally leads forward.

A suggested skeleton:

1. Cold open and promise.
2. Context and stakes.
3. First discovery / conflict.
4. Evidence and deeper explanation.
5. Complication or turning point.
6. Consequences and synthesis.
7. Conclusion and viewer question.

Do not apply this template mechanically if the subject needs a different structure.

---

# PART 6 — RESEARCH, FACT-CHECKING AND STORY

## 6.1. Research dossier

Build an evidence dossier before writing final narration.

For every important claim record:

- claim ID;
- exact claim text;
- source title;
- source organization / author;
- direct URL;
- publication date;
- access date;
- source type;
- supporting excerpt or precise location;
- whether the source is primary or secondary;
- confidence;
- potential contradictions;
- verification status;
- chapters / script paragraphs relying on it.

## 6.2. Evidence hierarchy

Prefer:

1. Primary records, datasets, official archive documents.
2. Peer-reviewed research and scholarly books.
3. Reputable institutional histories and reference material.
4. Established reporting with original interviews or documents.
5. Secondary summaries only when stronger sources are unavailable.

A source's prestige does not prove that every statement on it is correct.

## 6.3. Fact status

Use explicit statuses:

- `VERIFIED`;
- `SUPPORTED`;
- `CONTESTED`;
- `INFERENCE`;
- `UNKNOWN`;
- `REJECTED`.

Never turn a hypothesis into a fact.

Do not fabricate quotes, dates, figures, events, sources or names.

## 6.4. Fact-check procedure

For each high-impact claim:

- locate the original statement;
- check the date;
- verify the units;
- verify the population / region / period;
- inspect methodology where relevant;
- search for an independent corroborating source;
- look for contradictory evidence;
- make the narration's confidence match the evidence;
- preserve uncertainty in the script;
- add citation to the source map.

## 6.5. Script quality

The script must:

- hook the viewer in the first 20–30 seconds;
- make a clear promise;
- give the viewer a reason to continue;
- avoid a slow generic introduction;
- use concise spoken sentences;
- vary sentence rhythm;
- avoid repeated exposition;
- create curiosity without deception;
- provide context before dense detail;
- use transitions that move the story forward;
- return to the central question;
- resolve the promised story;
- end with a meaningful conclusion and question.

## 6.6. Editorial table-read

Before TTS:

- read the script aloud or use a short TTS preview;
- identify tongue-twisters;
- shorten overloaded sentences;
- check names and transliterations;
- verify pronunciation dictionary;
- check transitions;
- verify that each chapter adds new information;
- eliminate repeated explanations;
- estimate chapter duration;
- confirm the 20-minute target;
- freeze the approved script revision.

---

# PART 7 — NARRATION MASTER AND KAGGLE PIPER

## 7.1. Audio-first rule

The narration master is the fixed timing source.

Do not let the shot plan determine the narration duration.

Do not rewrite the frozen narration to fit arbitrary clips.

If the script misses the 20-minute target, revise the draft before generating and freezing the final WAV.

## 7.2. TTS model and voice licensing

Inspect existing Piper/Kokoro integration and the exact selected model/voice.

Verify:

- model source;
- model license;
- voice license;
- language support;
- commercial use rights;
- redistribution restrictions;
- attribution;
- model SHA256;
- voice configuration.

Do not assume a model is commercially reusable because it is downloadable.

## 7.3. Kaggle notebook

Use the existing project Kaggle notebook if valid. Improve it rather than creating duplicate notebooks.

Notebook must:

1. Receive a frozen script revision and segment manifest.
2. Verify model / voice files.
3. Download only the selected licensed model in Kaggle.
4. Generate narration by deterministic segment IDs.
5. Preserve segment order.
6. Record pronunciation substitutions.
7. Record audio parameters.
8. Validate each segment.
9. Join segments without clipping or unplanned silence removal.
10. Record actual sample count.
11. Record actual duration.
12. Produce waveform / loudness summary.
13. Compute SHA256 for each WAV and final master.
14. Produce `tts_manifest.json`.
15. Produce `audio_timeline_source.json` or the existing equivalent.
16. Create a ZIP with only required artifacts.
17. Create a readable execution report.
18. Never include API keys in the output.

## 7.4. Kaggle execution

First inspect:

- Kaggle CLI presence;
- `kaggle --version`;
- authorization status without printing credentials;
- available notebook access;
- network restrictions;
- runtime / accelerator availability.

If authenticated and allowed, run the notebook.

If not authenticated:

- do not request the secret in chat;
- create a complete importable notebook;
- provide exact owner steps in one action list;
- prepare input ZIP;
- prepare output validation/importer;
- continue independent work.

## 7.5. WAV acceptance

Validate:

- non-zero file size;
- decodable PCM;
- correct channel count;
- actual sample rate;
- actual duration;
- sample count;
- no unexpected clipping;
- no corrupted segments;
- no missing chapter;
- no duplicate segment ID;
- no wrong concatenation order;
- no unintelligible audio;
- no unexplained silence;
- hash matches the manifest.

Do not report a model-generated fake or synthetic test sample as the final narration.

## 7.6. Narration freeze

After final acceptance:

- write an immutable narration manifest;
- store the final SHA256;
- store script revision;
- store voice/model version;
- store sample rate and channel count;
- store segment map;
- prohibit silent overwrite.

Any narration change after freeze requires a new revision and a rebuilt timeline.

---

# PART 8 — SAMPLE-ACCURATE AUDIO TIMELINE

## 8.1. Required fields

Every timeline segment must map:

- `segment_id`;
- `chapter_id`;
- `script_paragraph_id`;
- `audio_asset_id`;
- `start_sample`;
- `end_sample`;
- `sample_rate`;
- `start_seconds`;
- `end_seconds`;
- `duration_samples`;
- `duration_seconds`;
- optional pause metadata;
- optional music cue;
- optional SFX cue.

Use integer sample positions as the source of truth.

## 8.2. Timeline mathematics

For a segment:

`duration_samples = end_sample - start_sample`

`start_seconds = start_sample / sample_rate`

`end_seconds = end_sample / sample_rate`

Use half-open intervals `[start_sample, end_sample)`.

Do not store an ambiguous inclusive end sample.

Ensure frame mapping is derived from sample positions and the target video fps. Keep the original sample positions even when converting boundaries to video frames.

## 8.3. Timeline validation

Test:

- sample rate positive;
- start sample non-negative;
- end sample greater than start;
- no invalid overlaps unless explicitly allowed;
- no gaps unless represented as an intentional pause;
- segment order monotonic;
- total timeline within the WAV sample count;
- chapter intervals consistent;
- voice asset hashes match;
- timestamps derived from sample positions;
- rounding only at presentation boundaries;
- timecode conversion stable;
- repeated generation deterministic;
- interruption recovery does not duplicate segments.

## 8.4. Audio cues

Audio cues must not change the frozen narration.

Store:

- cue type;
- target segment / sample range;
- source asset;
- rights status;
- volume automation;
- fade-in/out;
- ducking envelope;
- reviewer note.

Music and SFX must have documented rights.

---

# PART 9 — RIGHTS, FOOTAGE AND 35-SHOT RECONCILIATION

## 9.1. Required status model

Use:

- `PASS`;
- `UNKNOWN`;
- `BLOCKED`.

Also record editorial status separately:

- `DIRECT`;
- `CONTEXTUAL`;
- `PROGRAMMATIC_GRAPHIC`;
- `ILLUSTRATIVE_RECONSTRUCTION`;
- `EDITORIAL_WEAK`;
- `UNRESOLVED`.

Do not mix legal status with editorial quality.

## 9.2. Asset-level rights record

For each local file:

- asset ID;
- original filename;
- actual path;
- resolved path;
- file size;
- SHA256;
- original source URL;
- exact asset page URL;
- creator;
- copyright owner;
- license name;
- license URL;
- retrieval date;
- permitted commercial use;
- derivative / editing permission;
- attribution text;
- third-party content flags;
- people / trademarks / logos flags;
- music included;
- restrictions;
- shots using the asset;
- review decision;
- reviewer evidence.

## 9.3. NASA media

Do not mark all NASA material public domain as a group.

For each exact NASA file:

- inspect the official page;
- inspect image / video credits;
- inspect the downloaded file;
- check third-party visual material;
- check music;
- check logos and endorsement implications;
- check identifiable persons;
- retain attribution and source details.

Prefer NASA versions without licensed music where appropriate. A video being hosted on a NASA domain does not automatically make every embedded element unrestricted.

## 9.4. Third-party footage

Do not use the 25 previously UNKNOWN shots until each specific file is verified or replaced.

Public YouTube video availability is not a license.

A broadcaster's news report is not free just because it is publicly viewable.

A public event recording can still contain copyrighted camera work, music, logos or other rights.

Do not assume fair use or fair dealing automatically clears a shot.

## 9.5. Programmatic replacement

If footage is not both lawful and editorially suitable, use original code-built visuals:

- maps;
- timelines;
- charts;
- tables;
- geographic route maps;
- comparison graphics;
- event sequences;
- labelled archival stills when rights-cleared;
- process diagrams;
- scientific explanatory diagrams.

Make the graphic clearly illustrative, not falsely archival.

Every numerical graphic must be generated from verified data with source references.

## 9.6. Rights gate

A shot can enter final render only when:

- legal status is PASS, or
- the shot is an original programmatic graphic with clear provenance and no unlicensed imported asset.

UNKNOWN and BLOCKED footage must not be used.

If no suitable replacement exists, revise the shot's visual approach, not the fact or narration.

## 9.7. The 35-shot reconciliation

Review all actual shot IDs from the current `shot_plan.json`.

Do not invent IDs if the real plan contains different IDs.

For the known original 35 shots:

- map each old shot to current narration;
- inspect the candidate research;
- keep the strongest valid candidate;
- replace weak generic Earth-view B-roll with direct material or a coded visual;
- update the rights manifest;
- rebuild the audit;
- ensure all 35 are accounted for;
- preserve audit history and prior manifests.

A 20-minute film will usually need more than the original 35 shots. Expand the shot plan as required by the real narration. Do not constrain the new film to the old pilot's shot count.

---

# PART 10 — SHOT PLANNING AND VISUAL STORYBOARD

## 10.1. Shot card schema

Each shot should include:

- shot ID;
- chapter ID;
- narration start/end sample;
- narration text reference;
- factual claim IDs;
- intended visual;
- visual class;
- source asset IDs;
- legal status;
- editorial fit;
- shot scale;
- movement;
- duration;
- transition in/out;
- sound cue;
- graphic requirements;
- caption / source-credit requirements;
- notes for reviewer.

## 10.2. Visual relevance

For each narration line, ask:

1. What does the viewer need to understand?
2. Does the visual prove the statement, contextualize it or explain it?
3. Is the visual from the correct time period?
4. Is it from the correct location?
5. Does it imply a false cause or event?
6. Is the visual repetitive?
7. Does it provide new information?
8. Can a programmatic graphic explain this better?
9. Are rights documented?
10. Can the shot be edited without misleading the viewer?

## 10.3. Shot types

Use a deliberate mixture:

- establishing shot;
- wide geography;
- medium event view;
- detail / close-up;
- archive footage;
- archival still with motion;
- map;
- animated map;
- time line;
- data chart;
- process diagram;
- comparison;
- explanatory typography;
- contextual B-roll;
- interview / person only when licensed and relevant.

Do not randomly alternate shot types just to create variation.

## 10.4. Visual rhythm

Pacing must follow story beats.

Avoid:

- long static slides;
- generic footage unrelated to narration;
- repeated shots;
- too many text-only cards;
- abrupt random transitions;
- a map that is illegible on mobile;
- a chart with unreadable labels;
- animations that distract from the explanation.

No static or frozen image should linger without an editorial reason. Use motion, zoom, callouts or scene transitions when the still must stay on screen.

---

# PART 11 — PROGRAMMATIC GRAPHICS AND REMOTION

## 11.1. Division of responsibilities

Use:

- **Python** for data preparation, validation, asset generation, charts and automation.
- **Remotion** for selected high-value animated compositions when licensing, runtime and disk allow.
- **FFmpeg** for ingest validation, transformations, clip processing, audio mix, final assembly, encoding and technical QA.

Remotion is optional for the final 20-minute master. The factory must still work with FFmpeg/Python if Remotion cannot be used.

## 11.2. Remotion project setup

Do not scaffold a new Remotion project until:

- current architecture has been inspected;
- license eligibility has been checked;
- disk space has been measured;
- Node / npm versions have been checked;
- exact package versions are pinned;
- the project has a reason to use Remotion.

Keep Remotion inside a clearly scoped project folder (for example `factory/motion/`) or integrate with an existing JS project. Do not create a second unrelated app.

## 11.3. Remotion runtime

If installed:

- pin `remotion` and `@remotion/*` packages consistently;
- commit or preserve the lockfile in the isolated workspace;
- keep browser downloads controlled;
- avoid downloading multiple Chromium builds;
- set render concurrency conservatively;
- set memory caches explicitly when supported;
- render only short compositions, not 20-minute full-film chunks in a high-memory browser pipeline;
- save scene manifests and composition props;
- render preview frames before full composition clips;
- keep a fallback static PNG / SVG output for critical graphics.

## 11.4. What to build with Remotion

Use short reusable compositions for:

- chapter opening sequences;
- animated timelines;
- historical date transitions;
- geographic map reveals;
- animated charts;
- lower thirds;
- source labels;
- title sequences;
- visual comparisons;
- diagram animations;
- subtle transitions.

Avoid using Remotion for simple trims, concatenation, audio filters or codec transforms that FFmpeg already does reliably.

## 11.5. Remotion acceptance

For every composition:

- declare width, height, fps and duration;
- type-check props;
- avoid nondeterministic network images;
- use local assets with provenance;
- avoid remote fonts at render time unless cached / pinned;
- check text overflow;
- test mobile safe areas;
- render a still;
- render a short clip;
- check alpha / codec behavior if overlaying;
- verify exact duration and frame count;
- verify the final output through FFmpeg / ffprobe.

## 11.6. Programmatic design system

Use one consistent system:

- typography scale;
- limited color palette;
- source label style;
- map label style;
- chart palette;
- chapter title layout;
- subtitle safe area;
- lower-third layout;
- animation easing;
- border and shadow rules;
- iconography;
- motion speed.

Do not create a different visual language for every chapter.

## 11.7. Avoid oversized renders

Do not render every composition in one full-length Remotion composition.

Render only the actual animated sections.

Generate graphics at exact intended frame rate and duration.

Use deterministic frame counts.

Render short test clips first.

Release memory between render batches.

---

# PART 12 — FFMPEG MASTER EDITING PIPELINE

## 12.1. FFmpeg is the master media engine

Use FFmpeg for:

- probe;
- trim;
- normalize;
- scale;
- fps conversion;
- safe crop / pad;
- audio extraction;
- audio mixing;
- subtitles;
- overlays;
- concat;
- transitions;
- loudness;
- final MP4;
- full decode;
- QA filters.

Use `ffmpeg-skill` tools when they are verified and appropriate. Do not blindly create shell commands from model guesses.

## 12.2. Source protection

Every source file is immutable.

All derived outputs go to a dedicated episode working directory.

Never write output over an input.

Use unique output names or explicit `--overwrite` only for a generated temporary file created by the current task.

Record the source and output hashes.

## 12.3. Ingest

For every media input:

- verify file exists;
- verify size > 0;
- probe streams;
- validate duration;
- validate codecs;
- inspect time base;
- inspect frame rate;
- inspect dimensions;
- inspect pixel format;
- inspect audio layout;
- detect corruption;
- record metadata;
- validate rights;
- add to the library only after validation.

## 12.4. Normalization

Normalize only what the edit requires.

Do not unnecessarily re-encode high-quality source footage multiple times.

Maintain intermediate mezzanine or source references when disk allows.

Use consistent:

- 1920×1080;
- 30 fps target;
- progressive scan;
- correct aspect ratio;
- consistent color handling.

If source footage is a different aspect ratio, decide per shot between crop, fit, blurred background or reframing. Do not crop away important visual evidence.

## 12.5. Audio assembly

Use audio timeline sample positions to assemble narration and cues.

Prevent:

- drift;
- clipping;
- accidental gaps;
- double narration;
- duplicated cues;
- phase issues;
- sudden loudness changes.

Use ducking for music under narration.

Use fades at logical transitions.

## 12.6. Segment rendering

For disk safety:

- render previews first;
- use short scene/chapter segments only when useful;
- keep a segment manifest;
- verify each segment;
- use a consistent stream format for safe concat;
- do not create hundreds of giant temporary PNGs if unnecessary;
- do not remove a segment until the final render references or copies it safely;
- checkpoint after completed segments.

## 12.7. Final assembly

The final assembly must:

- cover the entire narration;
- contain no missing chapter;
- have no unintended gaps;
- have no repeated accidental segment;
- maintain 30 fps;
- maintain exact intended duration;
- have continuous audio;
- preserve intended transitions;
- contain subtitles and graphics as planned;
- retain source citations / credits where required.

## 12.8. Final render target

YouTube-recommended settings checked 28 November 2026:

- MP4 container;
- H.264 video;
- progressive scan;
- AAC-LC audio;
- 48 kHz audio;
- 4:2:0 chroma;
- moov atom at front (`faststart`);
- 1080p SDR standard frame rate recommendation: 8 Mbps video;
- stereo audio reference bitrate: 384 kbps.

For this project, use a measured high-quality 1080p SDR target around the official recommended range. Choose CRF or bitrate mode after test renders and file-size calculations. Do not blindly force a bitrate that causes artifacts or exceeds disk capacity.

Apply BT.709 tags for SDR where correct.

Do not alter source frame rate arbitrarily if the project timeline is designed for 30 fps; normalize intentionally and document frame duplication / interpolation.

Official YouTube settings: https://support.google.com/youtube/answer/1722171

---

# PART 13 — SOUND DESIGN

## 13.1. Narration priority

Narration remains the primary information carrier.

Music must never mask speech.

Use sound effects only when they help the viewer understand or feel a documented scene.

## 13.2. Music rights

For each music asset record:

- creator;
- source;
- license;
- license page;
- attribution;
- commercial use;
- derivatives / editing rights;
- date accessed;
- SHA256.

No unlicensed music.

NASA videos with licensed soundtrack should not be used with the music unless the music rights are verified. Prefer a legitimate version without music and design sound separately.

## 13.3. Audio mix checks

Check:

- voice loudness;
- music level;
- true peak;
- clipping;
- noise;
- hum;
- abrupt silence;
- fade length;
- stereo placement;
- mono compatibility;
- phase cancellation;
- sample rate;
- channel mapping.

## 13.4. Audio QC

Use EBU R128 / loudness measurement as a reference, but do not assume one numeric target is a universal YouTube requirement. Establish a project target, measure it and keep it consistent.

Save loudness analysis output.

If audio QA requires subjective listening, generate a review file and explicitly mark machine checks separately from human listening.

---

# PART 14 — SUBTITLES, CHAPTERS AND SOURCE CREDITS

## 14.1. Subtitles

Generate subtitles from the frozen transcript, then align them to actual narration.

Outputs:

- `.srt`;
- `.vtt`;
- optional styled burn-in version for review.

Check:

- timing;
- reading speed;
- line length;
- punctuation;
- speaker labels if applicable;
- names and numbers;
- safe-area placement;
- no overlap with lower thirds;
- no subtitle during unintended silence;
- no cut-off text.

Do not allow subtitle generation to rewrite the script.

## 14.2. Chapter timestamps

Generate chapter timestamps from the real final timeline, not from estimated script duration.

Use YouTube chapter formatting and ensure the first chapter begins at 00:00 where applicable.

## 14.3. Credits

Prepare source credits with:

- asset title;
- source creator;
- organization;
- license;
- URL;
- attribution text;
- date accessed.

Make credits available in the description and/or end credits as required.

Do not omit a license attribution because it is inconvenient.

---

# PART 15 — TECHNICAL QA

## 15.1. Container and stream validation

Use ffprobe JSON and assert:

- output file exists;
- output size > 0;
- container is MP4;
- video stream exists;
- audio stream exists;
- video codec is H.264;
- audio codec is AAC;
- width is 1920;
- height is 1080;
- frame rate is 30/1 or the declared equivalent;
- pixel format is yuv420p;
- audio sample rate is 48000;
- expected channels;
- duration within tolerance;
- expected stream count;
- nonzero bitrate;
- MP4 faststart is applied where supported.

## 15.2. Full decode

Run a complete FFmpeg decode test on the final video.

A short probe is not a full decode.

Record exact command and exit code.

## 15.3. Video defects

Check:

- black frames;
- frozen frames;
- corrupted frames;
- decoder errors;
- unexpected frame-rate changes;
- aspect ratio errors;
- flashes;
- missing shots;
- repeated shots;
- missing overlays;
- out-of-safe-area text;
- broken maps;
- visual discontinuities.

Use automated detection as a signal, not as the only editorial judgment. Intentional black / freeze moments must be allowlisted with a reason.

## 15.4. Audio defects

Check:

- missing stream;
- corrupted audio;
- clipping;
- discontinuities;
- unintended silence;
- channel issues;
- loudness deviation;
- sync drift;
- repeated segments;
- missing narration phrases.

## 15.5. Visual review assets

Create:

- low-resolution review proxy;
- contact sheet across the full 20 minutes;
- contact sheets per chapter;
- exact shot/frame index;
- list of black/freeze detections;
- subtitle preview;
- waveform / loudness report.

Use a sample interval dense enough to expose visual repetition and mismatched scenes. Every shot must be represented in the review material.

## 15.6. QA evidence

Each QA result must include:

- input hash;
- output hash;
- tool version;
- exact command;
- exit code;
- summary;
- raw log path;
- pass/fail threshold;
- reviewer disposition.

---

# PART 16 — EDITORIAL QA

Technical validity is not editorial quality.

Review the finished documentary for:

- whether the opening delivers a reason to watch;
- whether the central question is clear;
- whether every chapter advances the story;
- whether narration is understandable;
- whether claims are supported;
- whether visuals truly correspond to narration;
- whether generic B-roll is overused;
- whether visuals repeat;
- whether information density is appropriate;
- whether maps and charts are legible;
- whether the pacing feels intentional;
- whether emotional beats are supported;
- whether music enhances rather than manipulates;
- whether the conclusion resolves the promise;
- whether the title and thumbnail match the film.

The Editorial Reviewer must have read-only access to the actual rendered video review artifacts, script, source dossier and shot map. It must not be the same agent that performed the edit.

If no human has listened to the final audio or watched the full film, state that explicitly. Automated QA must not be described as human approval.

---

# PART 17 — YOUTUBE PACKAGE

For the completed film create:

1. Five truthful title options.
2. Three distinct thumbnail concepts.
3. At least one final thumbnail image.
4. Description with a compelling first two lines.
5. Chapters with exact timestamps.
6. Source credits.
7. References / citations.
8. Tags where useful.
9. Pinned comment idea.
10. Publication checklist.
11. Disclosure notes for archival / illustrative graphics where needed.

## 17.1. Thumbnail

Use high contrast and a single visual promise.

Do not use false images or invented historical moments.

Do not use a face or recognizable person without rights and context checks.

Check:

- mobile readability;
- 16:9 layout;
- large focal subject;
- legible 2–5 word text if text is used;
- strong separation;
- no tiny labels;
- title / thumbnail complement rather than repeat each other.

## 17.2. Titles

Each title must:

- make one clear promise;
- avoid unsupported superlatives;
- avoid misleading curiosity gaps;
- avoid claims absent from the film;
- be readable in Russian if the episode language is Russian;
- have a distinct angle from the other options.

## 17.3. Description

Include:

- short hook;
- summary;
- chapter list;
- sources;
- credits;
- rights attribution;
- appropriate links;
- clear distinction between facts and illustrative reconstruction.

## 17.4. Analytics readiness

Create an importer for YouTube Studio CSV/JSON when available.

Do not invent impressions, CTR, retention or watch time before publication.

Prepare metrics schema and post-publication analysis template only.

---

# PART 18 — FACTORY COMMANDS, STATUS AND RECOVERY

## 18.1. Keep the existing interface

Inspect and preserve:

- `/montage`;
- `/montage-status`;
- `python scripts/agent_status.py status`;
- watchdog command.

Do not invent new command syntax. Read actual CLI help and project implementation.

## 18.2. Status integrity

Allowed statuses:

- `PENDING`;
- `READY`;
- `RUNNING`;
- `COMPLETED`;
- `BLOCKED`;
- `FAILED`;
- `STALE`.

A status is `RUNNING` only if a real process/task is active and heartbeat is fresh.

If the process disappears or heartbeat exceeds the configured threshold, move to `STALE`.

## 18.3. Persistent task graph

Every task must have:

- stable ID;
- title;
- goal;
- dependencies;
- allowed workspace;
- input artifacts;
- output artifacts;
- acceptance criteria;
- test command;
- checkpoint;
- status;
- start / finish time;
- heartbeat;
- error;
- Reviewer verdict.

## 18.4. Resume

On resume:

1. read the task graph;
2. verify completed task outputs;
3. verify hashes where relevant;
4. identify the next READY task;
5. do not redo verified work;
6. do not repeat destructive side effects;
7. continue only within allowed workspace;
8. update the single project state.

---

# PART 19 — EXECUTION METHOD: ONE LARGE PRODUCTION RUN

The owner does not want one prompt per small stage.

The agent must:

- create or resume the dependency DAG;
- execute all safe READY tasks;
- save checkpoints;
- proceed to the next READY task automatically within the active Ordewell run;
- continue independent tasks when one stream is blocked;
- consolidate owner actions;
- not stop after writing a report;
- not treat a short model response as completion.

If the current Ordewell execution model requires a separate run/resume operation, use the actual installed CLI help and supported interface. Do not invent commands. Use bounded retries and concurrency 1.

Do not change global automation settings to fully unattended operation without verifying their safety and existing owner configuration. Keep guarded approvals, watch mode and automerge off.

If a long-running session cannot continue after the model invocation ends, preserve the DAG and checkpoint so the exact next READY task is resumable. Do not claim that a process is running when only a task graph exists.

---

# PART 20 — FINAL VIDEO SPECIFICATION

## 20.1. Main file

Recommended path (choose a measured persistent volume with sufficient free space):

`projects/<episode-slug>/exports/final_20min.mp4`

If this location lacks capacity, use the verified media-library export volume and record the path. Do not create symlinks or move media blindly.

## 20.2. Required deliverables

- `final_20min.mp4`;
- `final_20min.srt`;
- `final_20min.vtt`;
- `thumbnail_final.png`;
- three thumbnail concepts;
- YouTube package;
- credits / source bibliography;
- episode manifest;
- narration manifest;
- audio timeline;
- shot plan;
- rights manifest;
- render manifest;
- technical QA report;
- editorial QA report;
- independent review;
- SHA256 manifest;
- low-resolution review proxy;
- contact sheets;
- final consolidated report.

## 20.3. Duration

Target 20:00 / 1,200 seconds, with a final tolerance of ±15 seconds.

The MP4 audio/video duration must agree within the defined project sync tolerance.

No silent extension, no repeated scene used purely to fill time, no artificial audio slowdown.

## 20.4. YouTube technical target

Use official YouTube recommendations as a baseline and verify the current Help page at execution time:

- MP4;
- H.264;
- progressive;
- 1920×1080;
- 30 fps project target;
- AAC-LC;
- 48 kHz audio;
- yuv420p;
- faststart;
- SDR BT.709 where applicable.

YouTube's current 1080p standard-frame-rate SDR reference is 8 Mbps video bitrate and 384 kbps stereo audio. Tune through a test render, and record actual output.

## 20.5. Render safety

- render a short representative preview first;
- validate a full chapter before full film;
- use low concurrency;
- calculate file size;
- check available space on the actual output mount;
- use atomic output names;
- never overwrite source or approved previous exports;
- keep previous valid outputs intact;
- checkpoint each final render stage.

---

# PART 21 — ACCEPTANCE GATES

The episode and factory are not production-ready until every applicable gate has evidence.

| Gate | Required proof |
|---|---|
| G0 Workspace | Isolated workspace verified; original untouched |
| G1 Skills | FFmpeg / Remotion skills installed and loadable or documented fallback |
| G2 Topic | Episode topic and brief supported by research |
| G3 Research | Claims evidence mapped and fact-checked |
| G4 Script | Approved 20-minute script with editorial review |
| G5 TTS | Real narration master created and validated |
| G6 Timeline | Sample-accurate timeline passes tests |
| G7 Rights | Every used source has confirmed rights or is original programmatic output |
| G8 Shot plan | Every narration section has an editorially appropriate visual plan |
| G9 Graphics | All custom graphics validated |
| G10 Edit | FFmpeg master assembled successfully |
| G11 Sound | Narration, music and SFX mixed and checked |
| G12 Subtitles | SRT/VTT validated and synchronized |
| G13 Technical QA | Full decode and technical checks pass |
| G14 Editorial QA | Independent editorial review passes or remaining notes are disclosed |
| G15 Packaging | YouTube package complete |
| G16 Reliability | Checkpoints, state and resume behavior verified |
| G17 Final delivery | MP4, subtitles, poster, manifests, logs, hashes and report exist |

Possible final statuses:

- `BLOCKED`;
- `PARTIAL`;
- `PARTIAL_READY`;
- `PRODUCTION_READY`.

A 20-minute MP4 that is technically valid but uses UNKNOWN footage is not `PRODUCTION_READY`.

A factory with all unit tests passing but no real narration / real media render is not `PRODUCTION_READY`.

---

# PART 22 — CONSOLIDATED FINAL REPORT

Create:

`reports/MASTER_FACTORY_20MIN_DELIVERY_REPORT.md`

Outside the project also create a portable handoff.

The report must include:

1. workspace identity and original protection evidence;
2. baseline and final Git status comparison;
3. installed skill names, versions, sources and hashes;
4. installed Remotion / FFmpeg versions;
5. exact licenses / license-gate result;
6. architecture built and changed modules;
7. topic and episode brief;
8. research sources and claim map;
9. final script length and actual narration speed;
10. narration model, voice, file, duration, sample rate, sample count and SHA256;
11. timeline test results;
12. all used visual assets and legal statuses;
13. shot-plan count and unresolved shots;
14. graphics / Remotion compositions built;
15. FFmpeg assembly details;
16. final render settings;
17. final MP4 duration, codec, resolution, fps, bitrate and hash;
18. complete decode exit code;
19. technical QA results;
20. editorial review verdict;
21. subtitle validation;
22. final YouTube package;
23. test counts and failures;
24. remaining limitations;
25. all owner actions in one consolidated list;
26. final status and each gate result.

Do not use generic phrases such as "everything works". Include evidence paths and exit codes.

---

# PART 23 — MASTER EXECUTION PROMPT

The following instruction is the operational prompt. Execute the full specification above, not merely summarize it.

You are the Executive Producer and Principal Engineer of OpenMontage.

You must deliver one real, high-quality 20-minute documentary and a reusable production factory.

Start by reading this complete file and verifying the current isolated workspace.

Do not edit `/workspaces/OpenMontage`.

Do not ask routine questions. Use the strongest existing research, episode topic and available rights-cleared materials. Make reversible editorial decisions inside the isolated workspace. Keep narration audio-first. Use the existing Piper/Kaggle flow. Use FFmpeg as the final assembly engine. Install and load the verified FFmpeg skill and official Remotion skills where safe. Use Remotion only when licensing and available resources permit; otherwise create the same visuals through Python/FFmpeg.

Do not leave the 25 unknown historical shots in the final video. Replace them with verified footage or accurate programmatic graphics. Do not invent facts or visual evidence.

Do not stop after the first short response. Run the existing Ordewell task graph. Save checkpoints. Proceed to the next READY task. Continue independent work when one item is blocked. Return only after a substantial production milestone or when an external owner action is genuinely required.

When all dependencies permit, render the complete 20-minute MP4, run full decode, inspect review frames, validate narration sync, validate rights and obtain independent review.

If Kaggle authentication or an external right cannot be obtained without the owner, prepare the complete packet and keep working on all remaining tasks. Never fake the missing part.

The final success condition is a real `final_20min.mp4` with a full evidence pack, not a plan or a progress message.

---

# PART 24 — GRANULAR WORK PACKAGE REGISTER

The following work packages are mandatory. Each task must be represented in the Ordewell DAG with a stable task ID, dependencies, inputs, outputs, acceptance criteria, test evidence and Reviewer verdict.



## WP00 — Workspace identity, safety and baseline

### OM-0001 — Detect the active project root
- **Objective:** Run pwd and git rev-parse --show-toplevel. Confirm the current workspace is an isolated path and not the original checkout.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Record workspace path and proof; fail closed if the path resolves to /workspaces/OpenMontage.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0002 — Capture original-checkout state
- **Objective:** Read original HEAD, branch, porcelain status and file hashes using non-mutating commands.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Save external baseline evidence; do not create or update files under the original checkout.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0003 — Inventory existing snapshots
- **Objective:** Find existing isolated workspaces and compare their timestamps, status, code, tests and reports.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Select only the newest complete snapshot that includes all reported latest fixes.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0004 — Verify snapshot integrity
- **Objective:** Compare critical code and report hashes, check source/media symlinks and validate that the snapshot is usable.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Produce snapshot integrity record and do not edit an unverified copy.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0005 — Calculate disk headroom
- **Objective:** Check df, inode usage, directory sizes, output filesystem and temporary paths.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Choose safe working and output volumes; block heavy installs if below thresholds.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0006 — Identify active processes
- **Objective:** List active rendering, TTS, indexing, Ordewell and OpenCode processes without killing them.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Record active processes and avoid duplicate side effects.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0007 — Preserve user assets
- **Objective:** Verify V4/V5, media-library, checkpoints, .git, .swarm, .ordewell and reports exist.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Record preservation evidence; never delete or move them.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0008 — Capture current project state
- **Objective:** Read PROJECT_STATE, HANDOFF, AGENTS, current run files and all recent audit reports.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Write a concise state map with actual file references.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0009 — Verify baseline tests
- **Objective:** Inspect test configuration and run the lightest relevant baseline only if disk headroom allows.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Record exact command, counts, exit code and skips; do not infer from prior report.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0010 — Create isolated execution checkpoint
- **Objective:** Use the existing snapshot/checkpoint mechanism after verifying it will not touch the original.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Checkpoint must contain workspace ID, HEAD, task graph version and run ID.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP01 — Skills, tools and runtime

### OM-0101 — Inventory existing OpenCode skills
- **Objective:** Inspect .opencode/skills, .agents/skills, .claude/skills and existing .ordewell/skills.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Return a deduplicated skill inventory with IDs and file hashes.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0102 — Install FFmpeg skill
- **Objective:** Review kajisho5/ffmpeg-skill, license, security notes and current install help; install to the verified OpenCode project skill directory.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** SKILL.md and required references/scripts are present and OpenCode can load the exact skill ID.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0103 — Validate FFmpeg skill
- **Objective:** Run the documented doctor and contract commands after checking package help.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Record JSON contract, discovered tools, versions and missing capabilities.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0104 — Install official Remotion skills
- **Objective:** Use remotion-dev/skills via the documented CLI route; target OpenCode-discovered project skills.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Official skills are present, deduplicated, loadable and reference files resolve.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0105 — Audit Remotion license
- **Objective:** Check exact runtime version, applicable terms, free eligibility and any automation conditions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Use Remotion only after the license gate passes; otherwise keep it optional.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0106 — Pin Remotion versions
- **Objective:** If runtime is installed, pin all remotion and @remotion packages to a compatible exact version.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No mixed versions or unpinned package ranges; lockfile preserved.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0107 — Verify FFmpeg binary
- **Objective:** Inspect ffmpeg, ffprobe, buildconf, filters, encoders and license output.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All required features exist or a minimal fallback plan is recorded.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0108 — Verify Python and Node
- **Objective:** Inspect Python, Node, npm and package manager versions against project requirements.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No runtime upgrade unless required and disk-safe.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0109 — Verify skill security
- **Objective:** Read install scripts, network actions, filesystem writes, secret handling and licenses.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Untrusted or destructive skill content is rejected; all approved versions are hashed.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0110 — Build project-specific skill index
- **Objective:** Document skill IDs, when to load them, and cross-links to existing runbook and code.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** One compact skill index exists; no duplicate or contradictory instructions.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP02 — Factory architecture and contracts

### OM-0201 — Map current source architecture
- **Objective:** Trace current CLI, pipeline stages, validators, state, renderer, TTS and media modules.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Produce a current call graph and extension points; do not replace working modules.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0202 — Define episode manifest
- **Objective:** Use existing manifest or define episode identity, language, runtime, frame rate, output and source policy.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Schema validates an example episode and rejects invalid settings.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0203 — Define research claim contract
- **Objective:** Map claim IDs to sources, excerpts, confidence, conflicts and script references.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Claims can be traced from narration to source evidence.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0204 — Define narration manifest
- **Objective:** Record script revision, model, voice, parameters, sample rate, sample count, duration and hashes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Frozen narration is immutable by identity and checksum.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0205 — Define audio timeline contract
- **Objective:** Use integer sample ranges and derived timestamps; retain exact chapter and cue references.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Timeline schema validates all required fields and rejects invalid intervals.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0206 — Define shot contract
- **Objective:** Map shot ID to narration samples, visual objective, asset, rights and editorial class.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every shot can be traced to narration and source evidence.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0207 — Define asset-rights contract
- **Objective:** Separate rights status from editorial suitability and record exact file/source information.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** UNKNOWN/BLOCKED assets cannot enter a production render.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0208 — Define render manifest
- **Objective:** Record inputs, hashes, renderer versions, command parameters, output path and result.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** A render can be audited and reproduced from manifest inputs.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0209 — Define QA report schema
- **Objective:** Record checks, thresholds, logs, hashes, exit codes, severity and reviewer verdict.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No report can say PASS without evidence for each mandatory check.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0210 — Define migration and compatibility
- **Objective:** Preserve current manifests and adapt only with explicit schema versions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Existing valid projects load without destructive migration.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP03 — Research, topic and episode brief

### OM-0301 — Find the strongest existing episode topic
- **Objective:** Inspect current projects, scripts, dossiers, shot plans and prior pilot assets.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Choose one topic with documented reason; do not invent topic facts.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0302 — Scope the 20-minute story
- **Objective:** Define period, geography, people, events and exclusions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The story has clear boundaries and an evidence-backed central question.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0303 — Research primary sources
- **Objective:** Collect original records, official datasets, archives and primary documents.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every source has an accessible URL and provenance record.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0304 — Research independent corroboration
- **Objective:** Find independent sources for high-impact claims.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Key claims have corroboration or are explicitly marked uncertain.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0305 — Build claim ledger
- **Objective:** Create stable IDs for every substantial factual claim in the planned script.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Claim ledger is machine-readable and linked to source excerpts.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0306 — Resolve contradictions
- **Objective:** Record conflicting dates, figures, interpretations and source quality.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The script reflects unresolved disputes honestly.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0307 — Verify dates, units and geography
- **Objective:** Check calendar, numeric units, map boundaries and place names.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No unverified numeric or geographic fact reaches final narration.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0308 — Build chronology
- **Objective:** Create event-by-event chronological records from supported evidence.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Chronology can power maps and timeline graphics without invented dates.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0309 — Assess visual feasibility
- **Objective:** For each chapter, identify direct footage, contextual footage and programmatic graphic options.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The film has a realistic visual route before narration is frozen.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0310 — Create research dossier and review
- **Objective:** Store sources, claims, contradictions, confidence and open questions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Independent fact-checker reviews high-impact claims and records verdict.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP04 — Script, story and narration plan

### OM-0401 — Define viewer promise
- **Objective:** Write one clear sentence describing what the viewer will understand by the end.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Promise is supported by available evidence and the actual episode scope.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0402 — Design the hook
- **Objective:** Create a cold open that starts with a concrete event, contradiction, mystery or consequence.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The first 30 seconds contain a real hook, not generic channel introduction.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0403 — Build chapter outline
- **Objective:** Give each chapter a question, purpose, evidence and transition.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All chapters advance the central question and avoid repetition.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0404 — Draft spoken narration
- **Objective:** Write natural narration in the episode language with short speakable sentences.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Narration has source references and is suitable for TTS.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0405 — Write transitions
- **Objective:** Connect chapters through unresolved questions, consequences or evidence.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Transitions are coherent and do not manufacture suspense.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0406 — Insert fact citations in script map
- **Objective:** Link each important spoken claim to a claim ID.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No important factual assertion is orphaned.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0407 — Estimate narration duration
- **Objective:** Measure the selected Piper voice with a test segment or prior verified speaking rate.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Estimated runtime is grounded in actual voice pace.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0408 — Refine to 20-minute target
- **Objective:** Revise draft length and pacing before generating final narration.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Target 1,200 seconds ±15 seconds without filler or repeated content.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0409 — Perform spoken script review
- **Objective:** Read or audition sample sections and correct awkward names, rhythm and pronunciation.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Script is intelligible and natural when spoken aloud.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0410 — Freeze approved script revision
- **Objective:** Assign revision ID and hash before final TTS generation.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Narration generation references exactly this frozen revision.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP05 — TTS and Kaggle Piper workflow

### OM-0501 — Audit existing TTS integration
- **Objective:** Inspect Piper/Kokoro modules, adapters, schemas, tests and Kaggle notebook.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Re-use the functioning integration and list exact gaps.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0502 — Verify voice/model license
- **Objective:** Inspect exact model repository and model/voice license documents.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The selected voice has documented permitted use or is excluded.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0503 — Validate Kaggle environment
- **Objective:** Check CLI and auth status without printing secrets.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Report whether unattended Kaggle execution is possible.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0504 — Finalize notebook inputs
- **Objective:** Package frozen script segments and model/voice configuration.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Notebook input is versioned, deterministic and secret-free.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0505 — Generate narration segments
- **Objective:** Run Piper by stable segment IDs and preserve text ordering.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Each segment exists, is decodable and maps to the script.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0506 — Validate segment WAVs
- **Objective:** Check duration, sample rate, channels, samples, clipping and silence.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Invalid segments are rejected with reason codes.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0507 — Join narration master
- **Objective:** Concatenate approved segments with intended pauses and no unintended overlap.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Final narration duration is within target and every segment is accounted for.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0508 — Create narration manifest
- **Objective:** Record exact model, voice, parameters, source revision, sample count and hashes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Manifest matches actual files and verifies on re-read.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0509 — Package Kaggle output
- **Objective:** Create ZIP with master WAV, manifest, timeline source, hashes and report.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** ZIP can be imported without downloading large models into Codespaces.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0510 — Build safe import and recovery
- **Objective:** Validate ZIP paths, hashes, sizes and sample metadata before atomic import.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Import is idempotent and rejects path traversal / duplicate assets.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP06 — Audio timeline and sound engineering

### OM-0601 — Build sample-accurate timeline
- **Objective:** Create segment boundaries from actual WAV sample counts.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All timeline times derive from integer sample positions.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0602 — Validate timeline boundaries
- **Objective:** Check monotonic order, range, gap, overlap and chapter boundaries.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Invalid intervals fail tests with precise diagnostics.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0603 — Align script to narration
- **Objective:** Use exact segment IDs and optional ASR alignment if available.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Script references and audio timestamps are traceable.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0604 — Add music cue plan
- **Objective:** Place licensed music only where it supports narrative purpose.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Each cue has source, rights, start/end and level automation.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0605 — Add sound effect cue plan
- **Objective:** Use restrained SFX with clear meaning and rights.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No gratuitous effects or undocumented assets.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0606 — Implement ducking
- **Objective:** Keep music below narration with smooth envelopes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Voice intelligibility passes measurements and review.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0607 — Set loudness target
- **Objective:** Choose a consistent project loudness target and record it.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Final loudness and true peak fall within declared project limits.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0608 — Test silence and clipping
- **Objective:** Run audio-level and silence analysis, inspect detected regions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All unexpected silence/clipping is corrected or allowlisted.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0609 — Verify sync
- **Objective:** Compare video timing to narration sample / frame mapping.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Sync drift remains within the project's declared tolerance.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0610 — Create audio review pack
- **Objective:** Provide narration-only, mix preview, waveform, loudness report and cue sheet.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Reviewer can inspect real audio artifacts and evidence.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP07 — Rights, asset ingestion and shot planning

### OM-0701 — Reconcile the original 35 shots
- **Objective:** Read current shot plan and map all actual IDs.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No original shot is silently dropped or duplicated.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0702 — Verify prior NASA candidates
- **Objective:** Open exact NASA pages and inspect the exact selected files.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Legal status is assigned per file, not per website or collection.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0703 — Verify third-party sources
- **Objective:** Check broadcaster, archive, event and creator-specific conditions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Unclear rights stay UNKNOWN and are not rendered.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0704 — Select legal replacement or graphic
- **Objective:** Choose rights-cleared material or create a factual programmatic visual.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All 25 previously UNKNOWN shots receive a safe disposition.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0705 — Build asset provenance records
- **Objective:** Record exact URL, license, creator, hash, retrieval date and restrictions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every used file is traceable from output to original source.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0706 — Strengthen media indexing
- **Objective:** Verify size > 0, accessibility, ffprobe and metadata before indexing.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Zero-byte and corrupt media remain excluded with reason codes.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0707 — Strengthen retrieval revalidation
- **Objective:** Recheck the file immediately before use.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Missing, newly empty or corrupt assets fail closed.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0708 — Expand 20-minute shot plan
- **Objective:** Create enough distinct visual beats for full narration without arbitrary shot counts.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every chapter has a meaningful shot or graphic mapped to actual narration.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0709 — Validate visual classes
- **Objective:** Label direct evidence, contextual B-roll, programmatic graphic or reconstruction.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No generic B-roll is misrepresented as proof of a historical event.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0710 — Rebuild rights audit and review
- **Objective:** Update manifests in snapshot and run read-only legal/editorial review.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every used asset has a verified legal status and editorial rationale.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP08 — Programmatic visual design and Remotion

### OM-0801 — Define documentary visual system
- **Objective:** Set typography, colors, hierarchy, maps, labels, chart conventions and subtitle safe area.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** A single documented design system governs all chapters.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0802 — Build title and chapter cards
- **Objective:** Create reusable short animated/graphic compositions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Cards are legible, correctly timed and consistent.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0803 — Build map system
- **Objective:** Create maps from verified geographic data and date-specific boundaries.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Maps never imply incorrect borders or locations.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0804 — Build timeline system
- **Objective:** Generate chronological graphics from evidence-backed event data.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every date and event links to claim IDs.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0805 — Build chart system
- **Objective:** Create charts directly from validated datasets.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Axes, units, labels and source notes are readable and accurate.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0806 — Build process diagrams
- **Objective:** Render explanatory diagrams for complex relationships.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Diagram relationships are backed by source or marked as conceptual.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0807 — Build lower thirds and callouts
- **Objective:** Create consistent identifiers, captions and evidence labels.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No overflow, overlapping or unsafe placement.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0808 — Build transition language
- **Objective:** Use restrained transitions that serve temporal or conceptual changes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Transitions do not distract or imply false continuity.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0809 — Render Remotion preview scenes
- **Objective:** Render representative stills and short clips using pinned dependencies.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Exact frame count, text fit and visual output validated.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0810 — Provide Python/FFmpeg fallback
- **Objective:** Create equivalent static/animated graphics when Remotion is unavailable.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No essential scene depends solely on an unapproved runtime.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP09 — FFmpeg editing and rendering

### OM-0901 — Create edit decision list
- **Objective:** Map shot IDs, sample positions, source in/out and transition intent.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** EDL covers the entire narration and preserves source references.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0902 — Validate every source clip
- **Objective:** Probe and validate the exact source before trim or render.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Invalid clip is blocked before reaching the render graph.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0903 — Normalize visual streams
- **Objective:** Normalize size, frame rate, pixel format and color deliberately.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Every segment conforms to declared project settings.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0904 — Implement safe trims and overlays
- **Objective:** Use verified FFmpeg skill or project wrappers; keep source read-only.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Outputs are unique, validated and never overwrite source.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0905 — Implement audio graph
- **Objective:** Combine narration, music and SFX using exact sample/time cues.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No unintended mute, clipping or drift.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0906 — Render chapter previews
- **Objective:** Render a representative short clip from each chapter.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Each preview passes probe/decode and editorial inspection.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0907 — Assemble master timeline
- **Objective:** Assemble all chapters in exact order with intended transitions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No missing, duplicated or unintended segments.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0908 — Render final MP4
- **Objective:** Render 1920x1080, 30fps, H.264/AAC according to the final profile.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Output exists, is nonzero and matches target duration.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0909 — Run complete decode
- **Objective:** Decode the entire MP4 and save stderr / exit code.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Full decode exits successfully without unexplained errors.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-0910 — Preserve render reproducibility
- **Objective:** Save commands, tool versions, inputs, hashes and render manifest.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** The exact render can be audited and reproduced.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP10 — Subtitles, audio/video QA and editorial review

### OM-1001 — Generate SRT
- **Objective:** Create subtitles from the frozen transcript and actual narration timing.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** SRT has correct order, timestamps and text.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1002 — Generate VTT
- **Objective:** Create valid WebVTT from the same authoritative timing data.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** VTT parses and matches the SRT content.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1003 — Validate subtitle layout
- **Objective:** Check line length, reading speed, punctuation, safe area and overlap.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All captions are readable and do not cover essential evidence.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1004 — Run technical video QA
- **Objective:** Check codec, dimensions, fps, duration, pixel format and streams.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All technical acceptance checks pass.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1005 — Run black/freeze detection
- **Objective:** Detect black and frozen intervals and compare to planned intentional events.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No unexplained black/freeze segments remain.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1006 — Run audio QA
- **Objective:** Measure loudness, true peak, silence, clipping and channel integrity.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All deviations are corrected or explicitly allowlisted.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1007 — Build full-film contact sheets
- **Objective:** Sample the complete film and every chapter.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All shots and visual transitions are represented.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1008 — Review narrative-to-visual alignment
- **Objective:** Compare narration cues, storyboard, contact sheets and chapter structure.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Weak or misleading visuals are corrected.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1009 — Independent rights review
- **Objective:** Read the actual manifests and used asset hashes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Reviewer verifies every used asset or blocks unresolved rights.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1010 — Independent editorial review
- **Objective:** Review script, render proxy, contact sheets, captions and sound notes.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Reviewer issues a new evidence-based verdict after fixes.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


## WP11 — YouTube delivery and operational completion

### OM-1101 — Produce five titles
- **Objective:** Create five different truthful angles supported by film content.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No title promises evidence the film does not provide.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1102 — Produce three thumbnail concepts
- **Objective:** Design three distinct visual promises from cleared assets.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All concepts are accurate, legible and source-cleared.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1103 — Render final thumbnail
- **Objective:** Create high-quality 16:9 thumbnail at the current platform dimensions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Image is readable on a mobile preview and matches the film.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1104 — Write video description
- **Objective:** Write Russian description or episode language, chapters, references and credits.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Description is accurate and complete.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1105 — Create chapter list
- **Objective:** Generate chapters from final timestamps.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** All chapter timestamps point to real chapter boundaries.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1106 — Create publication checklist
- **Objective:** List owner steps for title choice, thumbnail choice, upload and captions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** No upload/publish occurs without owner action.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1107 — Prepare analytics schema
- **Objective:** Create CSV/JSON import contract for YouTube Studio exports.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Metrics can be imported without inventing unpublished data.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1108 — Verify launch and status commands
- **Objective:** Check actual /montage and /montage-status implementations and CLI.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** One command launches documented workflow; one command reads factual status.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1109 — Run recovery acceptance
- **Objective:** Simulate stop/resume or process restart in disposable episode workspace.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Checkpoint resume does not repeat completed side effects.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.

### OM-1110 — Assemble final delivery report
- **Objective:** Consolidate files, test evidence, review verdicts, hashes and owner actions.
- **Inputs:** current project artifacts, verified workspace state and relevant preceding task outputs.
- **Execution:** inspect first; implement the smallest compatible change; preserve source and manifest history; record every new output.
- **Acceptance:** Final status accurately reflects all acceptance gates.
- **Tests:** unit / integration / synthetic fixture tests appropriate to the task; record exact command and exit code.
- **Evidence:** output path, input/output SHA256 where applicable, logs, checkpoint ID and Reviewer result.
- **Failure path:** preserve state, mark BLOCKED/FAILED with cause, and continue independent READY tasks.
- **Owner interruption:** none for reversible local work; list only if an external authorization, license or credential is genuinely required.


# PART 25 — 35-SHOT RECONCILIATION REGISTER

Use actual shot IDs from the current shot plan. The labels below are slots, not permission to invent shot IDs. Map each slot to an actual shot or mark it not applicable with a reason. Do not drop any original shot silently.

## SHOT-SLOT-001
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-002
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-003
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-004
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-005
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-006
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-007
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-008
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-009
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-010
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-011
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-012
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-013
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-014
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-015
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-016
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-017
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-018
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-019
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-020
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-021
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-022
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-023
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-024
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-025
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-026
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-027
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-028
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-029
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-030
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-031
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-032
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-033
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-034
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.

## SHOT-SLOT-035
- Resolve the actual shot ID from the current `shot_plan.json`.
- Read the linked narration sample range and the claim IDs it supports.
- State what the viewer must see and whether the visual is direct evidence, contextual B-roll, a programmatic graphic or a reconstruction.
- Inspect the exact candidate asset page and exact file; record creator, rights, source URL, music, third-party elements and local hash.
- Evaluate whether the candidate is editorially direct, contextual, weak or misleading.
- If the candidate is weak, replace it with a better rights-cleared source or a factual code-built visual.
- Do not use generic Earth-view footage to illustrate an event it does not depict.
- Update shot references, rights manifest and audit only in the isolated workspace.
- Add a regression test for any indexing / retrieval behavior affected by this shot.
- Obtain independent rights and editorial review.
- Mark PASS only with evidence. Otherwise mark UNKNOWN / BLOCKED / UNRESOLVED and exclude it from the final render.


# PART 26 — DETAILED ACCEPTANCE TEST MATRIX


## Workspace and safety tests

- [ ] `01` original checkout path is never selected as write workspace. Evidence: test name / command / log path / exit code.
- [ ] `02` snapshot HEAD and branch are recorded. Evidence: test name / command / log path / exit code.
- [ ] `03` snapshot Git status is compared before and after each workstream. Evidence: test name / command / log path / exit code.
- [ ] `04` symlinks are not followed outside allowed roots. Evidence: test name / command / log path / exit code.
- [ ] `05` insufficient disk headroom prevents heavy installation. Evidence: test name / command / log path / exit code.
- [ ] `06` existing V4 and V5 artifacts remain unchanged. Evidence: test name / command / log path / exit code.
- [ ] `07` existing checkpoints remain readable. Evidence: test name / command / log path / exit code.
- [ ] `08` untracked user assets are preserved. Evidence: test name / command / log path / exit code.
- [ ] `09` no background render is orphaned. Evidence: test name / command / log path / exit code.
- [ ] `10` report writes occur only outside original checkout or in snapshot. Evidence: test name / command / log path / exit code.


## Skills and tools tests

- [ ] `01` OpenCode discovers ffmpeg-skill in a supported path. Evidence: test name / command / log path / exit code.
- [ ] `02` OpenCode loads ffmpeg-skill by exact ID. Evidence: test name / command / log path / exit code.
- [ ] `03` FFmpeg doctor exits successfully or records missing optional tools. Evidence: test name / command / log path / exit code.
- [ ] `04` FFmpeg contract JSON parses. Evidence: test name / command / log path / exit code.
- [ ] `05` Remotion best-practices skill exists. Evidence: test name / command / log path / exit code.
- [ ] `06` Remotion markup skill exists. Evidence: test name / command / log path / exit code.
- [ ] `07` Remotion render skill exists. Evidence: test name / command / log path / exit code.
- [ ] `08` Remotion maps skill exists. Evidence: test name / command / log path / exit code.
- [ ] `09` Remotion captions skill exists. Evidence: test name / command / log path / exit code.
- [ ] `10` all linked Remotion skill references resolve. Evidence: test name / command / log path / exit code.
- [ ] `11` skill IDs do not collide with existing skills. Evidence: test name / command / log path / exit code.
- [ ] `12` skill installer does not install system FFmpeg unexpectedly. Evidence: test name / command / log path / exit code.
- [ ] `13` no skill command exposes secrets. Evidence: test name / command / log path / exit code.
- [ ] `14` installed versions and hashes are recorded. Evidence: test name / command / log path / exit code.


## Research and fact-check tests

- [ ] `01` every central factual claim has a stable claim ID. Evidence: test name / command / log path / exit code.
- [ ] `02` every major claim has an original source URL. Evidence: test name / command / log path / exit code.
- [ ] `03` source access dates are recorded. Evidence: test name / command / log path / exit code.
- [ ] `04` publication dates are preserved. Evidence: test name / command / log path / exit code.
- [ ] `05` the source excerpt actually supports the claim. Evidence: test name / command / log path / exit code.
- [ ] `06` units and dates are checked. Evidence: test name / command / log path / exit code.
- [ ] `07` contradictory claims are represented. Evidence: test name / command / log path / exit code.
- [ ] `08` high-impact claims have independent corroboration where available. Evidence: test name / command / log path / exit code.
- [ ] `09` unknown claims are not narrated as verified. Evidence: test name / command / log path / exit code.
- [ ] `10` quotes are not fabricated. Evidence: test name / command / log path / exit code.
- [ ] `11` script paragraphs map to claim IDs. Evidence: test name / command / log path / exit code.
- [ ] `12` final credits list all used documentary sources. Evidence: test name / command / log path / exit code.


## Script and runtime tests

- [ ] `01` the first 30 seconds establish a viewer promise. Evidence: test name / command / log path / exit code.
- [ ] `02` the opening does not contain a long generic introduction. Evidence: test name / command / log path / exit code.
- [ ] `03` all chapters add new information. Evidence: test name / command / log path / exit code.
- [ ] `04` no paragraph is duplicated accidentally. Evidence: test name / command / log path / exit code.
- [ ] `05` the ending resolves the main question. Evidence: test name / command / log path / exit code.
- [ ] `06` script language is consistent. Evidence: test name / command / log path / exit code.
- [ ] `07` pronunciation dictionary includes difficult proper names. Evidence: test name / command / log path / exit code.
- [ ] `08` draft duration estimate uses observed voice pace. Evidence: test name / command / log path / exit code.
- [ ] `09` script revision is frozen before final TTS. Evidence: test name / command / log path / exit code.
- [ ] `10` no final audio is silently edited after freeze. Evidence: test name / command / log path / exit code.


## TTS and narration tests

- [ ] `01` Kaggle notebook inputs match the frozen script hash. Evidence: test name / command / log path / exit code.
- [ ] `02` voice and model licenses are recorded. Evidence: test name / command / log path / exit code.
- [ ] `03` every segment has a stable segment ID. Evidence: test name / command / log path / exit code.
- [ ] `04` every segment WAV is nonzero and decodable. Evidence: test name / command / log path / exit code.
- [ ] `05` segment sample rate is recorded. Evidence: test name / command / log path / exit code.
- [ ] `06` segment sample count is recorded. Evidence: test name / command / log path / exit code.
- [ ] `07` segment order matches the script. Evidence: test name / command / log path / exit code.
- [ ] `08` no segment is missing. Evidence: test name / command / log path / exit code.
- [ ] `09` no duplicate segment is included. Evidence: test name / command / log path / exit code.
- [ ] `10` master WAV is decodable. Evidence: test name / command / log path / exit code.
- [ ] `11` master sample count equals the sum of segments plus intended pauses. Evidence: test name / command / log path / exit code.
- [ ] `12` master duration matches the sample count. Evidence: test name / command / log path / exit code.
- [ ] `13` manifest SHA256 matches actual files. Evidence: test name / command / log path / exit code.
- [ ] `14` no secret is present in notebook output. Evidence: test name / command / log path / exit code.
- [ ] `15` import ZIP rejects path traversal. Evidence: test name / command / log path / exit code.
- [ ] `16` import ZIP is idempotent. Evidence: test name / command / log path / exit code.


## Audio timeline tests

- [ ] `01` all start_sample values are non-negative. Evidence: test name / command / log path / exit code.
- [ ] `02` all end_sample values exceed start_sample. Evidence: test name / command / log path / exit code.
- [ ] `03` all ranges are within the master sample count. Evidence: test name / command / log path / exit code.
- [ ] `04` all timestamps are derived from sample positions. Evidence: test name / command / log path / exit code.
- [ ] `05` no unintended overlap exists. Evidence: test name / command / log path / exit code.
- [ ] `06` no unexplained gap exists. Evidence: test name / command / log path / exit code.
- [ ] `07` chapter boundaries map to the script. Evidence: test name / command / log path / exit code.
- [ ] `08` music cues reference licensed assets. Evidence: test name / command / log path / exit code.
- [ ] `09` SFX cues reference licensed assets. Evidence: test name / command / log path / exit code.
- [ ] `10` timeline regeneration is deterministic. Evidence: test name / command / log path / exit code.
- [ ] `11` rounding does not accumulate drift. Evidence: test name / command / log path / exit code.
- [ ] `12` stop/resume does not duplicate segments. Evidence: test name / command / log path / exit code.


## Rights and media tests

- [ ] `01` every final-used local file has a source record. Evidence: test name / command / log path / exit code.
- [ ] `02` every rights PASS is file-specific. Evidence: test name / command / log path / exit code.
- [ ] `03` every legal status is separate from editorial suitability. Evidence: test name / command / log path / exit code.
- [ ] `04` UNKNOWN assets cannot be rendered. Evidence: test name / command / log path / exit code.
- [ ] `05` BLOCKED assets cannot be rendered. Evidence: test name / command / log path / exit code.
- [ ] `06` NASA music is excluded unless separately cleared. Evidence: test name / command / log path / exit code.
- [ ] `07` third-party content is flagged. Evidence: test name / command / log path / exit code.
- [ ] `08` identifiable people are reviewed. Evidence: test name / command / log path / exit code.
- [ ] `09` logos and endorsement implications are reviewed. Evidence: test name / command / log path / exit code.
- [ ] `10` zero-byte files are excluded. Evidence: test name / command / log path / exit code.
- [ ] `11` corrupt files are excluded. Evidence: test name / command / log path / exit code.
- [ ] `12` retrieval revalidates assets. Evidence: test name / command / log path / exit code.
- [ ] `13` missing files fail closed. Evidence: test name / command / log path / exit code.
- [ ] `14` hash mismatch is detected. Evidence: test name / command / log path / exit code.
- [ ] `15` library index contains no duplicate assets. Evidence: test name / command / log path / exit code.
- [ ] `16` index generation is deterministic. Evidence: test name / command / log path / exit code.
- [ ] `17` rights audit covers every used shot. Evidence: test name / command / log path / exit code.


## Shot plan and visual tests

- [ ] `01` every shot maps to a narration sample range. Evidence: test name / command / log path / exit code.
- [ ] `02` every shot has a visual objective. Evidence: test name / command / log path / exit code.
- [ ] `03` every direct evidence shot supports the stated scene. Evidence: test name / command / log path / exit code.
- [ ] `04` contextual B-roll is labeled as contextual. Evidence: test name / command / log path / exit code.
- [ ] `05` programmatic graphics have source-backed data. Evidence: test name / command / log path / exit code.
- [ ] `06` reconstruction is not presented as documentary footage. Evidence: test name / command / log path / exit code.
- [ ] `07` no shot is present only to fill runtime. Evidence: test name / command / log path / exit code.
- [ ] `08` no repeated shot is accidental. Evidence: test name / command / log path / exit code.
- [ ] `09` maps use correct period and geography. Evidence: test name / command / log path / exit code.
- [ ] `10` charts label values and units. Evidence: test name / command / log path / exit code.
- [ ] `11` all titles and labels fit safe areas. Evidence: test name / command / log path / exit code.
- [ ] `12` no subtitle is hidden by a graphic. Evidence: test name / command / log path / exit code.
- [ ] `13` contact sheets include all shots. Evidence: test name / command / log path / exit code.


## Remotion tests

- [ ] `01` Remotion license gate is recorded. Evidence: test name / command / log path / exit code.
- [ ] `02` all @remotion packages share the same exact version. Evidence: test name / command / log path / exit code.
- [ ] `03` composition width and height are explicit. Evidence: test name / command / log path / exit code.
- [ ] `04` composition fps is explicit. Evidence: test name / command / log path / exit code.
- [ ] `05` durationInFrames is explicit. Evidence: test name / command / log path / exit code.
- [ ] `06` props are validated. Evidence: test name / command / log path / exit code.
- [ ] `07` no unpinned remote asset is needed. Evidence: test name / command / log path / exit code.
- [ ] `08` rendered still is inspected. Evidence: test name / command / log path / exit code.
- [ ] `09` short render is decoded successfully. Evidence: test name / command / log path / exit code.
- [ ] `10` rendered frames match expected count. Evidence: test name / command / log path / exit code.
- [ ] `11` browser / memory usage is bounded. Evidence: test name / command / log path / exit code.
- [ ] `12` fallback graphic exists for critical scene. Evidence: test name / command / log path / exit code.


## FFmpeg tests

- [ ] `01` source files are never used as output paths. Evidence: test name / command / log path / exit code.
- [ ] `02` all inputs are probed before render. Evidence: test name / command / log path / exit code.
- [ ] `03` all rendered clips have valid frame count. Evidence: test name / command / log path / exit code.
- [ ] `04` all rendered clips have valid audio if expected. Evidence: test name / command / log path / exit code.
- [ ] `05` concat inputs have matching compatible stream parameters. Evidence: test name / command / log path / exit code.
- [ ] `06` final file is MP4. Evidence: test name / command / log path / exit code.
- [ ] `07` video codec is H.264. Evidence: test name / command / log path / exit code.
- [ ] `08` audio codec is AAC. Evidence: test name / command / log path / exit code.
- [ ] `09` resolution is 1920x1080. Evidence: test name / command / log path / exit code.
- [ ] `10` frame rate is 30 fps. Evidence: test name / command / log path / exit code.
- [ ] `11` audio sample rate is 48000 Hz. Evidence: test name / command / log path / exit code.
- [ ] `12` pixel format is yuv420p. Evidence: test name / command / log path / exit code.
- [ ] `13` faststart is enabled. Evidence: test name / command / log path / exit code.
- [ ] `14` full decode succeeds. Evidence: test name / command / log path / exit code.
- [ ] `15` final duration is within target tolerance. Evidence: test name / command / log path / exit code.
- [ ] `16` final file SHA256 is recorded. Evidence: test name / command / log path / exit code.


## Sound and subtitle tests

- [ ] `01` narration is intelligible. Evidence: test name / command / log path / exit code.
- [ ] `02` music does not mask narration. Evidence: test name / command / log path / exit code.
- [ ] `03` music rights are verified. Evidence: test name / command / log path / exit code.
- [ ] `04` SFX rights are verified. Evidence: test name / command / log path / exit code.
- [ ] `05` audio true peak is below project ceiling. Evidence: test name / command / log path / exit code.
- [ ] `06` no unexpected clipping exists. Evidence: test name / command / log path / exit code.
- [ ] `07` no unintended silence exists. Evidence: test name / command / log path / exit code.
- [ ] `08` no channel is missing. Evidence: test name / command / log path / exit code.
- [ ] `09` subtitle file parses. Evidence: test name / command / log path / exit code.
- [ ] `10` subtitle timestamps are ordered. Evidence: test name / command / log path / exit code.
- [ ] `11` subtitle text matches frozen transcript. Evidence: test name / command / log path / exit code.
- [ ] `12` subtitle lines fit mobile safe area. Evidence: test name / command / log path / exit code.
- [ ] `13` chapter timestamps match final render. Evidence: test name / command / log path / exit code.


## Editorial and YouTube tests

- [ ] `01` opening hook matches the title promise. Evidence: test name / command / log path / exit code.
- [ ] `02` thumbnail is truthful. Evidence: test name / command / log path / exit code.
- [ ] `03` title is supported by the film. Evidence: test name / command / log path / exit code.
- [ ] `04` no unsupported sensational claim appears. Evidence: test name / command / log path / exit code.
- [ ] `05` all chapter labels describe their content. Evidence: test name / command / log path / exit code.
- [ ] `06` credits include all rights-required attribution. Evidence: test name / command / log path / exit code.
- [ ] `07` final ending has a clear payoff. Evidence: test name / command / log path / exit code.
- [ ] `08` final film has no unresolved rights assets. Evidence: test name / command / log path / exit code.
- [ ] `09` final film has no unresolved factual blockers. Evidence: test name / command / log path / exit code.
- [ ] `10` analytics values are not fabricated. Evidence: test name / command / log path / exit code.
- [ ] `11` unpublished video is not represented as published. Evidence: test name / command / log path / exit code.


# PART 27 — 25 PREVIOUSLY UNKNOWN SOURCE / SHOT REMEDIATION

The following are 25 work slots for the original UNKNOWN shots. Resolve each to the actual source and shot IDs. Never assume a legal status from the old report alone.

## UNKNOWN-SOURCE-SLOT-01
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-02
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-03
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-04
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-05
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-06
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-07
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-08
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-09
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-10
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-11
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-12
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-13
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-14
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-15
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-16
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-17
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-18
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-19
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-20
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-21
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-22
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-23
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-24
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.

## UNKNOWN-SOURCE-SLOT-25
- Find original source and all affected shot IDs.
- Inspect the exact file and source page.
- Identify creator, copyright owner and license.
- Verify commercial use and derivative-edit permission.
- Check music, third-party material, people, brands and logos.
- Search for a more accurate rights-cleared direct visual.
- If no direct visual is possible, design an evidence-based programmatic graphic.
- Record new file hash, provenance and visual classification.
- Update status only in isolated snapshot.
- Ensure the unknown original is not included in the final render.
- Independent reviewer must sign off.


# PART 28 — DATA CONTRACT EXAMPLES

The following snippets are illustrative schemas. Adapt them to the project's existing schema and versioning. Do not create duplicate incompatible manifests.

## 28.1. Episode manifest example

```json
{
  "schema_version": 1,
  "episode_id": "episode-001",
  "title_working": "Evidence-backed working title",
  "language": "ru",
  "target_duration_seconds": 1200,
  "duration_tolerance_seconds": 15,
  "video": {
    "width": 1920,
    "height": 1080,
    "fps_num": 30,
    "fps_den": 1,
    "aspect_ratio": "16:9",
    "codec": "h264",
    "pixel_format": "yuv420p"
  },
  "audio": {
    "sample_rate": 48000,
    "channels": 2,
    "codec": "aac"
  },
  "source_policy": {
    "real_footage_primary": true,
    "ai_video_generation": false,
    "unknown_rights_allowed_in_final": false
  }
}
```

## 28.2. Research claim example

```json
{
  "claim_id": "CLM-0001",
  "claim": "A concise factual statement supported by the source.",
  "status": "VERIFIED",
  "confidence": "high",
  "source_ids": ["SRC-0001", "SRC-0002"],
  "script_refs": ["PAR-0004"],
  "notes": "The wording is narrower than the source interpretation."
}
```

## 28.3. Source record example

```json
{
  "source_id": "SRC-0001",
  "title": "Original source title",
  "organization": "Source organization",
  "creator": "Named creator or organization",
  "url": "https://example.org/original-record",
  "publication_date": null,
  "accessed_at": "2026-11-28",
  "source_type": "primary",
  "license": null,
  "supporting_excerpt_ref": "research/evidence/SRC-0001.txt"
}
```

## 28.4. Rights asset example

```json
{
  "asset_id": "AST-0001",
  "path": "assets/footage/example.mp4",
  "size_bytes": 1000000,
  "sha256": "actual-64-character-hash",
  "source_id": "SRC-0001",
  "rights_status": "PASS",
  "license_name": "Exact license or public-domain basis",
  "license_url": "https://example.org/license",
  "commercial_use": true,
  "derivatives_allowed": true,
  "attribution": "Exact required attribution",
  "music_included": false,
  "third_party_material": false,
  "restrictions": [],
  "shot_ids": ["SHOT-0001"]
}
```

## 28.5. Shot example

```json
{
  "shot_id": "SHOT-0001",
  "chapter_id": "CH-01",
  "start_sample": 0,
  "end_sample": 240000,
  "narration_refs": ["PAR-0001"],
  "claim_ids": ["CLM-0001"],
  "visual_class": "PROGRAMMATIC_GRAPHIC",
  "visual_objective": "Explain the relationship described by the narration.",
  "asset_ids": [],
  "rights_status": "PASS",
  "editorial_status": "DIRECT",
  "transition_in": "cut",
  "transition_out": "match",
  "review_status": "PENDING"
}
```

## 28.6. Render manifest example

```json
{
  "render_id": "RND-0001",
  "episode_id": "episode-001",
  "input_manifest_hash": "actual-hash",
  "script_revision": "script-v-final",
  "narration_sha256": "actual-hash",
  "timeline_sha256": "actual-hash",
  "shot_plan_sha256": "actual-hash",
  "ffmpeg_version": "actual-version",
  "remotion_version": null,
  "settings": {
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "video_codec": "h264",
    "audio_codec": "aac",
    "audio_sample_rate": 48000
  },
  "output_path": "exports/final_20min.mp4",
  "output_sha256": "actual-hash",
  "status": "COMPLETED"
}
```

---

# PART 29 — EDITORIAL QUALITY CONTROL RUBRIC

Score each category 0–5, with a written evidence-based note. Scores are internal diagnostic tools, not claims about audience performance.

1. Opening clarity.
2. Opening curiosity.
3. Viewer promise.
4. Narrative coherence.
5. Claim accuracy.
6. Source transparency.
7. Chapter progression.
8. Emotional pacing.
9. Visual relevance.
10. Visual variety.
11. Map / chart legibility.
12. Motion design consistency.
13. Narration intelligibility.
14. Sound quality.
15. Music restraint.
16. Subtitle readability.
17. Transition quality.
18. Ending payoff.
19. Title accuracy.
20. Thumbnail accuracy.

Minimum acceptance is not a high average hiding a blocker. A critical factual or legal defect blocks publication regardless of score.

---

# PART 30 — FAILURE HANDLING AND RECOVERY

For every stage, distinguish:

- user input missing;
- external authorization missing;
- network outage;
- rate limit;
- disk exhaustion;
- invalid input media;
- corrupt intermediate;
- code defect;
- test defect;
- reviewer defect;
- rights uncertainty;
- editorial mismatch.

Each failure must:

1. produce a structured error;
2. preserve completed outputs;
3. record a checkpoint;
4. avoid duplicate external side effects;
5. set task state accurately;
6. select a safe alternative if possible;
7. continue independent tasks.

## 30.1. HTTP 429

- max three bounded attempts;
- respect `Retry-After` seconds or HTTP date;
- cap wait time;
- use async sleep in async path;
- never block the event loop;
- no paid fallback;
- return controlled error after exhaustion;
- record provider/model and retry count without secrets.

## 30.2. Disk exhaustion

- stop resource-intensive work;
- do not delete user media;
- preserve the last valid render;
- remove only current-run temporary files whose ownership and reproducibility are proven;
- if uncertain, leave files untouched;
- record disk usage and blocked task.

## 30.3. Interrupted render

- use per-chapter or per-segment checkpoints;
- verify hashes of completed segments;
- skip valid segments;
- rerun only failed segments;
- never overwrite prior final render;
- assemble atomically into a new output name.

---

# PART 31 — TASK GRAPH DESIGN

Use one parent production task and stable child task IDs. Tasks should be small enough to test but large enough to avoid unnecessary model round-trips.

The parent task should not be marked complete until all required gates are done or genuinely blocked by owner actions.

Dependencies:

- `workspace_verified` precedes all writes;
- `skills_verified` precedes skill-guided rendering tasks;
- `topic_selected` precedes final research and script;
- `research_pass` precedes script freeze;
- `script_frozen` precedes TTS generation;
- `narration_validated` precedes audio timeline freeze;
- `rights_verified` precedes footage use;
- `shot_plan_validated` precedes final assembly;
- `graphics_validated` precedes final assembly;
- `audio_mix_validated` precedes final assembly;
- `render_pass` precedes final QA;
- `technical_qa_pass` and `editorial_review` precede delivery;
- `youtube_package` depends on final timestamps and final title/thumbnail content.

A blocked task must not block unrelated work. For example, an unavailable Kaggle account must not prevent implementation of the WAV importer, timeline validators, FFmpeg graphics, or YouTube package templates.


# PART 32 — RESEARCH QUALITY DETAIL

- [ ] D-001 Confirm a claim's exact scope: time period, geography, population, unit, and definition.
- [ ] D-002 Distinguish source fact from author interpretation.
- [ ] D-003 Check whether a source is quoting another source rather than reporting original evidence.
- [ ] D-004 Open primary documents where possible; do not rely only on search snippets.
- [ ] D-005 Record source access date and visible publication date separately.
- [ ] D-006 Check whether the source has been corrected or superseded.
- [ ] D-007 Record conflicting sources instead of silently choosing one.
- [ ] D-008 Check historical place names and spelling variants.
- [ ] D-009 Check numeric values against original tables or datasets.
- [ ] D-010 Retain source excerpts in a durable local evidence file.
- [ ] D-011 Keep source URL and source title in manifest.
- [ ] D-012 Do not fabricate the text of an unavailable source.
- [ ] D-013 Do not cite an aggregator when the original record is available.
- [ ] D-014 Record confidence and reviewer rationale.
- [ ] D-015 Link each fact to its script paragraph.
- [ ] D-016 Link on-screen labels to evidence IDs.
- [ ] D-017 Make uncertainty visible in narration when it matters.
- [ ] D-018 Do not imply causation when evidence shows correlation only.
- [ ] D-019 Check whether a quote is translated and preserve the original source.
- [ ] D-020 Verify the quote context before using it.
- [ ] D-021 Check spelling and pronunciation of names.
- [ ] D-022 Check dates in the selected episode timezone / calendar system.
- [ ] D-023 Identify which claims are essential to the central thesis.
- [ ] D-024 Remove unsupported claims before narration freeze.
- [ ] D-025 Keep an unresolved-claims section for claims not used.

# PART 33 — DOCUMENTARY SCRIPT DETAIL

- [ ] D-001 Cold open begins with a specific concrete question or event.
- [ ] D-002 First 10 seconds contain a meaningful image / sound / statement.
- [ ] D-003 First 30 seconds establish why the subject matters.
- [ ] D-004 Avoid opening with a channel logo longer than editorially necessary.
- [ ] D-005 State the central mystery or question clearly.
- [ ] D-006 Do not reveal the entire conclusion in the first sentence unless the structure requires it.
- [ ] D-007 Use a clear transition from hook to context.
- [ ] D-008 Introduce only names the viewer needs at that point.
- [ ] D-009 Explain uncommon terms in spoken language.
- [ ] D-010 Use short and medium sentences in alternation.
- [ ] D-011 Read all dates and numbers aloud during script review.
- [ ] D-012 Remove repetitive rhetorical questions.
- [ ] D-013 Do not repeat a fact in multiple chapters without adding meaning.
- [ ] D-014 Use transitions based on consequence or contrast.
- [ ] D-015 Build suspense only from actual unknowns or contradictions.
- [ ] D-016 Make chapter endings lead naturally to the next question.
- [ ] D-017 Include counter-evidence where it materially changes the story.
- [ ] D-018 Keep the narrator's certainty aligned with sources.
- [ ] D-019 Do not claim eyewitness knowledge when the source is secondary.
- [ ] D-020 Do not attribute thoughts or motives without evidence.
- [ ] D-021 Do not turn speculation into a dramatic assertion.
- [ ] D-022 Use a real payoff in the final act.
- [ ] D-023 End with a synthesis, not merely a recap list.
- [ ] D-024 Finish with a relevant viewer question.
- [ ] D-025 Keep promotional calls-to-action brief and separate from the documentary argument.

# PART 34 — AUDIO QUALITY DETAIL

- [ ] D-001 Check narration for mouth clicks where present.
- [ ] D-002 Check for clipped word beginnings.
- [ ] D-003 Check for clipped word endings.
- [ ] D-004 Check room / noise artifacts.
- [ ] D-005 Check unnatural pauses between concatenated segments.
- [ ] D-006 Check TTS pronunciation of proper nouns.
- [ ] D-007 Check difficult numbers and dates.
- [ ] D-008 Check inconsistent voice speed.
- [ ] D-009 Check audible pitch changes between segments.
- [ ] D-010 Check loudness jumps at chapter boundaries.
- [ ] D-011 Check for duplicated sentence fragments.
- [ ] D-012 Check for missing paragraphs.
- [ ] D-013 Check left/right channel consistency.
- [ ] D-014 Check mono compatibility after stereo mix.
- [ ] D-015 Check true peak.
- [ ] D-016 Check integrated loudness.
- [ ] D-017 Check loudness range if useful.
- [ ] D-018 Check background noise during pauses.
- [ ] D-019 Check fade-in and fade-out.
- [ ] D-020 Check music ducking against narration.
- [ ] D-021 Check SFX peaks.
- [ ] D-022 Check no music overlaps a source clip's existing music unexpectedly.
- [ ] D-023 Check all source audio tracks have rights.
- [ ] D-024 Check no hidden audio stream is accidentally included.
- [ ] D-025 Check WAV metadata and codec.

# PART 35 — VISUAL STORYTELLING DETAIL

- [ ] D-001 Every visual has a declared purpose.
- [ ] D-002 Every direct-evidence shot depicts the actual described event or object.
- [ ] D-003 Contextual footage is never captioned as the actual event.
- [ ] D-004 Historical reconstructions are labelled where needed.
- [ ] D-005 Maps use evidence-backed borders and place names.
- [ ] D-006 Charts use consistent units.
- [ ] D-007 Charts do not exaggerate visual differences.
- [ ] D-008 Timelines distinguish exact dates from approximate periods.
- [ ] D-009 Animation does not imply a causal connection that is not supported.
- [ ] D-010 Use establishing shots to orient the viewer.
- [ ] D-011 Use close-up/detail shots to focus attention.
- [ ] D-012 Use visual contrasts to explain a difference.
- [ ] D-013 Use on-screen source citations for critical figures.
- [ ] D-014 Keep source credits readable.
- [ ] D-015 Use consistent lower thirds.
- [ ] D-016 Keep title cards brief.
- [ ] D-017 Avoid unnecessary wipe / glitch transitions.
- [ ] D-018 Use match cuts only when the relationship is clear.
- [ ] D-019 Use J-cut / L-cut to smooth transitions where appropriate.
- [ ] D-020 Use audio bridge when the next scene begins before its visual.
- [ ] D-021 Check visual continuity at cut points.
- [ ] D-022 Check repeated B-roll across chapters.
- [ ] D-023 Check image crops do not remove context.
- [ ] D-024 Check no stretched images.
- [ ] D-025 Check no aspect-ratio distortion.

# PART 36 — FFMPEG AND RENDER DETAIL

- [ ] D-001 Probe each original asset before creating proxies.
- [ ] D-002 Do not assume extension identifies media format.
- [ ] D-003 Check variable-frame-rate sources.
- [ ] D-004 Check rotation metadata.
- [ ] D-005 Check sample aspect ratio.
- [ ] D-006 Check display aspect ratio.
- [ ] D-007 Check pixel format compatibility.
- [ ] D-008 Check color primaries and transfer characteristics.
- [ ] D-009 Check source audio stream count.
- [ ] D-010 Check source time base.
- [ ] D-011 Check timestamps for discontinuities.
- [ ] D-012 Check whether a source starts at non-zero PTS.
- [ ] D-013 Check concat stream compatibility.
- [ ] D-014 Check exact cut points around keyframes.
- [ ] D-015 Use accurate seeking when required.
- [ ] D-016 Check audio resample filter.
- [ ] D-017 Check scaling method.
- [ ] D-018 Check deinterlace if source is interlaced.
- [ ] D-019 Check crop bounds and safe framing.
- [ ] D-020 Check subtitle renderer availability.
- [ ] D-021 Check drawtext / fonts availability.
- [ ] D-022 Check required FFmpeg encoders.
- [ ] D-023 Check H.264 encoder build license.
- [ ] D-024 Check that output muxer supports faststart.
- [ ] D-025 Check output file before final rename.
- [ ] D-026 Use atomic rename after successful validation.

# PART 37 — DELIVERY DETAIL

- [ ] D-001 Use a stable episode slug.
- [ ] D-002 Use versioned render names for previews.
- [ ] D-003 Use a stable final export name only after acceptance.
- [ ] D-004 Keep subtitles beside final video.
- [ ] D-005 Keep thumbnail beside final video.
- [ ] D-006 Keep all sources and attribution in a separate file.
- [ ] D-007 Keep the render manifest.
- [ ] D-008 Keep the final QA report.
- [ ] D-009 Keep the editorial review report.
- [ ] D-010 Keep the final SHA256 manifest.
- [ ] D-011 Keep a review proxy separate from the final master.
- [ ] D-012 Keep the chapter contact sheets.
- [ ] D-013 Keep the exact final duration.
- [ ] D-014 Keep the final audio sample count.
- [ ] D-015 Keep the final frame count.
- [ ] D-016 Record the FFmpeg version.
- [ ] D-017 Record the Remotion version if used.
- [ ] D-018 Record the Python / Node versions.
- [ ] D-019 Record all installed skills and versions.
- [ ] D-020 Ensure final output path is readable by the owner.
- [ ] D-021 Ensure filename contains no ambiguous draft marker.
- [ ] D-022 Do not upload or publish automatically.
- [ ] D-023 Add publication-ready checklist.
- [ ] D-024 Add one-line status summary.
- [ ] D-025 Add owner actions in one place.

# PART 38 — SUBTASK SEQUENCE AND DEPENDENCY MAP

This sequence is a work queue reference. The agent must turn it into the installed Ordewell task graph and preserve actual task IDs and checkpoints. Dependencies below are conceptual; adapt to the existing runner's schema.

- `S00` — Workspace verification | Gate: G0 | Depends on: none
- `S01` — Read all current handoffs and reports | Gate: G0 | Depends on: S00
- `S02` — Inspect disk and mount topology | Gate: G0 | Depends on: S00
- `S03` — Inventory skills and toolchain | Gate: G1 | Depends on: S00
- `S04` — Review FFmpeg skill source and license | Gate: G1 | Depends on: S03
- `S05` — Install and verify FFmpeg skill | Gate: G1 | Depends on: S04
- `S06` — Review official Remotion skills and license | Gate: G1 | Depends on: S03
- `S07` — Install official Remotion skills | Gate: G1 | Depends on: S06
- `S08` — Verify Remotion runtime need and eligibility | Gate: G1 | Depends on: S06
- `S09` — Verify FFmpeg filters and encoders | Gate: G1 | Depends on: S02
- `S10` — Map current Factory architecture | Gate: G0 | Depends on: S01
- `S11` — Verify zero-byte code in snapshot | Gate: G0 | Depends on: S10
- `S12` — Verify KiloClient async and 429 code | Gate: G0 | Depends on: S10
- `S13` — Verify rights audit and remediation | Gate: G0 | Depends on: S10
- `S14` — Select episode topic | Gate: G2 | Depends on: S01
- `S15` — Build research dossier | Gate: G2 | Depends on: S14
- `S16` — Build claim ledger | Gate: G2 | Depends on: S15
- `S17` — Independent fact-check | Gate: G2 | Depends on: S16
- `S18` — Write story outline | Gate: G3 | Depends on: S17
- `S19` — Draft 20-minute script | Gate: G3 | Depends on: S18
- `S20` — Review spoken narration | Gate: G3 | Depends on: S19
- `S21` — Freeze script and hash | Gate: G3 | Depends on: S20
- `S22` — Verify TTS voice/model license | Gate: G5 | Depends on: S21
- `S23` — Prepare Kaggle notebook | Gate: G5 | Depends on: S22
- `S24` — Check Kaggle CLI and authorization | Gate: G5 | Depends on: S23
- `S25` — Run Kaggle Piper or prepare owner packet | Gate: G5 | Depends on: S24
- `S26` — Validate narration WAV | Gate: G5 | Depends on: S25
- `S27` — Freeze narration master | Gate: G5 | Depends on: S26
- `S28` — Build sample-accurate timeline | Gate: G6 | Depends on: S27
- `S29` — Validate timeline and chapter boundaries | Gate: G6 | Depends on: S28
- `S30` — Reconcile original 35 shots | Gate: G7 | Depends on: S13,S29
- `S31` — Find and verify exact legal asset candidates | Gate: G7 | Depends on: S30
- `S32` — Create code-built graphic replacements | Gate: G7 | Depends on: S31
- `S33` — Update shot plan | Gate: G7 | Depends on: S32
- `S34` — Update rights manifest and audit | Gate: G7 | Depends on: S33
- `S35` — Independent rights review | Gate: G7 | Depends on: S34
- `S36` — Independent editorial shot review | Gate: G7 | Depends on: S35
- `S37` — Expand shot plan for full runtime | Gate: G8 | Depends on: S36
- `S38` — Create EDL and scene manifests | Gate: G8 | Depends on: S37
- `S39` — Create motion design system | Gate: G8 | Depends on: S05,S07,S37
- `S40` — Create Remotion compositions if permitted | Gate: G8 | Depends on: S39
- `S41` — Create Python/FFmpeg fallback graphics | Gate: G8 | Depends on: S39
- `S42` — Create subtitle source and timing | Gate: G8 | Depends on: S28
- `S43` — Create sound cue and mix plan | Gate: G8 | Depends on: S29
- `S44` — Render chapter previews | Gate: G9 | Depends on: S38,S40,S41,S42,S43
- `S45` — Review preview clips | Gate: G9 | Depends on: S44
- `S46` — Correct all preview defects | Gate: G9 | Depends on: S45
- `S47` — Render final 20-minute master | Gate: G10 | Depends on: S46
- `S48` — Run full decode and technical QA | Gate: G10 | Depends on: S47
- `S49` — Run subtitle QA | Gate: G10 | Depends on: S47
- `S50` — Run audio QA | Gate: G10 | Depends on: S47
- `S51` — Create contact sheets and proxy | Gate: G10 | Depends on: S47
- `S52` — Independent editorial final review | Gate: G10 | Depends on: S48,S49,S50,S51
- `S53` — Correct final defects if needed | Gate: G10 | Depends on: S52
- `S54` — Re-render if required | Gate: G10 | Depends on: S53
- `S55` — Build YouTube package | Gate: G11 | Depends on: S47
- `S56` — Create final source / credits pack | Gate: G11 | Depends on: S34,S47
- `S57` — Create final hashes and delivery manifest | Gate: G11 | Depends on: S48,S55,S56
- `S58` — Verify status / resume behavior | Gate: G11 | Depends on: S57
- `S59` — Write consolidated final report | Gate: G11 | Depends on: S58
- `S60` — Update handoff and stop safely | Gate: G11 | Depends on: S59

# PART 39 — DETAILED SHOT / CHAPTER REVIEW TEMPLATE

For every chapter create a review record with:

- chapter ID;
- start / end time;
- central question;
- factual claims;
- narration segments;
- shot IDs;
- rights status;
- visual class;
- visual rhythm;
- map / chart references;
- sound cues;
- subtitle concerns;
- transition intent;
- chapter payoff;
- reviewer notes;
- corrected revision;
- reviewer verdict.

For each shot, create a separate entry if rights or editorial status differs.

---

# PART 40 — FINAL EXECUTION CHECKLIST

## Before work

- [ ] Read the entire master file.
- [ ] Verify active isolated workspace.
- [ ] Verify original checkout is untouched.
- [ ] Verify disk and inode headroom.
- [ ] Inspect existing reports and checkpoints.
- [ ] Inventory existing skills.
- [ ] Inspect FFmpeg / ffprobe.
- [ ] Verify model and concurrency settings.

## Before narration

- [ ] Select the episode topic.
- [ ] Complete research and claim ledger.
- [ ] Draft and review the script.
- [ ] Measure speaking rate.
- [ ] Verify TTS voice/model license.
- [ ] Freeze script revision.
- [ ] Generate genuine narration.
- [ ] Validate WAV.
- [ ] Build and validate sample-accurate timeline.

## Before final visuals

- [ ] Reconcile all 35 old shots.
- [ ] Replace or exclude all UNKNOWN rights footage.
- [ ] Verify all exact source files.
- [ ] Expand shot plan for full narration.
- [ ] Generate maps / charts from cited data.
- [ ] Render and validate Remotion clips if used.
- [ ] Verify every graphics asset.

## Before final render

- [ ] Build EDL.
- [ ] Validate all inputs.
- [ ] Check render output volume.
- [ ] Render chapter previews.
- [ ] Check audio mix.
- [ ] Validate subtitles.
- [ ] Render final MP4.
- [ ] Full decode.
- [ ] Technical QA.
- [ ] Editorial review.
- [ ] Rights review.
- [ ] Hash final output.

## Before delivery

- [ ] SRT and VTT exist.
- [ ] Thumbnail exists.
- [ ] Five titles exist.
- [ ] Description exists.
- [ ] Chapters are exact.
- [ ] Credits / sources exist.
- [ ] QA reports exist.
- [ ] Reviewer verdicts exist.
- [ ] Project state is accurate.
- [ ] One consolidated owner-action list exists.
- [ ] Original checkout remains unchanged.

---

# PART 41 — OFFICIAL AND PROJECT REFERENCES

The agent must re-open the current versions before installing or using the tools. The following sources were checked on 28 November 2026 and are the initial reference set.

## Remotion

- Agent Skills documentation: https://www.remotion.dev/docs/agents/skills
- Official Agent Skills repository: https://github.com/remotion-dev/skills
- Remotion releases: https://github.com/remotion-dev/remotion/releases
- License overview: https://www.remotion.dev/docs/license
- Pricing / eligibility: https://www.remotion.dev/docs/license/pricing
- Terms: https://www.remotion.dev/docs/terms
- Rendering: https://www.remotion.dev/docs/render
- Server-side renderer: https://www.remotion.dev/docs/api
- Passing props: https://www.remotion.dev/docs/passing-props
- FFmpeg documentation: https://www.ffmpeg.org/documentation.html

## FFmpeg Skill

- Repository: https://github.com/kajisho5/ffmpeg-skill
- README: https://github.com/kajisho5/ffmpeg-skill/blob/main/README.md
- Skill file: https://github.com/kajisho5/ffmpeg-skill/blob/main/SKILL.md
- Security: https://github.com/kajisho5/ffmpeg-skill/blob/main/SECURITY.md
- License: https://github.com/kajisho5/ffmpeg-skill/blob/main/LICENSE

## OpenCode Skills

- Official documentation: https://opencode.ai/docs/skills

## YouTube

- Recommended upload encoding: https://support.google.com/youtube/answer/1722171

---

# PART 42 — FINAL RULE

The owner wants one file to give to the agent, not a chain of tiny prompts.

This file is the single source of execution instructions for the first 20-minute documentary and the reusable factory.

Read all of it. Verify the workspace. Install the verified skills safely. Build the production graph. Execute every safe task. Keep the original repository untouched. Produce one real 20-minute documentary if the external dependencies permit. If an external dependency cannot be completed, prepare everything possible and report the exact owner action.

Do not return after 30–40 seconds with a progress summary.

Do not mark a workstream done because a model response ended.

Do not confuse `PARTIAL_READY` with `PRODUCTION_READY`.

The final report must link to the actual MP4 and show proof of full decode, rights status, narration validity, technical QA and independent review.

**The deliverable is the working factory plus the finished 20-minute documentary — not another plan.**
