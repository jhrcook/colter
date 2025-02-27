# Simple app to notify me when Colter Thorofare Nets are back in stock

```bash
# Create virtual environment.
uv venv --python 3.11.11
source .venv/bin/activate

# Install library.
uv pip install git+https://github.com/jhrcook/colter.git

# Add secrets.
echo "EMAIL_PASSWORD" > .secrets

# Run
colter
```
