# Installation Guide

## Prerequisites

Before installing, ensure you have:

- [ ] Windows 10/11
- [ ] Python 3.12 or later
- [ ] Git for Windows
- [ ] LM Studio (for local model serving)

## Step 1: Check Prerequisites

Run the prerequisites checker:

    recovery\validate-configs.bat

This will verify:
- Python installation
- Git installation
- LM Studio availability

## Step 2: Run Installation

    recovery\install-qwen.bat

The installer will:
1. Check prerequisites
2. Install PowerShell profile
3. Add qwen command
4. Test installation

## Step 3: Verify Installation

Open a NEW PowerShell window and type:

    qwen

You should see the Safe Workspace environment start.

## Step 4: Create USB Backup (Optional)

For backup and portability:

    recovery\install-usb-backup.bat

Follow the prompts to select your USB drive.

## Troubleshooting

### qwen not recognized

1. Close ALL PowerShell windows
2. Open NEW PowerShell
3. Try again

If still not working, run:

    . $PROFILE

### LM Studio not detected

1. Open LM Studio
2. Load a model
3. Start Local Server
4. Try qwen again

### Script execution errors

Run PowerShell as Administrator and run:

    Set-ExecutionPolicy RemoteSigned

## Next Steps

After installation:

1. Type qwen to start
2. Try: >>> create a python function
3. See ../README.md for commands
