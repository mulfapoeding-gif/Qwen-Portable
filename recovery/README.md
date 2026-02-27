# recovery - Installation and Repair Tools

## Tools

| File | Purpose |
|------|---------|
| install-qwen.bat | Fresh installation script |
| install-usb-backup.bat | Create USB backup |
| check-and-fix.bat | Scan and repair system |
| fix-powershell-profile.ps1 | Clean and fix PowerShell profile |
| restore-readmes.bat | Restore missing READMEs |
| validate-configs.bat | Validate configurations |

## Fresh Installation

1. Run install-qwen.bat
2. Follow on-screen instructions
3. Restart PowerShell

## System Check

If something isn't working:

1. Run check-and-fix.bat
2. Review repair report
3. Restart PowerShell

## PowerShell Profile Issues

If qwen command is broken or not recognized:

1. Run fix-powershell-profile.ps1
2. Close ALL PowerShell windows
3. Open NEW PowerShell window
4. Type: qwen

## Restore READMEs

If documentation files are missing:

1. Run restore-readmes.bat
2. All README files restored

## Validate Configuration

To check your installation:

1. Run validate-configs.bat
2. Review validation results

See ../docs/RECOVERY-GUIDE.md for details.
