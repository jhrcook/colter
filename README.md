# Simple app to notify me when Colter Thorofare Nets are back in stock

Originally planning to run on my Raspberry Pi, but after truoble with installation, I am pivoting to running from a GitHub Action.

For local install:

```bash
# Create virtual environment.
uv venv --python 3.11.11
source .venv/bin/activate

# Install library.
uv pip install git+https://github.com/jhrcook/colter.git

# Run
EMAIL_PASSWORD="EMAIL_PASSWORD" colter
```
