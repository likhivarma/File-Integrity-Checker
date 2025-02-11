import hashlib
import os
import json
import time
import sys

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(4096)
            while chunk:
                hasher.update(chunk)
                chunk = f.read(4096)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except PermissionError:
        print(f"❌ Permission denied: {file_path}")
        return None

def generate_baseline(directory, output_file="baseline.json"):
    """Create a baseline of file hashes."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = calculate_hash(file_path)
            if hash_value is not None:
                file_hashes[file_path] = hash_value
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print(f"✅ Baseline created and saved to {output_file}")

def check_integrity(directory, baseline_file="baseline.json"):
    """Compare current file hashes with the stored baseline."""
    try:
        with open(baseline_file, "r") as f:
            baseline_hashes = json.load(f)
    except FileNotFoundError:
        print("❌ Baseline file not found. Run the baseline generation first.")
        return
    
    current_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = calculate_hash(file_path)
            if hash_value is not None:
                current_hashes[file_path] = hash_value
    
    modified = {f for f in current_hashes if f in baseline_hashes and current_hashes[f] != baseline_hashes[f]}
    new_files = set(current_hashes.keys()) - set(baseline_hashes.keys())
    deleted_files = set(baseline_hashes.keys()) - set(current_hashes.keys())
    
    if modified or new_files or deleted_files:
        print("⚠️ Integrity Violations Detected:")
        if modified:
            print(f"Modified Files: {modified}")
        if new_files:
            print(f"New Files: {new_files}")
        if deleted_files:
            print(f"Deleted Files: {deleted_files}")
    else:
        print("✅ No integrity violations detected.")

def monitor(directory, interval=30):
    """Continuously monitor file integrity at intervals."""
    print(f"🔍 Monitoring {directory} every {interval} seconds...")
    try:
        while True:
            check_integrity(directory)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")
        sys.exit(0)

# Example Usage
if __name__ == "__main__":
    directory_to_monitor = "C:/path/to/monitor"  # Change as needed
    generate_baseline(directory_to_monitor)
    monitor(directory_to_monitor, interval=60)  # Check every 60 seconds
