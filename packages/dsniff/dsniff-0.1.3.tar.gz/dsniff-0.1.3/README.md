# dsniff Python Package

This package provides a Python wrapper for the **dsniff** network sniffer suite (originally by Dug Song), allowing you to install and use dsniff tools via `pip`.

pip install .

## Installation

Ensure you have the required dependencies:

- `berkeley-db` (optional; support is disabled by default)
- `libnet`
- `libnids`
- `libpcap`
- `openssl`

On macOS with Homebrew:
```bash
brew install berkeley-db libnet libnids libpcap openssl
```

### Enable Berkeley DB support (optional)
By default, Berkeley DB compatibility is disabled. To enable support with a newer
Berkeley DB installation, set the `DSNIFF_DB_PATH` environment variable to your
Berkeley DB prefix and install:
pip install .
```bash
DSNIFF_DB_PATH=/opt/homebrew/opt/berkeley-db@4 \
pip install .
```

> On macOS, the installer will attempt to auto-detect a Homebrew keg-only
> Berkeley DB under `/usr/local/opt` or `/opt/homebrew/opt`. If found, you
> do **not** need to set `DSNIFF_DB_PATH` manually. Manual setting is only
> required for non-standard installation paths.

Install via `pip`:
```bash
pip install .
```

To specify custom library paths (e.g., Homebrew on Apple Silicon):
```bash
DSNIFF_LIBPCAP=/opt/homebrew/opt/libpcap \
DSNIFF_LIBNET=/opt/homebrew/opt/libnet \
DSNIFF_LIBNIDS=/opt/homebrew/opt/libnids \
DSNIFF_OPENSSL=/opt/homebrew/opt/openssl \
pip install .
```

## Usage

After installation, the following commands are available:

- `dsniff`
- `arpspoof`
- `dnsspoof`
- `filesnarf`
- `mailsnarf`
- `msgsnarf`
- `urlsnarf`
- `macof`
- `sshow`
- `sshmitm`
- `webmitm`
- `webspy`
- `tcpkill`
- `tcpnice`

## Commands & Examples

Below are common usage patterns and examples for each tool. Replace `-i eth0` with your network interface and adjust filters as needed.

- **dsniff**: sniff credentials on the network (FTP, Telnet, SMTP, HTTP, etc.)
  ```bash
  dsniff -i eth0 tcp port ftp or tcp port telnet
  ```
- **arpspoof**: perform ARP spoofing to man-in-the-middle two hosts
  ```bash
  arpspoof -i eth0 TARGET_IP GATEWAY_IP
  ```
- **dnsspoof**: spoof DNS responses based on a hosts file
  ```bash
  dnsspoof -i eth0 hosts.txt
  ```
- **filesnarf**: capture NFS file reads
  ```bash
  filesnarf -i eth0 tcp port nfs
  ```
- **mailsnarf**: capture SMTP mail traffic
  ```bash
  mailsnarf -i eth0 tcp port 25
  ```
- **msgsnarf**: capture IRC, IM, and messaging traffic
  ```bash
  msgsnarf -i eth0 tcp port 6667 or tcp port 5190
  ```
- **urlsnarf**: capture URLs from HTTP traffic
  ```bash
  urlsnarf -i eth0 tcp port 80
  ```
- **macof**: flood a switch by generating random MAC traffic
  ```bash
  macof -i eth0
  ```
- **sshow**: display active sniffer sessions
  ```bash
  sshow
  ```
- **sshmitm**: perform SSH v1 man-in-the-middle attack
  ```bash
  sshmitm -i eth0 REMOTE_HOST
  ```
- **webmitm**: HTTPS man-in-the-middle (requires appropriate certs)
  ```bash
  webmitm -i eth0 SERVER_IP
  ```
- **webspy**: passive HTTP snooping
  ```bash
  webspy -i eth0 tcp port 80
  ```
- **tcpkill**: kill TCP connections matching a filter
  ```bash
  tcpkill -i eth0 port 80
  ```
- **tcpnice**: throttle TCP connections (window-nice)
  ```bash
  tcpnice -i eth0 port 80
  ```

For detailed help on each tool, run:
```bash
<tool-name> -h
```

## Notes

- Original documentation and license can be found in the `dsniff-old` directory.
- Binaries are built and installed into the Python package during installation.
- This wrapper invokes the compiled executables under the hood.

##

Absolutely, Kael here — I’ve drafted an updated `README.md` for your [`dsniff`](https://github.com/joshjvmes/dsniff) fork that reflects your work modernizing it, wrapping it in Python, and making it installable via PyPI. Here's a clean, structured version with sections for clarity and good developer UX:

---

# dsniff (modernized fork)

[![PyPI version](https://img.shields.io/pypi/v/dsniff.svg)](https://pypi.org/project/dsniff/)
A modernized and Python-wrapped version of the classic `dsniff` suite of network sniffing tools, originally released in 2000. Now working on modern macOS via Homebrew with automated builds and PyPI installation.

## ✨ What's New

This fork brings `dsniff` into the modern development environment:

* ✅ **macOS support**: Clean builds on modern macOS (Intel & Apple Silicon) via Homebrew.
* 🧠 **Python wrapper**: Native binaries wrapped in a Python package with `console_scripts` entry points.
* 📦 **Published on PyPI**: Install via `pip install dsniff`.
* ⚙️ **CI/CD ready**: Automated build/test/release via GitHub Actions.
* 🖥️ **Interactive CLI**: Optional curses-style interactive menu for tool selection.

---

## 🔧 Build & Compatibility Changes

* `C` source updated to build cleanly on modern systems (tested on macOS).
* No more static Berkeley DB 1.85 headers required.

  * Dynamic DB support is auto-detected via `--with-db`.
  * New `record_stubs.c` layer provides stubbed DB operations for tools like `dsniff`, `sshow`, `trigger`.
* `pcap_init()` renamed to `dsniff_pcap_init()` to avoid naming conflicts with modern `libpcap`.
* `sshmitm` (which relied on deprecated OpenSSL internals) is no longer built by default.
* Builds drop into `build/bin` and are then copied into `dsniff_py/bin` for packaging.

### Environment Variable Support

* `DSNIFF_DB_PATH` can override the default DB path.

  * If it points to a non-existent prefix, it is ignored and falls back to auto-detection (e.g., `/usr/local/opt/berkeley-db@*`).

---

## 📦 Python Package

### Installation

```bash
pip install dsniff
```

### Tools Included

These wrap the original `dsniff` binaries:

* `dsniff`
* `arpspoof`
* `dnsspoof`
* `macof`
* `filesnarf`
* `mailsnarf`
* `msgsnarf`
* `tcpkill`
* `tcpnice`
* and more...

### Usage

```bash
dsniff
# Or run the interactive curses-style CLI:
dsniff-menu
```

> Note: The interactive menu is optional and helps quickly run the right tool via keyboard input.

---

## 🧪 Development

### Build locally

```bash
brew install libpcap berkeley-db
./configure --with-db
make
```

Then build the Python package:

```bash
python3 setup.py install
```

### Run tests

```bash
pytest
```

---

## 🙌 Credits

Original tools by **Dug Song**
Modernized fork and Python wrapper by [@joshjvmes](https://github.com/joshjvmes)

---

## 📄 License

This project is distributed under the same license as the original dsniff tools. See [LICENSE](./LICENSE) for details.