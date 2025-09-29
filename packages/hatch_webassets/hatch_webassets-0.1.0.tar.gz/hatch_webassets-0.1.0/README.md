# hatch_webassets

<!-- TODO: Make it work, make it right, make it fast. -->

[![CI](https://github.com/hasansezertasan/hatch_webassets/actions/workflows/ci.yml/badge.svg)](https://github.com/hasansezertasan/hatch_webassets/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/hatch_webassets.svg)](https://pypi.org/project/hatch_webassets)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch_webassets.svg)](https://pypi.org/project/hatch_webassets)
[![License - MIT](https://img.shields.io/github/license/hasansezertasan/hatch_webassets.svg)](https://opensource.org/licenses/MIT)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/hatch_webassets)](https://github.com/hasansezertasan/hatch_webassets)

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![GitHub Tag](https://img.shields.io/github/tag/hasansezertasan/hatch_webassets?include_prereleases=&sort=semver&color=black)](https://github.com/hasansezertasan/hatch_webassets/releases/)

[![Downloads](https://pepy.tech/badge/hatch_webassets)](https://pepy.tech/project/hatch_webassets)
[![Downloads/Month](https://pepy.tech/badge/hatch_webassets/month)](https://pepy.tech/project/hatch_webassets)
[![Downloads/Week](https://pepy.tech/badge/hatch_webassets/week)](https://pepy.tech/project/hatch_webassets)

> **hatch_webassets** is a build-hook for webassets.

-----

## Table of Contents

- [Usage](#usage)
- [Support](#support-heart)
- [Author](#author-person_with_crown)
- [Contributing](#contributing-heart)
- [License](#license-scroll)
- [Changelog](#changelog-memo)

## Usage

```toml
[build-system]
requires = ["hatchling", "hatch_webassets"]
build-backend = "hatchling.build"
```

## Support :heart:

If you have any questions or need help, feel free to open an issue on the [GitHub repository][hatch_webassets].

## Author :person_with_crown:

<!-- # TODO @hasansezertasan: Update the author name. -->
This project is maintained by [Hasan Sezer Taşan][author], It's me :wave:

## Contributing :heart:

Any contributions are welcome! Please follow the [Contributing Guidelines](./CONTRIBUTING.md) to contribute to this project.

<!-- xc-heading -->
## Development :toolbox:

Clone the repository and cd into the project directory:

```sh
git clone https://github.com/hasansezertasan/hatch_webassets
cd hatch_webassets
```

The commands below can also be executed using the [xc task runner](https://xcfile.dev/), which combines the usage instructions with the actual commands. Simply run `xc`, it will pop up an interactive menu with all available tasks.

### `install`

Install the dependencies:

```sh
uv sync
```

### `style`

Run the style checks:

```sh
uv run --locked tox run -e style
```

### `ci`

Run the CI pipeline:

```sh
uv run --locked tox run
```

## License :scroll:

This project is licensed under the [MIT License](https://spdx.org/licenses/MIT.html).

## Changelog :memo:

For a detailed list of changes, please refer to the [CHANGELOG](./CHANGELOG.md).

<!-- Refs -->
[author]: https://github.com/hasansezertasan
[hatch_webassets]: https://github.com/hasansezertasan/hatch_webassets
