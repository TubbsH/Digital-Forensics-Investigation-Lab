# Digital Forensics Investigation Lab

A portfolio project demonstrating a simulated digital forensics investigation involving evidence preservation, artifact review, timeline reconstruction, and investigative reporting.

## Project Scenario

A fictional employee, **Jordan Blake**, is suspected of copying confidential project documents to removable media shortly before leaving the company. The goal of this lab is to determine whether the available digital artifacts support that allegation.

All evidence in this repository is **synthetic and created for training purposes**. No real personal or confidential information is included.

## Skills Demonstrated

- Digital evidence handling and chain-of-custody documentation
- MD5 and SHA-256 hashing
- File-system and artifact analysis
- Browser and removable-media artifact review
- Timeline reconstruction
- Python scripting for forensic workflows
- Investigative documentation and reporting
- Familiarity with Autopsy and FTK Imager workflows

## Tools & Technologies

- Autopsy
- FTK Imager
- Python 3
- CSV artifact analysis
- MD5 / SHA-256 hashing
- Windows forensic concepts
- Git / GitHub

## Repository Structure

```text
Digital-Forensics-Investigation-Lab/
├── README.md
├── case-files/
│   ├── case-background.md
│   └── chain-of-custody.md
├── analysis/
│   ├── acquisition-and-integrity.md
│   ├── browser-analysis.md
│   ├── removable-media-analysis.md
│   ├── timeline-analysis.md
│   └── findings.md
├── scripts/
│   ├── hash_file.py
│   └── build_timeline.py
├── sample-data/
│   ├── browser_history.csv
│   ├── usb_events.csv
│   └── file_activity.csv
├── report/
│   └── forensic-investigation-report.md
└── docs/
    └── resume-project-entry.md
```

## Investigation Summary

The synthetic artifacts show a sequence of activity consistent with the suspected behavior. On May 14, 2026, the user searched for information related to copying large files, accessed the confidential `Orion_Project` directory, connected a removable USB device, and copied multiple project files shortly afterward. The USB device was removed several minutes later.

These artifacts are **consistent with** data being copied to removable media, but the project intentionally avoids overstating the evidence. A real investigation would require validation against the source forensic image and corroboration with additional artifacts.

## How to Run the Python Tools

### 1. Hash a file

```bash
python scripts/hash_file.py sample-data/file_activity.csv
```

The script calculates both MD5 and SHA-256 hashes for the selected file.

### 2. Build a unified timeline

```bash
python scripts/build_timeline.py
```

This reads the three CSV files in `sample-data/`, normalizes their timestamps, sorts the events, and creates:

```text
sample-data/generated_timeline.csv
```

## Example Investigative Timeline

| Time | Artifact | Event |
|---|---|---|
| 2026-05-14 14:02:11 | Browser | Search: "copy large files to usb windows" |
| 2026-05-14 14:06:42 | File System | `Orion_Project` directory accessed |
| 2026-05-14 14:09:03 | USB | SanDisk Ultra USB device connected |
| 2026-05-14 14:10:18 | File System | `orion_financials.xlsx` copied |
| 2026-05-14 14:11:06 | File System | `client_list.csv` copied |
| 2026-05-14 14:15:27 | USB | SanDisk Ultra USB device removed |

## Forensic Methodology

1. Document the case background and evidence source.
2. Record evidence identifiers and chain-of-custody information.
3. Verify evidence integrity using cryptographic hashes.
4. Examine relevant system and user artifacts.
5. Correlate events across multiple artifact sources.
6. Build a chronological timeline.
7. Separate observed evidence from interpretation.
8. Document limitations and produce an investigative report.

## Portfolio Note

This project is intended to demonstrate an entry-level digital forensics workflow for cybersecurity, cybercrime, and digital forensics roles. The repository contains synthetic evidence only and does not represent a real criminal investigation.
