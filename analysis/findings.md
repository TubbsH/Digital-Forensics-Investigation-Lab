# Findings

## Finding 1: Removable media was connected

A SanDisk Ultra USB storage device was connected to the workstation at 14:09:03 on May 14, 2026 and removed at 14:15:27.

## Finding 2: Confidential files were accessed during the same period

The `Orion_Project` directory was accessed shortly before the USB connection. Two project files were subsequently recorded as copied.

## Finding 3: Browser activity provides additional context

Immediately before the file and USB activity, the user searched for information related to copying large files to USB storage.

## Assessment

The available synthetic artifacts are consistent with the hypothesis that confidential Orion project files were copied to removable media. The evidence set does not independently establish intent, authorization status, or the final contents of the USB device.

## Limitations

- The dataset is synthetic and intentionally simplified.
- No full forensic disk image is included.
- Destination-media contents are unavailable.
- No memory image or network telemetry is included.
- A real case would require validation of timestamps, time zone, system clock accuracy, acquisition method, and additional artifact sources.
