# File-Integrity-Checker

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CHANDRA LEKHA MUTHINENI

*INTERN ID*: CT6WTRE

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH


*DESCRIPTION*:
              This Python script is a File Integrity Checker that monitors changes in files within a specified directory. It detects modifications, new file additions, and deletions by comparing file hashes with a previously stored baseline. The tool ensures file integrity and security, making it useful for cybersecurity applications, ethical hacking, and system monitoring.

Features
✔ Calculate File Hashes: Uses SHA-256 hashing to compute and verify file integrity.
✔ Baseline Generation: Creates a JSON file storing the initial file hashes for future comparison.
✔ Integrity Checking: Compares current file states with the baseline to detect modifications, new files, or deleted files.
✔ Continuous Monitoring: Runs at specified intervals to automatically check for changes.
✔ Error Handling: Handles FileNotFoundError and PermissionError to ensure smooth execution.

How It Works
Generate Baseline: Computes hashes for all files in the directory and saves them in baseline.json.
Monitor Changes: Periodically checks files against the baseline and reports any integrity violations.
Alert on Changes: Notifies the user when files are modified, added, or deleted.


*EXAMPLE*:
          ✅ No integrity violations detected.
⚠️ Integrity Violations Detected:
🔹 Modified Files: ['C:/example/file1.txt']
🔹 New Files: ['C:/example/newfile.txt']
🔹 Deleted Files: ['C:/example/deleted.txt']
