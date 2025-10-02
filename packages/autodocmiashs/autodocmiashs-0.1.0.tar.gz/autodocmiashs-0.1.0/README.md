# autodocmiashs

One-command docstring generator using **Mistral (mistral-small-latest)** that writes
Google-style docstrings into your Python files under `src/`.

## Quick start (local dev)

```bash
# from project root
python -m pip install -e .
export MISTRAL_API_KEY="xq-..."   # put your key here

# run inside ANY project that has a src/ folder
autodocmiashs
