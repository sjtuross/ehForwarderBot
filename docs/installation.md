# Installation
EFB framework itself does not require any external modules to operate. However, most of its channels do require some external dependencies, mainly for multimedia processing and communication with remote chat platforms.

To install dependencies for **all** officially maintained channels, you may follow the following instructions, or refer to the respective documentations of each channel.

Firstly, clone this project and open it.

```bash
git clone https://github.com/blueset/ehForwarderBot.git
cd ehForwarderBot
```

## Storage directory

In order to process files and media (pictures, voices, videos, etc.), a storage folder is used to temporarily save and process them. Create a `storage` folder, if not existing, and give write and read permission to it.

Script for \*nix users:
```bash
mkdir storage
chmod +rw ./storage
```

## Non-python dependencies

* __libmagic__
* __libopus__
* __ffmpeg__ with libopus support
* Everything required by `pillow`, including but not limited to:
    * `libjpeg`, `zlib`, `libwebp`, (`libtiff`, `libfreetype`, `openjpeg`, `tk`, `littlecms`)

### Install non-Python dependencies

For more information regarding installation of Pillow, please visit [Pillow documentation](https://pillow.readthedocs.io/en/3.0.x/installation.html).

#### OS X / macOS (with Homebrew)

Install [Homebrew](https://brew.sh), then:

```bash
brew install libjpeg webp python3
brew install libmagic
brew install ffmpeg --with-opus
```

#### Ubuntu 16.04 with `apt-get`

```bash
sudo apt-get install python3-dev python3-setuptools
sudo apt-get install libwebp-dev
sudo apt-get install libmagic-dev ffmpeg
```

## Python dependencies

Refer to `requirements.txt`, or [Channels Repository](channels-repository.md) for more details.

### To install
```bash
pip3 install -r requirements.txt
```

> If you'd like to start to give EFB a try, you can now head to the [Getting started](getting-started.md) page.
