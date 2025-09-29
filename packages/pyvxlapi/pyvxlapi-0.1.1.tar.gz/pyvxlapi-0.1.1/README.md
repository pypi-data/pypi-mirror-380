# pyvxlapi

Python Wrapper for Vector XL Driver Library

The `pyvxlapi.py` is convert from `vxlapi.h` by [ctypesgen](https://github.com/ctypesgen/ctypesgen)

## Installation
```
$ uv venv
$ uv pip install pyvxlapi
```

## Development
```sh
$ uv venv
$ uv add --dev ctypesgen
$ uv run ctypesgen -lvxlapi64 -o src/pyvxlapi/pyvxlapi.py assets/vxlapi.h
```

## Example

```py
from pyvxlapi import (
    XLdriverConfig,
    xlGetDriverConfig,
)

driver_config = XLdriverConfig()
status = xlGetDriverConfig(driver_config)
print(status)

for i in range(driver_config.channelCount):
    channel_config = driver_config.channel[i]
    print(f"{i} {channel_config.name} {channel_config.channelMask}")
```
