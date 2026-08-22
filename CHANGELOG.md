# [1.97.0](https://github.com/project-david-ai/projectdavid/compare/v1.96.6...v1.97.0) (2026-08-22)


### Bug Fixes

* **ci:** skip incompatible NumPy stubs in mypy ([85a6243](https://github.com/project-david-ai/projectdavid/commit/85a6243da4aa817417d6ad7a26c4b1bc9b7fd9ed))
* **ci:** skip NumPy typing submodules in mypy ([381faf5](https://github.com/project-david-ai/projectdavid/commit/381faf52b738f7efa619904cec124391e1ba55f9))
* **deployments:** add trailing slash to list and deactivate_all endpoints ([6e98bb5](https://github.com/project-david-ai/projectdavid/commit/6e98bb5f686b0abd6fcfad698c1051a59f15c0cc))
* **deployments:** add trailing slash to list and deactivate_all endpoints ([9d58080](https://github.com/project-david-ai/projectdavid/commit/9d58080119365ed599aa0a60a3f39918e475dd10))
* **schemas:** TrainingConfig from entities_common ([fa436c5](https://github.com/project-david-ai/projectdavid/commit/fa436c5ea69e6c599178702baf1c3a0fc3192378))
* **sdk:** remove unused DeploymentUpdateRequest import, fix update() payload to use dict comprehension with exclude-None ([f029e40](https://github.com/project-david-ai/projectdavid/commit/f029e40573e46cd8292279af25d31534f11841e4))
* **stream:** close async resources before loop shutdown ([3e26147](https://github.com/project-david-ai/projectdavid/commit/3e261473bd19d9e5ca4bb30cf7b9db2f367ef935))
* **stream:** explicitly close aiter_lines in finally block — prevents Task destroyed RuntimeWarning from dangling aiter_raw coroutines ([6d46184](https://github.com/project-david-ai/projectdavid/commit/6d461848e01ed9b0589891d9190f866d33982ac0))
* **stream:** explicitly close async generator in stream_chunks finally block — prevents Task destroyed RuntimeWarning from dangling aiter_bytes coroutines ([b073fed](https://github.com/project-david-ai/projectdavid/commit/b073fed1e2865a542ce3933db066455042670346))


### Features

* **datasets:** add hard-delete and offset pagination ([4bdea56](https://github.com/project-david-ai/projectdavid/commit/4bdea56d1d904d8674d581d42c991072edfff787))
* **deployments_client:** add mm_processor_kwargs to all activation and update methods ([522fad9](https://github.com/project-david-ai/projectdavid/commit/522fad910150ce2b0853ca0fea6bb188d5c9d582))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b66e81c](https://github.com/project-david-ai/projectdavid/commit/b66e81c9ee7f91ad426e332f1386b4d711541129))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b3c77e5](https://github.com/project-david-ai/projectdavid/commit/b3c77e570a6a6c5832d66c6a851d71d556ae2bda))
* **sdk:** add on_poll heartbeat callback to wait_for_completion ([e75287b](https://github.com/project-david-ai/projectdavid/commit/e75287beebac0a3dc7c371132405840ad8639bf3))
* **sdk:** add training.cancel() and typed TrainingConfig support ([a7c4cc1](https://github.com/project-david-ai/projectdavid/commit/a7c4cc115ea52f6e196bc207875f888ffe1ad089))
* **sdk:** add wait_until_ready and wait_for_completion helpers ([1fb55a8](https://github.com/project-david-ai/projectdavid/commit/1fb55a84d750775dff9efbdb19b87bc400aec668))
* **sdk:** align DeploymentsClient with hyperparam API ([05c4a56](https://github.com/project-david-ai/projectdavid/commit/05c4a56f4aeb7d37d8df0741596d23991e3953db))
* **sdk:** align DeploymentsClient with hyperparam API ([a181456](https://github.com/project-david-ai/projectdavid/commit/a181456fd80335b5c517e89151a3758703737061))
* **sdk:** Delete _version.py ([851c27b](https://github.com/project-david-ai/projectdavid/commit/851c27b1e2634e9d957d6b2b84e017060139a2fc))
* **vision:** Force rebuild ([a37f332](https://github.com/project-david-ai/projectdavid/commit/a37f332df4bea6cf6420fafc81b3f269956f87f6))

# [1.97.0](https://github.com/project-david-ai/projectdavid/compare/v1.96.6...v1.97.0) (2026-05-18)


### Bug Fixes

* **deployments:** add trailing slash to list and deactivate_all endpoints ([6e98bb5](https://github.com/project-david-ai/projectdavid/commit/6e98bb5f686b0abd6fcfad698c1051a59f15c0cc))
* **deployments:** add trailing slash to list and deactivate_all endpoints ([9d58080](https://github.com/project-david-ai/projectdavid/commit/9d58080119365ed599aa0a60a3f39918e475dd10))
* **schemas:** TrainingConfig from entities_common ([fa436c5](https://github.com/project-david-ai/projectdavid/commit/fa436c5ea69e6c599178702baf1c3a0fc3192378))
* **sdk:** remove unused DeploymentUpdateRequest import, fix update() payload to use dict comprehension with exclude-None ([f029e40](https://github.com/project-david-ai/projectdavid/commit/f029e40573e46cd8292279af25d31534f11841e4))
* **stream:** explicitly close aiter_lines in finally block — prevents Task destroyed RuntimeWarning from dangling aiter_raw coroutines ([6d46184](https://github.com/project-david-ai/projectdavid/commit/6d461848e01ed9b0589891d9190f866d33982ac0))
* **stream:** explicitly close async generator in stream_chunks finally block — prevents Task destroyed RuntimeWarning from dangling aiter_bytes coroutines ([b073fed](https://github.com/project-david-ai/projectdavid/commit/b073fed1e2865a542ce3933db066455042670346))


### Features

* **datasets:** add hard-delete and offset pagination ([4bdea56](https://github.com/project-david-ai/projectdavid/commit/4bdea56d1d904d8674d581d42c991072edfff787))
* **deployments_client:** add mm_processor_kwargs to all activation and update methods ([522fad9](https://github.com/project-david-ai/projectdavid/commit/522fad910150ce2b0853ca0fea6bb188d5c9d582))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b66e81c](https://github.com/project-david-ai/projectdavid/commit/b66e81c9ee7f91ad426e332f1386b4d711541129))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b3c77e5](https://github.com/project-david-ai/projectdavid/commit/b3c77e570a6a6c5832d66c6a851d71d556ae2bda))
* **sdk:** add on_poll heartbeat callback to wait_for_completion ([e75287b](https://github.com/project-david-ai/projectdavid/commit/e75287beebac0a3dc7c371132405840ad8639bf3))
* **sdk:** add training.cancel() and typed TrainingConfig support ([a7c4cc1](https://github.com/project-david-ai/projectdavid/commit/a7c4cc115ea52f6e196bc207875f888ffe1ad089))
* **sdk:** add wait_until_ready and wait_for_completion helpers ([1fb55a8](https://github.com/project-david-ai/projectdavid/commit/1fb55a84d750775dff9efbdb19b87bc400aec668))
* **sdk:** align DeploymentsClient with hyperparam API ([05c4a56](https://github.com/project-david-ai/projectdavid/commit/05c4a56f4aeb7d37d8df0741596d23991e3953db))
* **sdk:** align DeploymentsClient with hyperparam API ([a181456](https://github.com/project-david-ai/projectdavid/commit/a181456fd80335b5c517e89151a3758703737061))
* **sdk:** Delete _version.py ([851c27b](https://github.com/project-david-ai/projectdavid/commit/851c27b1e2634e9d957d6b2b84e017060139a2fc))
* **vision:** Force rebuild ([a37f332](https://github.com/project-david-ai/projectdavid/commit/a37f332df4bea6cf6420fafc81b3f269956f87f6))

# [1.97.0](https://github.com/project-david-ai/projectdavid/compare/v1.96.6...v1.97.0) (2026-05-18)


### Bug Fixes

* **deployments:** add trailing slash to list and deactivate_all endpoints ([6e98bb5](https://github.com/project-david-ai/projectdavid/commit/6e98bb5f686b0abd6fcfad698c1051a59f15c0cc))
* **deployments:** add trailing slash to list and deactivate_all endpoints ([9d58080](https://github.com/project-david-ai/projectdavid/commit/9d58080119365ed599aa0a60a3f39918e475dd10))
* **schemas:** TrainingConfig from entities_common ([fa436c5](https://github.com/project-david-ai/projectdavid/commit/fa436c5ea69e6c599178702baf1c3a0fc3192378))
* **sdk:** remove unused DeploymentUpdateRequest import, fix update() payload to use dict comprehension with exclude-None ([f029e40](https://github.com/project-david-ai/projectdavid/commit/f029e40573e46cd8292279af25d31534f11841e4))
* **stream:** explicitly close aiter_lines in finally block — prevents Task destroyed RuntimeWarning from dangling aiter_raw coroutines ([6d46184](https://github.com/project-david-ai/projectdavid/commit/6d461848e01ed9b0589891d9190f866d33982ac0))
* **stream:** explicitly close async generator in stream_chunks finally block — prevents Task destroyed RuntimeWarning from dangling aiter_bytes coroutines ([b073fed](https://github.com/project-david-ai/projectdavid/commit/b073fed1e2865a542ce3933db066455042670346))


### Features

* **datasets:** add hard-delete and offset pagination ([4bdea56](https://github.com/project-david-ai/projectdavid/commit/4bdea56d1d904d8674d581d42c991072edfff787))
* **deployments_client:** add mm_processor_kwargs to all activation and update methods ([522fad9](https://github.com/project-david-ai/projectdavid/commit/522fad910150ce2b0853ca0fea6bb188d5c9d582))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b66e81c](https://github.com/project-david-ai/projectdavid/commit/b66e81c9ee7f91ad426e332f1386b4d711541129))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([b3c77e5](https://github.com/project-david-ai/projectdavid/commit/b3c77e570a6a6c5832d66c6a851d71d556ae2bda))
* **sdk:** add on_poll heartbeat callback to wait_for_completion ([e75287b](https://github.com/project-david-ai/projectdavid/commit/e75287beebac0a3dc7c371132405840ad8639bf3))
* **sdk:** add training.cancel() and typed TrainingConfig support ([a7c4cc1](https://github.com/project-david-ai/projectdavid/commit/a7c4cc115ea52f6e196bc207875f888ffe1ad089))
* **sdk:** add wait_until_ready and wait_for_completion helpers ([1fb55a8](https://github.com/project-david-ai/projectdavid/commit/1fb55a84d750775dff9efbdb19b87bc400aec668))
* **sdk:** align DeploymentsClient with hyperparam API ([05c4a56](https://github.com/project-david-ai/projectdavid/commit/05c4a56f4aeb7d37d8df0741596d23991e3953db))
* **sdk:** align DeploymentsClient with hyperparam API ([a181456](https://github.com/project-david-ai/projectdavid/commit/a181456fd80335b5c517e89151a3758703737061))
* **sdk:** Delete _version.py ([851c27b](https://github.com/project-david-ai/projectdavid/commit/851c27b1e2634e9d957d6b2b84e017060139a2fc))
* **vision:** Force rebuild ([a37f332](https://github.com/project-david-ai/projectdavid/commit/a37f332df4bea6cf6420fafc81b3f269956f87f6))

# [1.104.0](https://github.com/project-david-ai/projectdavid/compare/v1.103.0...v1.104.0) (2026-04-22)


### Features

* **sdk:** add on_poll heartbeat callback to wait_for_completion ([13cdc6c](https://github.com/project-david-ai/projectdavid/commit/13cdc6cd0602547c6602d8254ad32e1eee650c07))

# [1.103.0](https://github.com/project-david-ai/projectdavid/compare/v1.102.1...v1.103.0) (2026-04-22)


### Features

* **sdk:** add wait_until_ready and wait_for_completion helpers ([67a7c70](https://github.com/project-david-ai/projectdavid/commit/67a7c709aa0200af80f320c9a0fbbbfaa529fdbe))

## [1.102.1](https://github.com/project-david-ai/projectdavid/compare/v1.102.0...v1.102.1) (2026-04-22)


### Bug Fixes

* **schemas:** TrainingConfig from entities_common ([22e191f](https://github.com/project-david-ai/projectdavid/commit/22e191fc776dd46370791ad1ff4cba0dce743afa))

# [1.102.0](https://github.com/project-david-ai/projectdavid/compare/v1.101.0...v1.102.0) (2026-04-21)


### Features

* **sdk:** add training.cancel() and typed TrainingConfig support ([97344d6](https://github.com/project-david-ai/projectdavid/commit/97344d6363cf0572e1dd44c6c42d7898cb7409bc))

# [1.101.0](https://github.com/project-david-ai/projectdavid/compare/v1.100.0...v1.101.0) (2026-04-13)


### Features

* **vision:** Force rebuild ([b455079](https://github.com/project-david-ai/projectdavid/commit/b45507911b50da44d3d06e808dff04309e6b2221))

# [1.100.0](https://github.com/project-david-ai/projectdavid/compare/v1.99.0...v1.100.0) (2026-04-12)


### Features

* **deployments_client:** add mm_processor_kwargs to all activation and update methods ([e508217](https://github.com/project-david-ai/projectdavid/commit/e508217d6bd483197b61d097231e01fba5e63e71))

# [1.99.0](https://github.com/project-david-ai/projectdavid/compare/v1.98.1...v1.99.0) (2026-04-12)


### Bug Fixes

* **deployments:** add trailing slash to list and deactivate_all endpoints ([761f8a7](https://github.com/project-david-ai/projectdavid/commit/761f8a78c4cc07fc26375d9aae35e0a53a198dc3))
* **sdk:** remove unused DeploymentUpdateRequest import, fix update() payload to use dict comprehension with exclude-None ([26ae725](https://github.com/project-david-ai/projectdavid/commit/26ae7251f3552d6e4375909ab5e9aaecfa7c3403))
* **stream:** explicitly close aiter_lines in finally block — prevents Task destroyed RuntimeWarning from dangling aiter_raw coroutines ([2245446](https://github.com/project-david-ai/projectdavid/commit/2245446dfe3af75f926fff376c0045a2dca36394))
* **stream:** explicitly close async generator in stream_chunks finally block — prevents Task destroyed RuntimeWarning from dangling aiter_bytes coroutines ([238ac3a](https://github.com/project-david-ai/projectdavid/commit/238ac3a7b4b15d64a46a1873612eff55370ea0a7))


### Features

* **sdk:** align DeploymentsClient with hyperparam API ([df73a9d](https://github.com/project-david-ai/projectdavid/commit/df73a9d55241ad9222026cfed3f97b3c933e5b26))
* **sdk:** align DeploymentsClient with hyperparam API ([ad2d894](https://github.com/project-david-ai/projectdavid/commit/ad2d894675bb015049bad9dc6c443f9e0d449dc4))

# [1.99.0-dev.1](https://github.com/project-david-ai/projectdavid/compare/v1.98.2-dev.3...v1.99.0-dev.1) (2026-04-12)


### Features

* **sdk:** align DeploymentsClient with hyperparam API ([df73a9d](https://github.com/project-david-ai/projectdavid/commit/df73a9d55241ad9222026cfed3f97b3c933e5b26))
* **sdk:** align DeploymentsClient with hyperparam API ([ad2d894](https://github.com/project-david-ai/projectdavid/commit/ad2d894675bb015049bad9dc6c443f9e0d449dc4))

## [1.98.2-dev.3](https://github.com/project-david-ai/projectdavid/compare/v1.98.2-dev.2...v1.98.2-dev.3) (2026-04-12)


### Bug Fixes

* **stream:** explicitly close aiter_lines in finally block — prevents Task destroyed RuntimeWarning from dangling aiter_raw coroutines ([2245446](https://github.com/project-david-ai/projectdavid/commit/2245446dfe3af75f926fff376c0045a2dca36394))

## [1.98.2-dev.2](https://github.com/project-david-ai/projectdavid/compare/v1.98.2-dev.1...v1.98.2-dev.2) (2026-04-11)


### Bug Fixes

* **stream:** explicitly close async generator in stream_chunks finally block — prevents Task destroyed RuntimeWarning from dangling aiter_bytes coroutines ([238ac3a](https://github.com/project-david-ai/projectdavid/commit/238ac3a7b4b15d64a46a1873612eff55370ea0a7))

## [1.98.2-dev.1](https://github.com/project-david-ai/projectdavid/compare/v1.98.1...v1.98.2-dev.1) (2026-04-11)


### Bug Fixes

* **deployments:** add trailing slash to list and deactivate_all endpoints ([761f8a7](https://github.com/project-david-ai/projectdavid/commit/761f8a78c4cc07fc26375d9aae35e0a53a198dc3))

## [1.98.1](https://github.com/project-david-ai/projectdavid/compare/v1.98.0...v1.98.1) (2026-04-10)


### Bug Fixes

* **deployments:** add trailing slash to list and deactivate_all endpoints ([dfcf47d](https://github.com/project-david-ai/projectdavid/commit/dfcf47dc603718b102e800f917d84b5851762a19))

# [1.97.0-dev.1](https://github.com/project-david-ai/projectdavid/compare/v1.96.6...v1.97.0-dev.1) (2026-04-09)


### Features

* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([d4171ae](https://github.com/project-david-ai/projectdavid/commit/d4171ae5899b92e28846dbae6df7210479496bb1))
* **sdk:** add DeploymentsClient and deprecate ModelsClient activation methods ([d649deb](https://github.com/project-david-ai/projectdavid/commit/d649deb6f89f7c7aeaa956b55c936093480fe20b))

## [1.96.6](https://github.com/project-david-ai/projectdavid/compare/v1.96.5...v1.96.6) (2026-04-05)


### Bug Fixes

* **deps:** relax projectdavid_common pin to minimum version constraint ([1966a6a](https://github.com/project-david-ai/projectdavid/commit/1966a6a9b73588e896563bd26cb3e456ba1d6c5b))

## [1.96.5](https://github.com/project-david-ai/projectdavid/compare/v1.96.4...v1.96.5) (2026-04-04)


### Bug Fixes

* **release:** bump projectdavid-common to 0.64.1 ([e5bd86a](https://github.com/project-david-ai/projectdavid/commit/e5bd86aa0e658aad70e43e1f6a3d4e7b795d425d))

## [1.96.4](https://github.com/project-david-ai/projectdavid/compare/v1.96.3...v1.96.4) (2026-04-04)


### Bug Fixes

* **pyproject:** add missing comma in dependencies array ([8421950](https://github.com/project-david-ai/projectdavid/commit/84219505094072a1c527b6d721cf9c3c2cdb20bc))

## [1.96.3](https://github.com/project-david-ai/projectdavid/compare/v1.96.2...v1.96.3) (2026-04-02)


### Bug Fixes

* **deps:** Add _version.py ([5ab9fef](https://github.com/project-david-ai/projectdavid/commit/5ab9fef2116a6b0ee2ac2e8a76b538cdc9fcb303))

## [1.96.2](https://github.com/project-david-ai/projectdavid/compare/v1.96.1...v1.96.2) (2026-04-02)


### Bug Fixes

* **deps:** bump projectdavid-common to 0.63.0 ([abefc93](https://github.com/project-david-ai/projectdavid/commit/abefc9398bd7816983c3e1688f97ee164e2fe029))

## [1.96.1](https://github.com/project-david-ai/projectdavid/compare/v1.96.0...v1.96.1) (2026-03-31)


### Bug Fixes

* ModelsClient training_url defaults to base_url via nginx instead of direct port 9001 ([440c598](https://github.com/project-david-ai/projectdavid/commit/440c598b72a83378e2fc00dd54091c4c731d615c))

# [1.96.0](https://github.com/project-david-ai/projectdavid/compare/v1.95.0...v1.96.0) (2026-03-31)


### Features

* trigger publish — ModelsClient nginx routing fix ([096c62d](https://github.com/project-david-ai/projectdavid/commit/096c62dc734d90be8049df8554344d700d1251ab))

# [1.95.0](https://github.com/project-david-ai/projectdavid/compare/v1.94.1...v1.95.0) (2026-03-30)


### Features

* route training clients through nginx proxy, align base_url defaults ([3df61a0](https://github.com/project-david-ai/projectdavid/commit/3df61a020cdd660e437e16a746a0eba71fab5e7b))

## [1.94.1](https://github.com/project-david-ai/projectdavid/compare/v1.94.0...v1.94.1) (2026-03-30)


### Bug Fixes

* trigger release build for max_tokens inference parameter support ([42273da](https://github.com/project-david-ai/projectdavid/commit/42273daeb25713a8bf44fd78c3c164a5c9ede231))

# [1.94.0](https://github.com/project-david-ai/projectdavid/compare/v1.93.0...v1.94.0) (2026-03-29)


### Features

* add max_tokens parameter to create_assistant client method ([ebbf696](https://github.com/project-david-ai/projectdavid/commit/ebbf69649437a77afcb172f10d714e48babffc54))
* integrate max_tokens parameter into create_assistant client method & bump to projectdavid_common==0.61.5 ([c8ab9f5](https://github.com/project-david-ai/projectdavid/commit/c8ab9f54e497d383015715026101a01ec32c2e00))

# [1.93.0](https://github.com/project-david-ai/projectdavid/compare/v1.92.0...v1.93.0) (2026-03-28)


### Features

* **registry:** add registry client and finalize formatting ([acfa158](https://github.com/project-david-ai/projectdavid/commit/acfa1583ec1e02653a413248462971d4fc16c5ee))
* **registry:** implement registry client and project maintenance ([201868e](https://github.com/project-david-ai/projectdavid/commit/201868e0c8ea2c71cd25fd803bd6d0a711bae011))

# [1.92.0-dev.1](https://github.com/project-david-ai/projectdavid/compare/v1.91.0...v1.92.0-dev.1) (2026-03-26)


### Features

* **registry:** add registry client and finalize formatting ([acfa158](https://github.com/project-david-ai/projectdavid/commit/acfa1583ec1e02653a413248462971d4fc16c5ee))
* **registry:** implement registry client and project maintenance ([201868e](https://github.com/project-david-ai/projectdavid/commit/201868e0c8ea2c71cd25fd803bd6d0a711bae011))

# [1.91.0](https://github.com/project-david-ai/projectdavid/compare/v1.90.3...v1.91.0) (2026-03-25)


### Bug Fixes

* **bandit:** replace assert with RuntimeError raises in file_processor properties ([d6883f6](https://github.com/project-david-ai/projectdavid/commit/d6883f6c9197568899666ecd2030942466b0e369))
* **ci:** install pytest explicitly before running test suite ([15a3566](https://github.com/project-david-ai/projectdavid/commit/15a3566d247c9f17d51fc5fa1ef2892e84a16c89))
* **ci:** update TestPyPI upload URL to legacy endpoint ([d0d7783](https://github.com/project-david-ai/projectdavid/commit/d0d7783c691d0eff04597eb1808ec959b83af6f6))
* **mypy:** resolve remaining CI type errors across clients ([364aca8](https://github.com/project-david-ai/projectdavid/commit/364aca8c67a945cf3f793077c47bb87c03536a52))
* **typer:** Continue to resolve typer CI issues ([372ea61](https://github.com/project-david-ai/projectdavid/commit/372ea61e9980a19dddfebe8e718b233c2ef66d74))
* **typer:** Continue to resolve typer CI issues ([120af65](https://github.com/project-david-ai/projectdavid/commit/120af6548e965ec7972d116315a63e979c49ddcc))


### Features

* **types:** implement strict type safety and PEP 561 support ([5d9150e](https://github.com/project-david-ai/projectdavid/commit/5d9150e9e0338b502bba11c6aa204fad24f3ce72))

## [1.90.3](https://github.com/project-david-ai/projectdavid/compare/v1.90.2...v1.90.3) (2026-03-25)


### Bug Fixes

* **ci:** update TestPyPI upload URL to legacy endpoint ([fe108d8](https://github.com/project-david-ai/projectdavid/commit/fe108d852d3a8413cf346a38a463cd3936e14408))
* refactor HTTP error handling to avoid bare excepts" ([972078d](https://github.com/project-david-ai/projectdavid/commit/972078d2d3b868c9eb7feab05c46bb0471ca3796))
* **security:** resolve final Bandit security warnings in user client and runs ([54c64df](https://github.com/project-david-ai/projectdavid/commit/54c64dfda669006b7f499b77c022f6e11a23523e))

## [1.90.2-dev.1](https://github.com/project-david-ai/projectdavid/compare/v1.90.1...v1.90.2-dev.1) (2026-03-25)


### Bug Fixes

* add [@property](https://github.com/property) decorator and missing return to Entity.registry ([d0241eb](https://github.com/project-david-ai/projectdavid/commit/d0241eb334bff2137889abcb255fa2186be292b0))
* bump projectdavid_common version to 0.60.0 ([06334fb](https://github.com/project-david-ai/projectdavid/commit/06334fbe3e707dddc370cb96c7bd5f2198f01c09))
* refactor HTTP error handling to avoid bare excepts" ([972078d](https://github.com/project-david-ai/projectdavid/commit/972078d2d3b868c9eb7feab05c46bb0471ca3796))
* **security:** resolve final Bandit security warnings in user client and runs ([54c64df](https://github.com/project-david-ai/projectdavid/commit/54c64dfda669006b7f499b77c022f6e11a23523e))

## [1.90.1](https://github.com/project-david-ai/projectdavid/compare/v1.90.0...v1.90.1) (2026-03-24)


### Bug Fixes

* add [@property](https://github.com/property) decorator and missing return to Entity.registry ([ac19bcb](https://github.com/project-david-ai/projectdavid/commit/ac19bcb1ab895e5b56ff7f854829b2fb79559af1))
* bump projectdavid_common version to 0.60.0 ([3278c97](https://github.com/project-david-ai/projectdavid/commit/3278c97a8641e616c65c0ba364e6e2ab000f3cc3))

# [1.90.0](https://github.com/project-david-ai/projectdavid/compare/v1.89.1...v1.90.0) (2026-03-23)


### Features

* Add stream bool ([152c90b](https://github.com/project-david-ai/projectdavid/commit/152c90be3acbf0629443fba811e603fd307326d7))

## [1.89.1](https://github.com/project-david-ai/projectdavid/compare/v1.89.0...v1.89.1) (2026-03-23)


### Bug Fixes

* bump projectdavid_common version to 0.60.0 ([028cbc9](https://github.com/project-david-ai/projectdavid/commit/028cbc9743fdb3022b21e9e0b7c79bae1c6a33d0))

# [1.89.0](https://github.com/project-david-ai/projectdavid/compare/v1.88.0...v1.89.0) (2026-03-23)


### Features

* wire tensor_parallel_size into activation endpoints ([3b31fc5](https://github.com/project-david-ai/projectdavid/commit/3b31fc5d066b07c41b5b9dae174e025778853cbb))

# [1.88.0](https://github.com/project-david-ai/projectdavid/compare/v1.87.0...v1.88.0) (2026-03-22)


### Features

* bump projectdavid_common==0.58.0 ([5bb91ea](https://github.com/project-david-ai/projectdavid/commit/5bb91ea9158e3267819f0ed76bc3fdf9d86590da))

# [1.87.0](https://github.com/project-david-ai/projectdavid/compare/v1.86.0...v1.87.0) (2026-03-21)


### Features

* add activate_base ([5c11bfd](https://github.com/project-david-ai/projectdavid/commit/5c11bfd728218d038065e9fe4aef50723472d653))
* add activate_base ([0301844](https://github.com/project-david-ai/projectdavid/commit/030184435565065a59d4271d474a62a7985433c5))

# [1.86.0](https://github.com/project-david-ai/projectdavid/compare/v1.85.0...v1.86.0) (2026-03-21)


### Features

* bump projectdavid_common version to 0.57.0 in dependencies ([3ec5ffa](https://github.com/project-david-ai/projectdavid/commit/3ec5ffa1f8563ea7613ded82ae9994c7020dc940))

# [1.85.0](https://github.com/project-david-ai/projectdavid/compare/v1.84.2...v1.85.0) (2026-03-20)


### Features

* add `deactivate_all` method to `ModelsClient` for deactivating fine-tuned models ([257b6a2](https://github.com/project-david-ai/projectdavid/commit/257b6a27685065289dcdef9064db6d37c05a4606))

## [1.84.2](https://github.com/project-david-ai/projectdavid/compare/v1.84.1...v1.84.2) (2026-03-20)


### Bug Fixes

* bump `projectdavid_common` to v0.56.0 in dependencies ([8370828](https://github.com/project-david-ai/projectdavid/commit/8370828933d6dd860fc456756afaefb0037640a1))

## [1.84.1](https://github.com/project-david-ai/projectdavid/compare/v1.84.0...v1.84.1) (2026-03-20)


### Bug Fixes

* bump `projectdavid_common` to v0.56.0 in dependencies ([c7405ad](https://github.com/project-david-ai/projectdavid/commit/c7405adcb782a2209342991e5a02ff17570d9dcd))

# [1.84.0](https://github.com/project-david-ai/projectdavid/compare/v1.83.0...v1.84.0) (2026-03-20)


### Features

* add `activate` method to `ModelsClient` for activating fine-tuned models ([e87e103](https://github.com/project-david-ai/projectdavid/commit/e87e103a215093d778b86273cd85340f3f2e5b45))

# [1.83.0](https://github.com/project-david-ai/projectdavid/compare/v1.82.5...v1.83.0) (2026-03-20)


### Features

* add `ModelsClient` with fine-tuning support and integrate into `entity.py` ([bc6c1ab](https://github.com/project-david-ai/projectdavid/commit/bc6c1ab79dda4f01d2d42bda87830814086169cb))

## [1.82.5](https://github.com/project-david-ai/projectdavid/compare/v1.82.4...v1.82.5) (2026-03-20)


### Bug Fixes

* update projectdavid_common dependency to 0.55.0 ([6db9f0f](https://github.com/project-david-ai/projectdavid/commit/6db9f0fef367701c84486555f32ed59ef4247936))

## [1.82.4](https://github.com/project-david-ai/projectdavid/compare/v1.82.3...v1.82.4) (2026-03-19)


### Bug Fixes

* update projectdavid_common dependency to 0.55.0 ([b5015c4](https://github.com/project-david-ai/projectdavid/commit/b5015c433ff4c3e10cd3336a6d23b00532db38c9))
* update projectdavid_common dependency to 0.55.0 ([200a7de](https://github.com/project-david-ai/projectdavid/commit/200a7de3bf525a33ad292ff4bae1a0ae70e8bb40))

## [1.82.3](https://github.com/project-david-ai/projectdavid/compare/v1.82.2...v1.82.3) (2026-03-19)


### Bug Fixes

* bump `projectdavid_common` to v0.54.0 in dependencies ([0f24cc8](https://github.com/project-david-ai/projectdavid/commit/0f24cc8ba5babfef169af3218dd3aeea00ca232b))

## [1.82.2](https://github.com/project-david-ai/projectdavid/compare/v1.82.1...v1.82.2) (2026-03-19)


### Bug Fixes

* add `_version.py` file ([22823c7](https://github.com/project-david-ai/projectdavid/commit/22823c7fddb4ad5b91ec9f2607ac19f5c59e00a6))
* bump `projectdavid_common` to v0.51.0 in dependencies ([e6d25d8](https://github.com/project-david-ai/projectdavid/commit/e6d25d8e8be2507326e261f3760afc3ada0abc78))
* bump `projectdavid_common` to v0.52.0 in dependencies ([78c9a02](https://github.com/project-david-ai/projectdavid/commit/78c9a02f38e84466b40db0b1908f4b35cb8c3a8a))
* bump `projectdavid_common` to v0.53.0 in dependencies ([804ffb3](https://github.com/project-david-ai/projectdavid/commit/804ffb312f8386412b4ca6dd9c487010f5836e83))

## [1.82.1](https://github.com/project-david-ai/projectdavid/compare/v1.82.0...v1.82.1) (2026-03-19)


### Bug Fixes

* bump `projectdavid_common` to v0.51.0 in dependencies ([3a1e853](https://github.com/project-david-ai/projectdavid/commit/3a1e853fbcbaec84cdbb738025d13b19f90945df))

# [1.82.0](https://github.com/project-david-ai/projectdavid/compare/v1.81.0...v1.82.0) (2026-03-19)


### Features

* integrate `TrainingClient` into `entity.py` ([7287c9e](https://github.com/project-david-ai/projectdavid/commit/7287c9ede719b4d49dc7aaa5cbfc9e391de299ed))

# [1.81.0](https://github.com/project-david-ai/projectdavid/compare/v1.80.0...v1.81.0) (2026-03-19)


### Features

* add `TrainingClient` for managing training jobs ([feab38e](https://github.com/project-david-ai/projectdavid/commit/feab38e199cb62a6741abd60014c4503eae2e67d))

# [1.80.0](https://github.com/project-david-ai/projectdavid/compare/v1.79.0...v1.80.0) (2026-03-18)


### Features

* Resolve API key bug in datasets_client.py ([722f311](https://github.com/project-david-ai/projectdavid/commit/722f3119b124101d026b3c0a5729d52e15ee4b4b))

# [1.79.0](https://github.com/project-david-ai/projectdavid/compare/v1.78.0...v1.79.0) (2026-03-17)


### Features

* add `DatasetsClient` and integrate it into `entity.py`, bump `projectdavid_common` to v0.50.0 in dependencies ([d06978e](https://github.com/project-david-ai/projectdavid/commit/d06978e42439164188bbfd70dbdf8f12634965fe))

# [1.78.0](https://github.com/project-david-ai/projectdavid/compare/v1.77.10...v1.78.0) (2026-03-17)


### Features

* add `DatasetsClient` and integrate it into `entity.py`, bump `projectdavid_common` to v0.50.0 in dependencies ([e63e0cc](https://github.com/project-david-ai/projectdavid/commit/e63e0cc658b1692b49bea7c576e51e07866917ca))

## [1.77.10](https://github.com/project-david-ai/projectdavid/compare/v1.77.9...v1.77.10) (2026-03-17)


### Bug Fixes

* bump `projectdavid_common` to v0.49.0 in dependencies ([c09cb97](https://github.com/project-david-ai/projectdavid/commit/c09cb970202fe48d665bd32d2f7110d79573e273))

## [1.77.9](https://github.com/project-david-ai/projectdavid/compare/v1.77.8...v1.77.9) (2026-03-17)


### Bug Fixes

* bump `projectdavid_common` to v0.48.0 in dependencies ([0eec49f](https://github.com/project-david-ai/projectdavid/commit/0eec49f37f7b00412385010c8f48ef199faafa11))

## [1.77.8](https://github.com/project-david-ai/projectdavid/compare/v1.77.7...v1.77.8) (2026-03-16)


### Bug Fixes

* clean up unused import in vectors.py and update pyproject.toml formatting and dependencies ([afa3dd0](https://github.com/project-david-ai/projectdavid/commit/afa3dd0a0d26f328c33a63d09ba47a79a3f556eb))

## [1.77.7](https://github.com/project-david-ai/projectdavid/compare/v1.77.6...v1.77.7) (2026-03-14)


### Bug Fixes

* update default `BASE_URL` to `http://localhost:80` across all files ([af5aefa](https://github.com/project-david-ai/projectdavid/commit/af5aefa622f33d3075759422239afe914a8c9541))

## [1.77.6](https://github.com/project-david-ai/projectdavid/compare/v1.77.5...v1.77.6) (2026-03-13)


### Bug Fixes

* bump `projectdavid_common` to v0.47.0 in dependencies ([cea5532](https://github.com/project-david-ai/projectdavid/commit/cea5532989714b5dceafb48efc3dade68c52c821))
* remove unused `embeddings` requirement from pyproject.toml ([0e212d3](https://github.com/project-david-ai/projectdavid/commit/0e212d34d32ab05e2cac7500a2eba105dc81257e))

## [1.77.5](https://github.com/project-david-ai/projectdavid/compare/v1.77.4...v1.77.5) (2026-03-13)


### Bug Fixes

* bump `projectdavid_common` to v0.46.0 in dependencies ([9511f8e](https://github.com/project-david-ai/projectdavid/commit/9511f8ecfdcddee5f17b05b902aaba7c8ba2432c))

## [1.77.4](https://github.com/project-david-ai/projectdavid/compare/v1.77.3...v1.77.4) (2026-03-13)


### Bug Fixes

* bump `projectdavid_common` to v0.45.0 in dependencies ([1075762](https://github.com/project-david-ai/projectdavid/commit/1075762ddaab89efd7ab17dffeb79fb118a5bb59))

## [1.77.3](https://github.com/project-david-ai/projectdavid/compare/v1.77.2...v1.77.3) (2026-03-12)


### Bug Fixes

* enhance image processing in `MessagesClient` ([a786402](https://github.com/project-david-ai/projectdavid/commit/a786402c55b6aa71ed62b6076f3b01214c71f90a))

## [1.77.2](https://github.com/project-david-ai/projectdavid/compare/v1.77.1...v1.77.2) (2026-03-12)


### Bug Fixes

* add User-Agent header to `httpx.get` in `MessagesClient` to prevent 403 errors from strict servers ([c9561f1](https://github.com/project-david-ai/projectdavid/commit/c9561f11df6c102741d96523246ee9c8e41fc823))

## [1.77.1](https://github.com/project-david-ai/projectdavid/compare/v1.77.0...v1.77.1) (2026-03-12)


### Bug Fixes

* correct import path for `FileClient` in `MessagesClient` ([0a3aecc](https://github.com/project-david-ai/projectdavid/commit/0a3aecc7dcde703c5c5c65cbfeefe4fd519e16c6))

# [1.77.0](https://github.com/project-david-ai/projectdavid/compare/v1.76.2...v1.77.0) (2026-03-12)


### Features

* reintroduce multimodal message support and bump `projectdavid_common` to v0.44.0 ([616e966](https://github.com/project-david-ai/projectdavid/commit/616e966a36379b17a751ec48646333d22f56d3b9))

## [1.76.2](https://github.com/project-david-ai/projectdavid/compare/v1.76.1...v1.76.2) (2026-03-12)


### Bug Fixes

* simplify `MessagesClient` by removing multimodal support ([add6061](https://github.com/project-david-ai/projectdavid/commit/add6061c743dc84e49cd99ab6b8d4e562b440cf6))

## [1.76.1](https://github.com/project-david-ai/projectdavid/compare/v1.76.0...v1.76.1) (2026-03-12)


### Bug Fixes

* bump `projectdavid_common` to v0.43.1 in dependencies ([839cd00](https://github.com/project-david-ai/projectdavid/commit/839cd0082c57caf2012122243f0aa71b918306d1))
* bump `projectdavid_common` to v0.43.1 in dependencies ([d5182a5](https://github.com/project-david-ai/projectdavid/commit/d5182a51cfe80cc9d36f29e9b351c83d7a640416))

# [1.76.0](https://github.com/project-david-ai/projectdavid/compare/v1.75.2...v1.76.0) (2026-03-12)


### Features

* add multimodal message support and update `projectdavid_common` to v0.43.0 ([3eafade](https://github.com/project-david-ai/projectdavid/commit/3eafade96413b7c3aafbcfcd098be1ca34758d5e))

## [1.75.2](https://github.com/project-david-ai/projectdavid/compare/v1.75.1...v1.75.2) (2026-03-11)


### Bug Fixes

* bump `projectdavid_common` to v0.42.0 in dependencies ([1dac755](https://github.com/project-david-ai/projectdavid/commit/1dac7550366b0063f04007274cf43de74c13880f))

## [1.75.1](https://github.com/project-david-ai/projectdavid/compare/v1.75.0...v1.75.1) (2026-03-11)


### Bug Fixes

* suppress redundant `shell` session PTY text from SSE stream ([f3cdac7](https://github.com/project-david-ai/projectdavid/commit/f3cdac78f4059220ae8f20f2cdf5e515a573ffef))

# [1.75.0](https://github.com/project-david-ai/projectdavid/compare/v1.74.12...v1.75.0) (2026-03-11)


### Features

* expand event and chunk processing with new `shell` capabilities ([a661af5](https://github.com/project-david-ai/projectdavid/commit/a661af5bf7dbd7ddd9b08e22fd76ffbfd2381f56))

## [1.74.12](https://github.com/project-david-ai/projectdavid/compare/v1.74.11...v1.74.12) (2026-03-09)


### Bug Fixes

* add `soft_delete_file` method to `files_client` ([6437e60](https://github.com/project-david-ai/projectdavid/commit/6437e603e0415fe9f99aa30bd35b46a7481be52e))

## [1.74.11](https://github.com/project-david-ai/projectdavid/compare/v1.74.10...v1.74.11) (2026-03-08)


### Bug Fixes

* add `list_assistants` alias and clean up comments in `assistants_client.py` ([b0a8660](https://github.com/project-david-ai/projectdavid/commit/b0a8660a76aae4404e981fdab925ae0b39d77e57))

## [1.74.10](https://github.com/project-david-ai/projectdavid/compare/v1.74.9...v1.74.10) (2026-03-08)


### Bug Fixes

* improve import formatting and clean up spacing inconsistencies ([852034c](https://github.com/project-david-ai/projectdavid/commit/852034c41ea8edeeb07f68aad408cef4cc0d9b47))
* improve import formatting and consistency across modules ([ee30788](https://github.com/project-david-ai/projectdavid/commit/ee30788421a2180308a3d8f9e7e3869f99cbb09e))

## [1.74.9](https://github.com/project-david-ai/projectdavid/compare/v1.74.8...v1.74.9) (2026-03-08)


### Bug Fixes

* refactor dependencies and extras in `pyproject.toml` ([db3000a](https://github.com/project-david-ai/projectdavid/commit/db3000ab87fd34fe752598d42617b63f9c08c220))

## [1.74.8](https://github.com/project-david-ai/projectdavid/compare/v1.74.7...v1.74.8) (2026-03-08)


### Bug Fixes

* remove assistant-vector store orchestration, streamline vector store ops ([6c8897f](https://github.com/project-david-ai/projectdavid/commit/6c8897ff1dc025b8854a9a3a5605ee69574c5fe5))

## [1.74.7](https://github.com/project-david-ai/projectdavid/compare/v1.74.6...v1.74.7) (2026-03-08)


### Bug Fixes

* update `cancel_run` to return validated `Run` model ([25b60d6](https://github.com/project-david-ai/projectdavid/commit/25b60d6ae4af79c6dd8a47aec133798c22931051))

## [1.74.6](https://github.com/project-david-ai/projectdavid/compare/v1.74.5...v1.74.6) (2026-03-07)


### Bug Fixes

* remove `NetworkDeviceHandler` and related imports ([10be103](https://github.com/project-david-ai/projectdavid/commit/10be10375eb344ef296dcaf5983e6224d6d4a017))
* remove invalid `network` block from `pyproject.toml` ([2140814](https://github.com/project-david-ai/projectdavid/commit/21408147cf836f861c6ff368f16c727bef846143))

## [1.74.5](https://github.com/project-david-ai/projectdavid/compare/v1.74.4...v1.74.5) (2026-03-07)


### Bug Fixes

* bump `projectdavid_common` to v0.41.0 ([ec05e50](https://github.com/project-david-ai/projectdavid/commit/ec05e50288334b8db404d21b2d1fcc9a37ae6ad3))

## [1.74.4](https://github.com/project-david-ai/projectdavid/compare/v1.74.3...v1.74.4) (2026-03-07)


### Bug Fixes

* update `projectdavid_common` to v0.40.1 and standardize header usage for API key handling ([8f6b50e](https://github.com/project-david-ai/projectdavid/commit/8f6b50eec63c125641af747c4ba5d3af56ebdb75))

## [1.74.3](https://github.com/project-david-ai/projectdavid/compare/v1.74.2...v1.74.3) (2026-03-07)


### Bug Fixes

* add `service_token` support in inference client for internal bypass use ([3ead7a8](https://github.com/project-david-ai/projectdavid/commit/3ead7a873c8a237238265c83e109d0c84ad49c59))

## [1.74.2](https://github.com/project-david-ai/projectdavid/compare/v1.74.1...v1.74.2) (2026-03-06)


### Bug Fixes

* update projectdavid_common==0.39.0 ([53f913e](https://github.com/project-david-ai/projectdavid/commit/53f913e60e2afa141c4998e2409aeabd2577a856))

## [1.74.1](https://github.com/project-david-ai/projectdavid/compare/v1.74.0...v1.74.1) (2026-03-06)


### Bug Fixes

* stop LLM provider key overriding platform Authorization header in inference client ([e2ce46f](https://github.com/project-david-ai/projectdavid/commit/e2ce46fb403f0b8c663f40b345b496fee71d6b19))

# [1.74.0](https://github.com/project-david-ai/projectdavid/compare/v1.73.1...v1.74.0) (2026-03-06)


### Features

* propagate optional meta_data through inference stack (schema, wrapper, client) ([80d5bd9](https://github.com/project-david-ai/projectdavid/commit/80d5bd96a6f3a0e8bb1ee22e5baaa5cd0419d3ba))

## [1.73.1](https://github.com/project-david-ai/projectdavid/compare/v1.73.0...v1.73.1) (2026-03-04)


### Bug Fixes

* Update common utilities package to projectdavid_common==0.37.0 ([2527156](https://github.com/project-david-ai/projectdavid/commit/25271566d42755cca51cb41adb277e705e5a990c))

# [1.73.0](https://github.com/project-david-ai/projectdavid/compare/v1.72.0...v1.73.0) (2026-03-03)


### Features

* add cross-version Qdrant client compatibility ([b6919cd](https://github.com/project-david-ai/projectdavid/commit/b6919cd118dd9bf8257a2f9a8098dcd7297b0390))

# [1.72.0](https://github.com/project-david-ai/projectdavid/compare/v1.71.2...v1.72.0) (2026-03-01)


### Features

* integrate SearxNG as internal SERP provider ([4eb7ed1](https://github.com/project-david-ai/projectdavid/commit/4eb7ed173a429aaf841beb218a17effc71b3f8cd))

## [1.71.2](https://github.com/project-david-ai/projectdavid/compare/v1.71.1...v1.71.2) (2026-02-28)


### Bug Fixes

* add user_id propagation to BatfishClient methods for admin override orchestration ([9c91f53](https://github.com/project-david-ai/projectdavid/commit/9c91f53d3bdc11d367cc4c53877fa1a904e806d2))

## [1.71.1](https://github.com/project-david-ai/projectdavid/compare/v1.71.0...v1.71.1) (2026-02-27)


### Bug Fixes

* projectdavid_common==0.35.0 ([2fae4c3](https://github.com/project-david-ai/projectdavid/commit/2fae4c37f53c86930bb1798a6371352268b67a4f))

# [1.71.0](https://github.com/project-david-ai/projectdavid/compare/v1.70.0...v1.71.0) (2026-02-27)


### Features

* get_enriched_topology ([72ab056](https://github.com/project-david-ai/projectdavid/commit/72ab0560b7b699e6fefcb918746e76284992fe78))

# [1.70.0](https://github.com/project-david-ai/projectdavid/compare/v1.69.2...v1.70.0) (2026-02-27)


### Features

* add BatfishClient with create/refresh split and typed responses ([a2e0a18](https://github.com/project-david-ai/projectdavid/commit/a2e0a1807cbc035770100a2cfd9637cdea76b9df))

## [1.69.2](https://github.com/project-david-ai/projectdavid/compare/v1.69.1...v1.69.2) (2026-02-27)


### Bug Fixes

* prefix all client URLs with /v1/ to match api_router mount point ([aa5061d](https://github.com/project-david-ai/projectdavid/commit/aa5061de2b81bb4682d07fddba9acbe326a93d23))

## [1.69.1](https://github.com/project-david-ai/projectdavid/compare/v1.69.0...v1.69.1) (2026-02-27)


### Bug Fixes

* Expose batfish ([7d32fdd](https://github.com/project-david-ai/projectdavid/commit/7d32fdd00ddb29b21a09a21b06f521ff6c3432c3))
* update projectdavid-common to 0.34.0 ([01f796c](https://github.com/project-david-ai/projectdavid/commit/01f796c79afe492ed5249e11ee4c6367a9241898))

# [1.69.0](https://github.com/project-david-ai/projectdavid/compare/v1.68.0...v1.69.0) (2026-02-27)


### Features

* add Batfish SDK client for network RCA pipeline ([98b56cf](https://github.com/project-david-ai/projectdavid/commit/98b56cfe37be371fc5b4c6a284d380a876d710f8))

# [1.68.0](https://github.com/project-david-ai/projectdavid/compare/v1.67.1...v1.68.0) (2026-02-27)


### Features

* add Batfish SDK client for network RCA pipeline ([9380b45](https://github.com/project-david-ai/projectdavid/commit/9380b4532c775fe9b1f6af2e6ebf817e8d47153b))

## [1.67.1](https://github.com/project-david-ai/projectdavid/compare/v1.67.0...v1.67.1) (2026-02-26)


### Bug Fixes

* delete serializers.py ([5a57ace](https://github.com/project-david-ai/projectdavid/commit/5a57ace14293261f21f7e7016fe9039a17a893e4))

# [1.67.0](https://github.com/project-david-ai/projectdavid/compare/v1.66.0...v1.67.0) (2026-02-26)


### Features

* add update_run_fields for targeted mid-run lifecycle writes ([e128ee6](https://github.com/project-david-ai/projectdavid/commit/e128ee6ede6c052648b36f02cda318da98f592a1))

# [1.66.0](https://github.com/project-david-ai/projectdavid/compare/v1.65.0...v1.66.0) (2026-02-25)


### Features

* Finalize Engineering Event Mapping and Fix Missing Event Registrations ([e4c25a0](https://github.com/project-david-ai/projectdavid/commit/e4c25a0d3377e40a97198e57c92838df8b418d67))

# [1.65.0](https://github.com/project-david-ai/projectdavid/compare/v1.64.0...v1.65.0) (2026-02-25)


### Features

* enrich ToolInterceptEvent with junior context for self-contained execution ([dae7bba](https://github.com/project-david-ai/projectdavid/commit/dae7bbab5d9f16aef06e285aacec939b9876b138))

# [1.64.0](https://github.com/project-david-ai/projectdavid/compare/v1.63.0...v1.64.0) (2026-02-25)


### Features

* add execute_intercepted to ToolInterceptEvent ([a1b3989](https://github.com/project-david-ai/projectdavid/commit/a1b398941a8d5cecb3a3ad10f37adcd5e8a03146))

# [1.63.0](https://github.com/project-david-ai/projectdavid/compare/v1.62.1...v1.63.0) (2026-02-25)


### Features

* add ToolInterceptEvent pipeline and execute_delegated_action for worker tool handling ([e5e28ff](https://github.com/project-david-ai/projectdavid/commit/e5e28ff1d875372b05fd6e5c0b50aae9a35ae30c))

## [1.62.1](https://github.com/project-david-ai/projectdavid/compare/v1.62.0...v1.62.1) (2026-02-25)


### Bug Fixes

* wire ToolInterceptEvent through _map_chunk_to_event pipeline ([942dbef](https://github.com/project-david-ai/projectdavid/commit/942dbef919eb6b46732fc7f261cc3010855a96b0))

# [1.62.0](https://github.com/project-david-ai/projectdavid/compare/v1.61.1...v1.62.0) (2026-02-25)


### Features

* add ToolInterceptEvent for delegated worker tool call visibility ([80a6a02](https://github.com/project-david-ai/projectdavid/commit/80a6a02c7039ad914e04d189fad9aadd6ed68502))

## [1.61.1](https://github.com/project-david-ai/projectdavid/compare/v1.61.0...v1.61.1) (2026-02-25)


### Bug Fixes

* prevent thread-id bleed between concurrent requests ([8ef4b98](https://github.com/project-david-ai/projectdavid/commit/8ef4b98efc79b65ad561a7e220f2dd79256320dc))

# [1.61.0](https://github.com/project-david-ai/projectdavid/compare/v1.60.3...v1.61.0) (2026-02-25)


### Features

* Update to projectdavid_common==0.30.0 ([d8344b2](https://github.com/project-david-ai/projectdavid/commit/d8344b297aa9c756a93a9445a9d88dcd80361f4e))

## [1.60.3](https://github.com/project-david-ai/projectdavid/compare/v1.60.2...v1.60.3) (2026-02-25)


### Bug Fixes

* scope platform-side inventory lookups to the owning user ([348b510](https://github.com/project-david-ai/projectdavid/commit/348b510cda1f1fa9d98bbe6c31d4be6b87cf3a3f))

## [1.60.2](https://github.com/project-david-ai/projectdavid/compare/v1.60.1...v1.60.2) (2026-02-24)


### Bug Fixes

* Update to projectdavid_common==0.29.1 ([2e143d8](https://github.com/project-david-ai/projectdavid/commit/2e143d8e463b02d75d00c770faca0c5a96fc85b5))

## [1.60.1](https://github.com/project-david-ai/projectdavid/compare/v1.60.0...v1.60.1) (2026-02-24)


### Bug Fixes

* scope network inventory to user_id instead of assistant_id ([a04d555](https://github.com/project-david-ai/projectdavid/commit/a04d555281dc776a5fcd5ce5eb79b45f00712900))

# [1.60.0](https://github.com/project-david-ai/projectdavid/compare/v1.59.0...v1.60.0) (2026-02-24)


### Features

* bridge client and service layers for inventory tools ([2b8a961](https://github.com/project-david-ai/projectdavid/commit/2b8a96188230f14b045e4b87df7df3aa64bee897))

# [1.59.0](https://github.com/project-david-ai/projectdavid/compare/v1.58.0...v1.59.0) (2026-02-24)


### Bug Fixes

* NetworkDeviceHandler ([3aff2aa](https://github.com/project-david-ai/projectdavid/commit/3aff2aa9775d15450ad6ac84db05173e8ccde5a4))


### Features

* introduce zero-trust NetworkDeviceHandler with local Store & Slice ([04903e1](https://github.com/project-david-ai/projectdavid/commit/04903e181176592517ea2dd16ea3c1d9518d7e4f))

# [1.58.0](https://github.com/project-david-ai/projectdavid/compare/v1.57.0...v1.58.0) (2026-02-24)


### Features

* support engineer flag in AssistantsClient create_assistant method ([5e52d27](https://github.com/project-david-ai/projectdavid/commit/5e52d27c44f7d5b790929b6f93fa88423116dfb0))

# [1.57.0](https://github.com/project-david-ai/projectdavid/compare/v1.56.3...v1.57.0) (2026-02-24)


### Features

* Implement Engineering events ([a22a286](https://github.com/project-david-ai/projectdavid/commit/a22a286b991ffb7de43170eb2afb37ba9d52ca96))

## [1.56.3](https://github.com/project-david-ai/projectdavid/compare/v1.56.2...v1.56.3) (2026-02-23)


### Bug Fixes

* Update to projectdavid_common==0.27.1 ([7eba0c0](https://github.com/project-david-ai/projectdavid/commit/7eba0c003b581f6c873eb5243947a2a1c50e5f5b))

## [1.56.2](https://github.com/project-david-ai/projectdavid/compare/v1.56.1...v1.56.2) (2026-02-23)


### Bug Fixes

* Update to projectdavid_common==0.27.1 ([3f25f90](https://github.com/project-david-ai/projectdavid/commit/3f25f902dc3f1b593f55f4bfc282764b539c7e9c))

## [1.56.1](https://github.com/project-david-ai/projectdavid/compare/v1.56.0...v1.56.1) (2026-02-23)


### Bug Fixes

* remove provider from stream_inference_response ([b65b64e](https://github.com/project-david-ai/projectdavid/commit/b65b64eefc983107cd76633a0126857f5af14120))

# [1.56.0](https://github.com/project-david-ai/projectdavid/compare/v1.55.0...v1.56.0) (2026-02-23)


### Features

* remove provider from the inference_client.py payload. It is not needed for endpoint routing. ([9b63f79](https://github.com/project-david-ai/projectdavid/commit/9b63f79ba66fdbeeb13ab49754a4958ebb49bd43))

# [1.55.0](https://github.com/project-david-ai/projectdavid/compare/v1.54.9...v1.55.0) (2026-02-23)


### Features

* remove provider from the inference_client.py payload. It is not needed for endpoint routing. ([4d0829c](https://github.com/project-david-ai/projectdavid/commit/4d0829ce7a54ab147e7c6a39fcacc873786e41bc))

## [1.54.9](https://github.com/project-david-ai/projectdavid/compare/v1.54.8...v1.54.9) (2026-02-22)


### Bug Fixes

* propagate assistant_id through event stream ([497b5f6](https://github.com/project-david-ai/projectdavid/commit/497b5f64ccc9bc13a36b2c52fddeab5af1c974ac))

## [1.54.8](https://github.com/project-david-ai/projectdavid/compare/v1.54.7...v1.54.8) (2026-02-21)


### Bug Fixes

* correct stale type discriminators in get_event_type mapping ([285b3e1](https://github.com/project-david-ai/projectdavid/commit/285b3e10586f5d747c5859b5068eea04d4edb31e))

## [1.54.7](https://github.com/project-david-ai/projectdavid/compare/v1.54.6...v1.54.7) (2026-02-21)


### Bug Fixes

* narrow ScratchpadEvent routing to scratchpad_status type only ([935e236](https://github.com/project-david-ai/projectdavid/commit/935e2361b4e27e81025a16526b0355bc4a2b53ca))

## [1.54.6](https://github.com/project-david-ai/projectdavid/compare/v1.54.5...v1.54.6) (2026-02-21)


### Bug Fixes

* unwrap double-encoded mixin JSON and extract delegation payloads ([05c1e7b](https://github.com/project-david-ai/projectdavid/commit/05c1e7b684013d24802c45de9b0b20f680fb8aeb))

## [1.54.5](https://github.com/project-david-ai/projectdavid/compare/v1.54.4...v1.54.5) (2026-02-21)


### Bug Fixes

* remove redundant scratchpad event routing blocks ([6214e7c](https://github.com/project-david-ai/projectdavid/commit/6214e7c8c696029ec0e17db288e3887b7de011c9))
* resolve missing 'operation' argument in ScratchpadEvent ([76f8109](https://github.com/project-david-ai/projectdavid/commit/76f81095760dfb5cd7b4ba6e1020ff2f5dab513e))

## [1.54.4](https://github.com/project-david-ai/projectdavid/compare/v1.54.3...v1.54.4) (2026-02-21)


### Bug Fixes

* add src/projectdavid/events.py ([cf88ffb](https://github.com/project-david-ai/projectdavid/commit/cf88ffba7a1632569633d0ae5c2755144231d307))

## [1.54.3](https://github.com/project-david-ai/projectdavid/compare/v1.54.2...v1.54.3) (2026-02-21)


### Bug Fixes

* correct activity event routing — scratchpad ops were misrouted to ResearchStatusEvent ([8658203](https://github.com/project-david-ai/projectdavid/commit/865820340936787531daa02c4743bbece4cf9936))

## [1.54.2](https://github.com/frankie336/projectdavid/compare/v1.54.1...v1.54.2) (2026-02-20)


### Bug Fixes

* rename content event type discriminator to 'web_status' / 'research_status' ([ea5e0ff](https://github.com/frankie336/projectdavid/commit/ea5e0ff3a0d1430f433dcaed496cb2af53735f04))

## [1.54.1](https://github.com/frankie336/projectdavid/compare/v1.54.0...v1.54.1) (2026-02-20)


### Bug Fixes

* standardise WebEvent emission across backend, SDK, and frontend ([9eb43d8](https://github.com/frankie336/projectdavid/commit/9eb43d88750d46bb168d1d46e294da9d09d5664e))

# [1.54.0](https://github.com/frankie336/projectdavid/compare/v1.53.2...v1.54.0) (2026-02-19)


### Features

* Implement full-stack real-time Scratchpad visualization ([2bfdf50](https://github.com/frankie336/projectdavid/commit/2bfdf50a100069547b6d8fb125e2fb950d575efd))

## [1.53.2](https://github.com/frankie336/projectdavid/compare/v1.53.1...v1.53.2) (2026-02-17)


### Bug Fixes

* make base64_data optional ([620722a](https://github.com/frankie336/projectdavid/commit/620722a9d1884557bf86ee03a7393033e26a0273))

## [1.53.1](https://github.com/frankie336/projectdavid/compare/v1.53.0...v1.53.1) (2026-02-17)


### Bug Fixes

* add url to the CodeExecutionGeneratedFileEvent signature ([14d60eb](https://github.com/frankie336/projectdavid/commit/14d60eb7970de20cff36c5a6c61bba861b11e4fc))

# [1.53.0](https://github.com/frankie336/projectdavid/compare/v1.52.0...v1.53.0) (2026-02-14)


### Features

* update delete_assistant to support permanent deletion ([ee51e75](https://github.com/frankie336/projectdavid/commit/ee51e75c94bfbb8b501aa4d7af18ede3cc81f38c))

# [1.52.0](https://github.com/frankie336/projectdavid/compare/v1.51.2...v1.52.0) (2026-02-13)


### Features

* Add ResearchStatusEvent for user-visible progress updates ([21b5bc4](https://github.com/frankie336/projectdavid/commit/21b5bc4dd1ed3dbd3f5a6865dcde957968171409))

## [1.51.2](https://github.com/frankie336/projectdavid/compare/v1.51.1...v1.51.2) (2026-02-13)


### Bug Fixes

* Update to projectdavid_common==0.27.0 ([5e83aed](https://github.com/frankie336/projectdavid/commit/5e83aed075e0f3388d1161d27c6f8cc033e95a66))

## [1.51.1](https://github.com/frankie336/projectdavid/compare/v1.51.0...v1.51.1) (2026-02-12)


### Bug Fixes

* Resolve global loop issues. ([7277b27](https://github.com/frankie336/projectdavid/commit/7277b27c8a3ccd543ed3420a846e03e334c9a84c))

# [1.51.0](https://github.com/frankie336/projectdavid/compare/v1.50.0...v1.51.0) (2026-02-12)


### Bug Fixes

* delete vision-file_processor.py  llm synth ([b1a9831](https://github.com/frankie336/projectdavid/commit/b1a9831d3f2e367d2534fe62a86c62549917b161))
* Remove ollama from dependencies ([607fe6d](https://github.com/frankie336/projectdavid/commit/607fe6d0cb94d721a4244f9fa487c832c82dca57))


### Features

* Add deep_research toggle to assistants_client.py ([9911119](https://github.com/frankie336/projectdavid/commit/9911119e199abbab21639fe9955dead9662197e5))
* Add deep_research toggle to assistants_client.py ([106ee2e](https://github.com/frankie336/projectdavid/commit/106ee2e452efb7dfb1e2ee3491316686ac2528f2))

# [1.50.0](https://github.com/frankie336/projectdavid/compare/v1.49.3...v1.50.0) (2026-02-11)


### Features

* Implement deep research tools endpoints ([be98bce](https://github.com/frankie336/projectdavid/commit/be98bce6dcff8f1099c448fdc9656c041f32a4e1))

## [1.49.3](https://github.com/frankie336/projectdavid/compare/v1.49.2...v1.49.3) (2026-02-11)


### Bug Fixes

* properly map Web Tool status events in inference stream ([a224b9e](https://github.com/frankie336/projectdavid/commit/a224b9ea31b691248555c529e5b346cda99b971f))

## [1.49.2](https://github.com/frankie336/projectdavid/compare/v1.49.1...v1.49.2) (2026-02-10)


### Bug Fixes

* properly map Web Tool status events in inference stream ([4ed9000](https://github.com/frankie336/projectdavid/commit/4ed9000498828e828cf52c92d2d434ae721c689a))

## [1.49.1](https://github.com/frankie336/projectdavid/compare/v1.49.0...v1.49.1) (2026-02-10)


### Bug Fixes

* Update projectdavid_common package to  projectdavid-common 0.25.0 ([2815ef0](https://github.com/frankie336/projectdavid/commit/2815ef00f7a2900cdf506ffd580b8808217ebb80))

# [1.49.0](https://github.com/frankie336/projectdavid/compare/v1.48.0...v1.49.0) (2026-02-10)


### Features

*  Add web search status events to event manager. ([d245e11](https://github.com/frankie336/projectdavid/commit/d245e115690cee82799c6d4e90ee380276f27c78))

# [1.48.0](https://github.com/frankie336/projectdavid/compare/v1.47.5...v1.48.0) (2026-02-10)


### Features

*  Implement projectdavid.EngineerClient ([770e8b2](https://github.com/frankie336/projectdavid/commit/770e8b23cc217a9f57f5fa446392383063c44e4e))

## [1.47.5](https://github.com/frankie336/projectdavid/compare/v1.47.4...v1.47.5) (2026-02-09)


### Bug Fixes

* instantiate LoggingUtility in ToolsClient to fix AttributeError ([1c90f2a](https://github.com/frankie336/projectdavid/commit/1c90f2a0c35f109cd662f12a4e356e91d8f56534))

## [1.47.4](https://github.com/frankie336/projectdavid/compare/v1.47.3...v1.47.4) (2026-02-08)


### Bug Fixes

* Update to projectdavid_common==0.23.1 ([b3a106e](https://github.com/frankie336/projectdavid/commit/b3a106ef54df0dbe2c7a448fda98228f8bf4fcfc))

## [1.47.3](https://github.com/frankie336/projectdavid/compare/v1.47.2...v1.47.3) (2026-02-08)


### Bug Fixes

* Client update issues ([2ef6423](https://github.com/frankie336/projectdavid/commit/2ef642323cf4316ab3c5586d414b1bd1c54b1ad5))

## [1.47.2](https://github.com/frankie336/projectdavid/compare/v1.47.1...v1.47.2) (2026-02-08)


### Bug Fixes

* from projectdavid_common.utilities.logging_service import LoggingUtility ([633c24a](https://github.com/frankie336/projectdavid/commit/633c24a063f5d090b9a85096eb6f41a18610474d))

## [1.47.1](https://github.com/frankie336/projectdavid/compare/v1.47.0...v1.47.1) (2026-02-07)


### Bug Fixes

* Expose self._computer_client ([48d1c04](https://github.com/frankie336/projectdavid/commit/48d1c0454d1d36e7f79cc127631e800918b7082e))

# [1.47.0](https://github.com/frankie336/projectdavid/compare/v1.46.3...v1.47.0) (2026-02-07)


### Features

* Create Computer client. ([c1a2ed7](https://github.com/frankie336/projectdavid/commit/c1a2ed71d8fecc974221458ef61d1364c5755f02))

## [1.46.3](https://github.com/frankie336/projectdavid/compare/v1.46.2...v1.46.3) (2026-02-07)


### Bug Fixes

* Expose tools client ([735a1c1](https://github.com/frankie336/projectdavid/commit/735a1c1ff811f451ac580e3fcf37ccd8ddd6287f))
* Expose tools client ([280d470](https://github.com/frankie336/projectdavid/commit/280d4706ebb572a740858198c66282cedafe332e))
* Expose tools client ([9b7e2d7](https://github.com/frankie336/projectdavid/commit/9b7e2d728ce9dcea571ee5bb2149d328486eccb7))

## [1.46.2](https://github.com/frankie336/projectdavid/compare/v1.46.1...v1.46.2) (2026-02-07)


### Bug Fixes

* update to project_david_common 0.23.0 ([58954e1](https://github.com/frankie336/projectdavid/commit/58954e181b865a9efbc73d30d9331e49ab01afc8))

## [1.46.1](https://github.com/frankie336/projectdavid/compare/v1.46.0...v1.46.1) (2026-02-07)


### Bug Fixes

* update to project_david_common 0.23.0 ([ee3d340](https://github.com/frankie336/projectdavid/commit/ee3d340fa5e28f68d732b04d38f09ba5e824ce56))

# [1.46.0](https://github.com/frankie336/projectdavid/compare/v1.45.0...v1.46.0) (2026-02-07)


### Features

* implement ToolsClient for agentic interaction wi th platform tools. ([9c85f05](https://github.com/frankie336/projectdavid/commit/9c85f05d132cba115330c705f4ffb35a9b233281))

# [1.45.0](https://github.com/frankie336/projectdavid/compare/v1.44.2...v1.45.0) (2026-02-05)


### Features

* Add new agentic params to Assistants.Create ([bd61123](https://github.com/frankie336/projectdavid/commit/bd611233e4622c5acc4ce393b82bc1c461764323))

## [1.44.2](https://github.com/frankie336/projectdavid/compare/v1.44.1...v1.44.2) (2026-02-05)


### Bug Fixes

* Closing the Loop: When execute() is called, the tool_call_id is now passed down to the execute_pending_action method ([dac09f2](https://github.com/frankie336/projectdavid/commit/dac09f2380fe9ebbf2701509d2db3ca10451df1e))

## [1.44.1](https://github.com/frankie336/projectdavid/compare/v1.44.0...v1.44.1) (2026-02-04)


### Bug Fixes

* Expose PlanEvent ([5917f0d](https://github.com/frankie336/projectdavid/commit/5917f0deb8ca6aa544a651adfdbe4688f164602f))

# [1.44.0](https://github.com/frankie336/projectdavid/compare/v1.43.3...v1.44.0) (2026-02-04)


### Features

* Add PlanEvent to event handler ([45d1840](https://github.com/frankie336/projectdavid/commit/45d1840a92fa4d3f916671f63e8298b5a61dc476))

## [1.43.3](https://github.com/frankie336/projectdavid/compare/v1.43.2...v1.43.3) (2026-02-04)


### Bug Fixes

* Remove user_id from synchronous interface set up ([5dfd1d0](https://github.com/frankie336/projectdavid/commit/5dfd1d08fe4e235e5550815e20df9fbea66c05b7))

## [1.43.2](https://github.com/frankie336/projectdavid/compare/v1.43.1...v1.43.2) (2026-02-03)


### Bug Fixes

* Provide the assistant with error handling hints. ([ba463d6](https://github.com/frankie336/projectdavid/commit/ba463d657ca431b46fa229cab1b8cb1d1f6534f6))

## [1.43.1](https://github.com/frankie336/projectdavid/compare/v1.43.0...v1.43.1) (2026-02-03)


### Bug Fixes

* add assistants_client=self.assistants  param to main interface ([c65826f](https://github.com/frankie336/projectdavid/commit/c65826f56df983e04e6149084cb0cbdfd7987055))

# [1.43.0](https://github.com/frankie336/projectdavid/compare/v1.42.0...v1.43.0) (2026-02-03)


### Features

* Implement level 2 function calling validation and recovery. ([c898a9c](https://github.com/frankie336/projectdavid/commit/c898a9c3d59dff835ba898542d598fadb0809d7e))

# [1.42.0](https://github.com/frankie336/projectdavid/compare/v1.41.15...v1.42.0) (2026-02-03)


### Bug Fixes

* Asynchronous client updates. ([4a817a9](https://github.com/frankie336/projectdavid/commit/4a817a93d3c5e6987ee2a874c50d4e914846a4d5))
* Asynchronous client updates. ([b00f994](https://github.com/frankie336/projectdavid/commit/b00f9944f2c8cae0bcce41b16ea6902cea5a95fd))
* Asynchronous client updates. ([d5089a5](https://github.com/frankie336/projectdavid/commit/d5089a5d669faffbb9d40dcd2a0d16f1303a2153))


### Features

* Implement level 2, phase 1 recursive inference calls that handles subsequent turns during function calls. ([3db90a8](https://github.com/frankie336/projectdavid/commit/3db90a8ee87b429f417fba0c0b117555ed0b95f4))
* Implement level 2, phase 1 recursive inference calls that handles subsequent turns during function calls. ([15b9740](https://github.com/frankie336/projectdavid/commit/15b9740e4b403619ecf4993a25bd32fc36fc89b8))

## [1.41.15](https://github.com/frankie336/projectdavid/compare/v1.41.14...v1.41.15) (2026-02-01)


### Bug Fixes

* update to projectdavid_common==0.21.9 ([ca6235f](https://github.com/frankie336/projectdavid/commit/ca6235fa1aae606473b938d0598835327efec412))

## [1.41.14](https://github.com/frankie336/projectdavid/compare/v1.41.13...v1.41.14) (2026-01-31)


### Bug Fixes

* Add decision signature and payload to Actions.create_action ([c2b7d6c](https://github.com/frankie336/projectdavid/commit/c2b7d6c764b07716a3d17c9c1ea538fb5c2ee404))

## [1.41.13](https://github.com/frankie336/projectdavid/compare/v1.41.12...v1.41.13) (2026-01-31)


### Bug Fixes

* Expose: DecisionEvent ([0df02e7](https://github.com/frankie336/projectdavid/commit/0df02e701d1d870e3c995971102405eb3ba927f0))

## [1.41.12](https://github.com/frankie336/projectdavid/compare/v1.41.11...v1.41.12) (2026-01-31)


### Bug Fixes

* Add DecisionEvent to event management ([5e21612](https://github.com/frankie336/projectdavid/commit/5e21612c0ce6dfab97fd0bd3824a873e08ab48f0))

## [1.41.11](https://github.com/frankie336/projectdavid/compare/v1.41.10...v1.41.11) (2026-01-29)


### Bug Fixes

* Update to projectdavid_common==0.21.7 ([08ef2de](https://github.com/frankie336/projectdavid/commit/08ef2dea336b31e1cfdcd7f9acb4633e5dd38df4))

## [1.41.10](https://github.com/frankie336/projectdavid/compare/v1.41.9...v1.41.10) (2026-01-29)


### Bug Fixes

*  SDK is performing Legacy Tool Accumulation (client-side reconstruction) simultaneously with handling the new Tool Call Manifest events from the server. ([b47ea41](https://github.com/frankie336/projectdavid/commit/b47ea41e0f0adf4c524fcb3b678267b5dd01566e))

## [1.41.9](https://github.com/frankie336/projectdavid/compare/v1.41.8...v1.41.9) (2026-01-29)


### Bug Fixes

*  implement typed json streams in event based streaming. ([98fd4e5](https://github.com/frankie336/projectdavid/commit/98fd4e5fd29ff3463afd9ed67607b48e06ebef5a))

## [1.41.8](https://github.com/frankie336/projectdavid/compare/v1.41.7...v1.41.8) (2026-01-28)


### Bug Fixes

*  simplify: execute_pending_action ([2037f0b](https://github.com/frankie336/projectdavid/commit/2037f0b79fd8c7d2d063cf02a897b2fb83bc003f))

## [1.41.7](https://github.com/frankie336/projectdavid/compare/v1.41.6...v1.41.7) (2026-01-28)


### Bug Fixes

*  action_id is present, we completely ignore get_pending_actions. ([6716573](https://github.com/frankie336/projectdavid/commit/67165739ee01676e1f6eed20ee4f594773f5480d))

## [1.41.6](https://github.com/frankie336/projectdavid/compare/v1.41.5...v1.41.6) (2026-01-28)


### Bug Fixes

*  update RunsClient.execute_pending_action method to accept the action_id and tool_name that the event system is now passing to it. ([fc2c595](https://github.com/frankie336/projectdavid/commit/fc2c5956290170d1b86f600c8f66437b7c099c38))

## [1.41.5](https://github.com/frankie336/projectdavid/compare/v1.41.4...v1.41.5) (2026-01-28)


### Bug Fixes

* Resolve race condition by yielding manifest_chunk which contains the action id after the action has been entered into the main db ([1b716b0](https://github.com/frankie336/projectdavid/commit/1b716b0b338306d93ee3d22156226e2b0f670111))

## [1.41.4](https://github.com/frankie336/projectdavid/compare/v1.41.3...v1.41.4) (2026-01-28)


### Bug Fixes

* Resolve race condition in function call event handler ([c829df4](https://github.com/frankie336/projectdavid/commit/c829df42698bf58c4f12a21a002b97925b7a0e0a))

## [1.41.3](https://github.com/frankie336/projectdavid/compare/v1.41.2...v1.41.3) (2026-01-28)


### Bug Fixes

* Add an Event for shell output. ([f99a130](https://github.com/frankie336/projectdavid/commit/f99a130e10169e087aff1fdc87cd437d471374ac))
* Add an Event for shell output. ([9bf3e21](https://github.com/frankie336/projectdavid/commit/9bf3e2177d32bcc881368666d631b7cf54c0e513))

## [1.41.2](https://github.com/frankie336/projectdavid/compare/v1.41.1...v1.41.2) (2026-01-28)


### Bug Fixes

* Add an Event for shell output. ([c73124e](https://github.com/frankie336/projectdavid/commit/c73124e95cf344ac6ea627b55980a6e5a915ec5d))

## [1.41.1](https://github.com/frankie336/projectdavid/compare/v1.41.0...v1.41.1) (2026-01-28)


### Bug Fixes

* integrate events wrapper into entities main interface ([e2f8700](https://github.com/frankie336/projectdavid/commit/e2f870040a8b0b23369023f543a5ccb7bbc9cab9))

# [1.41.0](https://github.com/frankie336/projectdavid/compare/v1.40.0...v1.41.0) (2026-01-28)


### Features

* Add events wrapper and stream generator to synchronous_inference_wrapper ([0ec1308](https://github.com/frankie336/projectdavid/commit/0ec1308d007b700d9b31616d2d1e7e5c1d4a2a5d))

# [1.40.0](https://github.com/frankie336/projectdavid/compare/v1.39.11...v1.40.0) (2026-01-28)


### Features

* Implement execute_pending_action method. This eliminates the need for client side consumers to poll for pending actions before execution. Increases speed of function call handling, and cuts down on churn. ([385e977](https://github.com/frankie336/projectdavid/commit/385e977851d5b3558a03c39b47a17ebffe7e8eea))

## [1.39.11](https://github.com/frankie336/projectdavid/compare/v1.39.10...v1.39.11) (2026-01-27)


### Bug Fixes

* cutting back to unvalidated return from poll_and_execute_action ([9e24438](https://github.com/frankie336/projectdavid/commit/9e24438b1503819ac7c89ce2e4b879a5e0db7504))

## [1.39.10](https://github.com/frankie336/projectdavid/compare/v1.39.9...v1.39.10) (2026-01-27)


### Bug Fixes

* Return pydentic model objects from get_runs ([95407f9](https://github.com/frankie336/projectdavid/commit/95407f960d40e3b8df3dce37d2f04538d8f352e8))

## [1.39.9](https://github.com/frankie336/projectdavid/compare/v1.39.8...v1.39.9) (2026-01-25)


### Bug Fixes

* reverting streaming changes ([7573d70](https://github.com/frankie336/projectdavid/commit/7573d70169352528493f0e8ba514f90c31e0c6de))

## [1.39.8](https://github.com/frankie336/projectdavid/compare/v1.39.7...v1.39.8) (2026-01-25)


### Bug Fixes

* Persistent Connection Pooling (The TTFT Killer) ([177c43d](https://github.com/frankie336/projectdavid/commit/177c43dde076f95f05e9f09eda128759214d6420))

## [1.39.7](https://github.com/frankie336/projectdavid/compare/v1.39.6...v1.39.7) (2026-01-25)


### Bug Fixes

* upgrade to projectdavid_common==0.21.5 / Remove tools_client.py ([cb1ba35](https://github.com/frankie336/projectdavid/commit/cb1ba355c94d5769fbb3671effcf48ad9488ca56))

## [1.39.6](https://github.com/frankie336/projectdavid/compare/v1.39.5...v1.39.6) (2026-01-25)


### Bug Fixes

* upgrade to projectdavid_common==0.21.4 / Remove tools_client.py ([d8ede8b](https://github.com/frankie336/projectdavid/commit/d8ede8bb16f5a49a593bf109a6b5a975f19a83cf))

## [1.39.5](https://github.com/frankie336/projectdavid/compare/v1.39.4...v1.39.5) (2026-01-25)


### Bug Fixes

* upgrade to projectdavid_common==0.21.3 ([00985ab](https://github.com/frankie336/projectdavid/commit/00985ab81ba71f945675fd8f91a281272ab2b1f0))

## [1.39.4](https://github.com/frankie336/projectdavid/compare/v1.39.3...v1.39.4) (2026-01-24)


### Bug Fixes

* upgrade to projectdavid_common==0.21.2 ([7c5b414](https://github.com/frankie336/projectdavid/commit/7c5b4142585dda3f7e0f3164a442c56028d79c08))

## [1.39.3](https://github.com/frankie336/projectdavid/compare/v1.39.2...v1.39.3) (2026-01-20)


### Bug Fixes

* Add tool_call_id param to poll_and_execute_action ([b7ac9c4](https://github.com/frankie336/projectdavid/commit/b7ac9c45b38762021380eecb09abf903085fd6e1))

## [1.39.2](https://github.com/frankie336/projectdavid/compare/v1.39.1...v1.39.2) (2026-01-20)


### Bug Fixes

* update to projectdavid_common==0.21.1 ([4fad973](https://github.com/frankie336/projectdavid/commit/4fad973a49fa93792bcb76d0eb3ce770f1311560))
* update to projectdavid_common==0.21.1 ([83faf8e](https://github.com/frankie336/projectdavid/commit/83faf8e9f3391646957bd127500555fb981f7d23))

## [1.39.1](https://github.com/frankie336/projectdavid/compare/v1.39.0...v1.39.1) (2026-01-19)


### Bug Fixes

* Add tool_call_id to actions_client.py ([1f7dffd](https://github.com/frankie336/projectdavid/commit/1f7dffd411be5d1a6cbb15d76117ba586796cf10))
* Add tool_call_id to actions_client.py ([c4d5821](https://github.com/frankie336/projectdavid/commit/c4d58217149bd1fbd53207c746f8f75bb6dbe654))

# [1.39.0](https://github.com/frankie336/projectdavid/compare/v1.38.1...v1.39.0) (2026-01-17)


### Features

* Implement 0.20.0 projectdavid_common==0.20.0 ([589939b](https://github.com/frankie336/projectdavid/commit/589939b926768faa1617a80c30069a51ddedcdac))
* removed unused imports ([743e5c2](https://github.com/frankie336/projectdavid/commit/743e5c21f8b25ef8d9d76f90497ed889bae5e3a0))

## [1.38.1](https://github.com/frankie336/projectdavid/compare/v1.38.0...v1.38.1) (2026-01-17)


### Bug Fixes

* implement explicit action lifecycle management and tool error reporting ([d84a59b](https://github.com/frankie336/projectdavid/commit/d84a59bd5c172f95248f529345e2c2ea7651d1b4))

# [1.38.0](https://github.com/frankie336/projectdavid/compare/v1.37.1...v1.38.0) (2026-01-15)


### Features

* cutting back to full fat version. ([9473363](https://github.com/frankie336/projectdavid/commit/9473363167c476501be59958184f5a9b983e566f))

## [1.37.1](https://github.com/frankie336/projectdavid/compare/v1.37.0...v1.37.1) (2026-01-15)


### Bug Fixes

* Implementing light weight projectdavid ([134459d](https://github.com/frankie336/projectdavid/commit/134459d21bd0969175595d1bf565d988882724a3))
* Implementing light weight projectdavid ([6f5548b](https://github.com/frankie336/projectdavid/commit/6f5548b965c764f7f48fd4bd436eb3da114d5b20))

# [1.37.0](https://github.com/frankie336/projectdavid/compare/v1.36.1...v1.37.0) (2026-01-14)


### Features

* **sdk:** refactor streaming logic into a single-pass state machine ([8088dba](https://github.com/frankie336/projectdavid/commit/8088dba46865330ae66a6098dc9eaa1bb85d2282))
* **sdk:** refactor streaming logic into a single-pass state machine ([afd24b7](https://github.com/frankie336/projectdavid/commit/afd24b7918bc9487db0fdb9ffa34855a23a3a87e))

## [1.36.1](https://github.com/frankie336/projectdavid/compare/v1.36.0...v1.36.1) (2025-10-15)


### Bug Fixes

* Correctly handle optional truncation_strategy in run creation ([ef10d2e](https://github.com/frankie336/projectdavid/commit/ef10d2e67ca13f04feb3b87edf3c956cf0a91e0c))

# [1.36.0](https://github.com/frankie336/projectdavid/compare/v1.35.0...v1.36.0) (2025-10-14)


### Features

* **deps:** bump projectdavid_common; align Runs schema + client ([f70d5fc](https://github.com/frankie336/projectdavid/commit/f70d5fcc0164037b78ac0c14d325a5f30d4daa07))

# [1.35.0](https://github.com/frankie336/projectdavid/compare/v1.34.13...v1.35.0) (2025-10-13)


### Features

* **deps:** bump projectdavid_common; align Runs schema + client ([23d525e](https://github.com/frankie336/projectdavid/commit/23d525e10a8dd3a4ee39fb3c0e7c0be42832e1a7))

## [1.34.13](https://github.com/frankie336/projectdavid/compare/v1.34.12...v1.34.13) (2025-09-30)


### Bug Fixes

* correct projectdavid_common==0.17.19 ([1a72e36](https://github.com/frankie336/projectdavid/commit/1a72e368ab0228f26c3dae08be0cc9a0b4edfcbe))

## [1.34.12](https://github.com/frankie336/projectdavid/compare/v1.34.11...v1.34.12) (2025-09-30)


### Bug Fixes

* correct projectdavid_common==0.17.19 ([d636c31](https://github.com/frankie336/projectdavid/commit/d636c31066e33bce0332df2538093040ae36f40f))
* set truncation strategy to auto ([3d00a38](https://github.com/frankie336/projectdavid/commit/3d00a383eb688a51f9d8bbfc66b0a47e52e86b2a))
* set truncation strategy to auto ([357ec09](https://github.com/frankie336/projectdavid/commit/357ec09bc34ca36d837cae4e279e740074d9756d))

## [1.34.11](https://github.com/frankie336/projectdavid/compare/v1.34.10...v1.34.11) (2025-08-25)


### Bug Fixes

* set tool choice default from 'None' --> None ([0288eb3](https://github.com/frankie336/projectdavid/commit/0288eb30ac173b2fc7323158454a726da7883c81))
* set tool choice default from 'None' --> None ([dd172b5](https://github.com/frankie336/projectdavid/commit/dd172b5a0d1f08a2aa7ccb1714141f80e2954130))

## [1.34.10](https://github.com/frankie336/projectdavid/compare/v1.34.9...v1.34.10) (2025-08-22)


### Bug Fixes

* remove redundant epoch helper ([e53c074](https://github.com/frankie336/projectdavid/commit/e53c074f2c50e39bc44ceec911acb42dc9dcc930))

## [1.34.9](https://github.com/frankie336/projectdavid/compare/v1.34.8...v1.34.9) (2025-08-22)


### Bug Fixes

* remove redundant epoch helper ([4d2171a](https://github.com/frankie336/projectdavid/commit/4d2171a5cff841edd33b36027d5648c1d132ffbf))

## [1.34.8](https://github.com/frankie336/projectdavid/compare/v1.34.7...v1.34.8) (2025-08-22)


### Bug Fixes

* set incomplete_details type to string ([2af2d16](https://github.com/frankie336/projectdavid/commit/2af2d16843139884b9878edcd0c5b452a0e28e30))

## [1.34.7](https://github.com/frankie336/projectdavid/compare/v1.34.6...v1.34.7) (2025-08-21)


### Bug Fixes

* Normalize time stamps to epoch integer format instead of datetime. ([43af583](https://github.com/frankie336/projectdavid/commit/43af5830f80d9eafde694449d7119a2da8a8d127))

## [1.34.6](https://github.com/frankie336/projectdavid/compare/v1.34.5...v1.34.6) (2025-08-20)


### Bug Fixes

* epoch time on .create_run ([be013d4](https://github.com/frankie336/projectdavid/commit/be013d4e98724a2c252a7daa5b31bfda61253d15))

## [1.34.5](https://github.com/frankie336/projectdavid/compare/v1.34.4...v1.34.5) (2025-08-17)


### Bug Fixes

* Adding update_run ([10b1c6f](https://github.com/frankie336/projectdavid/commit/10b1c6f1b7da9f77d3bd7c9478edf8f1dc41fc82))

## [1.34.4](https://github.com/frankie336/projectdavid/compare/v1.34.3...v1.34.4) (2025-08-15)


### Bug Fixes

* Adding update_run ([ce98a68](https://github.com/frankie336/projectdavid/commit/ce98a688150c5073d1041815542012e486cf706e))

## [1.34.3](https://github.com/frankie336/projectdavid/compare/v1.34.2...v1.34.3) (2025-08-13)


### Bug Fixes

* rename list_all_runs and list_runs ([7efb822](https://github.com/frankie336/projectdavid/commit/7efb8220c82184df941fc897132ca3caa96d07a0))

## [1.34.2](https://github.com/frankie336/projectdavid/compare/v1.34.1...v1.34.2) (2025-08-13)


### Bug Fixes

* standard model ([8c8785b](https://github.com/frankie336/projectdavid/commit/8c8785babe81420ee211499a4d8972e8a42d5d2e))

## [1.34.1](https://github.com/frankie336/projectdavid/compare/v1.34.0...v1.34.1) (2025-08-13)


### Bug Fixes

* correctly import RunListResponse ([7f923cc](https://github.com/frankie336/projectdavid/commit/7f923ccfcaac890f1eaf0b94406f5ee003b2cf4e))

# [1.34.0](https://github.com/frankie336/projectdavid/compare/v1.33.33...v1.34.0) (2025-08-12)


### Features

* Adding runs list methods. ([61975b2](https://github.com/frankie336/projectdavid/commit/61975b2c8fa44de254b979160566bd8e89b6799b))

## [1.33.33](https://github.com/frankie336/projectdavid/compare/v1.33.32...v1.33.33) (2025-07-10)


### Bug Fixes

* wrap delete_message in a return envelope ([7ed1815](https://github.com/frankie336/projectdavid/commit/7ed18155b85d39cbecf0354c16b2a8a20131b9e2))
* wrap delete_message in a return envelope ([3e9e6fb](https://github.com/frankie336/projectdavid/commit/3e9e6fbb93ec0670c0e9a39b7eb446bcb1e7df40))

## [1.33.32](https://github.com/frankie336/projectdavid/compare/v1.33.31...v1.33.32) (2025-07-09)


### Bug Fixes

* use project_david_common 0.17.9 and refactor list_messages to use new envelope ([3fc565c](https://github.com/frankie336/projectdavid/commit/3fc565ce1f69af47fc102d5abd55f90a1fce2288))
* use project_david_common 0.17.9 and refactor list_messages to use new envelope ([3d802ef](https://github.com/frankie336/projectdavid/commit/3d802efc8cd0ec7425d0d1a1ead944c4d23d0838))
* use project_david_common 0.17.9 and refactor list_messages to use new envelope ([0549842](https://github.com/frankie336/projectdavid/commit/054984252097c9e843a12fed9a87eacea95aee33))

## [1.33.31](https://github.com/frankie336/projectdavid/compare/v1.33.30...v1.33.31) (2025-07-08)


### Bug Fixes

* update_thread ([2041347](https://github.com/frankie336/projectdavid/commit/2041347839922e2745d14e4ad9136f1aa797b254))

## [1.33.30](https://github.com/frankie336/projectdavid/compare/v1.33.29...v1.33.30) (2025-07-06)


### Bug Fixes

* Add DeleteThread schema2. ([de9fd17](https://github.com/frankie336/projectdavid/commit/de9fd17d81116c503ebda23d90d7cb031938b952))
* Add DeleteThread schema2. ([c43cdd6](https://github.com/frankie336/projectdavid/commit/c43cdd6c950847cb1a79e686848ca42d958126b9))
* Add DeleteThread schema2. ([0c4c548](https://github.com/frankie336/projectdavid/commit/0c4c54878d10d5535c4427481ebd32d7910b15f8))
* Add DeleteThread schema3. ([540c445](https://github.com/frankie336/projectdavid/commit/540c445829809e785dcab0b0dcd1600b0913ffcf))

## [1.33.29](https://github.com/frankie336/projectdavid/compare/v1.33.28...v1.33.29) (2025-07-06)


### Bug Fixes

* Add DeleteThread schema. ([d4f1270](https://github.com/frankie336/projectdavid/commit/d4f1270863fcefadc949e165125287a7b52e1ef6))

## [1.33.28](https://github.com/frankie336/projectdavid/compare/v1.33.27...v1.33.28) (2025-07-01)


### Bug Fixes

* remove platform_tools from assistant create method signature and payload. ([8caf3b0](https://github.com/frankie336/projectdavid/commit/8caf3b00f5d45422af9bda088ed266b9c39dddee))

## [1.33.27](https://github.com/frankie336/projectdavid/compare/v1.33.26...v1.33.27) (2025-06-30)


### Bug Fixes

* correct list method! ([bf17205](https://github.com/frankie336/projectdavid/commit/bf1720583f37cf09844a06c5c95f319ba5192d41))

## [1.33.26](https://github.com/frankie336/projectdavid/compare/v1.33.25...v1.33.26) (2025-06-30)


### Bug Fixes

* Remove platform_tools from request body ([01f79be](https://github.com/frankie336/projectdavid/commit/01f79be53bbe5b9e29c14c3757044a954c65711d))

## [1.33.25](https://github.com/frankie336/projectdavid/compare/v1.33.24...v1.33.25) (2025-06-28)


### Bug Fixes

* attempt to load api-key from client users .env file ([3bf2f26](https://github.com/frankie336/projectdavid/commit/3bf2f26506c8755adb510d7f6ed852e9aca47a46))

## [1.33.24](https://github.com/frankie336/projectdavid/compare/v1.33.23...v1.33.24) (2025-06-22)


### Bug Fixes

* Remove Kargs from FileProcessor() ([17a19b3](https://github.com/frankie336/projectdavid/commit/17a19b36f2275bc408b60333f4798b1a462fb96c))

## [1.33.23](https://github.com/frankie336/projectdavid/compare/v1.33.22...v1.33.23) (2025-06-17)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-17 ([db124a0](https://github.com/frankie336/projectdavid/commit/db124a0a5da8da045ef2e6edc01827252a0bad11))

## [1.33.22](https://github.com/frankie336/projectdavid/compare/v1.33.21...v1.33.22) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-16 ([bc3c298](https://github.com/frankie336/projectdavid/commit/bc3c298034ee40580ec4e92223782a9f2aee279f))

## [1.33.21](https://github.com/frankie336/projectdavid/compare/v1.33.20...v1.33.21) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-13 ([f43db04](https://github.com/frankie336/projectdavid/commit/f43db045d2c99be59586d7b0700f0a55f2efefd7))

## [1.33.20](https://github.com/frankie336/projectdavid/compare/v1.33.19...v1.33.20) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-11 ([a40b74e](https://github.com/frankie336/projectdavid/commit/a40b74ecadb38df56134d722c1edd000f9d06537))

## [1.33.19](https://github.com/frankie336/projectdavid/compare/v1.33.18...v1.33.19) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-8 ([5740d62](https://github.com/frankie336/projectdavid/commit/5740d6270d511a92b05a14105157c07c1f0be609))
* Back out from vision support - resource issue. Revisit in grand plan-9 ([421aba8](https://github.com/frankie336/projectdavid/commit/421aba8e8e1eef0fc6aa873b3686e660747172da))

## [1.33.18](https://github.com/frankie336/projectdavid/compare/v1.33.17...v1.33.18) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-5 ([cb68423](https://github.com/frankie336/projectdavid/commit/cb6842339dbef4efe0b579bafd9b6cbf677dd282))

## [1.33.17](https://github.com/frankie336/projectdavid/compare/v1.33.16...v1.33.17) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-4 ([61bbd6e](https://github.com/frankie336/projectdavid/commit/61bbd6e8bb2bf7213dd097bf7d4ba1af8e4aaff6))

## [1.33.16](https://github.com/frankie336/projectdavid/compare/v1.33.15...v1.33.16) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-3 ([14568e9](https://github.com/frankie336/projectdavid/commit/14568e97edef6e82fd93e3ee034fbf160d4a302b))

## [1.33.15](https://github.com/frankie336/projectdavid/compare/v1.33.14...v1.33.15) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan-2 ([a735034](https://github.com/frankie336/projectdavid/commit/a735034879ce50ce1dc2a508ce304796105f5830))

## [1.33.14](https://github.com/frankie336/projectdavid/compare/v1.33.13...v1.33.14) (2025-06-16)


### Bug Fixes

* Back out from vision support - resource issue. Revisit in grand plan ([3199ba7](https://github.com/frankie336/projectdavid/commit/3199ba7a18b3cfcc0f7306cd8748105f593a1836))

## [1.33.13](https://github.com/frankie336/projectdavid/compare/v1.33.12...v1.33.13) (2025-06-13)


### Bug Fixes

* restore code_interpreter_stream passthrough.14 ([df2a75f](https://github.com/frankie336/projectdavid/commit/df2a75f47a55d07d42af3a9949ef9bed4496a602))

## [1.33.12](https://github.com/frankie336/projectdavid/compare/v1.33.11...v1.33.12) (2025-06-13)


### Bug Fixes

* restore code_interpreter_stream passthrough.12 ([6c1fd4d](https://github.com/frankie336/projectdavid/commit/6c1fd4dafb5680cd7898f005e866b32c78e61ca1))

## [1.33.11](https://github.com/frankie336/projectdavid/compare/v1.33.10...v1.33.11) (2025-06-13)


### Bug Fixes

* restore code_interpreter_stream passthrough.11 ([57274ef](https://github.com/frankie336/projectdavid/commit/57274efea469b4cc513a2260202b4872f1ae64f2))

## [1.33.10](https://github.com/frankie336/projectdavid/compare/v1.33.9...v1.33.10) (2025-06-13)


### Bug Fixes

* restore code_interpreter_stream passthrough.10 ([54c084e](https://github.com/frankie336/projectdavid/commit/54c084ea6ef03d677b8e544db9afe9eff88266b5))

## [1.33.9](https://github.com/frankie336/projectdavid/compare/v1.33.8...v1.33.9) (2025-06-13)


### Bug Fixes

* restore code_interpreter_stream passthrough.9 ([98999d3](https://github.com/frankie336/projectdavid/commit/98999d3eca403d675d3cd8d54e2e59ec3f99f5a7))

## [1.33.8](https://github.com/frankie336/projectdavid/compare/v1.33.7...v1.33.8) (2025-06-12)


### Bug Fixes

* restore code_interpreter_stream passthrough.8 ([f5c7f61](https://github.com/frankie336/projectdavid/commit/f5c7f61cc43019d7af7f2524ce2c4fe4fd4da999))

## [1.33.7](https://github.com/frankie336/projectdavid/compare/v1.33.6...v1.33.7) (2025-06-12)


### Bug Fixes

* restore code_interpreter_stream passthrough.7 ([5998bca](https://github.com/frankie336/projectdavid/commit/5998bca1d3212004b05bf0036fd67af9ffd78ddc))

## [1.33.6](https://github.com/frankie336/projectdavid/compare/v1.33.5...v1.33.6) (2025-06-12)


### Bug Fixes

* restore code_interpreter_stream passthrough.3 ([8e87c6a](https://github.com/frankie336/projectdavid/commit/8e87c6aa2b9187a040148794f3bdd25aade753fb))

## [1.33.5](https://github.com/frankie336/projectdavid/compare/v1.33.4...v1.33.5) (2025-06-12)


### Bug Fixes

* restore code_interpreter_stream passthrough.2 ([16139a3](https://github.com/frankie336/projectdavid/commit/16139a31190aef846eaf114ad33df6bb740ff2a7))

## [1.33.4](https://github.com/frankie336/projectdavid/compare/v1.33.3...v1.33.4) (2025-06-12)


### Bug Fixes

* restore code_interpreter_stream passthrough. ([f598a06](https://github.com/frankie336/projectdavid/commit/f598a068ff523783d04f0bda5f97b79b2f4c5e40))

## [1.33.3](https://github.com/frankie336/projectdavid/compare/v1.33.2...v1.33.3) (2025-06-11)


### Bug Fixes

* Place vision features in dormant experimental mode with [@experimental](https://github.com/experimental) decorators.py ([1c41702](https://github.com/frankie336/projectdavid/commit/1c41702a55ec9c6c7ad89de559cfa309ace88174))

## [1.33.2](https://github.com/frankie336/projectdavid/compare/v1.33.1...v1.33.2) (2025-06-11)


### Bug Fixes

* pass file_processor_kwargs from public interface  and add default fallbacks. ([597b274](https://github.com/frankie336/projectdavid/commit/597b274e0f54fc87ac5449ac8259c8ad244b0214))

## [1.33.1](https://github.com/frankie336/projectdavid/compare/v1.33.0...v1.33.1) (2025-06-10)


### Bug Fixes

* Add create_vector_vision_store_for_user ([392813b](https://github.com/frankie336/projectdavid/commit/392813bef20e12c2aca456e349b6d937e686f78c))

# [1.33.0](https://github.com/frankie336/projectdavid/compare/v1.32.21...v1.33.0) (2025-06-10)


### Features

* Add support for multi-modal image search ([58e7e27](https://github.com/frankie336/projectdavid/commit/58e7e270be849e36bcd93e6a19942fa3e8abbd25))
* Add support for multi-modal image search-1 ([b8ebc7c](https://github.com/frankie336/projectdavid/commit/b8ebc7c4fb73cec0bff1b98ee45fa5b52e41a9b3))
* Add support for multi-modal image search-1 ([2362069](https://github.com/frankie336/projectdavid/commit/2362069e4b5390b4eb2b1007a413a6adb1a8bc7b))
* Add support for multi-modal image search-2 ([07f81fe](https://github.com/frankie336/projectdavid/commit/07f81fe0a475652bc6d316f3dc45e341452f43b7))
* Add support for multi-modal image search-3 ([29bce72](https://github.com/frankie336/projectdavid/commit/29bce72b12e3b2b5d2daeafe2367908e0cc3b402))
* Add support for multi-modal image search-3 ([3f8149e](https://github.com/frankie336/projectdavid/commit/3f8149e31371efa8727b96fa16d92fbe5474f727))
* Add support for multi-modal image search-4 ([b434d6d](https://github.com/frankie336/projectdavid/commit/b434d6d035324f444b46bd49dd15cbed528527a5))
* Add support for multi-modal image search-4 ([6acddf0](https://github.com/frankie336/projectdavid/commit/6acddf0c3b38ed6ca9e786ddb6d8ebf1a1328ac5))
* Add support for multi-modal image search-5 ([1dd9dd9](https://github.com/frankie336/projectdavid/commit/1dd9dd9d91556df8a0089255efad82bfe3f9a6b6))
* Add support for multi-modal image search-6 ([33a6069](https://github.com/frankie336/projectdavid/commit/33a6069b9f7a9e9007c156d511b3cb8abf859760))
* Add support for multi-modal image search-7 ([01d68e5](https://github.com/frankie336/projectdavid/commit/01d68e591c8dbc52c81b6bfcd522bb95d27c9ddd))
* Add support for multi-modal image search-8 ([8663b2a](https://github.com/frankie336/projectdavid/commit/8663b2ab7f0f035ae953281d86ba01a0db926839))

## [1.32.21](https://github.com/frankie336/projectdavid/compare/v1.32.20...v1.32.21) (2025-06-10)


### Bug Fixes

* allow status chunks to bypass suppression ([9a21581](https://github.com/frankie336/projectdavid/commit/9a2158156b85c1685aff65925c17730722972ddb))

## [1.32.20](https://github.com/frankie336/projectdavid/compare/v1.32.19...v1.32.20) (2025-06-09)


### Bug Fixes

* parse run_id into emission. ([60ace8c](https://github.com/frankie336/projectdavid/commit/60ace8cf669c873c40a1b031740b2f7103a59c53))

## [1.32.19](https://github.com/frankie336/projectdavid/compare/v1.32.18...v1.32.19) (2025-06-09)


### Bug Fixes

* Add support for type: status chunks ([27c4227](https://github.com/frankie336/projectdavid/commit/27c4227ef3e3c95c28c37549090285f86a09fc49))

## [1.32.18](https://github.com/frankie336/projectdavid/compare/v1.32.17...v1.32.18) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-10 ([3687397](https://github.com/frankie336/projectdavid/commit/368739719cbce46936241dcf9ec47a16a7aa745f))
* Filter and supress file_search inline-10 ([8799863](https://github.com/frankie336/projectdavid/commit/8799863c5ae8fee8633ba598849af478db23ebfd))

## [1.32.17](https://github.com/frankie336/projectdavid/compare/v1.32.16...v1.32.17) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-9 ([eec7587](https://github.com/frankie336/projectdavid/commit/eec7587e46cf8b2ce315928a5476f1d7c3bde616))

## [1.32.16](https://github.com/frankie336/projectdavid/compare/v1.32.15...v1.32.16) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-8 ([6c8532e](https://github.com/frankie336/projectdavid/commit/6c8532e5360996283e5361b8587d78b810daf48b))

## [1.32.15](https://github.com/frankie336/projectdavid/compare/v1.32.14...v1.32.15) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-7 ([7c85449](https://github.com/frankie336/projectdavid/commit/7c85449a288384eed76aa5c87c657f1a149be937))

## [1.32.14](https://github.com/frankie336/projectdavid/compare/v1.32.13...v1.32.14) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-5 ([2ed7419](https://github.com/frankie336/projectdavid/commit/2ed7419d9d2ff8d73559b40b29942a3d2319734c))

## [1.32.13](https://github.com/frankie336/projectdavid/compare/v1.32.12...v1.32.13) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline-4 ([c255c3b](https://github.com/frankie336/projectdavid/commit/c255c3b2ef93c784ca90504d34d523c32457223e))

## [1.32.12](https://github.com/frankie336/projectdavid/compare/v1.32.11...v1.32.12) (2025-06-09)


### Bug Fixes

* Filter and supress file_search inline ([9dad4b0](https://github.com/frankie336/projectdavid/commit/9dad4b017215c2c0941835827ba4fd20174298da))
* Filter and supress file_search inline-3 ([7077439](https://github.com/frankie336/projectdavid/commit/70774397fd3eaebbfe00fd1b4e8bb1792b1400c3))

## [1.32.11](https://github.com/frankie336/projectdavid/compare/v1.32.10...v1.32.11) (2025-06-08)


### Bug Fixes

* Filter and supress file_search inline ([03d5262](https://github.com/frankie336/projectdavid/commit/03d5262081cac65570796fb5c98a8fecc6242c71))

## [1.32.10](https://github.com/frankie336/projectdavid/compare/v1.32.9...v1.32.10) (2025-06-08)


### Bug Fixes

* Let content through-3 ([3b6d66e](https://github.com/frankie336/projectdavid/commit/3b6d66edcaf1e3c1550b111f0ef88c35871b28bc)), closes [throu#3](https://github.com/throu/issues/3)

## [1.32.9](https://github.com/frankie336/projectdavid/compare/v1.32.8...v1.32.9) (2025-06-08)


### Bug Fixes

* Let hot_code_output through-1 ([92e3619](https://github.com/frankie336/projectdavid/commit/92e36194eb22245da4371ac9dbf7dc896f3b3345)), closes [throu#1](https://github.com/throu/issues/1)

## [1.32.8](https://github.com/frankie336/projectdavid/compare/v1.32.7...v1.32.8) (2025-06-08)


### Bug Fixes

* Let every other chunk pass straight through-2 ([0bf280e](https://github.com/frankie336/projectdavid/commit/0bf280e9acd612fc3e788bda7cccc35e910324d2)), closes [throu#2](https://github.com/throu/issues/2)

## [1.32.7](https://github.com/frankie336/projectdavid/compare/v1.32.6...v1.32.7) (2025-06-08)


### Bug Fixes

* Let every other chunk pass straight through ([c0a11bb](https://github.com/frankie336/projectdavid/commit/c0a11bbfd5fbbb0247792fdfb12f4001b76dc8aa))
* Let every other chunk pass straight through-1 ([bf102db](https://github.com/frankie336/projectdavid/commit/bf102dbaa71d610f4ba4b6e2ed99ffe640fdd40c)), closes [throu#1](https://github.com/throu/issues/1)

## [1.32.6](https://github.com/frankie336/projectdavid/compare/v1.32.5...v1.32.6) (2025-06-08)


### Bug Fixes

*  code_execution chunks now bypass suppression ([e2762d4](https://github.com/frankie336/projectdavid/commit/e2762d49fc1b8ed60235be98a512e29eea4f3d4a))

## [1.32.5](https://github.com/frankie336/projectdavid/compare/v1.32.4...v1.32.5) (2025-06-08)


### Bug Fixes

*  code_execution chunks now bypass suppression ([d5f4c11](https://github.com/frankie336/projectdavid/commit/d5f4c11f14cce3017608129c2a94fd52f343cd2d))

## [1.32.4](https://github.com/frankie336/projectdavid/compare/v1.32.3...v1.32.4) (2025-06-08)


### Bug Fixes

*  code_execution chunks now bypass suppression ([69fb39e](https://github.com/frankie336/projectdavid/commit/69fb39e552ef312c4f772b88db31e65f9cd1b5e7))
*  code_execution chunks now bypass suppression ([bfcbefd](https://github.com/frankie336/projectdavid/commit/bfcbefddbe2809b8051e4ff44e8039c56495883d))

## [1.32.3](https://github.com/frankie336/projectdavid/compare/v1.32.2...v1.32.3) (2025-06-08)


### Bug Fixes

*  hot_code chunks now bypass suppression ([4f908e0](https://github.com/frankie336/projectdavid/commit/4f908e0a678f58fa3ea039f6f19c8787fc8e8260))

## [1.32.2](https://github.com/frankie336/projectdavid/compare/v1.32.1...v1.32.2) (2025-06-08)


### Bug Fixes

* supress mode code_interpreter_calls ([d7862d8](https://github.com/frankie336/projectdavid/commit/d7862d87234d1647ab7e4ba700971ed24d4a228e))

## [1.32.1](https://github.com/frankie336/projectdavid/compare/v1.32.0...v1.32.1) (2025-06-08)


### Bug Fixes

* supress mode suppressing all content ([657ab23](https://github.com/frankie336/projectdavid/commit/657ab23668337133ce93995a6acce4b503d12fce))

# [1.32.0](https://github.com/frankie336/projectdavid/compare/v1.31.1...v1.32.0) (2025-06-08)


### Features

* Integrate function call suppression. The provides optional methods to clean <fc><\fc> wrapped function calls from stream. ([05b357e](https://github.com/frankie336/projectdavid/commit/05b357e17a5dfacc019bfea106d3be560878df4b))

## [1.31.1](https://github.com/frankie336/projectdavid/compare/v1.31.0...v1.31.1) (2025-05-26)


### Bug Fixes

* Remove magic dependency when finding file type ([7063c14](https://github.com/frankie336/projectdavid/commit/7063c14c3d9f21bc9bd9579d4d7d2c55004a627f))

# [1.31.0](https://github.com/frankie336/projectdavid/compare/v1.30.4...v1.31.0) (2025-05-26)


### Features

* expand file-processing-types ([f6267c9](https://github.com/frankie336/projectdavid/commit/f6267c94e230e8390c2439907f8df7b45c69da2f))

## [1.30.4](https://github.com/frankie336/projectdavid/compare/v1.30.3...v1.30.4) (2025-05-24)


### Bug Fixes

* change async def _list_vs_by_user_async to admin endpoint ([5b7ae9c](https://github.com/frankie336/projectdavid/commit/5b7ae9ca9334dba5a431b0feafb7cf55699fa1db))

## [1.30.3](https://github.com/frankie336/projectdavid/compare/v1.30.2...v1.30.3) (2025-05-24)



There  are some major changes and enhancements to vector store creation and life cycle management (RAG).
 Creating a vector store
No longer requires you manually pass the user id into the creaction method

```python
vs = client.vectors.create_vector_store(
    name="movielens-complete-demo",
    user_id=USER_ID,
)
```

Becomes:

```python
vs = client.vectors.create_vector_store(
    name="movielens-complete-demo",

)
```

**Search Methods**

Several new search method have been added:
vector_file_search_raw
Search hits are returned in a raw format with similarity scoring. There is no further post processing, formatting or ranking. This is most appropriate where you need to apply custom or third party ranking and or post processing.

**Example:**

````python
hits = client.vectors.vector_file_search_raw(
    vector_store_id="vect_GsSezuKiXy11rFssDcRFAg",
    query_text=query,
    top_k=top_k,
    vector_store_host=host_override,
)
````

**Simple_vector_file_search**

Search hits are returned wrapped in an envelope that provides anotation and citations per hit. This is most appropriate for bodies of text where you might need the assistant to provide authorities and citations; a legal document for example.

**Example**

```python
hits = client.vectors.simple_vector_file_search(
    vector_store_id=STORE_ID,
    query_text=query,
    top_k=top_k,
)
```

**attended_file_search**

Search results are synthesized by an integrated agent; results are passed to the Large Language model. The output comes with AI insights and organization. Additionally, result rankings are enhanced by a second pass through a ranking model. Suited for cumilitative research (deep research) and multi agent   tasks.

**Example:**

```
hits = client.vectors.attended_file_search(
    vector_store_id=STORE_ID,
    query_text=query,
    top_k=top_k,
)
```

**unattended_file_search**

Search hits are returned wrapped in an envelope that provides anotation and citations per hit. Additionally, result rankings are enhanced by a second pass through a ranking model

**Example:**

```python
 hits = client.vectors.unattended_file_search(
    vector_store_id=STORE_ID,
    query_text=query,
    top_k=top_k,
)
```

### Bug Fixes

* restores the original behaviour while still ([c75c5fd](https://github.com/frankie336/projectdavid/commit/c75c5fdc562d7988b5db69cc582fa9e3ab0fa8d3))
* restores the original behaviour while still ([c9c15ef](https://github.com/frankie336/projectdavid/commit/c9c15ef7187abe766c87b5f7c6de60bf8203c4fc))

## [1.30.2](https://github.com/frankie336/projectdavid/compare/v1.30.1...v1.30.2) (2025-05-24)


### Bug Fixes

* get_vector_store ([779714c](https://github.com/frankie336/projectdavid/commit/779714c3c73ad1258e86ccfa4c0f11666c98c7fe))
* restores the original behaviour while still ([9224b8f](https://github.com/frankie336/projectdavid/commit/9224b8f37e962fa115e6686eabe58a295bc6eb3b))

## [1.30.1](https://github.com/frankie336/projectdavid/compare/v1.30.0...v1.30.1) (2025-05-24)


### Bug Fixes

* get_or_create_file_search_store ([688e07f](https://github.com/frankie336/projectdavid/commit/688e07fc800b927ed8d4f5657092454d576cc014))

# [1.30.0](https://github.com/frankie336/projectdavid/compare/v1.29.9...v1.30.0) (2025-05-23)


### Features

* Add unattended_file_search method ([2885400](https://github.com/frankie336/projectdavid/commit/288540003a0553a77ed316be5fd182911f202cd4))

## [1.29.9](https://github.com/frankie336/projectdavid/compare/v1.29.8...v1.29.9) (2025-05-15)


### Bug Fixes

* enforce specific platform tool types ([8a00b62](https://github.com/frankie336/projectdavid/commit/8a00b62548b36d491d0df5b5cc2e6aa190d61c8b))

## [1.29.8](https://github.com/frankie336/projectdavid/compare/v1.29.7...v1.29.8) (2025-05-15)


### Bug Fixes

* status=StatusEnum.queued ([50a00e9](https://github.com/frankie336/projectdavid/commit/50a00e95ed7f5159e20e3e7d9378314849fd7571))

## [1.29.7](https://github.com/frankie336/projectdavid/compare/v1.29.6...v1.29.7) (2025-05-14)


### Bug Fixes

* Creating run for assistant_id=%s, thread_id=%s ([3b45b72](https://github.com/frankie336/projectdavid/commit/3b45b7249b815ed09d96fb8847651efce88113bf))
* Creating run for assistant_id=%s, thread_id=%s ([31de1ab](https://github.com/frankie336/projectdavid/commit/31de1abb647658fa6bf1c4d11fd5a3f023c7afe9))

## [1.29.6](https://github.com/frankie336/projectdavid/compare/v1.29.5...v1.29.6) (2025-05-14)


### Bug Fixes

* Creating run for assistant_id=%s, thread_id=%s ([9898eb6](https://github.com/frankie336/projectdavid/commit/9898eb6b9d0f6b4525f97517937e6c22a898cea6))

## [1.29.5](https://github.com/frankie336/projectdavid/compare/v1.29.4...v1.29.5) (2025-05-14)


### Bug Fixes

* fix runs payload ([b7c89e4](https://github.com/frankie336/projectdavid/commit/b7c89e43aea6cdd84744f1a89352a7b8b2146afd))

## [1.29.4](https://github.com/frankie336/projectdavid/compare/v1.29.3...v1.29.4) (2025-05-14)


### Bug Fixes

* RunsClient.create_run—drop user_id ([4ee4d74](https://github.com/frankie336/projectdavid/commit/4ee4d74029ac6719ab0accc1d04fdca11b06fa1d))

## [1.29.3](https://github.com/frankie336/projectdavid/compare/v1.29.2...v1.29.3) (2025-05-14)


### Bug Fixes

* user-id logic ([d1a8ab4](https://github.com/frankie336/projectdavid/commit/d1a8ab4f4a0e855cc935d80048f2818a4b03ca26))

## [1.29.2](https://github.com/frankie336/projectdavid/compare/v1.29.1...v1.29.2) (2025-05-14)


### Bug Fixes

* user-id logic ([1d2375a](https://github.com/frankie336/projectdavid/commit/1d2375ad6579d332aa18d964eb3d212510bf43c3))

## [1.29.1](https://github.com/frankie336/projectdavid/compare/v1.29.0...v1.29.1) (2025-05-13)


### Bug Fixes

* project_david_common 16.0.2 -->project_david_common 17.0.0 ([8e3691f](https://github.com/frankie336/projectdavid/commit/8e3691ffc18082fb6de540104e89674a5a354d63))

# [1.29.0](https://github.com/frankie336/projectdavid/compare/v1.28.0...v1.29.0) (2025-05-13)


### Features

* Associate runs with user_id ([eed69dc](https://github.com/frankie336/projectdavid/commit/eed69dc724df730657ab3fba305950d3e67398b6))

# [1.28.0](https://github.com/frankie336/projectdavid/compare/v1.27.0...v1.28.0) (2025-05-11)


### Features

* allow an admin to choose the owner ([2aac857](https://github.com/frankie336/projectdavid/commit/2aac857f58c7bd828e980a2eb00eac52ef16fb6c))

# [1.27.0](https://github.com/frankie336/projectdavid/compare/v1.26.13...v1.27.0) (2025-05-11)


### Features

* get_user_store_ids ([e5d074d](https://github.com/frankie336/projectdavid/commit/e5d074d2a77cec7c9987cab5efb04c8de9c689f8))

## [1.26.13](https://github.com/frankie336/projectdavid/compare/v1.26.12...v1.26.13) (2025-05-10)


### Bug Fixes

* create_thread-make-participant-ids-optional0.62 ([a73854c](https://github.com/frankie336/projectdavid/commit/a73854cee21decee90e10fb861cdb6c5bf91ff84))

## [1.26.12](https://github.com/frankie336/projectdavid/compare/v1.26.11...v1.26.12) (2025-05-10)


### Bug Fixes

* create_thread-make-participant-ids-optional ([c01cb8d](https://github.com/frankie336/projectdavid/commit/c01cb8dc357a5b2143aac770d97b0772fe085566))

## [1.26.11](https://github.com/frankie336/projectdavid/compare/v1.26.10...v1.26.11) (2025-05-10)


### Bug Fixes

* create_thread-make-participant-ids-optional ([012ea53](https://github.com/frankie336/projectdavid/commit/012ea53910be70093c39b98e2ba2817b89302d23))

## [1.26.10](https://github.com/frankie336/projectdavid/compare/v1.26.9...v1.26.10) (2025-05-10)


### Bug Fixes

* Migrate to DEFAULT_ASSISTANT ([613cf00](https://github.com/frankie336/projectdavid/commit/613cf0015385ea8cbccbd34a71adddac5e7c9bdf))
* Migrate to DEFAULT_ASSISTANT ([1ef337a](https://github.com/frankie336/projectdavid/commit/1ef337a114593ec0c5b449ccd877a5ec24c5a14e))

## [1.26.9](https://github.com/frankie336/projectdavid/compare/v1.26.8...v1.26.9) (2025-05-10)


### Bug Fixes

* vector store host address passthrough ([9ce8f51](https://github.com/frankie336/projectdavid/commit/9ce8f51a6f55516d93bd452009461631f7a07059))

## [1.26.8](https://github.com/frankie336/projectdavid/compare/v1.26.7...v1.26.8) (2025-05-09)


### Bug Fixes

* timers ([6e0743b](https://github.com/frankie336/projectdavid/commit/6e0743bd8c04b51b170ab962678802fb686611a1))

## [1.26.7](https://github.com/frankie336/projectdavid/compare/v1.26.6...v1.26.7) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([224ba91](https://github.com/frankie336/projectdavid/commit/224ba914c8c1023bfae9bb9ca4a25413fae982fe))

## [1.26.6](https://github.com/frankie336/projectdavid/compare/v1.26.5...v1.26.6) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([41cfe2d](https://github.com/frankie336/projectdavid/commit/41cfe2d161477db801e6fe979cf983f3bca6057f))
* user_36xmJoz1ywAiuOAxYvKq2Z ([4620760](https://github.com/frankie336/projectdavid/commit/46207605a1a1f2e2a9cd8712e4168dc2ad593275))

## [1.26.5](https://github.com/frankie336/projectdavid/compare/v1.26.4...v1.26.5) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([4b80332](https://github.com/frankie336/projectdavid/commit/4b80332272c719878e6b76345f5547de54b1b5a2))

## [1.26.4](https://github.com/frankie336/projectdavid/compare/v1.26.3...v1.26.4) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([88784d2](https://github.com/frankie336/projectdavid/commit/88784d20fe95ae00d439a8937736f500a6f3f7f1))

## [1.26.3](https://github.com/frankie336/projectdavid/compare/v1.26.2...v1.26.3) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([455beb2](https://github.com/frankie336/projectdavid/commit/455beb24febed330ffba5aef75e3982501d061df))

## [1.26.2](https://github.com/frankie336/projectdavid/compare/v1.26.1...v1.26.2) (2025-05-08)


### Bug Fixes

* user_36xmJoz1ywAiuOAxYvKq2Z ([5151e32](https://github.com/frankie336/projectdavid/commit/5151e32bf820b863f1bfb6e85217b280290b2750))

## [1.26.1](https://github.com/frankie336/projectdavid/compare/v1.26.0...v1.26.1) (2025-05-08)


### Bug Fixes

* remove ephemeral assistant creation ([579c486](https://github.com/frankie336/projectdavid/commit/579c486e4018dd6f7e04286a09a33190fba50166))
* remove ephemeral assistant creation ([6fe937c](https://github.com/frankie336/projectdavid/commit/6fe937c578577741b3afb5a58bb96a5fb0e0618b))

# [1.26.0](https://github.com/frankie336/projectdavid/compare/v1.25.8...v1.26.0) (2025-05-08)


### Features

* PLATFORM_ASSISTANT_ID_MAP ([fd4ea9a](https://github.com/frankie336/projectdavid/commit/fd4ea9a9d2d0aa3fa4aa8806035dc08ab76b3fd5))
* PLATFORM_ASSISTANT_ID_MAP ([8605783](https://github.com/frankie336/projectdavid/commit/8605783b0dce176777713b6fcbf1a57af43727ce))

## [1.25.8](https://github.com/frankie336/projectdavid/compare/v1.25.7...v1.25.8) (2025-05-07)


### Bug Fixes

* Pydantic schema – make participant_ids optional ([621a3fe](https://github.com/frankie336/projectdavid/commit/621a3fef75092dfff4d375cfeda4699644f6c380))
* Pydantic schema – make participant_ids optional ([1d01162](https://github.com/frankie336/projectdavid/commit/1d0116257cf445f20fc5b1a10e87c9147d96b855))
* Pydantic schema – make participant_ids optional ([af2bdb5](https://github.com/frankie336/projectdavid/commit/af2bdb5b74f5f392ae21c1e971c7c2cd97104d9e))

## [1.25.7](https://github.com/frankie336/projectdavid/compare/v1.25.6...v1.25.7) (2025-05-07)


### Bug Fixes

* cross-encoder/ms-marco-MiniLM-L-6-v2 ([a54173d](https://github.com/frankie336/projectdavid/commit/a54173dcae46e03b3961285d189d4ca466d96546))

## [1.25.6](https://github.com/frankie336/projectdavid/compare/v1.25.5...v1.25.6) (2025-05-06)


### Bug Fixes

* resolve import error ([3e45ddd](https://github.com/frankie336/projectdavid/commit/3e45dddc627c4d6be2be2bdd34be14fa2cc08e7b))

## [1.25.5](https://github.com/frankie336/projectdavid/compare/v1.25.4...v1.25.5) (2025-05-06)


### Bug Fixes

* Replace raw file_id tokens with human‑friendly file_name ([a92abf2](https://github.com/frankie336/projectdavid/commit/a92abf28bcf9f1dfd852ed27ae500bcc12ad7219))

## [1.25.4](https://github.com/frankie336/projectdavid/compare/v1.25.3...v1.25.4) (2025-05-06)


### Bug Fixes

* method name changes ([8de1fdf](https://github.com/frankie336/projectdavid/commit/8de1fdf1bf3225dbf5bf4788b914a4a90db04e63))

## [1.25.3](https://github.com/frankie336/projectdavid/compare/v1.25.2...v1.25.3) (2025-05-05)


### Bug Fixes

* Make vector search method names intuitive ([b3aca19](https://github.com/frankie336/projectdavid/commit/b3aca191ba3a0d09fad00ddf63f274c6ea5b3990))
* Make vector search method names intuitive ([fff4b97](https://github.com/frankie336/projectdavid/commit/fff4b9726d3995653f7f4bd38b67125710ad7b79))
* Make vector search method names intuitive ([84d1d6f](https://github.com/frankie336/projectdavid/commit/84d1d6f43399a658e327af72972ef054a19fcf40))
* Make vector search method names intuitive ([2e0741c](https://github.com/frankie336/projectdavid/commit/2e0741cd13d646e42f6aeebc66af68b1479518c7))
* Make vector search method names intuitive ([001e931](https://github.com/frankie336/projectdavid/commit/001e93173114ccb3cf2a0631f036a65e7cd0572f))
* Make vector search method names intuitive ([e2b4b7c](https://github.com/frankie336/projectdavid/commit/e2b4b7c1a1ff2f6dd6bc3e4708382304d57e2216))

## [1.25.2](https://github.com/frankie336/projectdavid/compare/v1.25.1...v1.25.2) (2025-05-04)


### Bug Fixes

* API key passthrough ([61fdd9a](https://github.com/frankie336/projectdavid/commit/61fdd9a6554e45c904b6aae3f778fd08013ef78b))

## [1.25.1](https://github.com/frankie336/projectdavid/compare/v1.25.0...v1.25.1) (2025-05-04)


### Bug Fixes

* API key passthrough ([0e974f6](https://github.com/frankie336/projectdavid/commit/0e974f6cf5c26de4191ce8349fd8102a6b2fa03d))

# [1.25.0](https://github.com/frankie336/projectdavid/compare/v1.24.0...v1.25.0) (2025-05-04)


### Bug Fixes

* API key passthrough ([a088b61](https://github.com/frankie336/projectdavid/commit/a088b61115a83c6e6a1e6ee8de8d8142b2d158e1))
* API key passthrough ([34d2653](https://github.com/frankie336/projectdavid/commit/34d2653fd62edc8fc3aae8f010f8da55a649dd2f))
* API key passthrough ([acbe3d9](https://github.com/frankie336/projectdavid/commit/acbe3d91f01fbef0abf55ed8aa80b7ef446f6a56))
* API key passthrough ([7333b45](https://github.com/frankie336/projectdavid/commit/7333b4566f22ad5695108ece3b5694befa74aa29))


### Features

* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([307f494](https://github.com/frankie336/projectdavid/commit/307f4946ebc29f61533f978d6d2a7675e0469bd2))

# [1.24.0](https://github.com/frankie336/projectdavid/compare/v1.23.0...v1.24.0) (2025-05-04)


### Features

* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([4a77383](https://github.com/frankie336/projectdavid/commit/4a7738379bf9c5375767311df2165ab7ba670661))

# [1.23.0](https://github.com/frankie336/projectdavid/compare/v1.22.0...v1.23.0) (2025-05-04)


### Features

* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([a3a48b2](https://github.com/frankie336/projectdavid/commit/a3a48b2519aa5edd0a6c3ce1a8694e210dc3870a))

# [1.22.0](https://github.com/frankie336/projectdavid/compare/v1.21.0...v1.22.0) (2025-05-04)


### Features

* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([d6a98b1](https://github.com/frankie336/projectdavid/commit/d6a98b1376e3e65e48612f5e0485bf22b0855b88))
* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([da68992](https://github.com/frankie336/projectdavid/commit/da68992d38ad108368250df018f4eb512a7808f5))
* Retriever → (Optionally Reranker) → Synthesizer → Citation‑mapper ([bc95378](https://github.com/frankie336/projectdavid/commit/bc95378155fb3153262f729775cbbe684e941393))

# [1.21.0](https://github.com/frankie336/projectdavid/compare/v1.20.2...v1.21.0) (2025-05-04)


### Features

* Add support to display line and page numbers in vector search output ([08f656a](https://github.com/frankie336/projectdavid/commit/08f656a617577ab12a74504467020d3c44c8d244))

## [1.20.2](https://github.com/frankie336/projectdavid/compare/v1.20.1...v1.20.2) (2025-05-04)


### Bug Fixes

* Add Metadata Wrapping to search_vector_store_openai ([4fb49ba](https://github.com/frankie336/projectdavid/commit/4fb49ba72da9615307a0f9741cb7a0188e15d176))

## [1.20.1](https://github.com/frankie336/projectdavid/compare/v1.20.0...v1.20.1) (2025-05-04)


### Bug Fixes

* Add Metadata Wrapping to search_vector_store_openai ([8879ad0](https://github.com/frankie336/projectdavid/commit/8879ad0faec499e1b5e6d5f68b23c84d9a637cf7))

# [1.20.0](https://github.com/frankie336/projectdavid/compare/v1.19.0...v1.20.0) (2025-05-04)


### Features

* Adding support for structured vector search output ([919c121](https://github.com/frankie336/projectdavid/commit/919c121598330215552b003c1c360c2e182353f4))
* Adding support for structured vector search output ([e0d95ab](https://github.com/frankie336/projectdavid/commit/e0d95ab61bd2dc7d13f81b29107e9add980e3935))

# [1.19.0](https://github.com/frankie336/projectdavid/compare/v1.18.1...v1.19.0) (2025-05-01)


### Features

* attach any referenced vector stores ([ab57374](https://github.com/frankie336/projectdavid/commit/ab573748410640aa014194babcaf2016c746b4e0))

## [1.18.1](https://github.com/frankie336/projectdavid/compare/v1.18.0...v1.18.1) (2025-05-01)


### Bug Fixes

* Adding  tool_resources schema. ([116f587](https://github.com/frankie336/projectdavid/commit/116f5875fd07a6b185e48a811919fd8bb185a1e6))

# [1.18.0](https://github.com/frankie336/projectdavid/compare/v1.17.0...v1.18.0) (2025-04-30)


### Features

* Drop user_id from create_vector_store(), inferring it from the API key. Add list_my_vector_stores() (token-scoped) and deprecates the old get_stores_by_user() ([7a22fcb](https://github.com/frankie336/projectdavid/commit/7a22fcbce8dbf80cd1cfa6a9790bfedbc5b1e85a))
* Drop user_id from create_vector_store(), inferring it from the API key. Add list_my_vector_stores() (token-scoped) and deprecates the old get_stores_by_user() ([2ec3263](https://github.com/frankie336/projectdavid/commit/2ec326368e2ad58432a4b9608681d55ead6a4209))

# [1.17.0](https://github.com/frankie336/projectdavid/compare/v1.16.0...v1.17.0) (2025-04-29)


### Features

* add tools_resources field ([d55bfd3](https://github.com/frankie336/projectdavid/commit/d55bfd320c3adcbc5afe3a4617288381271bafd8))

# [1.16.0](https://github.com/frankie336/projectdavid/compare/v1.15.0...v1.16.0) (2025-04-28)


### Features

* auto tools-attachment logic ([c27907e](https://github.com/frankie336/projectdavid/commit/c27907ef98147060c533a1e44edbc52dadb7618e))
* auto tools-attachment logic ([b2d5cd6](https://github.com/frankie336/projectdavid/commit/b2d5cd6e7948b3960bdc5e2886c9f123b5c6df44))

# [1.15.0](https://github.com/frankie336/projectdavid/compare/v1.14.0...v1.15.0) (2025-04-28)


### Features

* auto tools-attachment logic ([fba3cbd](https://github.com/frankie336/projectdavid/commit/fba3cbde7934d67a1e0a66a7b73c9e6797277d63))

# [1.14.0](https://github.com/frankie336/projectdavid/compare/v1.13.0...v1.14.0) (2025-04-28)


### Features

* auto tools-attachment logic ([73ae06d](https://github.com/frankie336/projectdavid/commit/73ae06d01c3991e7a53dc066164d89dabce9dd06))

# [1.13.0](https://github.com/frankie336/projectdavid/compare/v1.12.13...v1.13.0) (2025-04-27)


### Features

* adding platform_tools ([a84c62b](https://github.com/frankie336/projectdavid/commit/a84c62b690c8ed9e87a309a042cc630931e0d62a))

## [1.12.13](https://github.com/frankie336/projectdavid/compare/v1.12.12...v1.12.13) (2025-04-22)


### Bug Fixes

* list_threads ([ed56dd9](https://github.com/frankie336/projectdavid/commit/ed56dd952bd66e125a7082b2a63cd46ba32176a3))
* Restore base client ([7c10684](https://github.com/frankie336/projectdavid/commit/7c10684c4d59aa30b33cf2c29f52a54805ddd60a))

## [1.12.12](https://github.com/frankie336/projectdavid/compare/v1.12.11...v1.12.12) (2025-04-22)


### Bug Fixes

* base client ([3faadef](https://github.com/frankie336/projectdavid/commit/3faadef63a1a23ab6ec36a94a54905c2ee76d270))

## [1.12.11](https://github.com/frankie336/projectdavid/compare/v1.12.10...v1.12.11) (2025-04-22)


### Bug Fixes

* projectdavid_common==0.10.7 ([d68895f](https://github.com/frankie336/projectdavid/commit/d68895fc5986701a9fb2d7e2ceb8dca4d0b1426d))

## [1.12.10](https://github.com/frankie336/projectdavid/compare/v1.12.9...v1.12.10) (2025-04-22)


### Bug Fixes

* projectdavid_common==0.10.6 ([a34f0c8](https://github.com/frankie336/projectdavid/commit/a34f0c8ea27213de8e66e8958ef0b2e0b5666c28))
* projectdavid_common==0.10.6 ([8889fda](https://github.com/frankie336/projectdavid/commit/8889fda4f61165d81ff91e1c449633efc171180a))

## [1.12.9](https://github.com/frankie336/projectdavid/compare/v1.12.8...v1.12.9) (2025-04-22)


### Bug Fixes

* base_client.py ([86a526d](https://github.com/frankie336/projectdavid/commit/86a526d04b00ea861e34c4f70649f89019ba6a16))

## [1.12.8](https://github.com/frankie336/projectdavid/compare/v1.12.7...v1.12.8) (2025-04-22)


### Bug Fixes

* projectdavid_common==0.10.5 ([82d5bec](https://github.com/frankie336/projectdavid/commit/82d5bec6a0a0784e1f9bd28eb7dba282c66fa256))

## [1.12.7](https://github.com/frankie336/projectdavid/compare/v1.12.6...v1.12.7) (2025-04-22)


### Bug Fixes

* "projectdavid_common==0.10.4" ([21727c8](https://github.com/frankie336/projectdavid/commit/21727c8186e972daf3623191ebc3a60a5a0f7963))

## [1.12.6](https://github.com/frankie336/projectdavid/compare/v1.12.5...v1.12.6) (2025-04-22)


### Bug Fixes

* projectdavid_common==0.10.3 ([1220cc0](https://github.com/frankie336/projectdavid/commit/1220cc061eec911d90563b0c9b3362376fef2db9))

## [1.12.5](https://github.com/frankie336/projectdavid/compare/v1.12.4...v1.12.5) (2025-04-20)


### Bug Fixes

* files_client.py ([8191593](https://github.com/frankie336/projectdavid/commit/81915935ea5adef931c2902c67c28c0cf9e2d624))

## [1.12.4](https://github.com/frankie336/projectdavid/compare/v1.12.3...v1.12.4) (2025-04-19)


### Bug Fixes

* watch_run_events4 ([567f767](https://github.com/frankie336/projectdavid/commit/567f76789d83e6a9333fc1cac7dd53934817180f))

## [1.12.3](https://github.com/frankie336/projectdavid/compare/v1.12.2...v1.12.3) (2025-04-19)


### Bug Fixes

* watch_run_events3 ([ec2e24b](https://github.com/frankie336/projectdavid/commit/ec2e24b8126b86d9c16b2a7a996691e79b2ccd4e))

## [1.12.2](https://github.com/frankie336/projectdavid/compare/v1.12.1...v1.12.2) (2025-04-19)


### Bug Fixes

* watch_run_events2 ([46b66b7](https://github.com/frankie336/projectdavid/commit/46b66b7807bdcfeb3dcbc00885be005c5d132429))

## [1.12.1](https://github.com/frankie336/projectdavid/compare/v1.12.0...v1.12.1) (2025-04-19)


### Bug Fixes

* watch_run_events ([654e6ab](https://github.com/frankie336/projectdavid/commit/654e6ab1b28e8216d8b112e2eaf63bdcdfa58e6d))

# [1.12.0](https://github.com/frankie336/projectdavid/compare/v1.11.11...v1.12.0) (2025-04-18)


### Features

* watch_run_events ([7c926d2](https://github.com/frankie336/projectdavid/commit/7c926d25ca96e3df4430dffeb3a570fc737f77ad))

## [1.11.11](https://github.com/frankie336/projectdavid/compare/v1.11.10...v1.11.11) (2025-04-18)


### Bug Fixes

* def _extract_pdf_text ([7d5dc95](https://github.com/frankie336/projectdavid/commit/7d5dc95cd503b99c416160012a7552eff63c1e01))

## [1.11.10](https://github.com/frankie336/projectdavid/compare/v1.11.9...v1.11.10) (2025-04-18)


### Bug Fixes

* improved-csv-support ([9be9313](https://github.com/frankie336/projectdavid/commit/9be93137e8e325e29ef77aac5679f9ff5565601c))

## [1.11.9](https://github.com/frankie336/projectdavid/compare/v1.11.8...v1.11.9) (2025-04-18)


### Bug Fixes

* query_store ([84df1cf](https://github.com/frankie336/projectdavid/commit/84df1cf60ccf234e559a183082842b0b1c4a9fa9))

## [1.11.8](https://github.com/frankie336/projectdavid/compare/v1.11.7...v1.11.8) (2025-04-18)


### Bug Fixes

* query_store ([45d8d6e](https://github.com/frankie336/projectdavid/commit/45d8d6e11568cd881badea4212d45d9cfe2d5955))

## [1.11.7](https://github.com/frankie336/projectdavid/compare/v1.11.6...v1.11.7) (2025-04-18)


### Bug Fixes

* projectdavid.clients.vector_store_manager ([770eece](https://github.com/frankie336/projectdavid/commit/770eece5f0079fff56da232707137b1e80918e39))

## [1.11.6](https://github.com/frankie336/projectdavid/compare/v1.11.5...v1.11.6) (2025-04-18)


### Bug Fixes

* attach_vector_store_to_assistant ([7e60556](https://github.com/frankie336/projectdavid/commit/7e605568ed68462733166d4b440f957bc5b3ca61))

## [1.11.5](https://github.com/frankie336/projectdavid/compare/v1.11.4...v1.11.5) (2025-04-17)


### Bug Fixes

* attach_vector_store_to_assistant2 ([592211a](https://github.com/frankie336/projectdavid/commit/592211ad5dcf7a03d7af0c0cca12728fc8cc32ec))

## [1.11.4](https://github.com/frankie336/projectdavid/compare/v1.11.3...v1.11.4) (2025-04-17)


### Bug Fixes

* attach_vector_store_to_assistant ([3cf0096](https://github.com/frankie336/projectdavid/commit/3cf0096d66e73bce70dc2c2c33c4c2f88b6caee2))

## [1.11.3](https://github.com/frankie336/projectdavid/compare/v1.11.2...v1.11.3) (2025-04-17)


### Bug Fixes

* vectors.py ([db4a8b4](https://github.com/frankie336/projectdavid/commit/db4a8b45a8294af60530ac2cd34e291917645cf1))

## [1.11.2](https://github.com/frankie336/projectdavid/compare/v1.11.1...v1.11.2) (2025-04-17)


### Bug Fixes

* projectdavid_common>=0.6 ([d64d055](https://github.com/frankie336/projectdavid/commit/d64d05557f42ac76d2f2338571a8a3ffd28a508a))

## [1.11.1](https://github.com/frankie336/projectdavid/compare/v1.11.0...v1.11.1) (2025-04-17)


### Bug Fixes

* projectdavid_common>=0.5.0,<0.12.0 ([4a7dd78](https://github.com/frankie336/projectdavid/commit/4a7dd78b05bd00ec617b5c0be2955aa30189b12e))

# [1.11.0](https://github.com/frankie336/projectdavid/compare/v1.10.0...v1.11.0) (2025-04-17)


### Features

* add support for new models1 ([48ae477](https://github.com/frankie336/projectdavid/commit/48ae477c2d14d4d8f9315009841f64e794c8a691))

# [1.10.0](https://github.com/frankie336/projectdavid/compare/v1.9.0...v1.10.0) (2025-04-17)


### Features

* add support for new models ([3d49a22](https://github.com/frankie336/projectdavid/commit/3d49a22663374b978957019e13bd475d6d2394cc))

# [1.9.0](https://github.com/frankie336/projectdavid/compare/v1.8.0...v1.9.0) (2025-04-17)


### Features

* add new model support ([447e633](https://github.com/frankie336/projectdavid/commit/447e6336854ca5c5eead627373b6237b041dbab7))

# [1.8.0](https://github.com/frankie336/projectdavid/compare/v1.7.0...v1.8.0) (2025-04-15)


### Bug Fixes

* isort ([c12e219](https://github.com/frankie336/projectdavid/commit/c12e219c9111aef80b92fe85ee8db0da4e2d1b23))
* linting ([bc69c11](https://github.com/frankie336/projectdavid/commit/bc69c114e8278b1cb6edcc33f8e738dbeb7e82c3))
* linting ([dbeef51](https://github.com/frankie336/projectdavid/commit/dbeef51a4cc92e95e4e557e949793dbc60960a83))


### Features

* Qwen/QwQ-32B-Preview ([10e0382](https://github.com/frankie336/projectdavid/commit/10e03826ca3fa6632325953706a24433914421d0))

# [1.7.0](https://github.com/frankie336/projectdavid/compare/v1.6.0...v1.7.0) (2025-04-14)


### Features

* Qwen/QwQ-32B-Preview ([1f3b401](https://github.com/frankie336/projectdavid/commit/1f3b4013e673c3287615b5640cb73cdc6301e71b))

# [1.6.0](https://github.com/frankie336/projectdavid/compare/v1.5.0...v1.6.0) (2025-04-14)


### Features

* Qwen/QwQ-32B-Preview ([dfc605d](https://github.com/frankie336/projectdavid/commit/dfc605d50362b33156636efe8807887eb1ef1bd3))

# [1.5.0](https://github.com/frankie336/projectdavid/compare/v1.4.9...v1.5.0) (2025-04-14)


### Features

* PolyForm Noncommercial License 1.0.0 ([5e95d58](https://github.com/frankie336/projectdavid/commit/5e95d58c4d25b62733f4f963dd3b4bc24c1f333a))

## [1.4.9](https://github.com/frankie336/projectdavid/compare/v1.4.8...v1.4.9) (2025-04-13)


### Bug Fixes

* ToolsClient ([1cb2ad9](https://github.com/frankie336/projectdavid/commit/1cb2ad956963c69a08ebada97d77d91694fd74e3))

## [1.4.8](https://github.com/frankie336/projectdavid/compare/v1.4.7...v1.4.8) (2025-04-13)


### Bug Fixes

* StreamRequest ([81d7faa](https://github.com/frankie336/projectdavid/commit/81d7faac531cd1546429b2c17c67c43f164049f5))

## [1.4.7](https://github.com/frankie336/projectdavid/compare/v1.4.6...v1.4.7) (2025-04-13)


### Bug Fixes

* tools_client.py ([7c8344f](https://github.com/frankie336/projectdavid/commit/7c8344f8051c1e9a6acef03e631c5cfc98d0c233))

## [1.4.6](https://github.com/frankie336/projectdavid/compare/v1.4.5...v1.4.6) (2025-04-13)


### Bug Fixes

* MessagesClient ([78df74f](https://github.com/frankie336/projectdavid/commit/78df74f7560889f4434a886f77571afe664dd840))

## [1.4.5](https://github.com/frankie336/projectdavid/compare/v1.4.4...v1.4.5) (2025-04-13)


### Bug Fixes

* assistants_client.py ([4509fcd](https://github.com/frankie336/projectdavid/commit/4509fcd248fa7a82264e41ef6d804213e6677ea2))

## [1.4.4](https://github.com/frankie336/projectdavid/compare/v1.4.3...v1.4.4) (2025-04-13)


### Bug Fixes

* threads_client.py ([8e84c8a](https://github.com/frankie336/projectdavid/commit/8e84c8a35fff8ab63aeaefa4a72d0f09e2f34fef))

## [1.4.3](https://github.com/frankie336/projectdavid/compare/v1.4.2...v1.4.3) (2025-04-13)


### Bug Fixes

* X-API-Key alignment. ([e4f8661](https://github.com/frankie336/projectdavid/commit/e4f8661803542312d7893ae31a57d1c0cb90e80a))

## [1.4.2](https://github.com/frankie336/projectdavid/compare/v1.4.1...v1.4.2) (2025-04-13)


### Bug Fixes

* Integrate admin endpoint ([9f305ff](https://github.com/frankie336/projectdavid/commit/9f305ffc6536602f744c4c1f9680309baf6f4913))

## [1.4.1](https://github.com/frankie336/projectdavid/compare/v1.4.0...v1.4.1) (2025-04-13)


### Bug Fixes

* Align users client ([d7a2cac](https://github.com/frankie336/projectdavid/commit/d7a2cace19cd000f428abc32f61e0fb08139bc3d))

# [1.4.0](https://github.com/frankie336/projectdavid/compare/v1.3.14...v1.4.0) (2025-04-12)


### Features

* Implement API key protected routes ([f0dae30](https://github.com/frankie336/projectdavid/commit/f0dae30ec80746918d613ec679fa54b690ed5d27))

## [1.3.14](https://github.com/frankie336/projectdavid/compare/v1.3.13...v1.3.14) (2025-04-11)


### Bug Fixes

* constants ([b3c363a](https://github.com/frankie336/projectdavid/commit/b3c363aabb8cd0305d7fd2971dafcca9efc78a62))

## [1.3.13](https://github.com/frankie336/projectdavid/compare/v1.3.12...v1.3.13) (2025-04-11)


### Bug Fixes

* constants import ([1d4503e](https://github.com/frankie336/projectdavid/commit/1d4503e57872b84c00643768813f323c93d505af))

## [1.3.12](https://github.com/frankie336/projectdavid/compare/v1.3.11...v1.3.12) (2025-04-11)


### Bug Fixes

* hyperbolic/deepseek-ai/DeepSeek-V3-0324 bug ([cd9606f](https://github.com/frankie336/projectdavid/commit/cd9606fe40e04032e47be9691b6bff7298d349ab))
* hyperbolic/deepseek-ai/DeepSeek-V3-0324 bug ([99b397f](https://github.com/frankie336/projectdavid/commit/99b397fd7655f57bfc51fa4960e3004040931595))

## [1.3.11](https://github.com/frankie336/projectdavid/compare/v1.3.10...v1.3.11) (2025-04-11)


### Bug Fixes

* implement DEFAULT_TIMEOUT ([fe3575a](https://github.com/frankie336/projectdavid/commit/fe3575ad2f8c9a7ee74ee1848ec5fe917c31a4f8))
* implement DEFAULT_TIMEOUT ([65c72d2](https://github.com/frankie336/projectdavid/commit/65c72d21f3013286e9f29a1bb86288b6e85cc67b))

## [1.3.10](https://github.com/frankie336/projectdavid/compare/v1.3.9...v1.3.10) (2025-04-11)


### Bug Fixes

* restore-params ([dbf61db](https://github.com/frankie336/projectdavid/commit/dbf61db1d7b554bd2f92d910065b9f9b61c92997))
* restore-params-black ([4bdd63f](https://github.com/frankie336/projectdavid/commit/4bdd63faa37f6c2dd402e871bd40e2adcadf8a99))

## [1.3.9](https://github.com/frankie336/projectdavid/compare/v1.3.8...v1.3.9) (2025-04-11)


### Bug Fixes

* restore ([327da56](https://github.com/frankie336/projectdavid/commit/327da56668beb19c7933cdd9bbfa76d632f7f2bb))

## [1.3.8](https://github.com/frankie336/projectdavid/compare/v1.3.7...v1.3.8) (2025-04-11)


### Bug Fixes

* provider param ([93e2bb5](https://github.com/frankie336/projectdavid/commit/93e2bb5a31796998d33b1f60fe859f0996cfaa7f))
* provider param ([5c5fd48](https://github.com/frankie336/projectdavid/commit/5c5fd48bc7debc844fcfbeb990c27472608861d9))

## [1.3.7](https://github.com/frankie336/projectdavid/compare/v1.3.6...v1.3.7) (2025-04-11)


### Bug Fixes

* restore6 ([4a6ea35](https://github.com/frankie336/projectdavid/commit/4a6ea350e93292fe80c210cb992b35f1813cd1a5))
* restore6 ([ad57dbb](https://github.com/frankie336/projectdavid/commit/ad57dbb555b06d0df25063e11570b7c6e00d8de8))

## [1.3.6](https://github.com/frankie336/projectdavid/compare/v1.3.5...v1.3.6) (2025-04-11)


### Bug Fixes

* restore ([16b0d91](https://github.com/frankie336/projectdavid/commit/16b0d91921f62f8c7cd2261e87350a6da481e5e1))
* restore ([efbd123](https://github.com/frankie336/projectdavid/commit/efbd1231d0eb2a73b38361844a5dc15a83d74911))
* restore ([1986706](https://github.com/frankie336/projectdavid/commit/198670663410bce713e1429c7820076ad3c43a10))
* restore ([70768f4](https://github.com/frankie336/projectdavid/commit/70768f4056e53b80fb532f20566f38855f43f866))

## [1.3.5](https://github.com/frankie336/projectdavid/compare/v1.3.4...v1.3.5) (2025-04-11)


### Bug Fixes

* import name ([4d87f1c](https://github.com/frankie336/projectdavid/commit/4d87f1c4eeeacd13d0ad3fd43c089265abb93572))

## [1.3.4](https://github.com/frankie336/projectdavid/compare/v1.3.3...v1.3.4) (2025-04-11)


### Bug Fixes

* broken synch wrapper! ([2bc61cb](https://github.com/frankie336/projectdavid/commit/2bc61cbf713184113112d3ee6f1251b2c2c38d27))
* broken synch wrapper! ([0c28400](https://github.com/frankie336/projectdavid/commit/0c28400cf9b7d2db5a903e788db2a05ab3401b2b))

## [1.3.3](https://github.com/frankie336/projectdavid/compare/v1.3.2...v1.3.3) (2025-04-11)


### Bug Fixes

* structured file naming convention ([cf0aad9](https://github.com/frankie336/projectdavid/commit/cf0aad9cc2cea4d139bd0e5e065e431101408256))

## [1.3.2](https://github.com/frankie336/projectdavid/compare/v1.3.1...v1.3.2) (2025-04-11)


### Bug Fixes

* broken  logic ([077e41f](https://github.com/frankie336/projectdavid/commit/077e41f183470f7f7dda9d8c21ec43d198285a9e))

## [1.3.1](https://github.com/frankie336/projectdavid/compare/v1.3.0...v1.3.1) (2025-04-11)


### Bug Fixes

* time out issues. ([9c68435](https://github.com/frankie336/projectdavid/commit/9c68435ef573f25a032bb0a7e1c0b72184293f8c))

# [1.3.0](https://github.com/frankie336/projectdavid/compare/v1.2.3...v1.3.0) (2025-04-10)


### Features

* Add support for all google models. ([f5a7c10](https://github.com/frankie336/projectdavid/commit/f5a7c10ccef3d6ddeda0ad96d2359813a26ce61f))
* Add support for all google models. ([539c51d](https://github.com/frankie336/projectdavid/commit/539c51d53cbc0698691e8231b4626243f18060c9))
* Add support for all google models. ([82b4181](https://github.com/frankie336/projectdavid/commit/82b41815115f9a1c8f1f5293ce9f21de00dac755))

## [1.2.3](https://github.com/frankie336/projectdavid/compare/v1.2.2...v1.2.3) (2025-04-10)


### Bug Fixes

* ✅ api_key passed into stream_chunks(...) overrides ([35438bf](https://github.com/frankie336/projectdavid/commit/35438bfaf949bbb4c91f2ad75e05ce6dec3d9e87))

## [1.2.2](https://github.com/frankie336/projectdavid/compare/v1.2.1...v1.2.2) (2025-04-10)


### Bug Fixes

* Runs payload.2 ([0dea118](https://github.com/frankie336/projectdavid/commit/0dea118bcc9be39ddd03aa1fffc5c5fffc2aac75))

## [1.2.1](https://github.com/frankie336/projectdavid/compare/v1.2.0...v1.2.1) (2025-04-10)


### Bug Fixes

* Runs payload. ([6c24cc0](https://github.com/frankie336/projectdavid/commit/6c24cc04754302ea01278a8bf57cd1706b007d3d))
* Runs payload. ([a40cdf1](https://github.com/frankie336/projectdavid/commit/a40cdf1655ac71bf8a3fe1270a6d74f20bf9849d))
* Runs payload.1 ([767005e](https://github.com/frankie336/projectdavid/commit/767005e4b8de2b77907dc7e48cea4ce1e6c6ea05))

# [1.2.0](https://github.com/frankie336/projectdavid/compare/v1.1.11...v1.2.0) (2025-04-10)


### Features

* Add action required polling helper in runs client. ([2b41aec](https://github.com/frankie336/projectdavid/commit/2b41aec65e6107b61263019e75ccd18f247b9d5e))
* Add consumer function call execution client ([7cf5f5c](https://github.com/frankie336/projectdavid/commit/7cf5f5c4d289ef99906f7159cbbd04c1909cea39))

## [1.1.11](https://github.com/frankie336/projectdavid/compare/v1.1.10...v1.1.11) (2025-04-09)


### Bug Fixes

* event monitor handler and off issue ([24c9dc4](https://github.com/frankie336/projectdavid/commit/24c9dc41f307972ce00f070eb0fe2f2fb714f83d))

## [1.1.10](https://github.com/frankie336/projectdavid/compare/v1.1.9...v1.1.10) (2025-04-09)


### Bug Fixes

* restore inference.py 2 ([434969c](https://github.com/frankie336/projectdavid/commit/434969c95bf1b51e219cdd5d8594962d89bfcb05))

## [1.1.9](https://github.com/frankie336/projectdavid/compare/v1.1.8...v1.1.9) (2025-04-09)


### Bug Fixes

* pass key in set-up[#3](https://github.com/frankie336/projectdavid/issues/3) ([80e3462](https://github.com/frankie336/projectdavid/commit/80e3462266e64f084539274144ef95e86272150b))
* restore inference.py ([7619c54](https://github.com/frankie336/projectdavid/commit/7619c546fe30e69ba99799bef44c647c8f4a75c2))

## [1.1.8](https://github.com/frankie336/projectdavid/compare/v1.1.7...v1.1.8) (2025-04-09)


### Bug Fixes

* pass key in set-up[#2](https://github.com/frankie336/projectdavid/issues/2) ([d27bbeb](https://github.com/frankie336/projectdavid/commit/d27bbeb1453e0ac5454db87c74f31addc0e50a7b))

## [1.1.7](https://github.com/frankie336/projectdavid/compare/v1.1.6...v1.1.7) (2025-04-08)


### Bug Fixes

* stream timeout issue[#8](https://github.com/frankie336/projectdavid/issues/8) ([16d75c3](https://github.com/frankie336/projectdavid/commit/16d75c3e7d5efa31a18b86e4b0815f2f3d218656))

## [1.1.6](https://github.com/frankie336/projectdavid/compare/v1.1.5...v1.1.6) (2025-04-08)


### Bug Fixes

* stream timeout issue[#6](https://github.com/frankie336/projectdavid/issues/6) ([43e9d07](https://github.com/frankie336/projectdavid/commit/43e9d07f50d0b1785878ed0ee392b41c82acf57f))
* stream timeout issue[#7](https://github.com/frankie336/projectdavid/issues/7) ([a062765](https://github.com/frankie336/projectdavid/commit/a062765cb77efb71f8a54551cad3c37b54f8e5a3))

## [1.1.5](https://github.com/frankie336/projectdavid/compare/v1.1.4...v1.1.5) (2025-04-08)


### Bug Fixes

* stream timeout issue[#4](https://github.com/frankie336/projectdavid/issues/4) ([c01e345](https://github.com/frankie336/projectdavid/commit/c01e34572e946b20342aa7dac59c14a416c332da))
* stream timeout issue[#4](https://github.com/frankie336/projectdavid/issues/4) ([1173ded](https://github.com/frankie336/projectdavid/commit/1173ded023218ac1c1aae8936f11a32398f9b6a5))

## [1.1.4](https://github.com/frankie336/projectdavid/compare/v1.1.3...v1.1.4) (2025-04-08)


### Bug Fixes

* stream timeout issue. ([9639df6](https://github.com/frankie336/projectdavid/commit/9639df6536cfa9e9a36928615f411e9b393d0560))
* stream timeout issue[#3](https://github.com/frankie336/projectdavid/issues/3) ([074321a](https://github.com/frankie336/projectdavid/commit/074321a281f39cf909510f92d7730f6a4f66ebed))

## [1.1.3](https://github.com/frankie336/projectdavid/compare/v1.1.2...v1.1.3) (2025-04-08)


### Bug Fixes

* stream timeout issue. ([c35981b](https://github.com/frankie336/projectdavid/commit/c35981b378cb1f398c9eedf5e3b6e320b38000bb))
* stream timeout issue. ([cf3d813](https://github.com/frankie336/projectdavid/commit/cf3d8132e1730d57d2f778b171ba8b093349e2f0))
* stream timeout issue. ([e519f08](https://github.com/frankie336/projectdavid/commit/e519f08afea6d3daf34c200456196b1e84c4f16e))

## [1.1.2](https://github.com/frankie336/projectdavid/compare/v1.1.1...v1.1.2) (2025-04-08)


### Bug Fixes

* optional key param ([21e7d9a](https://github.com/frankie336/projectdavid/commit/21e7d9aac7f270625b1ef11522badf2d3ce2efb7))

## [1.1.1](https://github.com/frankie336/projectdavid/compare/v1.1.0...v1.1.1) (2025-04-08)


### Bug Fixes

* Global loop ([615cfe3](https://github.com/frankie336/projectdavid/commit/615cfe36462d628eec3d4211f318fc0714b119e8))
* Global loop ([e8e04ca](https://github.com/frankie336/projectdavid/commit/e8e04ca56083092f5b97a082b16fe4b438ac6ee4))

# [1.1.0](https://github.com/frankie336/projectdavid/compare/v1.0.26...v1.1.0) (2025-04-08)


### Features

* add support for passing provider api keys during synchronous streams ([48df025](https://github.com/frankie336/projectdavid/commit/48df025d2da7c229d70ab7a7cb93410dc2624f32))
* add support for passing provider api keys during synchronous streams ([d0333b1](https://github.com/frankie336/projectdavid/commit/d0333b13e6952c66cf386fa07282a496d4f9a3d5))

## [1.0.26](https://github.com/frankie336/projectdavid/compare/v1.0.25...v1.0.26) (2025-04-08)


### Bug Fixes

* dependency array ([2e8be32](https://github.com/frankie336/projectdavid/commit/2e8be32d7c03aa413eaffb90e54c4e17619fbc0f))
* dependency array ([63e7f1a](https://github.com/frankie336/projectdavid/commit/63e7f1a68b34dd082ca553efe8c449f8486b62d5))
* requirements.txt ([4d24aa4](https://github.com/frankie336/projectdavid/commit/4d24aa412ff43fdc3621c314b5e6fe3eab504cca))

## [1.0.25](https://github.com/frankie336/entitites_sdk/compare/v1.0.24...v1.0.25) (2025-04-08)


### Bug Fixes

* align-with-common ([810aae5](https://github.com/frankie336/entitites_sdk/commit/810aae55869d1f3bf73943f453962b8fa5a813c9))
* formatting ([31528ba](https://github.com/frankie336/entitites_sdk/commit/31528bac2b7b791113f37f92393fbfb1b589640b))
* formatting-isort ([d4ed068](https://github.com/frankie336/entitites_sdk/commit/d4ed0687be8544ab81cce302b18c3653e0fc758f))
* url ([70946f0](https://github.com/frankie336/entitites_sdk/commit/70946f065f3411b7d3b0425cbbb6c1e6e852af0b))

## [1.0.24](https://github.com/frankie336/entitites_sdk/compare/v1.0.23...v1.0.24) (2025-04-08)


### Bug Fixes

* name change-projectdavid ([0632dc7](https://github.com/frankie336/entitites_sdk/commit/0632dc74fc7b3a500365b95cde21c9dbc6d3e4fc))

## [1.0.23](https://github.com/frankie336/entitites_sdk/compare/v1.0.22...v1.0.23) (2025-04-08)


### Bug Fixes

* name change ([0c7d4dd](https://github.com/frankie336/entitites_sdk/commit/0c7d4ddd04538ee0d089bbf96e1aaffd65e67e81))

## [1.0.22](https://github.com/frankie336/entitites_sdk/compare/v1.0.21...v1.0.22) (2025-04-08)


### Bug Fixes

* name change ([654c9e9](https://github.com/frankie336/entitites_sdk/commit/654c9e936bf28d7e0c754c93ca9f5d68b16b4f36))

## [1.0.21](https://github.com/frankie336/entitites_sdk/compare/v1.0.20...v1.0.21) (2025-04-08)


### Bug Fixes

* workflow ([583145e](https://github.com/frankie336/entitites_sdk/commit/583145ec50ca882332613e802ae0c5f55c9122ce))

## [1.0.20](https://github.com/frankie336/entitites_sdk/compare/v1.0.19...v1.0.20) (2025-04-08)


### Bug Fixes

* black formatting. ([34572e3](https://github.com/frankie336/entitites_sdk/commit/34572e32c5858bda4b19efbc21455609d79a2c84))
* conditional release in ci. ([22242ee](https://github.com/frankie336/entitites_sdk/commit/22242ee05ea0ca5552b82d56c7ac7fcb2bba0ad7))
* def _internal_add_file_to_vector_store_async-validation-type ([fa97c40](https://github.com/frankie336/entitites_sdk/commit/fa97c4064ea542601199b117f6c4a1d6a6e69fa6))
* entities release.json ([884a2b5](https://github.com/frankie336/entitites_sdk/commit/884a2b56aa6d864dab45a718ae135bcef7206895))
* entities release.json2 ([8c0c8d6](https://github.com/frankie336/entitites_sdk/commit/8c0c8d6c078fa04c4aeb230a1680e430c379c7a4))
* entities release.json3 ([0c09a5f](https://github.com/frankie336/entitites_sdk/commit/0c09a5ff942cfd02b86906feb8cb8775e02a6a08))
* entities version in requirements.txt. ([34d7394](https://github.com/frankie336/entitites_sdk/commit/34d7394199b86692ef4ddaa4b5c6cd721afefe81))
* entities version in requirements.txt2. ([bd47a4c](https://github.com/frankie336/entitites_sdk/commit/bd47a4c8071fedec21c7418c5c7da5c3ee76711b))
* entities version in requirements.txt3. ([3d49ff9](https://github.com/frankie336/entitites_sdk/commit/3d49ff9d20271c6bb02f01f622e7b8bffdb81d24))
* entities_common version. ([edd6cd2](https://github.com/frankie336/entitites_sdk/commit/edd6cd24bf5d3fd16c2fa159316e166f347605d6))
* isort ([072f3c4](https://github.com/frankie336/entitites_sdk/commit/072f3c430903c778d8504524f4b220d99aaaa0a3))
* isort import order ([6595b0d](https://github.com/frankie336/entitites_sdk/commit/6595b0d7e1ba800d06e85f32d3dfa793541ff9b6))
* isort imports ([0a16a41](https://github.com/frankie336/entitites_sdk/commit/0a16a41b68160f7afffe1d951879ad01d9f84c55))
* isort imports3 ([fe515b1](https://github.com/frankie336/entitites_sdk/commit/fe515b14e804b4381eed23e2568a980b051c76ed))
* publish ([6eee97a](https://github.com/frankie336/entitites_sdk/commit/6eee97ad114cd4f119a9e6610b8981c8739d9eaa))
* remove non release branch from CI logic ([4e37ece](https://github.com/frankie336/entitites_sdk/commit/4e37ece55899dd64ee666cb6327393d5fc9316f2))
* remove non release branch from CI logic2 ([db1bb94](https://github.com/frankie336/entitites_sdk/commit/db1bb9422cc70326001f14ee82df4963c6c3a954))
* run black formatting. ([babcdf1](https://github.com/frankie336/entitites_sdk/commit/babcdf178ee3ce5e159b890dca64a10350f2e70e))
* scripts/update_pyproject_version.py ([ee62a49](https://github.com/frankie336/entitites_sdk/commit/ee62a49866c1a36058e56ca801556a0c533b95d1))
* toml file path ([f1ec5b4](https://github.com/frankie336/entitites_sdk/commit/f1ec5b4df7c5ad02cf811f5fb9dcd956045defe6))

## [1.0.19](https://github.com/frankie336/entitites_sdk/compare/v1.0.18...v1.0.19) (2025-04-07)


### Bug Fixes

* def _internal_add_file_to_vector_store_async-validation-type ([bd21178](https://github.com/frankie336/entitites_sdk/commit/bd2117874842e52d403aff905cc44944166ac46d))

## [1.0.18](https://github.com/frankie336/entitites_sdk/compare/v1.0.17...v1.0.18) (2025-04-07)


### Bug Fixes

* def _internal_add_file_to_vector_store_async ([60e88b3](https://github.com/frankie336/entitites_sdk/commit/60e88b35cf53aad55c17d4376282c5aa5c689efa))

## [1.0.17](https://github.com/frankie336/entitites_sdk/compare/v1.0.16...v1.0.17) (2025-04-07)


### Bug Fixes

* store_name param ([3fc8b50](https://github.com/frankie336/entitites_sdk/commit/3fc8b5047b103b1860c26cbe82efa77cdd1bda91))

## [1.0.16](https://github.com/frankie336/entitites_sdk/compare/v1.0.15...v1.0.16) (2025-04-07)


### Bug Fixes

* store_name param ([d991581](https://github.com/frankie336/entitites_sdk/commit/d9915812dae6aa00d819b81f62a49a09154ee348))

## [1.0.15](https://github.com/frankie336/entitites_sdk/compare/v1.0.14...v1.0.15) (2025-04-06)


### Bug Fixes

* Vector store collection name issue ([eed4db5](https://github.com/frankie336/entitites_sdk/commit/eed4db5c3dcffbdc5a9b11d3495bec3e18706825))

## [1.0.14](https://github.com/frankie336/entitites_sdk/compare/v1.0.13...v1.0.14) (2025-04-06)


### Bug Fixes

* Migrate vector store endpoints ([7efbeea](https://github.com/frankie336/entitites_sdk/commit/7efbeeaebf0306f7f6d6d62c47f878e586c161d9))

## [1.0.13](https://github.com/frankie336/entitites_sdk/compare/v1.0.12...v1.0.13) (2025-04-06)


### Bug Fixes

* add sentence-transformers dependency to toml ([0c684b5](https://github.com/frankie336/entitites_sdk/commit/0c684b558c2c8b1b018ddd0a52b2052ee5ae4b99))

## [1.0.12](https://github.com/frankie336/entitites_sdk/compare/v1.0.11...v1.0.12) (2025-04-06)


### Bug Fixes

* add validators dependency ([2c52f21](https://github.com/frankie336/entitites_sdk/commit/2c52f212035ed9245540d93df064aedf4a2cb7e0))

## [1.0.11](https://github.com/frankie336/entitites_sdk/compare/v1.0.10...v1.0.11) (2025-04-06)


### Bug Fixes

* README.md with correct badge ([a59df73](https://github.com/frankie336/entitites_sdk/commit/a59df73a289e5847d2246686da448ab1d4ad257c))

## [1.0.10](https://github.com/frankie336/entitites_sdk/compare/v1.0.9...v1.0.10) (2025-04-06)


### Bug Fixes

* Add missing dependencies to toml ([5a78cdc](https://github.com/frankie336/entitites_sdk/commit/5a78cdc170390ffcc95f85aba000e9868a7d33db))

## [1.0.9](https://github.com/frankie336/entitites_sdk/compare/v1.0.8...v1.0.9) (2025-04-06)


### Bug Fixes

* _version.py relative import error ([96a5be4](https://github.com/frankie336/entitites_sdk/commit/96a5be4dd5ad85bb158332c7ca86dfe87151af31))

## [1.0.8](https://github.com/frankie336/entitites_sdk/compare/v1.0.7...v1.0.8) (2025-04-06)


### Bug Fixes

* test_tag_release.yml ([53bb318](https://github.com/frankie336/entitites_sdk/commit/53bb3186d60dfc38ba76c3180cc064a3f193d42e))

## [1.0.7](https://github.com/frankie336/entitites_sdk/compare/v1.0.6...v1.0.7) (2025-04-06)


### Bug Fixes

* update workflow to use new trusted publisher and build flow ([1179def](https://github.com/frankie336/entitites_sdk/commit/1179def6e74ef2cbcb4dc570cd76d239ad84e1b2))

## [1.0.6](https://github.com/frankie336/entitites_sdk/compare/v1.0.5...v1.0.6) (2025-04-06)


### Bug Fixes

* align pyproject version to v1.0.5 ([e8d12e0](https://github.com/frankie336/entitites_sdk/commit/e8d12e0e86f46d745a8b8731c7e663180e04c143))

## [1.0.5](https://github.com/frankie336/entitites_sdk/compare/v1.0.4...v1.0.5) (2025-04-06)


### Bug Fixes

* bump version to 1.0.4 ([37650d9](https://github.com/frankie336/entitites_sdk/commit/37650d948585fa3e176016b49dcad2967c83a4f2))
* Test workflow-8 ([cc0c25e](https://github.com/frankie336/entitites_sdk/commit/cc0c25ef60732bd28d5d70ad6554745439124cf4))

## [1.0.4](https://github.com/frankie336/entitites_sdk/compare/v1.0.3...v1.0.4) (2025-04-06)


### Bug Fixes

* Test workflow-3 ([0fb760c](https://github.com/frankie336/entitites_sdk/commit/0fb760c0a3dbc2a7e43256ad891e900808cf0eac))

## [1.0.3](https://github.com/frankie336/entitites_sdk/compare/v1.0.2...v1.0.3) (2025-04-06)


### Bug Fixes

* Test workflow-2 ([cc8730f](https://github.com/frankie336/entitites_sdk/commit/cc8730f290b2b2a3ff10f3fc76092650debcbb5f))

## [1.0.2](https://github.com/frankie336/entitites_sdk/compare/v1.0.1...v1.0.2) (2025-04-06)


### Bug Fixes

* Test workflow ([afc8e6b](https://github.com/frankie336/entitites_sdk/commit/afc8e6b4e036baa5f4a66a5bf8bed62c2ec2fde7))

## [1.0.1](https://github.com/frankie336/entitites_sdk/compare/v1.0.0...v1.0.1) (2025-04-06)


### Bug Fixes

* entities_common version issue again ([6dc6c45](https://github.com/frankie336/entitites_sdk/commit/6dc6c4500c81e61278bdb0254881cc1dfc537798))

# 1.0.0 (2025-04-06)


### Bug Fixes

* Fix auto release ([a9a1b2e](https://github.com/frankie336/entitites_sdk/commit/a9a1b2e0d03a707be0510e171fd57cb0c3c7d5f2))
* Require latest entities_common in toml ([6ca402b](https://github.com/frankie336/entitites_sdk/commit/6ca402b0532946eef68e93862324d281e181cc39))
* resolve entities_common version issue ([6b64ef6](https://github.com/frankie336/entitites_sdk/commit/6b64ef6bdde7f21245a728d106d3f95daa1422b9))


### Features

* add support for auto version tagging ([5ea9aed](https://github.com/frankie336/entitites_sdk/commit/5ea9aed79fa4f37789c463458409126d60da2388))

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.3.1] - 2025-04-05

### Added
- Trusted publishing setup for PyPI and TestPyPI, including GitHub Actions workflow with tag-based trigger.
- `scripts/pin_entities_common.py`: utility to pin latest commit SHA from `entities_common` into `pyproject.toml` and `requirements.txt`.
- CI workflow `pin-dependencies.yml` that auto-pins `entities_common` on each push to `main`.

### Fixed
- Flake8 linting issues across `file_processor.py` due to missing typing imports.
- `LiteralString` fallback import for Python < 3.11 environments.
- Typos and inconsistencies in GitHub workflow tags (`test-v*` vs `v*`) that prevented job execution.

### Changed
- Replaced dynamic `entities_common` Git dependency with pinned SHA references.
- Made the `publish` workflow fully conformant with [Trusted Publishing](https://docs.pypi.org/trusted-publishers/).



## [0.3.0] - 2025-04-04

### Added
- Introduced `RunMonitorClient` with full lifecycle event handling for assistant runs.
- Added `EntitiesInternalInterface` as a unified internal service orchestrator.
- `ActionsClient`, `MessagesClient`, `RunsClient`, and `VectorStoreClient` now wrapped and lazy-loaded under `Entities(...)`.
- Support for tool invocation streaming with `on_action_required`, `on_tool_invoked`, and `on_complete` callbacks.
- `code_interpreter_stream` and `file_download_url` support in SSE stream parsing.

### Changed
- Moved `EntitiesEventHandler` logic from Flask backend into internal API and SDK boundary.
- enties_common package is now an auto installed dependency. No meed to install it directly.

---

## [0.2.0] - 2025-03-01

### Added

---

## [0.1.0-alpha] - 2025-01-15

### Added
- Core SDK skeleton: `Entities`, `UsersClient`, `MessagesClient`, etc.
- Basic message submission and tool output lifecycle.
- Initial assistant threading and function call support.
