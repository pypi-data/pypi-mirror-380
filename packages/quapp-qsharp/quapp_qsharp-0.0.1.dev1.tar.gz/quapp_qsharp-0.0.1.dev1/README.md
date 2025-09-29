# quapp-pennylane

Quapp PennyLane library supporting the Quapp Platform for Quantum Computing with
providers, devices, circuit export, invocation, and job fetching utilities.

## Overview

`quapp-pennylane` is a Python library that integrates the Quapp Platform with
PennyLane-based quantum backends and simulators. It provides common abstractions
for providers and devices, helpers for circuit construction/export, robust job
submission and result fetching flows, and consistent, job-scoped logging across
components. Recent improvements focus on cleaner and more consistent logging,
better error handling, and clear separation of concerns between invocation and
fetching flows.

## Features

- Provider and device factories for PennyLane-compatible platforms (e.g., local
  simulators and vendor-backed devices exposed via PennyLane).
- Circuit export utilities and helpers for building and running PennyLane
  circuits.
- Handlers for job invocation and job result fetching with enhanced,
  context-rich logging.
- Job-scoped, instance-bound logging for improved traceability and debugging.
- Refined log levels and simplified imports to reduce noise and improve clarity.

## Installation

Install via pip:

```bash
pip install quapp-pennylane
```

## Recently Changes Highlights

- refactor: Update probability measurement handling and histogram generation
  logic
- refactor: Add `_transpile_circuit` method with logging improvements
- refactor: Switch to `job_logger` and improve logging consistency in PennyLane
  factories
- build: Bump a version to 0.0.4.dev6 and update dependency `quapp-common` to
  0.0.11.dev7
- refactor: Enhance logging and error handling across QAppPennylane components

For detailed usage and API references, please refer to the in-code documentation
or contact the maintainers.