# audiotrans-transform-stft

[![License](https://img.shields.io/pypi/l/audiotrans-transform-stft.svg?style=flat-square)](https://github.com/keik/audiotrans-transform-stft/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/audiotrans-transform-stft.svg?style=flat-square)](https://pypi.python.org/pypi/audiotrans-transform-stft)
[![PyPI](https://img.shields.io/pypi/v/audiotrans-transform-stft.svg?style=flat-square)](https://pypi.python.org/pypi/audiotrans-transform-stft)
[![Travis CI](https://img.shields.io/travis/keik/audiotrans-transform-stft.svg?style=flat-square)](https://travis-ci.org/keik/audiotrans-transform-stft)
[![Coverage Status](https://img.shields.io/coveralls/keik/audiotrans-transform-stft.svg?style=flat-square)](https://coveralls.io/github/keik/audiotrans-transform-stft)

[audiotrans](https://github.com/keik/audiotrans) transform module to Short-Time Fourier Transformation (STFT)


## Installation

```
pip install audiotrans-transform-stft
```


## Usage

As `audiotrans` transform module, like

```
audiotrans <filepath> -t stft -v -c spec
```

Options of the below is available through subarg (like `[ foo -h ]`)

```
usage: stft [-h] [-v] [-w WINDOW_SIZE] [-H]

audiotrans transform module for Short-Time Fourier Transformation (STFT)

Transform wave array as np.ndarray shaped (1,) to STFT matrix as
np.ndarray shaped (1 + widnow_size/2, (len(wave) - window_size) / hop-size + 1).

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Run as verbose mode
  -w WINDOW_SIZE, --window-size WINDOW_SIZE
                        Window size to FFT. Default is 1024
  -H, --hop-size        Hop size to FFT. Default is 256
```
