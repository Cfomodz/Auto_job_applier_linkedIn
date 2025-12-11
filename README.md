# LinkedIn Auto Job Applier 🤖

Automate LinkedIn job applications with intelligent form filling and optional AI.

## Quick Start

```bash
# Clone & setup
git clone https://github.com/GodsScion/Auto_job_applier_linkedIn.git
cd Auto_job_applier_linkedIn

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure (interactive)
python setup.py

# Run
python runAiBot.py
```

## Configuration

All config is in two files:

| File | Contains |
|------|----------|
| `.env` | Personal info, credentials, API keys (gitignored) |
| `config.py` | Job search terms, filters, bot settings |

### Quick Edits

**Change job search terms:** Edit `search_terms` list in `config.py`

**Update personal info:** Edit `.env` file directly

**Re-run setup:** `python setup.py`

## Project Structure

```
Auto_job_applier_linkedIn/
├── .env              # Secrets & PII (gitignored)
├── .env.example      # Template
├── config.py         # All settings in one place
├── setup.py          # Interactive setup
├── runAiBot.py       # Main app
├── app.py            # Job history web UI
├── resumes/          # Your resume (gitignored)
└── modules/          # Core code
```

## Features

- 🔍 Multi-term job search with filters
- 📝 Auto-fill application questions
- 📄 Resume upload
- 🤖 Optional AI for unknown questions
- 🛡️ Stealth mode to avoid detection
- 📊 CSV tracking + web UI

## Requirements

- Python 3.10+
- Google Chrome

## License

[AGPL-3.0](LICENSE)
