# init-mater-project

[![PyPI version](https://img.shields.io/pypi/v/init-mater-project.svg)](https://pypi.org/project/init-mater-project/)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
![Coverage](https://gricad-gitlab.univ-grenoble-alpes.fr/isterre-dynamic-modeling/mater-project/init-mater-project/badges/main/coverage.svg)
[![MATER](https://img.shields.io/badge/framework-MATER-orange.svg)](https://isterre-dynamic-modeling.gricad-pages.univ-grenoble-alpes.fr/mater-project/mater)
[![UV](https://img.shields.io/badge/managed_by-UV-blue.svg)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/license-LGPLv3-blue.svg)](LICENSE)

**CLI tool to transform raw datasets into MATER-ready data and run your own MATER simulations.**

## Quick Start

```bash
# Run without install — recommended
uvx init-mater-project my-simulation
# Or 
pipx run init-mater-project my-simulation

# Navigate and start
cd my-simulation
uv run mater-cli run --example
```

`init-mater-project` creates a complete MATER project with:
- Configuration templates
- Data pipeline structure  
- CLI toolchain
- Example datasets
- Documentation

## Documentation

- **[Detailed Documentation](link-to-come)** — MkDocs with configuration, user guide, developer guide, testing, deployment, architecture
- **[Contributing](https://gricad-gitlab.univ-grenoble-alpes.fr/isterre-dynamic-modeling/mater-project/init-mater-project/-/blob/main/CONTRIBUTING.md)** — Contribution guidelines
- **[License](https://gricad-gitlab.univ-grenoble-alpes.fr/isterre-dynamic-modeling/mater-project/init-mater-project/-/blob/main/LICENSE)** — LGPLv3 License details