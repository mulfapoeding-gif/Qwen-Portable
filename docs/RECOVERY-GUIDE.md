# Recovery Guide - Fixing Issues

## Quick Fixes

### Issue: qwen not recognized

Solution:

    recovery\install-qwen.bat

Then restart PowerShell.

### Issue: PowerShell profile broken

Solution:

    recovery\check-and-fix.bat

### Issue: Missing README files

Solution:

    recovery\restore-readmes.bat

### Issue: Configuration problems

Solution:

    recovery\validate-configs.bat

## Full System Check

If multiple things aren't working:

    recovery\check-and-fix.bat

This will:
1. Scan for missing files
2. Check file integrity
3. Verify README files
4. Fix PowerShell profile
5. Restore default configs
6. Generate repair report

## Restore from USB Backup

If your installation is severely broken:

1. Plug in USB backup
2. Run: sync\sync-from-usb.bat
3. Confirm full restore

## Reinstall Everything

Last resort - clean reinstall:

1. Backup your projects manually
2. Delete Qwen-Portable folder
3. Run structure creator again
4. Run recovery\install-qwen.bat

## Getting Help

If nothing works:

1. Check docs/INSTALL-GUIDE.md
2. Review repair report from check-and-fix.bat
3. Check LM Studio is running
4. Verify Python and Git are installed
