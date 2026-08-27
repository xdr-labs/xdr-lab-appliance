# Legacy Bash PoC (Archived)

These files are the **pre-DSP** Stellar PoC bash orchestrator bundle. They are
archived in the appliance repo for historical reference and legacy test harnesses
only.

## Status

| Item | Detail |
|------|--------|
| **Replacement** | [xdr-poc-script](https://github.com/xdr-labs/xdr-poc-script) (`dsp` Python package) |
| **Appliance workflow** | Does **not** use these scripts (`aella_cli`, bootstrap, installer) |
| **Maintenance** | No new features; bugfixes belong in `xdr-poc-script` |

## Files

- `stellar_poc.sh` — main orchestrator (sources the other scripts in this directory)
- `stellar_poc_followup.sh`, `stellar_poc_humanize.sh`, `stellar_poc_fast_safe.sh`
- `stellar_poc_event_sot.sh`, `stellar_poc_network_simulators.sh`
- `stellar_poc.version` — bundle version manifest
- `stellar_dns_tunnel_file_client.py`, `stellar_dga_model_client.py`

## Running (legacy only)

```bash
cd /path/to/xdr-lab-appliance/legacy/bash-poc
./stellar_poc.sh --help
```

For current detection scenario work, clone and use **xdr-poc-script** instead:

```bash
git clone git@github.com:xdr-labs/xdr-poc-script.git
cd xdr-poc-script
git checkout release/v1.4.0-rc
```
