# Francis Agent
![CI](https://github.com/Ap3pp3rs94/francis-agent/actions/workflows/ci.yml/badge.svg)
![CI](https://github.com/Ap3pp3rs94/francis-agent/actions/workflows/ci.yml/badge.svg)

Local autonomy loop with tools (files, gitops, httpjson, kvstore, search, shell, web).

## Quickstart
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\francis.py

## Dev
pre-commit install
pre-commit run --all-files
pytest -q



## CLI

`ash
francis --version
francis
``r

