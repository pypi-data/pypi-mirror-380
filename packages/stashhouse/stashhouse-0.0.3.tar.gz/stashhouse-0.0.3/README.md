<div align="center">
   <h1>🏠 StashHouse</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🏁 Usage](#usage)

</div>

<hr />

# Purpose

StashHouse is a framework for centrally collecting files to enable rapid file transfers. The framework is designed with
a plugin system to enable the inclusion of additional file transfer protocols while working to minimize the overhead
required for file transfers.

### Use Cases

<details style="border: 1px solid; border-radius: 8px; padding: 8px; margin-top: 4px;">
<summary>🔬Data Donation</summary>

Accept data from a population while prohibiting parties from accessing each other's data.

</details>

<details style="border: 1px solid; border-radius: 8px; padding: 8px; margin-top: 4px;">
<summary>📦 Bulk Data Collection</summary>

Acquire system data from internet of thing devices and scripts without requiring authentication tokens while preventing 
data exfiltration.

</details>

<details style="border: 1px solid; border-radius: 8px; padding: 8px; margin-top: 4px;">
<summary>🪂 Malware Analysis</summary>

Allow customers to drop artifacts for analysis with minimal overhead and through their preferred protocol.

</details>

# Usage

StashHouse provides a `stashhouse` command to quickly start installed plugins.

Install the `stashhouse` package:
```commandline
python3 -m pip install stashhouse
```

To see available configuration options, use the `--help` flag:
```commandline
stashhouse --help
```