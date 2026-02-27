# Qwen-Portable - AI Development Environment

Your complete organized AI workspace with portable backup capability.

## Quick Start

### First Time Setup

1. Run recovery/install-qwen.bat - Fresh installation
2. Run recovery/install-usb-backup.bat - Create USB backup (32GB recommended)
3. Open PowerShell and type qwen - Start coding!

## Structure

    Qwen-Portable/
    ├── bin/           # Launchers and installers
    ├── projects/      # Your work (default save location)
    ├── models/        # AI models (categorized)
    ├── ai-tools/      # AI tools and frameworks
    ├── config/        # Configuration files
    ├── sync/          # USB sync scripts
    ├── recovery/      # Install and repair tools
    └── docs/          # Documentation

## Commands

| Command | Action |
|---------|--------|
| qwen | Start safe workspace |
| q | Short alias |
| qwen-backup | Backup utilities |
| qwen-undo | Undo last AI change |
| qwen-help | Show help |

## USB Backup

- Plug in 32GB USB drive
- Run sync/sync-to-usb.bat
- USB contains: code + configs + 1 core model

## Documentation

- docs/INSTALL-GUIDE.md - Installation instructions
- docs/USB-BACKUP-GUIDE.md - USB backup guide
- docs/PORTABLE-MODE.md - Running from USB
- docs/RECOVERY-GUIDE.md - Repair and fix issues

## Requirements

- Python 3.12+
- Git
- LM Studio (for local models)

Start with: Run recovery/install-qwen.bat
