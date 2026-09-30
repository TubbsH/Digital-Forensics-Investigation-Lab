# Acquisition and Evidence Integrity

A core digital-forensics principle is preserving the integrity of evidence. In a real examination, the source device would be documented, write-protected when appropriate, and imaged with a forensic acquisition tool such as FTK Imager.

The original evidence hash and forensic image hash should match when calculated using the same algorithm. This project includes `scripts/hash_file.py` to demonstrate MD5 and SHA-256 hashing of evidence files.

Example command:

```bash
python scripts/hash_file.py sample-data/file_activity.csv
```

MD5 can still be useful for evidence verification and comparison, while SHA-256 provides a stronger modern cryptographic digest. Hash values alone do not establish what occurred; they support integrity verification.
