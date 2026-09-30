# Digital Forensic Investigation Report

**Case ID:** DFI-2026-001  
**Examination Type:** Simulated Unauthorized Data Copy Investigation

## Executive Summary

A simulated forensic examination was conducted to determine whether digital artifacts were consistent with confidential project files being copied to removable media. Analysis of synthetic browser, file-system, and USB artifacts identified a sequence in which the user searched for USB copying instructions, accessed confidential project data, connected a SanDisk USB storage device, and copied two project files during the period in which the removable device was connected.

The evidence is consistent with a transfer of confidential files to removable media. Because this is a limited synthetic evidence set, the findings do not establish intent or authorization status and should not be interpreted beyond the available artifacts.

## Evidence Examined

- Synthetic browser history
- Synthetic USB device events
- Synthetic file activity records

## Methodology

The evidence files were preserved as read-only analysis inputs. Cryptographic hashing was demonstrated using MD5 and SHA-256. Artifact timestamps were normalized and correlated into a unified timeline using a Python script. Findings were documented separately from interpretation.

## Key Findings

A search related to copying large files to USB occurred at 14:02:11. The Orion project directory was accessed at 14:06:42. A SanDisk Ultra USB device was connected at 14:09:03. Two project files were recorded as copied at 14:10:18 and 14:11:06. The USB device was removed at 14:15:27.

## Conclusion

The available artifacts are consistent with confidential project files being copied during the period in which removable storage was connected. Additional evidence would be required to determine the destination contents, authorization status, and user intent with greater confidence.
