# USB Backup Guide

## Requirements

- 32GB USB 3.0 flash drive (recommended)
- Minimum 16GB (with limited models)

## What's on the USB

The USB backup contains:

- [OK] All code and tools
- [OK] Configuration files
- [OK] Active projects
- [OK] Documentation
- [OK] 1 core model: Qwen2.5-Coder-3B-Instruct-Q4_K_M.gguf

Total size: ~8-10 GB

## Creating USB Backup

### Method 1: Automated Script

1. Plug in USB drive
2. Run: recovery\install-usb-backup.bat
3. Select USB drive letter when prompted
4. Wait for copy to complete
5. Safely eject USB

### Method 2: Manual Sync

1. Plug in USB drive
2. Run: sync\sync-to-usb.bat

## Using USB Backup

### On Another PC

1. Plug USB into any PC with:
   - Python 3.12+ installed
   - LM Studio running

2. Open File Explorer
3. Navigate to USB drive
4. Run: bin\qwen.bat

5. Your workspace starts with your models and projects!

### Restoring to PC

If your PC installation is corrupted:

1. Plug in USB
2. Run: sync\sync-from-usb.bat
3. Confirm restore operation

## Syncing Changes

### After Making Changes on PC

    sync\sync-to-usb.bat

### After Working on Another PC

    sync\sync-from-usb.bat

## Best Practices

- [OK] Sync after each work session
- [OK] Always safely eject USB
- [OK] Keep USB in safe location
- [OK] Test USB on another PC periodically
- [SKIP] Don't edit files directly on USB
- [SKIP] Don't remove USB during sync

## Troubleshooting

### USB not detected

- Ensure USB is properly inserted
- Check Disk Management for drive letter
- Try different USB port

### Not enough space

- USB needs at least 16GB free
- Delete old backups from USB
- Use 32GB drive for full backup
