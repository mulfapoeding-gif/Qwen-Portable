"""
Hugging Face Model Downloader
Download any model with progress bar
"""

from huggingface_hub import list_repo_files, hf_hub_download
import os
import sys

def download_model(model_id, output_dir=None):
    """Download all files from a Hugging Face model"""
    
    if output_dir is None:
        output_dir = os.path.join(
            os.path.expanduser("~"),
            ".lmstudio",
            "models",
            "imported-models",
            "uncategorized",
            model_id.replace("/", "_")
        )
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"  Hugging Face Model Downloader")
    print(f"{'='*60}")
    print(f"\nModel: {model_id}")
    print(f"Output: {output_dir}\n")
    
    try:
        # List all files in repo
        print("Scanning repository...")
        files = list_repo_files(model_id, repo_type="model")
        
        print(f"Found {len(files)} files:\n")
        for f in files:
            print(f"  - {f}")
        
        print(f"\n{'='*60}")
        print(f"Downloading {len(files)} files...")
        print(f"{'='*60}\n")
        
        # Download each file
        downloaded = []
        for i, file in enumerate(files, 1):
            print(f"[{i}/{len(files)}] Downloading: {file}")
            
            try:
                file_path = hf_hub_download(
                    repo_id=model_id,
                    filename=file,
                    repo_type="model",
                    local_dir=output_dir,
                    local_dir_use_symlinks=False
                )
                print(f"  ✅ Saved: {file_path}")
                downloaded.append(file)
            except Exception as e:
                print(f"  ❌ Error: {e}")
            
            print()
        
        print(f"\n{'='*60}")
        print(f"  Download Complete!")
        print(f"{'='*60}")
        print(f"\nDownloaded: {len(downloaded)}/{len(files)} files")
        print(f"Location: {output_dir}")
        print(f"\nGGUF files ready for:")
        print(f"  - LM Studio")
        print(f"  - llama.cpp")
        print(f"  - Ollama (import)")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print(f"\nPossible issues:")
        print(f"  1. Model ID is incorrect")
        print(f"  2. Model requires authentication")
        print(f"  3. Internet connection issue")
        print(f"\nFor private models, login first:")
        print(f"  huggingface-cli login")
        print()
        return False


def main():
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python hf-downloader.py MODEL_ID [OUTPUT_DIR]")
        print("\nExamples:")
        print("  python hf-downloader.py Nerdsking/Nerdsking-python-coder-7B-i")
        print("  python hf-downloader.py microsoft/phi-2 models/phi-2")
        print()
        return
    
    model_id = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = download_model(model_id, output_dir)
    
    if success:
        print("✅ Done!")
    else:
        print("❌ Failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
