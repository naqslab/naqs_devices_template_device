# naqs_devices_template_device

This repository is both a template to follow for a labscript-device belonging
to a namespace (here `naqs_devices`) as well as a github template repository.
Use the green `Use this template` button above to copy the files and structure
of this repository to fit your new device. We denote what lines in
configuration files (such as `pyproject.toml`) should be edited when using this
repository as a template with `# EDITME`

## Directory structure

```text

└── naqs_devices_template_device/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE.txt
    ├── CITATION.cff
    ├── src/naqs_devices/ # note: must be same as in the parent naqs_devices repo to be in the same namespace
    │   └── TemplateDevice/
    │       ├── __init__.py
    │       ├── register_classes.py
    │       ├── labscript_devices.py
    │       ├── blacs_tabs.py
    │       ├── blacs_workers.py
    │       └── runviewer_parsers.py
    └── docs/
        └── index.rst

```

## How to document your device

To work within the labscript paradigm, we enforce that you write all
specification related documentation in the top-level README.md (here). Then,
any API related documentation should go in the `docs/index.rst`.
