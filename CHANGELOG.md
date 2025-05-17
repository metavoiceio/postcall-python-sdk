# Changelog

## 0.1.0-alpha.4 (2025-05-17)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/metavoiceio/postcall-python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Bug Fixes

* **package:** support direct resource imports ([4b04db6](https://github.com/metavoiceio/postcall-python-sdk/commit/4b04db64aafc1779bfdde44741ecb5ef0e8bc7fa))
* **perf:** optimize some hot paths ([ecb9584](https://github.com/metavoiceio/postcall-python-sdk/commit/ecb9584f8036124fc3ddb790137a9b89eb831b6e))
* **perf:** skip traversing types for NotGiven values ([8aa6646](https://github.com/metavoiceio/postcall-python-sdk/commit/8aa664658cb5ef7f5e1ce83879153a5bfc13bb51))
* **pydantic v1:** more robust ModelField.annotation check ([9f21dda](https://github.com/metavoiceio/postcall-python-sdk/commit/9f21dda26442323bf3593e01ae9881e0538b87cd))


### Chores

* broadly detect json family of content-type headers ([b1102cc](https://github.com/metavoiceio/postcall-python-sdk/commit/b1102cc444c038685fc5054ce1640f106c00809e))
* **ci:** add timeout thresholds for CI jobs ([8543410](https://github.com/metavoiceio/postcall-python-sdk/commit/85434108fded1daf5474c27c14d08007f3314ed2))
* **ci:** fix installation instructions ([f1e5b1b](https://github.com/metavoiceio/postcall-python-sdk/commit/f1e5b1bbb1fd583b098b53f1471eff930b89959e))
* **ci:** only use depot for staging repos ([7c65d52](https://github.com/metavoiceio/postcall-python-sdk/commit/7c65d52cf380e558f08e674fa181ab4118aa4814))
* **ci:** upload sdks to package manager ([789f72e](https://github.com/metavoiceio/postcall-python-sdk/commit/789f72e6148887ce95e81cb0d1ec23d1706778ba))
* **client:** minor internal fixes ([d24355f](https://github.com/metavoiceio/postcall-python-sdk/commit/d24355f4724c10a740b0f194bcdf10c4972beb38))
* fix typos ([#14](https://github.com/metavoiceio/postcall-python-sdk/issues/14)) ([eb2a3c0](https://github.com/metavoiceio/postcall-python-sdk/commit/eb2a3c098ebfe67e716367b3224f738b11707d16))
* **internal:** avoid errors for isinstance checks on proxies ([95d0df1](https://github.com/metavoiceio/postcall-python-sdk/commit/95d0df148fe419a337a1f93c90990081073a45bd))
* **internal:** base client updates ([dee6c3e](https://github.com/metavoiceio/postcall-python-sdk/commit/dee6c3ef9c7292359f6ac2bab4357a1b2b2b87c3))
* **internal:** bump pyright version ([879292d](https://github.com/metavoiceio/postcall-python-sdk/commit/879292dba00b4e72ad92cddf7d04705044214b99))
* **internal:** codegen related update ([e7d87d4](https://github.com/metavoiceio/postcall-python-sdk/commit/e7d87d4dbd4f05cf2267a140395b37a991c18da2))
* **internal:** codegen related update ([1129dd7](https://github.com/metavoiceio/postcall-python-sdk/commit/1129dd74e4a72ab42e3f29796710a4a2c449e8cb))
* **internal:** expand CI branch coverage ([3a957ac](https://github.com/metavoiceio/postcall-python-sdk/commit/3a957ac21c2e4b83edc8987202c6a4e777a86a40))
* **internal:** fix list file params ([a21db39](https://github.com/metavoiceio/postcall-python-sdk/commit/a21db3954c633e41cafeb2ee0592d93099c2843a))
* **internal:** import reformatting ([dff6dbc](https://github.com/metavoiceio/postcall-python-sdk/commit/dff6dbc5b2174dc22d61bdfbf956fa15a3bec444))
* **internal:** reduce CI branch coverage ([d430c9e](https://github.com/metavoiceio/postcall-python-sdk/commit/d430c9e7721e788a4d7f07be09f4db0c2fdfc2fd))
* **internal:** refactor retries to not use recursion ([2240d34](https://github.com/metavoiceio/postcall-python-sdk/commit/2240d34cf754144f04c2805bce70547037be914c))
* **internal:** remove trailing character ([#16](https://github.com/metavoiceio/postcall-python-sdk/issues/16)) ([6767b9e](https://github.com/metavoiceio/postcall-python-sdk/commit/6767b9ecc2264d69984db9d7fa59c34a672487c0))
* **internal:** slight transform perf improvement ([#17](https://github.com/metavoiceio/postcall-python-sdk/issues/17)) ([4e0ac65](https://github.com/metavoiceio/postcall-python-sdk/commit/4e0ac65d5cd7f3233705312152ded82d84771682))
* **internal:** update models test ([0b4fc44](https://github.com/metavoiceio/postcall-python-sdk/commit/0b4fc44e40883a30180ac46971af0e4ce4d22d3e))
* **internal:** update pyright settings ([ad15860](https://github.com/metavoiceio/postcall-python-sdk/commit/ad15860a9f338e088392dcfca63c19e71303faf3))

## 0.1.0-alpha.3 (2025-03-19)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/metavoiceio/postcall-python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#11](https://github.com/metavoiceio/postcall-python-sdk/issues/11)) ([00c5f40](https://github.com/metavoiceio/postcall-python-sdk/commit/00c5f405a91c400e4cfad5062398fe5947f2e3f5))

## 0.1.0-alpha.2 (2025-03-19)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/metavoiceio/postcall-python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#8](https://github.com/metavoiceio/postcall-python-sdk/issues/8)) ([8b9b40a](https://github.com/metavoiceio/postcall-python-sdk/commit/8b9b40a95c95e84363d0bbb71fb9410df03890ec))

## 0.1.0-alpha.1 (2025-03-19)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/metavoiceio/postcall-python-sdk/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#5](https://github.com/metavoiceio/postcall-python-sdk/issues/5)) ([2f47478](https://github.com/metavoiceio/postcall-python-sdk/commit/2f474789c2baf98490d1c6910753cda277f93f00))

## 0.0.1-alpha.1 (2025-03-19)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/metavoiceio/postcall-python-sdk/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* go live ([#1](https://github.com/metavoiceio/postcall-python-sdk/issues/1)) ([ee787d6](https://github.com/metavoiceio/postcall-python-sdk/commit/ee787d6527f5fe40e13517bed9db41ff7092f4a1))
* update SDK settings ([#3](https://github.com/metavoiceio/postcall-python-sdk/issues/3)) ([3a7b65d](https://github.com/metavoiceio/postcall-python-sdk/commit/3a7b65d79f35f9b64843dfc6ca449bb5e22f6c1f))
