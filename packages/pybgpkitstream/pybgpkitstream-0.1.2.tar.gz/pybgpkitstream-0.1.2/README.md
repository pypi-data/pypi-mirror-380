# PyBGPKITStream

A drop-in replacement for PyBGPStream using BGPKIT

## Features

- Effortless BGP Stream Switching:
  - Seamless, drop-in replacement ([example](tests/test_stream.py#L38))
  - Lazy message generation: generates time-ordered BGP messages on the fly, consuming minimal memory and making it suitable for large datasets
  - Supports multiple route collectors
  - Supports both ribs and updates
- Caching with concurrent downloading is enabled and is fully compatible with the BGPKIT parser's caching functionality.
- [Similar performance to PyBGPStream](examples/perf.ipynb)
- A CLI tool

## Quick start

Installation:

```sh
pip install pybgpkitstream
```

Usage:

```python
import datetime
from pybgpkitstream import BGPStreamConfig, BGPKITStream

config = BGPStreamConfig(
    start_time=datetime.datetime(2010, 9, 1, 0, 0),
    end_time=datetime.datetime(2010, 9, 1, 1, 59),
    collectors=["route-views.sydney", "route-views.wide"],
    data_types=["ribs", "updates"],
)

stream = BGPKITStream.from_config(config)

n_elems = 0
for _ in stream:
    n_elems += 1
    
print(f"Processed {n_elems} BGP elements")
```

or in the terminal:

```sh
pybgpkitstream --start-time 2010-09-01T00:00:00 --end-time 2010-09-01T01:59:00 --collectors route-views.sydney route-views.wide --data-types updates > updates.txt
```

## Motivation

PyBGPStream is great but the implementation is complex and stops working when UC San Diego experiences a power outage.
BGPKIT broker and parser are great, but cannot be used to create an ordered stream of BGP messages from multiple collectors and multiple data types.

## Missing features

- live mode
- `pybgpkitstream.BGPElement` is not fully compatible with `pybgpstream.BGPElem`: missing record_type (BGPKIT limitation), project (BGPKIT limitation), router (could be improved), router_ip (could be improved)
- CLI output is not yet compatible with `bgpdump -m` or `bgpreader` (right now a similar-looking output is produced)

## Issues

- Program will crash when working with many update files per collector (~ more than few hours of data), only when caching is disabled. This might be caused by [BGPKIT parser not being lazy](https://github.com/bgpkit/bgpkit-parser/pull/239). See [details and workaround fix](examples/many_updates.ipynb)
- Filters are designed with BGPKIT in mind, and can slightly differ to pybgpstream. See [this file](tests/pybgpstream_utils.py) for a conversion to PyBGPStream filter. Note that for now the filters have not been heavily tested...
- ... just like the rest of the project. Use at your own risk. The only tests I did are in /tests
