# Portable Mode - Running from USB

## What is Portable Mode

Portable mode lets you run your Qwen environment from a USB drive
on any computer without installing anything.

## Requirements on Host PC

- Python 3.12+ installed
- LM Studio running (or access to)
- USB 3.0 port

## Starting Portable Mode

1. Plug USB into host PC
2. Open File Explorer
3. Navigate to USB drive
4. Run: bin\qwen.bat

## What Works

- [OK] Your code and projects
- [OK] AI tools and frameworks
- [OK] Core model on USB
- [OK] Configuration files
- [OK] Backup and restore

## What Doesn't Work

- [SKIP] Models not on USB (need host PC models)
- [SKIP] LM Studio if not installed on host
- [SKIP] Python packages not installed on host

## Tips

### Use Host PC's LM Studio

Ask the host PC's LM Studio to load your model, or use the model
on your USB if it's available.

### Sync After Use

After working on another PC, sync your changes back:

    sync\sync-from-usb.bat

### Future: Full Portable

When LM Studio releases a portable version, we'll add it to the USB
for completely self-contained operation.
