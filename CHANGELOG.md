# Changelog

## 1.2.0 (2026-01-24)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/morta-technology/morta-python/compare/v1.1.0...v1.2.0)

### Features

* **client:** add support for binary request streaming ([c8fbb1d](https://github.com/morta-technology/morta-python/commit/c8fbb1d243b5db1c8e2cdcc4ae73c562c9cc8cc0))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([a45cd02](https://github.com/morta-technology/morta-python/commit/a45cd022a8cb4f5d5ffc74b3ba8af948417e6638))
* use async_to_httpx_files in patch method ([f84efeb](https://github.com/morta-technology/morta-python/commit/f84efeb47c0f4bfcc3847374e263e157ffe3d029))


### Chores

* add missing docstrings ([be6aaea](https://github.com/morta-technology/morta-python/commit/be6aaea7d82a3706cba1b08b1dbe1ca7abdcd0c4))
* **ci:** upgrade `actions/github-script` ([8991d7e](https://github.com/morta-technology/morta-python/commit/8991d7e976790571555b634ed03e747d92b4df1c))
* **docs:** use environment variables for authentication in code snippets ([4cde93c](https://github.com/morta-technology/morta-python/commit/4cde93c98bb07a05cfa5526f98ca5ddb0d9a5c85))
* **internal:** add `--fix` argument to lint script ([bcef260](https://github.com/morta-technology/morta-python/commit/bcef260b322dcf4fbee19088d07512d25d046740))
* **internal:** add missing files argument to base client ([684fe1f](https://github.com/morta-technology/morta-python/commit/684fe1f49cba936d1c596136cce6c8efc127a64f))
* **internal:** codegen related update ([9878244](https://github.com/morta-technology/morta-python/commit/9878244b095697b0180177fe97c24c6d5c5d847f))
* **internal:** update `actions/checkout` version ([0b78808](https://github.com/morta-technology/morta-python/commit/0b78808fd5bdcbb66c36c2b247a1dba13a4a2d69))
* speedup initial import ([5d44502](https://github.com/morta-technology/morta-python/commit/5d44502fe3f2cd8e612eee4778b9de2ea763f6be))
* update lockfile ([06335c1](https://github.com/morta-technology/morta-python/commit/06335c15214b25e0e0c7ef5098bf7bc6137dab6d))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([933889f](https://github.com/morta-technology/morta-python/commit/933889f5f03b7532d670a2df0ba3929f40456407))

## 1.1.0 (2025-11-28)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/morta-technology/morta-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** manual updates ([87d9617](https://github.com/morta-technology/morta-python/commit/87d9617d5073b1eeb1ab5ab745524f6707f457c2))
* **api:** update via SDK Studio ([51a28e2](https://github.com/morta-technology/morta-python/commit/51a28e20d7932829c70b525d1ae062af9f9704fa))
* **api:** update via SDK Studio ([7d97ebc](https://github.com/morta-technology/morta-python/commit/7d97ebc692232d98acc8f9caecaf168dcecee42c))
* **api:** update via SDK Studio ([f139f40](https://github.com/morta-technology/morta-python/commit/f139f407bead2fabc27eee4b461e505955946e14))
* **api:** update via SDK Studio ([187ac6b](https://github.com/morta-technology/morta-python/commit/187ac6bcf5d2f9d87d5b6396aec0fbeaed22303a))
* **api:** update via SDK Studio ([555c015](https://github.com/morta-technology/morta-python/commit/555c0158594461bfa92fe202f29e085b3694173d))
* **api:** update via SDK Studio ([3e1c49f](https://github.com/morta-technology/morta-python/commit/3e1c49fdee2931f50ee438473ac1c8335b1bcf82))
* **api:** update via SDK Studio ([cd2a93b](https://github.com/morta-technology/morta-python/commit/cd2a93b3c7f583266a1133caf9d6a66d03ab39eb))
* clean up environment call outs ([0136c74](https://github.com/morta-technology/morta-python/commit/0136c747916fecbbc2fb3cb78a616aad53d7ad33))
* **client:** support file upload requests ([90cab0f](https://github.com/morta-technology/morta-python/commit/90cab0f72fa0e00ad480939b857bcdc9e93ab13b))


### Bug Fixes

* add missing import ([dce0033](https://github.com/morta-technology/morta-python/commit/dce003323f297f74ebc88bb0930fb193daf2d0c6))
* **ci:** correct conditional ([8e8245e](https://github.com/morta-technology/morta-python/commit/8e8245e16903f7c4e0b13046cc5af18cb587c3e3))
* **client:** don't send Content-Type header on GET requests ([582fe1d](https://github.com/morta-technology/morta-python/commit/582fe1d68576f8c3d120208dbab848317c82ff0f))
* **parsing:** correctly handle nested discriminated unions ([eb07229](https://github.com/morta-technology/morta-python/commit/eb07229eb9eca1f69e2513cb7fb11d9febe7b602))
* **parsing:** ignore empty metadata ([f0847f2](https://github.com/morta-technology/morta-python/commit/f0847f26b421ea6c59555bb462450966bdf7543f))
* **parsing:** parse extra field types ([2a2742e](https://github.com/morta-technology/morta-python/commit/2a2742e0bc889c05925e12c0b854ee1373f757d2))


### Chores

* **ci:** change upload type ([db50c30](https://github.com/morta-technology/morta-python/commit/db50c30df7906a4476166b499dba85a071e2a446))
* **ci:** only run for pushes and fork pull requests ([9f98261](https://github.com/morta-technology/morta-python/commit/9f98261cc65c3207abbd7a72f20b69059d96593f))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([8b71f21](https://github.com/morta-technology/morta-python/commit/8b71f2157e467b447fa6003ba9ca25dce4b53846))
* **internal:** bump pinned h11 dep ([453cc7e](https://github.com/morta-technology/morta-python/commit/453cc7eafb0992a051b734ee01ef3101c8e3928f))
* **internal:** change ci workflow machines ([2dc7f05](https://github.com/morta-technology/morta-python/commit/2dc7f05dc3e59e98ebabe944f88f2e692827bba7))
* **internal:** codegen related update ([ea99d66](https://github.com/morta-technology/morta-python/commit/ea99d66b38e92f8bae30f47992330622ebf42db1))
* **internal:** codegen related update ([3e6e3a5](https://github.com/morta-technology/morta-python/commit/3e6e3a5da56c47a4b1f85c235c0a70f61039624b))
* **internal:** codegen related update ([28d45cf](https://github.com/morta-technology/morta-python/commit/28d45cf53a91ffd3d8bd21349d4812ecb999b954))
* **internal:** codegen related update ([ffb23d1](https://github.com/morta-technology/morta-python/commit/ffb23d11f9d793c991d01d8cad82fcc3b8477ef0))
* **internal:** codegen related update ([782ade2](https://github.com/morta-technology/morta-python/commit/782ade2ec9b9bffcb3b79d922f0df2c29619c39f))
* **internal:** codegen related update ([d71d014](https://github.com/morta-technology/morta-python/commit/d71d014f4d35a0ddb2fa10f560506ad669c0d609))
* **internal:** codegen related update ([799b166](https://github.com/morta-technology/morta-python/commit/799b1665f28527b3797c0cf0947162e71e369e2e))
* **internal:** codegen related update ([ba95f8b](https://github.com/morta-technology/morta-python/commit/ba95f8b18e234628eb8e8ac8237b7903444d466f))
* **internal:** codegen related update ([506b519](https://github.com/morta-technology/morta-python/commit/506b5197799007e81de3caa37b7b76ae87a3000d))
* **internal:** fix ruff target version ([4b65407](https://github.com/morta-technology/morta-python/commit/4b65407db4f011b75179f81d46bb3926e86a1b4a))
* **internal:** update comment in script ([7edbbee](https://github.com/morta-technology/morta-python/commit/7edbbee80e0f2b7306e3a50d6aaef01253cfd086))
* **package:** mark python 3.13 as supported ([ed4b882](https://github.com/morta-technology/morta-python/commit/ed4b882fa175494dcfc81c499cc0c79ed6a16db5))
* **project:** add settings file for vscode ([ba59cce](https://github.com/morta-technology/morta-python/commit/ba59ccec85c57ef0bb2d57755faaa387edf10319))
* **readme:** fix version rendering on pypi ([656d8ef](https://github.com/morta-technology/morta-python/commit/656d8ef9ab9ce19be4b76b12a267dbaa7ae1e28c))
* **types:** rebuild Pydantic models after all types are defined ([9bc2e47](https://github.com/morta-technology/morta-python/commit/9bc2e472cd3b1f4963aba811eaa74480c16bb41f))
* update @stainless-api/prism-cli to v5.15.0 ([214b6fc](https://github.com/morta-technology/morta-python/commit/214b6fcab026c50fe36b7dea3ca1251147e7c94b))
* update github action ([cf6b8ea](https://github.com/morta-technology/morta-python/commit/cf6b8ea3c91f032be8160935857c0395e96c865d))

## 1.0.1 (2025-06-26)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/morta-technology/morta-python/compare/v1.0.0...v1.0.1)

### Chores

* **internal:** version bump ([be7f940](https://github.com/morta-technology/morta-python/commit/be7f940aaeda2822a62b99dfb104382339eec02a))

## 1.0.0 (2025-06-26)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/morta-technology/morta-python/compare/v0.0.1-alpha.0...v1.0.0)

### Features

* **api:** update via SDK Studio ([fbe90a4](https://github.com/morta-technology/morta-python/commit/fbe90a422219e7bf6fa27833113ee7ba30de6bca))
* **api:** update via SDK Studio ([d746540](https://github.com/morta-technology/morta-python/commit/d7465407e3c85df6c50a551d01334c92e2018527))
* **api:** update via SDK Studio ([c6a3d90](https://github.com/morta-technology/morta-python/commit/c6a3d9022dbf2e361a1f9eb7aa6ee6bec40bcb50))
* **api:** update via SDK Studio ([64662fe](https://github.com/morta-technology/morta-python/commit/64662fe4bfaaaf55d68eea713c41d3da27fdf811))
* **api:** update via SDK Studio ([49bf91d](https://github.com/morta-technology/morta-python/commit/49bf91da48c0493062e21e0a337d57274acd03aa))
* **api:** update via SDK Studio ([5d8ff4c](https://github.com/morta-technology/morta-python/commit/5d8ff4c174a5eb3e909fea14aef4bab234c92d81))


### Chores

* update SDK settings ([479021a](https://github.com/morta-technology/morta-python/commit/479021aaf3477e524f07504563b1ef82e325ff67))
* update SDK settings ([a7aea8e](https://github.com/morta-technology/morta-python/commit/a7aea8e6bdeb8c180268d1ac7e08cac5388fab61))
