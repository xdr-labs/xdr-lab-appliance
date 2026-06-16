# DSP External Dependency

The **Detection Scenario Platform (DSP)** is **not** part of the XDR Lab
Appliance repository.

## Official source

| Item | Value |
|------|-------|
| Repository | `git@github.com:RickLee-kr/xdr-poc-script.git` |
| Active branch | `release/v1.4.0-rc` |
| Local path (operator default) | `/home/aella/xdr-poc-script` |

## Install / update

```bash
git clone git@github.com:RickLee-kr/xdr-poc-script.git
cd xdr-poc-script
git checkout release/v1.4.0-rc
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

Override the local path when invoking appliance helpers:

```bash
export XDR_POC_SCRIPT_ROOT=/path/to/xdr-poc-script
python3 scripts/run_dsp_release_1_0_lab_test.py
```

## Appliance boundary

- **Do not** vendor or commit DSP source under `xdr-lab-appliance/`.
- **Do not** treat `detection-scenario-platform/` as a subdirectory of this repo.
- Appliance provides lab infrastructure (VMs, network, `aella_cli`); DSP runs
  scenarios against targets the lab exposes.

See also [REPOSITORY_BOUNDARY.md](./REPOSITORY_BOUNDARY.md).
