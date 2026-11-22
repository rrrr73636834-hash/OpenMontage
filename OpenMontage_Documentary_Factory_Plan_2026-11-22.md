# FACTORY PLAN
## OpenMontage → Documentary Factory (20–40 минут)

**Назначение:** техническое задание для coding-agent в GitHub Codespaces. Реализовать отдельный long-form pipeline на основе проверенных компонентов OpenMontage, с локальными провайдерами, независимыми задачами по главам и блокирующим QA.

**Дата исследования:** 22 ноября 2026  
**Исходный репозиторий:** [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)  
**Текущий канонический адрес после переноса:** [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)  
**Проверенный commit `main`:** `2e003e65fa99a0f329478a2c1cdcf26bc481933a` (16 Nov 2026)  
**Проверенный tree:** `a221ab9fa50d1089dcf08a4b38f6322a3c99a395`  
**Лицензия:** GNU Affero General Public License v3 (AGPL-3.0).

---

# 0. Инструкция coding-agent: обязательные ограничения

Это не просьба «сгенерировать видео». Выполняй этапы строго по порядку, запускай тесты после каждого этапа и не переходи к следующему при провале критериев.

## 0.1 Жёсткие требования

1. Финальный формат — документальное видео **20–40 минут, 16:9, 1920×1080, 30 fps**.
2. Источник визуала по умолчанию — **локальная библиотека видеофутажа**. Поиск учитывает тему, объект, действие, настроение, эпоху, локацию, композицию и права на использование.
3. FLUX.1 Schnell — только fallback для конкретного visual slot, когда подходящего клипа в библиотеке нет и статичный визуал уместен. Рендерить AI-фото через controlled pan/zoom. **AI-video / motion generation запрещены.**
4. Озвучка — локальный Kokoro, голос `af_heart`; не вызывать ElevenLabs, Azure, Google TTS, OpenAI TTS, HeyGen и другие облачные TTS.
5. Сценарный LLM — локальный Ollama или совместимый локальный endpoint. Не использовать OpenAI, Anthropic, Gemini или другой облачный LLM.
6. Codespaces — orchestration, планирование, retrieval, сборка и QA. Kaggle — только изолированные GPU-задачи генерации FLUX-изображений.
7. Длинный фильм разбить на главы-задачи. Retry/resume работает **по конкретной главе и конкретному этапу**, а не перезапускает весь проект.
8. Автоматическое QA — на 100% shot/clip-единиц. Ручная проверка — выборочная: ключевые кадры, рискованные клипы, минимум один набор кадров на главу.
9. В production запрещены платные API и незаметный cloud fallback. Нет локального провайдера — остановка с понятной ошибкой.
10. Не запускать длинный production render, пока не пройдены smoke-тесты local LLM, Kokoro, retrieval, FLUX worker, chapter resume и QA.

## 0.2 Безопасность и сохранность репозитория

В начале работы:

```bash
git status --short --branch
git rev-parse HEAD
git remote -v
git switch -c factory/documentary-longform
```

Если рабочее дерево не чистое — сначала зафиксируй список изменений и не перезаписывай файлы пользователя. Не делай массовый рефакторинг и не удаляй существующие pipeline. Новую фабрику добавляй отдельно.

Не коммить медиа, модели, `.env`, Kaggle credentials и rendered outputs. Используй `.gitignore`, Codespaces Secrets и отдельный persistent media root.

## 0.3 Fail-closed правило

Блокируй следующий этап при любой ошибке, которая может дать неправильное, немое, неполное или не принадлежащее проекту видео. Запрещено:
- заменять неудачный local LLM cloud LLM;
- заменять Kokoro на ElevenLabs/Azure/Google;
- заменять FLUX worker на `fal.ai`, Replicate или OpenAI;
- заменять отсутствие local footage случайным stock clip;
- считать AAC stream доказательством слышимого аудио;
- отмечать chapter как `QA_PASSED`, если не проверены все shots этой главы.

---

# 1. Результат исследования OpenMontage

## 1.1 Архитектура по фактическому коду

OpenMontage — **agent-orchestrated production system**, а не автономный Python workflow engine. `docs/ARCHITECTURE.md` и `AGENT_GUIDE.md` описывают фактическую модель:

1. Coding-agent читает manifest `pipeline_defs/*.yaml`.
2. Читает stage instructions из `skills/pipelines/.../*.md`.
3. Принимает редакторские решения и вызывает Python tools через `tools/tool_registry.py`.
4. Передаёт результаты как JSON artifacts, валидирует их JSON Schema.
5. Сохраняет stage checkpoints через `lib/checkpoint.py`.

**Python не управляет всем pipeline самостоятельно.** Python предоставляет tools, schemas, конфигурацию, media processing и persistence. Control plane — coding-agent.

```text
Coding-agent
  ├── pipeline_defs/*.yaml
  ├── skills/pipelines/<pipeline>/*.md
  ├── schemas/artifacts/*.schema.json
  ├── tools/tool_registry.py → BaseTool implementations
  └── lib/checkpoint.py → projects/<id>/checkpoint_<stage>.json

Media
  ├── tools/video/stock_sources/* → remote source adapters
  ├── tools/video/corpus_builder.py → downloads + thumbnails + embeddings
  ├── lib/corpus.py + lib/clip_embedder.py → local indexed corpus
  ├── tools/video/clip_search.py → CLIP/tag retrieval
  ├── tools/audio/* → TTS/music/audio processing
  ├── tools/graphics/* → local/cloud image generation
  └── tools/video/video_compose.py / video_stitch.py → render/assembly

Review & export
  ├── tools/analysis/audio_probe.py
  ├── tools/analysis/visual_qa.py
  ├── tools/analysis/composition_validator.py
  └── tools/publishers/export_bundle.py
```

Tool registry автоматически обнаруживает Python tools. `BaseTool` описывает `capability`, `provider`, `runtime`, статус, resource profile, retry/idempotency и стоимость. Селекторы `tts_selector`, `image_selector`, `video_selector` могут выбирать cloud provider — новой фабрике нужен строгий allowlist.

## 1.2 Что уже можно использовать

| Компонент | Что реально есть | Решение |
|---|---|---|
| Pipeline manifests | YAML + `lib/pipeline_loader.py` | Использовать формат; создать отдельный `documentary-longform.yaml` |
| Tool registry | `tools/tool_registry.py`, `tools/base_tool.py` | Использовать для локальных tools; добавить provider policy |
| Checkpoints | `lib/checkpoint.py`: JSON, schema validation, history/archive, stage order | Переиспользовать как project persistence; добавить chapter/job state |
| Clip corpus | `lib/corpus.py`, embeddings/index/tag fields | Переиспользовать после filesystem ingest |
| CLIP retrieval | `lib/clip_embedder.py`, `tools/video/clip_search.py` | Переиспользовать и протестировать на своей библиотеке |
| Source contract | `tools/video/stock_sources/base.py` | Контракт источника есть, текущие adapters в основном remote |
| FFmpeg processing | `video_stitch.py`, `audio_mixer.py` | Использовать после regression tests на codecs/silence |
| Probe | `tools/analysis/audio_probe.py` | Переиспользовать, добавить строгие expected values |
| Visual review frames | `tools/analysis/visual_qa.py` | Для выборочной ручной проверки, не вместо 100% QA |
| Composition preflight | `tools/analysis/composition_validator.py` | Для pre-render check, не для post-render gate |
| ComfyUI | `tools/graphics/comfyui_image.py`, `tools/_comfyui/client.py` | Local image route; запретить cloud fallback |
| Export | `tools/publishers/export_bundle.py` | Локальная упаковка; поддерживает `chapters` |

## 1.3 Почему `documentary-montage` не подходит

`pipeline_defs/documentary-montage.yaml` и `skills/pipelines/documentary-montage/*` **не являются готовой основой 20–40-минутного narrated documentary**:
- `executive-producer.md` предназначен для **30–180 секунд**;
- формат non-narrative montage, а не длинный фильм с дикторской дорожкой;
- narration по умолчанию не предусмотрена;
- музыка и end-tag обязательны по умолчанию, если явно не отключить;
- этапы — `idea → scene_plan → assets → edit → compose`, а не chapter job graph;
- инструкции некоторых edit/grade/music решений не соответствуют фактическому render path (issues #937, #575).

**Решение:** не переделывать documentary-montage; создать новый `documentary-longform`, старый pipeline оставить без изменений.

## 1.4 Local footage: важный пробел

`tools/video/stock_sources/` содержит adapters вроде Pexels, Pixabay Video, Archive.org, NASA, Wikimedia, LOC, ESA, NOAA и др. Это удалённые источники.

`tools/video/corpus_builder.py` загружает кандидатов из доступных источников, строит thumbnails/embeddings и пополняет локальный corpus. Это **не scanner пользовательской файловой папки**.

`lib/corpus.py` хранит локальный поисковый индекс, но штатного filesystem ingester с sidecar tags, checksum deduplication и правами на использование в проекте не найдено.

**Нужно создать filesystem ingester.** После ingestion существующий `clip_search` можно применять для retrieval. Удалённые stock adapters отключить для production factory, если заказчик явно не разрешил источник.

## 1.5 LLM: реальный путь

- `config.yaml` задаёт `llm.provider: anthropic` по умолчанию.
- Ollama/LM Studio встречаются в комментариях/документации, но local LLM integration помечена как future/coming soon.
- Замена `llm.provider` на `ollama` сама по себе не подключает рабочий сценарный LLM client.
- Текстовые решения стадий в текущей архитектуре принимает coding-agent, читающий skills и вызывающий tools.

**Вывод:** нужен `factory/llm/ollama_client.py`: явный local HTTP contract, structured JSON output, validation, timeout/retry и запрет cloud fallback.

## 1.6 TTS: фактические варианты

- `tools/audio/tts_selector.py` автоматически обнаруживает `capability="tts"` и ранжирует providers. Без явного `allowed_providers` возможна нежелательная маршрутизация.
- `tools/audio/piper_tts.py` — локальный Piper, не Kokoro.
- Kokoro есть в отдельном JS flow: `.agents/skills/hyperframes-media/scripts/lib/tts.mjs` и `scripts/audio.mjs`, где можно явно выбрать `provider=kokoro` и передать voice. Это не штатный Python TTS tool documentary pipeline.
- В `requirements.txt` нет `kokoro-onnx` и `soundfile`; Makefile содержит Piper setup, не полноценную Python установку Kokoro.

**Вывод:** добавить `KokoroTTS` adapter или отдельный локальный module. Не использовать auto-mode selector.

### Критическое уточнение по `af_heart`

Официальный список Kokoro относит `af_heart` к **American English**. Официальный список языков модели не содержит русского.
- `af_heart` подходит для англоязычной narration (`en-US`).
- Для русского сценария нельзя обещать native pronunciation с `af_heart`; нужен отдельный тест, а не смена параметра.
- В config validation требовать соответствия script language и voice/language. Если narration должна быть русской, комбинация «Kokoro + af_heart» — блокирующее языковое несоответствие до подтверждения качества.

## 1.7 Image/video generation: фактическая реализация

### Изображения
`tools/graphics/comfyui_image.py` — настоящий `BaseTool` (`capability=image_generation`, `runtime=LOCAL_GPU`) с `workflow_json` / `workflow_path` и `output_node`.

`tools/_comfyui/client.py` проверяет `/system_stats`, отправляет workflow через `POST /prompt`, опрашивает `GET /history/{prompt_id}` и скачивает через `GET /view`.

Но встроенный workflow рассчитан на **FLUX.2 Dev NVFP4**, а не FLUX.1 Schnell. У `ComfyUIImage` есть fallback на `flux_image` и другие tools; `tools/graphics/flux_image.py` — fal.ai API, требует `FAL_KEY`. Нельзя просто включить `image_selector` в auto mode.

**Решение:** custom workflow/worker для FLUX.1 Schnell; вызывать явно; cloud fallback заблокировать.

### AI-видео
В репозитории есть `comfyui_video.py` и другие video-generation providers. В этой фабрике они запрещены. Pipeline manifest и runtime policy должны запрещать capability `video_generation`, `text_to_video`, `image_to_video` и все соответствующие tools. Разрешена только генерация still images.

### Kaggle T4
В актуальной документации Kaggle CLI accelerator `NvidiaTeslaT4` обозначает T4 ×2. Worker обязан определить device count и VRAM через PyTorch. Не считать, что два GPU автоматически образуют единый memory pool.

FLUX.1 Schnell — 12B-параметрическая модель с Apache-2.0 license и 1–4 inference steps. Это не гарантирует, что full weights + encoders поместятся в 16 GB VRAM без quantization/offload. Нужен benchmark на фактическом Kaggle runtime. OOM → fail + diagnostics, не paid endpoint.

## 1.8 Видео: главы и resume

Частично пригодные contracts:
- `schemas/artifacts/script.schema.json`: `sections[]`, `start_seconds`, `end_seconds`, `voice_performance`;
- `schemas/artifacts/scene_plan.schema.json`: `scenes[]`, timestamps, `script_section_id`;
- `tools/publishers/export_bundle.py`: `chapters` в export metadata / description;
- `skills/creative/long-form.md`: long-form editorial guidance, но это instructions, не scheduler.

`lib/checkpoint.py` сохраняет stage-level state (`checkpoint_<stage>.json`), а не независимые chapter jobs с per-chapter retries, hash invalidation и resume. Partial progress metadata не заменяет chapter scheduler.

**Нужно создать chapter task layer.** Для 20–40 минут использовать главы по 2–4 минуты как starting point (ориентировочно 6–14 глав; число определяется сценарием).

## 1.9 QA: фактическое состояние

| Проверка | Состояние сейчас | Что добавить |
|---|---|---|
| `ffprobe` metadata/duration/streams | Есть в `audio_probe.py`, `video_stitch.py`, `video_compose.py` | Strict expected values |
| Full decode каждого clip | Нет единого обязательного shot gate | `ffmpeg -f null -` |
| `blackdetect` | Полного обязательного shot check не найдено | Реализовать parser + blocking policy |
| `freezedetect` | Полного обязательного shot check не найдено | Реализовать parser + low-motion policy |
| Audio stream | Проверяется местами | Недостаточно: возможна цифровая тишина |
| `volumedetect`, `ebur128`, `loudnorm` | Есть отдельные инструменты | Объединить в blocking gate |
| Narration/visual coverage | Есть вспомогательные анализаторы | Chapter beat coverage check |
| Manual review frames | `visual_qa.py` умеет извлекать кадры | Использовать для выборочного review |
| Single release gate | Нет полного user-required gate | Добавить QA aggregator |

`video_compose.py` содержит ffprobe и post-render audio spotcheck, но issue #937 описывает воспроизводимый случай: valid MP4 + AAC stream + `success: true`, но digital silence (примерно `-91 dB`). `edit_decisions.audio.music` не проходит полноценное разрешение/staging в render path. Issue #575 ранее описывал аналогичные проблемы с music, `grade_profile` и schema конфликтом. **Нельзя принимать `video_compose.success` за release decision.**

## 1.10 Зависимости, package files, CI

Проверены: `requirements.txt`, `requirements-dev.txt`, `requirements-gpu.txt`, `setup.py`, `Makefile`, `config.yaml`, `.env.example`, `remotion-composer/package.json`, `package-lock.json`, `.github/workflows/ci.yml`.

Основные зависимости root `requirements.txt`: PyYAML, Pydantic 2, jsonschema, python-dotenv, Pillow, NumPy, requests, certifi, google-auth, google-genai, openai, FastAPI, Uvicorn, watchfiles, websockets, pythainlp. `requirements-dev.txt`: pytest, pytest-asyncio, httpx. `requirements-gpu.txt`: torch, torchaudio, torchvision. `setup.py` требует Python >=3.10; CI использует Python 3.11. Root `pyproject.toml` не найден.

Node package присутствует в `remotion-composer/package.json`; engines: `^22.23.4 || ^24.22.1 || ^26.12.1`, Remotion packages — `^4.0.484`.

Наличие `openai`/`google-genai` в requirements не означает, что их надо использовать. Не удалять SDK массово до проверки lazy imports и полного regression suite; для новой фабрики создать отдельный local dependency group и не включать cloud providers в allowlist.

CI на checked main commit: Python 3.11, ffmpeg, `make install-dev`, `make lint`, `make test`. Последний завершённый `Validate Python` check на этом commit был green. Но `tests/qa/test_08_end_to_end.py` — synthetic 60-second animated-explainer fixture, не реальная 20–40-минутная documentary integration с Kokoro, local library и FLUX worker.

## 1.11 Issues и Discussions

| Issue | Реальная проблема | Значение для фабрики |
|---|---|---|
| [#937](https://github.com/OpenMontageInc/OpenMontage/issues/937) | Music block не применяется; рендер может быть формально успешным, но silent | Explicit audio mux + RMS/LUFS gate |
| [#575](https://github.com/OpenMontageInc/OpenMontage/issues/575) | Music не смешивается, grade profile игнорируется, schema/instructions conflict | Не полагаться на documentary-montage spec как на гарантированную реализацию |
| [#723](https://github.com/OpenMontageInc/OpenMontage/issues/723) | `CostTracker` есть, но production code его не запускает | Не считать budget config runtime safety mechanism |
| [#722](https://github.com/OpenMontageInc/OpenMontage/issues/722) | Test network guard может обходиться через `ssl.SSLSocket.connect` / `requests` | Исправить guard; добавить no-cloud policy tests |
| [#596](https://github.com/OpenMontageInc/OpenMontage/issues/596) | Некоторые source adapters используют process-seeded `hash(url)` для IDs | Asset IDs — SHA-256 |
| [#511](https://github.com/OpenMontageInc/OpenMontage/issues/511) | Transport errors некоторых adapters проглатываются как пустая выдача | `NO_MATCH` != `SOURCE_ERROR` |
| [#888](https://github.com/OpenMontageInc/OpenMontage/issues/888) | Piper binary не обнаруживается без venv в PATH | Указывать executable/model paths явно |
| [#855](https://github.com/OpenMontageInc/OpenMontage/issues/855) | Slow-motion в Remotion может давать black tail | Shot black/freeze QA |
| [#222](https://github.com/OpenMontageInc/OpenMontage/issues/222) | Нет полноценного blocking semantic A/V alignment gate | Beat/shot/narration coverage |
| [#864](https://github.com/OpenMontageInc/OpenMontage/issues/864) | Possible bypass static safety scan в `math_animate.py` | Не исполнять generated scene code без sandbox |

Discussions:
- [#892 OpenMontage Studio: Inviting Early users](https://github.com/OpenMontageInc/OpenMontage/discussions/892): автор описывает Studio с локальными ComfyUI моделями, но для внешних сервисов нужны собственные API/subscription keys; обсуждение говорит о Windows-only early access. Это не готовая Codespaces workflow интеграция.
- [#231 OpenMontage now supports ComfyUI](https://github.com/calesthio/OpenMontage/discussions/231): подтверждает локальные ComfyUI workflows; реализацию подтверждали `comfyui_image.py` и `_comfyui/client.py`.
- В Discussions вопрос `openmontage in docker?` и `Can I use OpenMontage on Vast.ai?` были unanswered на момент проверки. Не считать такие deployment paths готовыми.

---

# 2. Юридический разбор AGPL-3.0 и рекомендация

## 2.1 Точная лицензия

Файл `LICENSE` начинается с:

```text
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
```

Это **GNU Affero General Public License, Version 3 (AGPL-3.0)**, не обычная GPL-3.0 и не старая Affero GPL v1.

- §2: разрешено запускать и изменять private copies; само выполнение программы не равно передаче её копии.
- §§4–6: условия при convey/distribution covered software, включая copyright/license notices и Corresponding Source.
- §13: если вы модифицировали программу и она поддерживает удалённое взаимодействие пользователей по сети, modified version должна заметно предлагать всем таким remote users бесплатно получить Corresponding Source через обычный сетевой способ.
- §14: варианты будущих версий зависят от конкретного license notice; проверенный текст — AGPL Version 3, GitHub classifier — AGPL-3.0. Не считать это blanket permission для всех будущих лицензий.

§13 не говорит «опубликовать всему миру независимо от того, кто пользуется сервисом». Требование адресовано пользователям, взаимодействующим с modified program remotely. Но если сервис публичный, source offer должен быть доступен всем его remote users.

## 2.2 Сценарии

| Сценарий | Что означает AGPL |
|---|---|
| Локальная разработка/личное использование, копия не передаётся | Можно модифицировать и использовать privately. Нет автоматической обязанности публиковать исходники всему Интернету. Если modified app поддерживает network interaction, §13 требует source offer remote users. |
| Внутренний self-hosted сервис одной организации | Внутренние копии сами по себе не означают передачу другим организациям. FSF FAQ подтверждает private modifications/internal use без публикации наружу. Но безопасно предоставить Corresponding Source сотрудникам/операторам, которые удалённо используют modified network app. |
| Установка modified OpenMontage на сервер заказчика и передача программы | Это convey covered work. Соблюдать §§4–6: notices, текст лицензии, Corresponding Source соответствующей версии. Коммерческая плата за установку/поддержку допустима. |
| SaaS/web UI/API для клиентов на modified OpenMontage | §13 требует заметно предложить бесплатный Corresponding Source всем пользователям, удалённо взаимодействующим с этой modified version. Можно брать деньги за сервис/поддержку, но нельзя закрыть от remote users исходники covered modified program. |
| Клиент получает только конечный MP4 и не получает UI/API/удалённый доступ | Сам видеоролик обычно является output, а не передаваемой копией программы. §2 говорит, что output покрывается лицензией только если его содержание само является covered work. Права на footage/music/images учитывать отдельно. |
| Закрытое приложение общается с OpenMontage через API/файлы | Разделение процессов/контейнеров/репозиториев или HTTP API само по себе не является гарантированным исключением. Если plugin фактически модифицирует, связывает или образует combined/derivative work, нужен анализ по конкретной архитектуре и copyright law. |

Это техническая оценка для планирования, не юридическое заключение. До передачи modified software клиенту или запуска SaaS нужен review юриста по software licensing.

## 2.3 Рекомендация для freelance

### Вариант A — AGPL-compliant fork (основная ветка этого плана)

1. Создать fork; изменения, являющиеся частью OpenMontage/производного проекта, держать под AGPL-3.0.
2. Не встраивать в fork proprietary client code, для которого необходимо закрыть исходный код.
3. Продавать производство видео, исследование, сценарии, монтаж и конечные MP4 — AGPL не запрещает коммерческие услуги.
4. Если заказчик получает копию modified factory/app, передать AGPL notices и Corresponding Source.
5. Если заказчик/клиенты удалённо пользуются modified web/API, сделать заметный пункт `Source code` с бесплатным доступом к соответствующей версии.
6. Хранить upstream commit, список изменений, версии зависимостей, лицензии моделей и media provenance.

### Вариант B — требуется закрытый исходный код

Не пытаться «обойти AGPL» выносом файлов в plugin repo. Сделать clean-room отдельную фабрику, которая не импортирует OpenMontage modules, не наследуется от `BaseTool`, не копирует исходники или существенно охраняемые skills, использует публичные protocol/data contracts и независимо лицензированные библиотеки. Либо получить commercial license/relicense от правообладателя. Это не автоматический safe harbor: независимость проекта оценивается по фактам.

**Основная ветка исполнения здесь — A: AGPL-compliant fork.** Coding-agent сохраняет license notices и не добавляет закрытые proprietary modules в AGPL tree.

## 2.4 Лицензии других компонентов

| Компонент | Лицензия/условие | Что делать |
|---|---|---|
| FLUX.1 Schnell weights | Apache-2.0 | Сохранить notices/conditions; commercial use допускается |
| `kokoro-onnx` runtime | MIT | Сохранить MIT notice |
| Kokoro-82M weights | Apache-2.0 | Сохранить model attribution/notices |
| Remotion | Отдельная лицензия/terms, не OSI open source | Current pricing page: Free License для individuals и компаний до 3 человек с commercial/automation use при соблюдении условий; для остальных Company License; Automators pricing — `$0.01/render`, `$100/mo minimum`. Для первой фабрики предпочесть FFmpeg. |
| Local footage/music | Индивидуальная лицензия каждого asset | Rights/creator/source/evidence обязательны; локальное хранение не означает clearance |

---

# 3. Целевая архитектура Documentary Factory

## 3.1 Схема

```text
GitHub Codespaces
  ├── Factory CLI / deterministic orchestrator
  ├── Local LLM client ───── authenticated private Ollama endpoint
  ├── Chapter/task state ─── JSON/SQLite + atomic files
  ├── Local footage scanner ─ persistent media library
  ├── CLIP/tag retrieval ─── local index
  ├── Kokoro TTS ─────────── local CPU
  ├── FFmpeg renderer ────── CPU
  ├── Shot/chapter QA ────── ffprobe + FFmpeg filters
  └── Export bundle

Kaggle GPU worker (on demand)
  ├── input: chapter/shot image requests + model/workflow metadata
  ├── FLUX.1 Schnell local inference (no provider API)
  ├── output: image files + result manifest + SHA-256
  └── result pulled to Codespaces by Kaggle CLI

FORBIDDEN: cloud LLM, cloud TTS, fal.ai/Replicate/OpenAI image API,
           AI-video/text-to-video/image-to-video providers.
```

## 3.2 Workflow

1. Research/source registry — claims, source URLs, references.
2. Outline — narrative arc, hook, chapters, re-hooks.
3. Script — narration sections, timing, claim/source refs.
4. Chapter plan — independent manifest per chapter.
5. Local asset retrieval — search local library first.
6. FLUX still fallback — only for approved slots with no suitable footage.
7. Narration — Kokoro chunks by paragraph/phrase, not one monolithic 40-minute WAV.
8. Shot render — normalize footage/images to chapter timeline.
9. Chapter audio mix — narration + approved local music/ambience; signal checks.
10. Chapter QA — 100% of shots and chapter outputs.
11. Final assembly — combine passed chapters, verify continuity.
12. Final QA + export — only after all gates pass.

## 3.3 Новые файлы и модули

```text
pipeline_defs/
  documentary-longform.yaml                 # NEW

skills/pipelines/documentary-longform/
  executive-producer.md                     # NEW
  research-director.md                      # NEW
  outline-director.md                       # NEW
  script-director.md                        # NEW
  chapter-planner.md                        # NEW
  asset-director.md                          # NEW
  narration-director.md                      # NEW
  edit-director.md                           # NEW
  qa-director.md                             # NEW
  export-director.md                         # NEW

schemas/artifacts/
  chapter_plan.schema.json                  # NEW
  chapter_job.schema.json                   # NEW
  shot_manifest.schema.json                 # NEW
  qa_report.schema.json                     # NEW

factory/
  __init__.py
  config.py                                  # NEW: Pydantic settings
  models.py                                  # NEW: typed contracts
  policy.py                                  # NEW: provider allow/deny lists
  runner.py                                  # NEW: workflow CLI orchestration
  project.py                                 # NEW: project init/layout
  state.py                                   # NEW: state persistence
  chapters.py                                # NEW: chapter scheduler
  retry.py                                   # NEW: retry classification/backoff
  hashing.py                                 # NEW: SHA-256/idempotency
  llm/ollama_client.py                       # NEW
  llm/json_contract.py                       # NEW
  llm/prompts/{research,outline,script,chapter_plan,shot_plan}.md
  media/local_library.py                     # NEW: filesystem scanner
  media/metadata.py                          # NEW: rights/tags schema
  media/ingest.py                            # NEW: probe/thumb/CLIP index
  media/retrieval.py                         # NEW: local-first scoring
  media/provenance.py                        # NEW: asset checksums
  voice/kokoro.py                            # NEW: explicit Kokoro local
  voice/chunking.py                          # NEW
  voice/timing.py                            # NEW: local word timing
  gpu/kaggle_client.py                       # NEW
  gpu/flux_jobs.py                           # NEW
  render/shot_renderer.py                    # NEW
  render/chapter_renderer.py                 # NEW
  render/audio_mix.py                        # NEW
  render/final_assembler.py                  # NEW
  qa/probe.py                                # NEW
  qa/decode.py                               # NEW
  qa/black_freeze.py                         # NEW
  qa/audio.py                                # NEW
  qa/coverage.py                             # NEW
  qa/shot_qa.py                              # NEW
  qa/chapter_qa.py                            # NEW
  qa/final_qa.py                             # NEW
  qa/sampling.py                             # NEW
  export/youtube_bundle.py                   # NEW

scripts/
  factory_init.py                            # NEW
  factory_run.py                             # NEW
  chapter_run.py                             # NEW
  library_scan.py                            # NEW
  qa_project.py                              # NEW
  kaggle_flux_submit.py                      # NEW

kaggle/flux_schnell_worker/
  kernel-metadata.json                       # NEW
  worker.py                                  # NEW
  job.json.example                           # NEW
  workflow_flux1_schnell.json                # NEW if ComfyUI workflow selected
  requirements.txt                           # NEW, minimal/pinned

tests/factory/
  test_policy_no_cloud.py                    # NEW
  test_ollama_client.py                      # NEW
  test_local_library.py                      # NEW
  test_asset_provenance.py                   # NEW
  test_kokoro_tts.py                          # NEW
  test_chapter_resume.py                      # NEW
  test_retry_idempotency.py                   # NEW
  test_flux_job_contract.py                   # NEW
  test_shot_qa.py                             # NEW
  test_chapter_qa.py                          # NEW
  test_final_qa.py                            # NEW
  test_end_to_end_fixture.py                  # NEW
```

### Модификации существующих файлов

- `.env.example`: добавить local settings, paid keys оставить пустыми и пометить forbidden.
- `.gitignore`: media/model weights/Kaggle I/O/renders/secrets.
- `Makefile`: `factory-setup`, `factory-test`, `factory-smoke`, `factory-qa`.
- `requirements-factory.txt`: только дополнительные local dependencies.
- `pipeline_defs/`: новая manifest; старый documentary-montage не менять.
- `tools/audio/`: optional Kokoro `BaseTool`, только если требуется integration; не использовать auto `tts_selector`.
- `tools/video/stock_sources/`: optional local adapter; иначе scanner остаётся в `factory/media`.
- `schemas/`: новые contracts отдельно, не ломать существующие schemas.

---

# 4. Конфигурация провайдеров

## 4.1 Новые environment variables

```dotenv
# Factory
FACTORY_MODE=production
FACTORY_ALLOW_CLOUD=false
FACTORY_ALLOW_AI_VIDEO=false
FACTORY_OUTPUT_ROOT=projects
FACTORY_FPS=30
FACTORY_WIDTH=1920
FACTORY_HEIGHT=1080
FACTORY_CHAPTER_TARGET_MINUTES=3.5

# Local LLM (must be reachable from Codespaces)
LOCAL_LLM_PROVIDER=ollama
LOCAL_LLM_BASE_URL=http://127.0.0.1:11434
LOCAL_LLM_MODEL=<locally-installed-model>
LOCAL_LLM_TIMEOUT_SECONDS=240
LOCAL_LLM_API_KEY=

# Local footage
LOCAL_LIBRARY_ROOT=/workspaces/media-library
LOCAL_LIBRARY_INDEX=projects/_library/index
LOCAL_LIBRARY_REQUIRE_LICENSE_METADATA=true

# Kokoro
KOKORO_MODEL_PATH=/models/kokoro-v1.0.onnx
KOKORO_VOICES_PATH=/models/voices-v1.0.bin
KOKORO_VOICE=af_heart
KOKORO_LANGUAGE=en-US
KOKORO_SAMPLE_RATE=24000

# FLUX worker
FLUX_MODEL_ID=black-forest-labs/FLUX.1-schnell
FLUX_WORKER=kaggle
FLUX_MAX_STEPS=4
FLUX_MAX_IMAGES_PER_CHAPTER=3
FLUX_ALLOW_API_FALLBACK=false
KAGGLE_KERNEL_REF=<account/kernel-slug>
```

`LOCAL_LLM_BASE_URL=http://127.0.0.1:11434` корректен только если Ollama запущен в том же Codespace/container. `localhost` в Codespaces не означает Android/локальный PC пользователя. Если Ollama работает на другом устройстве, подключить его через private network/tunnel с authentication; **не публиковать порт 11434 напрямую в Интернет**. Без защищённого соединения preflight должен завершиться ошибкой.

## 4.2 Provider allowlist

В `factory/policy.py` ввести:

```python
ALLOWED_PROVIDERS = {
    "llm": {"ollama_local"},
    "tts": {"kokoro_local"},
    "footage": {"local_library"},
    "image": {"kaggle_flux_schnell"},
    "render": {"ffmpeg_local"},
    "publish": {"local_export"},
}

DENIED_CAPABILITIES = {
    "video_generation",
    "text_to_video",
    "image_to_video",
}
```

Имена могут быть внутренними, но однозначно означают local runtime. В production policy обязана отклонять неизвестный provider; `ToolRuntime.API`; video generation; `flux_image`/`openai_image`/Replicate; auto fallback. Проверять policy до run и перед каждым execution. Наличие cloud API key не должно менять provider selection.

## 4.3 Что не вызывать

- `tools/audio/elevenlabs_tts.py`, `azure_tts.py`, `google_tts.py`, `openai_tts.py`, `heygen_tts.py`;
- `tools/graphics/flux_image.py` (fal.ai), `openai_image.py`;
- `image_selector` и `video_selector` в auto mode;
- `tools/video/comfyui_video.py` и остальные video-generation providers;
- cloud `music_gen` routes.

SDK можно оставить в root deps, чтобы не ломать другие pipelines, но production factory должна запретить execution. Тесты с dummy paid keys доказывают, что paid requests не происходят.

---

# 5. Data contracts и chapter-level resume

## 5.1 Chapter plan

`chapter_plan.schema.json` должен описывать:
- `project_id`, `version`, `language`, `target_duration_seconds`;
- ordered chapters с `chapter_id` stable slug/UUID;
- `title`, `purpose`, `narrative_question`, `hook`, `re_hook`, `summary`;
- `start_seconds`, `end_seconds`, target duration;
- `script_sections[]`: `section_id`, text, narration cues, source references;
- `shots[]`: `shot_id`, `script_section_id`, visual intent, keywords/tags, desired duration, `visual_type`, `allow_still_fallback`, selected asset ref;
- `narration_chunks[]`, expected audio duration, `qa_policy`.

`visual_type` ограничить `local_footage | generated_still | title_card | diagram`. Не добавлять `generated_video`.

## 5.2 Chapter state machine

```text
projects/<project_id>/
  project.json
  research/
  script/
  chapters/
    <chapter_id>/
      chapter.json
      state.json
      inputs/
      assets/
      narration/
      shots/
      render/
      qa/
      logs/
  final/
  exports/
```

Статусы:

```text
PENDING → PLANNED → ASSETS_READY → NARRATION_READY
        → SHOTS_RENDERED → CHAPTER_RENDERED → QA_PASSED → FINALIZED
```

`FAILED` хранит failed stage, normalized error type, attempts и retryability.

Для каждого этапа сохранять input/output hashes; писать outputs атомарно (`.tmp` → `os.replace`); retry только transient errors; не retry-ить invalid schema, missing rights metadata, policy violations, unsupported voice language, permanent auth/4xx errors. При изменении script/shot hash инвалидировать downstream только этой главы. Kaggle timeout должен приводить к status check/download existing outputs, а не слепому повторному submit.

Пример `state.json`:

```json
{
  "project_id": "sample-doc",
  "chapter_id": "ch-04",
  "status": "NARRATION_READY",
  "current_stage": "assets",
  "attempts": {"assets": 1, "narration": 1, "render": 0, "qa": 0},
  "input_hashes": {"script": "<sha256>", "chapter_plan": "<sha256>"},
  "outputs": {"narration": {"path": "narration/ch-04.wav", "sha256": "<sha256>"}},
  "last_error": null,
  "updated_at": "ISO-8601"
}
```

`current_stage` в этом примере — следующий этап к выполнению; задокументировать это в schema.

## 5.3 Metadata локальной библиотеки

Пример sidecar metadata:

```json
{
  "asset_id": "sha256:<content-hash>",
  "path": "nature/forests/forest_rain_001.mp4",
  "media_type": "video",
  "duration_seconds": 18.42,
  "width": 3840,
  "height": 2160,
  "fps": 25.0,
  "tags": {
    "subject": ["forest", "rain"],
    "objects": ["trees", "leaves"],
    "actions": ["wind", "falling rain"],
    "mood": ["calm", "mysterious"],
    "era": ["modern"],
    "location": ["unknown"]
  },
  "description": "Rain falling through dense green forest canopy",
  "creator": "creator name",
  "source_url": "https://...",
  "license": "license identifier / URL",
  "commercial_use": "allowed | restricted | unknown",
  "attribution_required": true,
  "rights_evidence": "path or URL",
  "sha256": "<hex>",
  "indexed_at": "ISO-8601"
}
```

При `LOCAL_LIBRARY_REQUIRE_LICENSE_METADATA=true` неизвестные права блокируют commercial export или требуют manual approval. Не назначать `commercial_use=allowed` автоматически.

Scanner должен рекурсивно находить форматы, probe-ить через ffprobe, считать SHA-256, дедуплицировать, создавать thumbnails/contact sheets, читать sidecars, строить CLIP/tag index, сохранять provenance, не загружать медиа в Git. Различать `NO_MATCH`, `UNREADABLE_FILE`, `SOURCE_PERMISSION_ERROR`, `INDEX_ERROR`.

---

# 6. LLM, narration и image fallback

## 6.1 Local Ollama

Создать `factory/llm/ollama_client.py`:
- использовать только `LOCAL_LLM_BASE_URL` из allowlisted config;
- поддержать Ollama API или OpenAI-compatible endpoint, но только локальный URL;
- явно задавать model;
- JSON/structured output валидировать Pydantic + JSON Schema;
- timeout/retry только на timeout/5xx;
- логировать model, prompt version, input/response hashes и token stats, если доступны;
- никакого cloud fallback;
- не выбирать провайдера по наличию `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`.

Unit tests — mocked HTTP; integration smoke — реально доступный local Ollama.

## 6.2 Kokoro

Создать `factory/voice/kokoro.py`:
- `kokoro-onnx` + `soundfile`;
- explicit model path и voices file;
- voice строго `af_heart`, language `en-US`, пока не подтверждена другая пара;
- WAV output per chapter/chunk;
- chunking по абзацам/предложениям, не разрезать слова;
- mapping `section_id → chunk_id → WAV → duration → transcript/timestamps`;
- проверить sample rate, channels, duration, RMS;
- сохранять runtime/model/voice в manifest;
- не использовать `tts_selector` auto mode и cloud fallback.

Word timings: локальный Whisper/faster-whisper или local aligner. Не считать равномерно распределённые timestamps точными. Если точной синхронизации нет, сохранять `timing_source` и не использовать такой файл как точный word alignment.

**Language gate:** если script language не `en-US`, а voice `af_heart`, остановить synthesis и запросить корректную конфигурацию. Не маркировать русский voiceover с English voice id как supported.

## 6.3 Local footage first, FLUX second

Для каждого shot:
1. Query local library по tags, captions, CLIP embedding.
2. Rank по semantic match, aspect ratio, resolution, duration, diversity и rights status.
3. Reject unknown/forbidden rights, unreadable files, wrong-topic clips.
4. Сохранить выбранный asset, score и rejected candidates/reasons.
5. Если score не проходит threshold и `allow_still_fallback=true`, создать FLUX image job.
6. Ошибка FLUX/Kaggle → stop shot/chapter и запросить решение человека. Без random stock/cloud fallback.
7. Generated still анимировать через FFmpeg pan/zoom; записать provenance/seed/model.

Тесты обязаны доказать: хороший local match → `flux_job_count=0`; нет match и fallback off → explicit failure; fallback on → только локальный Kaggle job; никогда не вызывается `flux_image` (fal.ai).

## 6.4 Kaggle FLUX worker

Создать `kaggle/flux_schnell_worker/`.

Protocol:
1. Codespaces пишет `job.json`: `job_id`, `shot_id`, prompt, negative prompt, dimensions, seed, steps, model id, output paths.
2. Submit: `kaggle kernels push -p kaggle/flux_schnell_worker --accelerator NvidiaTeslaT4 --timeout <seconds>`.
3. Worker логирует GPU name/count/VRAM, torch/CUDA version.
4. Worker запускает FLUX.1 Schnell local inference; разрешён download весов из официального model repository, запрещены inference APIs.
5. Smoke сначала 512×512, затем 1024×1024; измерить peak VRAM/runtime; не включать batch по умолчанию.
6. `result_manifest.json`: job/shot id, model, workflow, seed, steps, dimensions, runtime, output hashes, success/failure, error/VRAM stats.
7. Codespaces проверяет status и получает output через `kaggle kernels output <owner/kernel-slug> -p <output_dir>`.
8. Validate ids, model, file exists, dimensions, checksum, corruption.

Не публиковать ComfyUI `8188` в открытый интернет. Лучше запускать worker целиком внутри Kaggle kernel и передавать файлы через Kaggle CLI. Если full FLUX weights не помещаются в T4, протестировать quantization/offload/custom ComfyUI workflow; fail closed при OOM, не переходить на paid endpoint.

---

# 7. Рендер и сборка

## 7.1 FFmpeg-first

Для первой версии использовать **FFmpeg-first**, без Remotion как обязательного renderer. Это сокращает Node/Chromium failure points, избегает Remotion Automators/Company license вопросов и подходит для B-roll, pan/zoom stills, titles, narration/music mix и chapter resume.

`video_compose.py` можно использовать только после regression test music/audio resolution. Его `success=true` недостаточно.

## 7.2 Shot normalization

Для каждого shot:
- normalize canvas to 1920×1080, 30 fps, `yuv420p`;
- fit/crop сохранять в manifest как явную policy;
- consistent codec/profile/pixel format;
- still image превратить в animated pan/zoom shot;
- source audio выключить, если он не approved ambience;
- сохранить `chapters/<id>/shots/<shot_id>.mp4`.

Пример фильтра (порядок проверить на fixtures):

```bash
ffmpeg -hide_banner -y -i input.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p" \
  -an -c:v libx264 -preset medium -crf 18 \
  -movflags +faststart output_shot.mp4
```

Не применять безусловно к portrait/low-res footage; реализовать `fit`, `fill`, `blurred_background` modes.

## 7.3 Chapter assembly

- Сначала собрать video-only shots, нормализованные под единый codec/dimensions/fps.
- Потом добавить narration и approved local music/ambience отдельным explicit audio-mix step.
- Не добавлять `anullsrc` в качестве замены отсутствующей обязательной narration/music.
- Для concat demuxer использовать FFmpeg concat manifest; проверять exit code/stderr.
- Сохранять `shot_id → timeline interval` mapping.
- Chapter MP4 проходит ffprobe/full decode/black/freeze/audio QA до `QA_PASSED`.

`audio_mixer.py` допускается после проверки, что все expected tracks попали во входы и output не silent.

## 7.4 Final assembly

Собирать только chapters со статусом `QA_PASSED`. Проверить порядок, отсутствующие/повторные главы, gaps/overlaps, narration continuity, crossfades, duration 1200–2400 seconds, full decode и YouTube chapter timestamps.

---

# 8. Автоматический QA

QA запускается для **100% shots**, всех chapter renders и final export. Команды запускать через `subprocess.run(..., check=False, capture_output=True, timeout=...)`, сохранять stdout/stderr/return code. Timeout — ошибка, не PASS.

## 8.1 ffprobe для каждого shot

```bash
ffprobe -v error -show_format -show_streams -of json input.mp4
```

Проверять: файл существует/размер > 0; video stream; width/height; fps; codec; pixel format; валидная duration в tolerance; frame count в ±1–2 frames; format/stream duration не расходятся; audio stream присутствует только когда ожидается manifest.

Для original footage проверять исходные ожидаемые характеристики, а не требовать 1080p до normalisation.

## 8.2 Full decode

```bash
ffmpeg -v error -i input.mp4 -map 0:v:0 -f null -
ffmpeg -v error -i input.mp4 -map 0:a:0 -f null -
```

Вторую команду запускать для outputs с ожидаемым audio. Non-zero exit, decode errors, premature EOF — FAIL.

## 8.3 Black frames

```bash
ffmpeg -hide_banner -i input.mp4 \
  -vf "blackdetect=d=0.30:pix_th=0.10" -an -f null -
```

Парсер сохраняет `black_start`, `black_end`, `black_duration`. Неожиданный black interval дольше порога — FAIL. Planned fade/black card задаётся в edit manifest точным временем. Чёрный участок в середине без разрешённого интервала — FAIL. Night footage не получает глобальное исключение.

## 8.4 Freeze

```bash
ffmpeg -hide_banner -i input.mp4 \
  -vf "freezedetect=n=-50dB:d=1.0" -an -f null -
```

Сохранять `freeze_start/end/duration`. Freeze >1 sec в dynamic footage — FAIL/REVIEW согласно policy. Для intentional low-motion указать `allow_low_motion=true` на конкретном shot. Для generated still применять pan/zoom. Не ослаблять threshold глобально ради одного кадра.

## 8.5 Audio QA

```bash
ffmpeg -hide_banner -i chapter.mp4 -map 0:a:0 -af volumedetect -f null -
ffmpeg -hide_banner -i chapter.mp4 -map 0:a:0 -af ebur128=peak=true -f null -
```

Использовать `volumedetect`, `astats`/RMS и `ebur128`; дополнительно проверить silence intervals и full audio decode. Ориентир финального YouTube mix — около `-14 LUFS integrated`, true peak <= `-1 dBTP`; параметры сделать configurable и проверить на тестовой главе.

Mandatory:
- expected narration → audible signal во всех expected intervals;
- music declared present → signal above configured floor, кроме intentional silence;
- digital silence (например mean около `-90 dB`) → FAIL даже при AAC stream;
- missing expected audio stream → FAIL;
- clipping/true-peak violation → FAIL;
- narration/chapter duration mismatch за tolerance → FAIL.

Не нормализовать цифровую тишину так, чтобы она выглядела исправной.

## 8.6 Narration & semantic timing

Проверять WAV duration, sample rate, finite samples, RMS. Каждому `section_id` соответствует chunk и timeline; каждый narration beat должен быть покрыт одним или несколькими visual shots. Timeline holes — FAIL. При изменении script/voice/rate инвалидировать старые timing outputs. LLM semantic review — advisory; deterministic interval coverage — blocking.

## 8.7 Chapter/final gate

Chapter PASS только если все shots присутствуют и прошли ffprobe/decode/black/freeze/audio policy; narration coverage 100%; chapter output прошёл probe/decode; audio mix не silent; asset rights/provenance валидны; `qa_report.json` schema-valid.

Final PASS только если все главы `QA_PASSED`; нет unresolved shots; final duration 1200–2400 sec; final decode/audio проходит; chapter timestamps valid; manual review sample создан.

## 8.8 Выборочная визуальная проверка

Собирать review sheet автоматически:
- первый и последний shot каждой главы;
- 1–2 кадра каждой главы;
- низкий CLIP match score;
- alerts black/freeze/audio;
- все generated stills;
- переходы глав;
- random supplement sample с фиксированным seed.

Ориентир 5–10% shots + все risk-flagged; минимум один contact sheet на главу. Сохранять `manual_review.json` с reviewer, timestamp, approved/rejected и notes.

---

# 9. План реализации: порядок и критерии

## Этап 0 — baseline и pin

**Действия:** feature branch; зафиксировать upstream SHA, Python/Node/FFmpeg versions; запустить `make lint`, `make test`; сохранить baseline logs; проверить clean working tree.

**Завершён, когда:** результаты baseline зафиксированы в `factory/research-baseline.md`; существующие pipelines не изменены.

## Этап 1 — provider security/no-cloud policy

**Действия:** `factory/policy.py`; allowlist/denylist; запрет auto fallback; tests с dummy cloud keys; review/исправление network guard из #722.

**Завершён, когда:** dummy paid keys не меняют provider; production допускает только local providers; video generation unavailable; unknown provider fails; no silent fallback tests PASS.

## Этап 2 — config/manifests/contracts

**Действия:** `factory/config.py`, `models.py`, 4 schemas, `documentary-longform.yaml`, stage skills, approval gates.

**Завершён, когда:** fixtures schema-valid; invalid IDs/timestamps/providers отклоняются; manifest фиксирует language/voice/rights/output profile; старый montage pipeline проходит без изменений.

## Этап 3 — local footage library

**Действия:** scanner, sidecar parser, `ffprobe`, SHA-256, thumbnails, CLIP/tag index, local-first retrieval, remote stock disabled.

**Завершён, когда:** тестовая папка 20–50 clips ingest-ится повторно без duplicates; ID стабилен между процессами; retrieval даёт объяснимый match score; неизвестные права блокируются; `NO_MATCH` отдельно от ingest/index errors.

## Этап 4 — local LLM

**Действия:** Ollama client; structured JSON; research/outline/script/chapter prompts; endpoint preflight; allowlisted private host.

**Завершён, когда:** local endpoint выдаёт valid JSON; malformed JSON/timeout/5xx тестируются; endpoint unavailable → stop; OpenAI/Anthropic/Gemini calls отсутствуют даже с dummy keys.

## Этап 5 — Kokoro narration

**Действия:** `kokoro-onnx`, `soundfile`, pinned models/checksums; chunking; WAV/durations/word timing; language gate.

**Завершён, когда:** 2–3 минут sample синтезируется локально после model cache; voice именно `af_heart`; WAV проходит probe/decode/RMS; chunks не теряют текст; cloud TTS недостижим; language mismatch fail.

## Этап 6 — chapter scheduler/resume

**Действия:** chapter state, retries, hashing, atomic writes, stale output invalidation, recovery after disconnect.

**Завершён, когда:** тест с 3 главами может остановиться после второй и возобновиться без пересборки первой; ошибка одного shot не сбрасывает другие главы; rerun `chapter_run --chapter-id ... --resume` не дублирует outputs; script edit invalidates только downstream затронутой главы; crash не портит state.

## Этап 7 — FLUX fallback

**Действия:** Kaggle worker/dispatcher; job/result manifests; ComfyUI custom workflow или Diffusers; official FLUX.1 Schnell; smoke 512 и 1024; VRAM/runtime benchmark.

**Завершён, когда:** worker без inference API генерирует still; manifest и hash проверены; подходящий local footage всегда предотвращает FLUX job; error не вызывает fal.ai/Replicate/OpenAI; video generation недоступна.

## Этап 8 — shot/chapter rendering

**Действия:** shot renderer, chapter renderer, explicit audio mixer, FFmpeg normalization/concat, timeline map.

**Завершён, когда:** 2–3 min chapter собран из footage + generated still + Kokoro narration; A/V sync в tolerance; output проходит probe/decode/black/freeze/audio gate; аудио слышимо; повторный render controlled deterministic.

## Этап 9 — full QA

**Действия:** probe/decode/black_freeze/audio/coverage/shot/chapter/final QA; positive/negative fixtures; contact sheets.

**Завершён, когда:** 100% shot IDs имеют QA record; black/freeze/silent AAC/missing stream/A-V mismatch fixtures блокируют export; positive fixture проходит; manual sample генерируется.

## Этап 10 — assemble/export/integration

**Действия:** final assembler + YouTube bundle; объединять только QA-passed chapters; CLI; staged integration: 1 chapter → 3 chapters → 20-minute sample → 40-minute capacity.

**Завершён, когда:** 20 min test project проходит QA/export; resume partial run подтверждён; export содержит MP4, subtitles (если включены), chapters, description, metadata, QA report; 40 min capacity test измерен; нет paid API и AI-video.

---

# 10. Предлагаемый pipeline manifest

Coding-agent обязан сверить skeleton с текущей `schemas/pipelines/pipeline_manifest.schema.json` и использовать только реальные допустимые keys. Это концептуальная последовательность, не утверждение, что все ключи уже поддерживаются:

```yaml
name: documentary-longform
version: "1.0"
description: "Narrated 20-40 minute documentary production using local footage first."
stability: beta
mode: chapter_factory
default_checkpoint_policy: guided
stages:
  - name: research
    produces: research_brief
  - name: outline
    produces: outline
  - name: script
    produces: script
  - name: chapter_plan
    produces: chapter_plan
  - name: assets
    produces: asset_manifest
  - name: narration
    produces: narration_manifest
  - name: chapter_render
    produces: chapter_render_manifest
  - name: qa
    produces: qa_report
  - name: export
    produces: export_manifest
```

Для каждой stage заполнить реальные manifest fields: `skill`, `tools_available`, `success_criteria`, `review_focus`, `human_approval_default`. Если текущая schema требует другие имена — адаптировать skeleton к schema, не ломать validator.

---

# 11. Целевой CLI contract

Это команды, которые агент должен реализовать; не считать их существующими до merge и smoke tests:

```bash
python scripts/factory_init.py --project-id example-doc --preflight
python scripts/library_scan.py --root "$LOCAL_LIBRARY_ROOT" --rebuild-index
python scripts/factory_run.py --project-id example-doc
python scripts/chapter_run.py --project-id example-doc --chapter-id ch-04 --resume
python scripts/factory_run.py --project-id example-doc --resume-failed
python scripts/qa_project.py --project-id example-doc --scope all
python scripts/factory_run.py --project-id example-doc --stage export
```

---

# 12. Риски первого запуска

| Риск | Почему реален | Предотвращение |
|---|---|---|
| Ollama недоступен из Codespaces | `localhost` Codespace — не телефон/ПК пользователя | Preflight URL; private authenticated tunnel или Ollama в том же runtime; не открывать порт публично |
| `af_heart` не подходит языку | Голос — American English; русский не указан в official voice list | Language gate + listening test |
| FLUX OOM на T4 | 12B model; memory зависит от encoders/precision/resolution | GPU inventory, 512→1024 smoke, quantization/offload; no cloud fallback |
| Kaggle timeout/quota | Kernel может завершиться до выгрузки outputs | Durable job manifest, status check, hash validation, one job at a time |
| ComfyUI выбирает не ту модель/provider | Built-in workflow FLUX.2; tool fallback включает fal.ai | Custom FLUX.1 Schnell workflow, direct route, policy block `flux_image` |
| Большая/нетегированная local library | Retrieval зависит от metadata/embeddings | Incremental scan, SHA-256 dedupe, sidecar schema, thumbnails/contact sheets |
| Нет прав на media assets | Local file не означает коммерческое разрешение | Rights metadata required; unknown = manual hold |
| Damaged source clips | Corruption может проявиться только при render | ffprobe + full decode при ingest, quarantine |
| Freeze detector флагирует intentional still | Документальные планы часто мало двигаются | Per-shot low-motion policy; не выключать global gate |
| Blackdetect флагирует night/fade | Dark image/fade может быть задумана | Declared intervals, thresholds, review flagged timestamps |
| AAC stream с цифровой тишиной | #937 уже воспроизводил такое поведение | RMS/EBUR128 + expected narration interval checks |
| `video_stitch` добавляет silent stream | `_ensure_audio_for_clips` может добавить `anullsrc` | Audio отдельно; проверять actual signal, не existence stream |
| Chapter state устаревает | Script/voice change invalidates timings/renders | SHA-256 dependency graph + targeted invalidation |
| Codespaces disk exhausted | 20–40 min media/cache/output | Media вне Git, retention policy, preflight disk estimate |
| Source adapter masks error as no match | #511 | Enum `NO_MATCH` vs `SOURCE_ERROR`; remote adapters off |
| AGPL exposure | Obligations depend on distribution/remote users | Decide compliance model before client access; preserve notices/source offer |
| Remotion terms | Not open-source, automation licensing | FFmpeg-first; if reintroduced, check eligibility/terms |
| Coding-agent overreach | Repo содержит unrelated tools и risky code paths | Scope to new pipeline/factory; allowlist; no arbitrary generated code execution |

---

# 13. Test strategy and release gate

## 13.1 Fast tests

```bash
python -m compileall -q factory scripts
python -m pytest tests/factory -q
make lint
```

## 13.2 Existing regression suite

```bash
make test
```

Run before and after each integration milestone; save logs.

## 13.3 Local integration tests

- Ollama: valid output, invalid JSON, timeout, unavailable endpoint.
- Kokoro: short text, multi-paragraph chunking, corrupt model path, wrong language, no cloud fallback.
- Library: video formats, corrupt file, absent tags, repeated file, changed content, same basename in different folders.
- Retrieval: match/no match, rights metadata allowed/restricted/unknown.
- Kaggle worker: success, OOM, timeout, missing output, mismatched job id, wrong hash, no inference API call.
- Renderer: landscape/portrait/low-res footage, still image, short shot, nonstandard fps, missing audio.
- QA: black, freeze, silent AAC, clipping, missing stream, corrupt last GOP, duration mismatch.
- Resume: process termination after assets, TTS, during render and QA; resume only one chapter.

## 13.4 Synthetic fixtures

Создать FFmpeg fixtures:
- clean moving video + expected audio;
- all-black video;
- frozen-frame video;
- silent AAC track;
- missing-audio video;
- truncated/corrupt video;
- mismatched fps/resolution clips;
- low-motion valid clip with explicit override.

Negative fixtures должны падать по ожидаемой причине; positive fixture — проходить. Проверять command logs и содержимое `qa_report.json`, не только return bool.

## 13.5 Release gate

- [ ] No paid provider reachable from production orchestration.
- [ ] No AI-video tools available to this pipeline.
- [ ] Local footage scan/retrieval verified.
- [ ] FLUX.1 Schnell smoke run on actual Kaggle accelerator; result hash verified.
- [ ] Kokoro voice/language pair passes listening test.
- [ ] Chapter resume verified with injected failure.
- [ ] 100% shot IDs have QA entries.
- [ ] Black/freeze/silence/truncated fixtures block export.
- [ ] 20-minute sample passes complete QA.
- [ ] 40-minute capacity test or measured capacity report exists.
- [ ] Export metadata contains correct YouTube chapters.
- [ ] AGPL compliance route documented for intended client access model.

---

# 14. Документация и исходники исследования

## 14.1 Upstream repository/core

- [Repository](https://github.com/OpenMontageInc/OpenMontage)
- [Pinned main tree](https://github.com/OpenMontageInc/OpenMontage/tree/2e003e65fa99a0f329478a2c1cdcf26bc481933a)
- [LICENSE](https://github.com/OpenMontageInc/OpenMontage/blob/main/LICENSE)
- [README](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md)
- [AGENT_GUIDE](https://github.com/OpenMontageInc/OpenMontage/blob/main/AGENT_GUIDE.md)
- [Architecture](https://github.com/OpenMontageInc/OpenMontage/blob/main/docs/ARCHITECTURE.md)
- [Providers](https://github.com/OpenMontageInc/OpenMontage/blob/main/docs/PROVIDERS.md)
- [config.yaml](https://github.com/OpenMontageInc/OpenMontage/blob/main/config.yaml)
- [requirements.txt](https://github.com/OpenMontageInc/OpenMontage/blob/main/requirements.txt)
- [requirements-dev.txt](https://github.com/OpenMontageInc/OpenMontage/blob/main/requirements-dev.txt)
- [requirements-gpu.txt](https://github.com/OpenMontageInc/OpenMontage/blob/main/requirements-gpu.txt)
- [setup.py](https://github.com/OpenMontageInc/OpenMontage/blob/main/setup.py)
- [Makefile](https://github.com/OpenMontageInc/OpenMontage/blob/main/Makefile)
- [.env.example](https://github.com/OpenMontageInc/OpenMontage/blob/main/.env.example)
- [CI](https://github.com/OpenMontageInc/OpenMontage/blob/main/.github/workflows/ci.yml)

### Core source

- [`lib/pipeline_loader.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/lib/pipeline_loader.py)
- [`lib/config_model.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/lib/config_model.py)
- [`lib/checkpoint.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/lib/checkpoint.py)
- [`lib/corpus.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/lib/corpus.py)
- [`tools/base_tool.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/base_tool.py)
- [`tools/tool_registry.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/tool_registry.py)
- [`tools/provider_routing.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/provider_routing.py)
- [`tools/video/stock_sources/base.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/stock_sources/base.py)
- [`tools/video/stock_sources/__init__.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/stock_sources/__init__.py)
- [`tools/video/corpus_builder.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/corpus_builder.py)
- [`tools/video/direct_clip_search.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/direct_clip_search.py)
- [`tools/video/clip_search.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/clip_search.py)
- [`tools/video/video_compose.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/video_compose.py)
- [`tools/video/video_stitch.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/video/video_stitch.py)
- [`tools/graphics/comfyui_image.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/graphics/comfyui_image.py)
- [`tools/_comfyui/client.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/_comfyui/client.py)
- [`tools/graphics/flux_image.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/graphics/flux_image.py)
- [`tools/graphics/local_diffusion.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/graphics/local_diffusion.py)
- [`tools/audio/tts_selector.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/audio/tts_selector.py)
- [`tools/audio/piper_tts.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/audio/piper_tts.py)
- [`tools/audio/audio_mixer.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/audio/audio_mixer.py)
- [`tools/analysis/audio_probe.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/analysis/audio_probe.py)
- [`tools/analysis/audio_energy.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/analysis/audio_energy.py)
- [`tools/analysis/visual_qa.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/analysis/visual_qa.py)
- [`tools/analysis/composition_validator.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/analysis/composition_validator.py)
- [`tools/publishers/export_bundle.py`](https://github.com/OpenMontageInc/OpenMontage/blob/main/tools/publishers/export_bundle.py)
- [Remotion package.json](https://github.com/OpenMontageInc/OpenMontage/blob/main/remotion-composer/package.json)

### Pipeline, skills, schemas, tests

- [documentary-montage manifest](https://github.com/OpenMontageInc/OpenMontage/blob/main/pipeline_defs/documentary-montage.yaml)
- [executive producer](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/executive-producer.md)
- [idea director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/idea-director.md)
- [scene director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/scene-director.md)
- [asset director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/asset-director.md)
- [edit director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/edit-director.md)
- [compose director](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/pipelines/documentary-montage/compose-director.md)
- [long-form editorial guide](https://github.com/OpenMontageInc/OpenMontage/blob/main/skills/creative/long-form.md)
- [script schema](https://github.com/OpenMontageInc/OpenMontage/blob/main/schemas/artifacts/script.schema.json)
- [scene-plan schema](https://github.com/OpenMontageInc/OpenMontage/blob/main/schemas/artifacts/scene_plan.schema.json)
- [render-report schema](https://github.com/OpenMontageInc/OpenMontage/blob/main/schemas/artifacts/render_report.schema.json)
- [QA plan](https://github.com/OpenMontageInc/OpenMontage/blob/main/tests/qa/QA_PLAN.md)
- [E2E test 08](https://github.com/OpenMontageInc/OpenMontage/blob/main/tests/qa/test_08_end_to_end.py)
- [network guard conftest](https://github.com/OpenMontageInc/OpenMontage/blob/main/tests/conftest.py)
- [network guard tests](https://github.com/OpenMontageInc/OpenMontage/blob/main/tests/test_network_guard.py)

## 14.2 Issues and discussions

- [#937](https://github.com/OpenMontageInc/OpenMontage/issues/937)
- [#575](https://github.com/OpenMontageInc/OpenMontage/issues/575)
- [#723](https://github.com/OpenMontageInc/OpenMontage/issues/723)
- [#722](https://github.com/OpenMontageInc/OpenMontage/issues/722)
- [#596](https://github.com/OpenMontageInc/OpenMontage/issues/596)
- [#511](https://github.com/OpenMontageInc/OpenMontage/issues/511)
- [#888](https://github.com/OpenMontageInc/OpenMontage/issues/888)
- [#855](https://github.com/OpenMontageInc/OpenMontage/issues/855)
- [#222](https://github.com/OpenMontageInc/OpenMontage/issues/222)
- [#864](https://github.com/OpenMontageInc/OpenMontage/issues/864)
- [Discussion #892](https://github.com/OpenMontageInc/OpenMontage/discussions/892)
- [Discussion #231](https://github.com/calesthio/OpenMontage/discussions/231)

## 14.3 Official license/model/runtime references

- [GNU AGPL-3.0 full text](https://www.gnu.org/licenses/agpl-3.0.en.html)
- [FSF FAQ: private modifications and AGPL network services](https://www.gnu.org/licenses/gpl-faq.html)
- [FLUX.1 Schnell official model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
- [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M)
- [kokoro-onnx README](https://github.com/thewh1teagle/kokoro-onnx)
- [kokoro-onnx MIT license](https://github.com/thewh1teagle/kokoro-onnx/blob/main/LICENSE)
- [Kokoro voices/languages](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)
- [Remotion license & pricing](https://www.remotion.dev/docs/license/pricing)
- [Kaggle CLI kernel docs](https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels.md)

---

# 15. Финальное техническое решение

**Не запускать `documentary-montage` как есть для 20–40-минутной narration-документалки.** Он решает другой формат: короткий non-narrative montage. Из OpenMontage переиспользовать pipeline conventions, artifact schemas, checkpoint infrastructure, corpus/CLIP retrieval, подходящие media tools и локальный ComfyUI client — с соблюдением AGPL.

Создать новый `documentary-longform` и `factory/`:
- deterministic local orchestrator;
- local Ollama endpoint для сценария;
- local Kokoro `af_heart` только для подходящего языка narration;
- tagged local footage как основной визуальный источник;
- Kaggle FLUX.1 Schnell — редкий still-image fallback;
- chapter-level retry/resume;
- FFmpeg-first rendering и assembly;
- blocking 100% shot QA и выборочная human visual review;
- export только после PASS.

**Главные блокирующие риски:** доступ Ollama из Codespaces; соответствие `af_heart` языку сценария; реальная скорость/VRAM FLUX.1 Schnell на Kaggle T4; rights на каждый footage/music asset; audio QA, которое не принимает AAC с цифровой тишиной; chapter resume после разрыва Codespaces/Kaggle job.

---

## Примечание о полноте исследования

Полное дерево репозитория инвентаризировано через GitHub tree API: **2 285 файлов**, в том числе **660 Python-файлов**, **222 Python-модуля в `tools/`**, 212 файлов в `tests/`, 158 в `skills/`, 13 pipeline manifests. Глубокий source review выполнен по всем модулям целевого production path: pipeline loader/config/checkpoint, registry/base tool/provider routing, corpus/CLIP/retrieval/source adapters, documentary-montage skills, Kokoro/Piper/TTS routing, ComfyUI/FLUX, rendering/audio, QA, export, schemas, CI and relevant tests/issues. Не утверждается, что каждый из 660 Python-файлов, включая не относящиеся к этому workflow 3D/avatar/realtime integrations, был вручную перечитан построчно. Для заявленной фабрики эти unrelated tools не входят в план реализации.
