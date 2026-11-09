# ORBIT / GROK BOT CLONE (GBC) — New Machine Setup Guide

This guide explains how to clone and immediately set up the complete ORBIT / Grok Bot Clone environment on any new PC or Windows device with a single command.

---

## 1. Prerequisites on the New Device

Before running the setup, ensure your new computer has:

| Tool | Minimum Version | Download Link | Notes |
| :--- | :--- | :--- | :--- |
| **Git** | 2.30+ | [git-scm.com](https://git-scm.com/) | Ensure "Add Git to PATH" is checked |
| **Python** | 3.11+ | [python.org](https://www.python.org/) | Ensure "Add Python to PATH" is checked |
| **Node.js** | 18+ (Recommended) | [nodejs.org](https://nodejs.org/) | Required for React 19 / Electron UI |
| **pnpm** | Optional | `npm install -g pnpm` | Faster package management |

---

## 2. 1-Step Automatic Setup

Open **Command Prompt (CMD)** or **PowerShell** on your new device and run:

```bat
:: 1. Clone the repository to any directory or drive
git clone <your-repository-url> orbit
cd orbit

:: 2. Run the one-click setup script
setup_new_machine.bat
```

---

## 3. What `setup_new_machine.bat` Automates

The script executes 6 automated steps:

1. **Prerequisite Check**: Validates that Git, Python 3.11+, and Node.js are available in PATH.
2. **Directory Layout**: Initializes all required directories (`upstream/`, `logs/`, `reports/`, `.orbit/`, `.antigravity/`, `antigravity_platform/`).
3. **Python Virtual Environment**:
   - Creates a local isolated `.venv` at the repository root.
   - Installs and upgrades `pip`, `pyyaml`, and `pytest`.
4. **Upstream Source Acquisition**:
   - Clones **`OpenGrokBot`** (`https://github.com/Z4YT0N/OpenGrokBot.git`) into `upstream/opengrokbot` and pins it to commit `86e45d2`.
   - Clones **`OmniVoice`** (`https://github.com/k2-fsa/OmniVoice.git`) into `upstream/omnivoice` for real-time conversational voice.
5. **System Health Check (`orbit doctor`)**: Runs diagnostic inspection reporting OS, architecture, and toolpaths.
6. **Unit Test Verification**: Runs all 17 unit tests covering DAG execution, context packing, and storage validation to confirm a 100% green baseline.

---

## 4. Daily Development Commands

Once the setup script finishes, you can use the portable launchers from anywhere in the project:

### System Diagnostics
```powershell
# PowerShell
.\orbit.ps1 doctor

# Command Prompt (CMD)
orbit.bat doctor
```

### Validate Task DAG Manifests
```powershell
.\orbit.ps1 run --manifest configs\tasks.example.json --validate-only
```

### Run Unit Tests
```powershell
$env:PYTHONPATH = "src"; python -m unittest discover -s tests -v
```

### Check Storage Budget & Status
```powershell
.\orbit.ps1 storage status
```

---

## 5. Working in Google Antigravity IDE

1. Open **Google Antigravity IDE**.
2. Select **File > Open Folder...** and choose your cloned `orbit` folder.
3. The IDE automatically detects:
   - **`.agent/rules/`**: Mandatory guidelines (`orbit.md`, `ponytail_senior_dev.md`, `ui_ux_and_research.md`).
   - **`.antigravity/mcp_config.json`**: Pre-configured MCP servers (REA reverse engineering, notebooks, data agent).
   - **`antigravity_platform/`**: Builtin skills, schemas, and IDE extension specs.
4. You are ready to develop immediately with full agent capabilities!

