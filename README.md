<h1 align="center">QR Code Generator 📟</h1

---

<p align="center"><em>A very simple QR code generator for URLs</em></p>

---

## Installation 💬

Install the package with [pip](https://pip.pypa.io/en/stable/installing/):

``` bash
$ pip install qr-code-generator
```

You can also clone the repository and install with [poetry](https://python-poetry.org/):

``` bash
$ pip install poetry
$ poetry install
```

## Usage ✅

It's pretty simple, check the example:

``` bash
$ qr-code https://github.com/kludex
```

If you want to see more options:

``` bash
$ qr-code --help
Usage: qr-code [OPTIONS] URL

  Generate a QR code that points to a URL.

Arguments:
  URL  [required]

Options:
  -o, --output TEXT  path to output  [default: qr-code.svg]
  --help             Show this message and exit.
```

## License 📜

This project is under the MIT license.
