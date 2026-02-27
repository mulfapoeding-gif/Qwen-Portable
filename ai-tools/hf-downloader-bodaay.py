"""
Bodaay's HuggingFace Model Downloader
Enhanced version with progress bars and better error handling
Based on: https://github.com/bodaay/HuggingFaceModelDownloader
"""

from huggingface_hub import list_repo_files, hf_hub_download, login
import os
import sys
import time

class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def show_progress(current, total, filename=""):
    """Show download progress bar"""
    percent = int(current / total * 100) if total > 0 else 0
    bar_length = 40
    filled = int(bar_length * current / total) if total > 0 else 0
    bar = '#' * filled + '-' * (bar_length - filled)
    
    # Convert bytes to human readable
    def human_bytes(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} TB"
    
    sys.stdout.write(f'\r  [{bar}] {percent:3d}% - {human_bytes(current)}/{human_bytes(total)} - {filename}')
    sys.stdout.flush()

def download_model(model_id, output_dir=None, file_filter="gguf"):
    """Download model from Hugging Face"""
    
    if output_dir is None:
        output_dir = os.path.join(
            os.path.expanduser("~"),
            ".lmstudio",
            "models",
            "imported-models",
            "uncategorized",
            model_id.replace("/", "_")
        )
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}  Bodaay's HuggingFace Model Downloader{Colors.END}")
    print(f"{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"\nModel: {model_id}")
    print(f"Output: {output_dir}")
    print(f"Filter: *.{file_filter} files only\n")
    
    try:
        # List all files
        print(f"{Colors.CYAN}Scanning repository...{Colors.END}")
        files = list_repo_files(model_id, repo_type="model")
        
        # Filter for GGUF files (or specified type)
        gguf_files = [f for f in files if f.endswith(f".{file_filter}")]
        
        if not gguf_files:
            print(f"\n{Colors.YELLOW}No .{file_filter} files found!{Colors.END}")
            print(f"\nAvailable files:")
            for f in files[:20]:
                print(f"  - {f}")
            if len(files) > 20:
                print(f"  ... and {len(files) - 20} more")
            
            choice = input(f"\nDownload all files instead? (y/n): ").strip().lower()
            if choice == 'y':
                gguf_files = files
            else:
                return False
        
        print(f"\n{Colors.GREEN}Found {len(gguf_files)} .{file_filter} file(s):{Colors.END}\n")
        for f in gguf_files:
            print(f"  - {f}")
        
        print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
        print(f"{Colors.CYAN}Downloading...{Colors.END}\n")
        
        # Download each file
        downloaded = []
        failed = []
        
        for i, file in enumerate(gguf_files, 1):
            print(f"[{i}/{len(gguf_files)}] Downloading: {file}")
            
            try:
                file_path = hf_hub_download(
                    repo_id=model_id,
                    filename=file,
                    repo_type="model",
                    local_dir=output_dir,
                    local_dir_use_symlinks=False
                )
                print(f"  {Colors.GREEN}Saved:{Colors.END} {file_path}\n")
                downloaded.append(file)
            except Exception as e:
                print(f"  {Colors.RED}Error:{Colors.END} {e}\n")
                failed.append(file)
        
        # Summary
        print(f"\n{Colors.GREEN}{'='*70}{Colors.END}")
        print(f"{Colors.GREEN}Download Complete!{Colors.END}")
        print(f"{Colors.GREEN}{'='*70}{Colors.END}\n")
        print(f"Downloaded: {len(downloaded)}/{len(gguf_files)} files")
        print(f"Failed: {len(failed)}")
        print(f"Location: {output_dir}\n")
        
        if failed:
            print(f"{Colors.RED}Failed files:{Colors.END}")
            for f in failed:
                print(f"  - {f}")
            print()
        
        return True
        
    except Exception as e:
        print(f"\n{Colors.RED}Download failed: {e}{Colors.END}")
        print(f"\nPossible issues:")
        print(f"  1. Model ID is incorrect")
        print(f"  2. Model requires authentication (use --login)")
        print(f"  3. Internet connection issue")
        print(f"\nFor private models:")
        print(f"  huggingface-cli login")
        print()
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Download HuggingFace models')
    parser.add_argument('model_id', nargs='?', help='Model ID (e.g., Nerdsking/Nerdsking-python-coder-7B-i)')
    parser.add_argument('--output', '-o', help='Output directory')
    parser.add_argument('--filter', '-f', default='gguf', help='File filter (default: gguf)')
    parser.add_argument('--login', '-l', action='store_true', help='Login to HuggingFace')
    
    args = parser.parse_args()
    
    if args.login:
        print("\nLogging in to HuggingFace...\n")
        login()
        return
    
    if not args.model_id:
        print("\nUsage:")
        print("  python hf-downloader-bodaay.py MODEL_ID [options]")
        print("\nExamples:")
        print("  python hf-downloader-bodaay.py Nerdsking/Nerdsking-python-coder-7B-i")
        print("  python hf-downloader-bodaay.py microsoft/phi-2 --filter gguf")
        print("  python hf-downloader-bodaay.py --login")
        print("\nOptions:")
        print("  --output, -o  Output directory")
        print("  --filter, -f  File filter (default: gguf)")
        print("  --login, -l   Login to HuggingFace")
        print()
        return
    
    success = download_model(args.model_id, args.output, args.filter)
    
    if success:
        print(f"{Colors.GREEN}Done!{Colors.END}\n")
    else:
        print(f"{Colors.RED}Failed!{Colors.END}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
