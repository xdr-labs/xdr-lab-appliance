# Repository Boundary

## What this repo is

**xdr-lab-appliance** is the source of truth for the XDR Lab deployment
automation stack:

- KVM / Open vSwitch lab networking
- `aella_cli` and appliance runtime
- cloud-init, bootstrap, installer, config
- lab operator documentation

## What this repo is not

This repository is **not** the DSP / PoC scenario source of truth.

| Removed / forbidden | Replacement |
|---------------------|-------------|
| `detection-scenario-platform/` subtree | External clone of `xdr-poc-script` |
| Editable DSP Python under appliance | `/home/aella/xdr-poc-script` |
| New DSP features in appliance | `xdr-labs/xdr-poc-script` |

## Legacy bash PoC

Pre-DSP bash scripts live under `legacy/bash-poc/` for archive and legacy tests
only. They are **not** used by `aella_cli` or deployment workflows.

## Pre-commit checklist

Before committing in this repository:

1. `pwd` ends with `xdr-lab-appliance` (not `xdr-poc-script`).
2. `git remote -v` shows `xdr-labs/xdr-lab-appliance.git`.
3. No `detection-scenario-platform/` or `dsp/` package trees are being added.
4. DSP code changes belong in **xdr-poc-script**, not here.
