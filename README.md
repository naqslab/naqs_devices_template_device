# naqs_devices_template_device

This repository is both a template to follow for a labscript-device belonging
to a namespace (here `naqs_devices`) as well as a github template repository.
Use the green `Use this template` button above to copy the files and structure
of this repository to fit your new device. You will need to modify at least
`pyproject.toml`, `README.md`, `index.rst`, `conf.py`, and everything in `src/`.

## Directory structure

```text

└── naqs_devices_template_device/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE.txt # Choose a license, labscript uses BSD
    ├── CITATION.cff # Optional to define citation for citing the device repository
    ├── docs/
    │   ├── conf.py
    │   ├── make.bat
    │   ├── Makefile
    │   └── index.rst
    └── src/naqs_devices/ # note: must be same as in the parent naqs_devices repo to be in the same namespace
        └── TemplateDevice/
            ├── __init__.py
            ├── blacs_tabs.py
            ├── blacs_workers.py
            ├── labscript_devices.py
            ├── register_classes.py
            └── runviewer_parsers.py
```

## How to document your device

To work within the labscript paradigm, we enforce that you write all
specification related documentation in the top-level README.md (here). Then,
any API related documentation should go in the `docs/index.rst`. The project
is structured and has the machinery so that the device can be hosted on Read
The Docs. This is optional and requires extra configuration steps as outlined
in the [RTD Docs](https://docs.readthedocs.com/platform/latest/tutorial/index.html).
