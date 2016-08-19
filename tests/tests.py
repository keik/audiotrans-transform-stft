# -*- coding: utf-8 -*-

import pytest
import wave
import numpy as np
from audiotrans_transform_stft import STFTTransform


def test_accept_arg_of_verbose():
    STFTTransform(['-v'])  # no error would be raised


def test_accept_args_of_window_and_hop_sizes():

    # 2048 element array to 5 row matrix (= 1024 / 1024 + 1024 / 256)
    tr = STFTTransform('-w 1024 -H 256'.split())
    data = np.arange(2048)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 5)

    # 2048 element array to 7 row matrix (= 512 / 512 + 1536 / 256)
    tr = STFTTransform('-w 512 -H 256'.split())
    data = np.arange(2048)
    transformed = tr.transform(data)
    assert transformed.shape == (257, 7)

    # 2048 element array to 13 row matrix (= 512 / 512 + 1536 / 128)
    tr = STFTTransform('-w 512 -H 128'.split())
    data = np.arange(2048)
    transformed = tr.transform(data)
    assert transformed.shape == (257, 13)


def test_int_array_should_transform_to_matrix_formed_properly_shape():

    # 0 element array to 0 row matrix (= 0 / 1024)
    tr = STFTTransform()
    data = np.arange(0)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 0)

    # 1023 element array to 0 row matrix (= 1023 / 1024)
    tr = STFTTransform()
    data = np.arange(1023)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 0)

    # 1024 element array to 1 row matrix (= 1024 / 1024 + 0 / 256)
    tr = STFTTransform()
    data = np.arange(1024)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 1)

    # 2047 element array to 4 row matrix (= 1024 / 1024 + 1023 / 256)
    tr = STFTTransform()
    data = np.arange(2047)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 4)

    # 2048 element array to 5 row matrix (= 1024 / 1024 + 1024 / 256)
    tr = STFTTransform()
    data = np.arange(2048)
    transformed = tr.transform(data)
    assert transformed.shape == (513, 5)


@pytest.mark.parametrize('buf_size, win_size, hop_size', [(1024, 1024, 256),
                                                          (160, 100, 30)])
def test_repeatedly_transform_should_be_connected_smoothly(buf_size, win_size, hop_size):

    tr = STFTTransform('-w {} -H {}'.format(win_size, hop_size).split())
    wf = wave.open('tests/fixture/drums+bass.wav')
    all_data = np.fromstring(wf.readframes(wf.getnframes()), np.int16)
    d = stft(all_data, win_size, hop_size)
    transformed = np.reshape([], (win_size // 2 + 1, -1))
    for idx, s in enumerate(range(0, len(all_data), buf_size)):
        tmp = tr.transform(all_data[s:s + buf_size])
        transformed = np.concatenate((transformed, tmp), 1)
    for i in range(transformed.shape[1]):
        assert (transformed[:, i] == d[:, i]).all()


def stft(x, window_size, hop_size):
    win = np.hamming(window_size)
    return np.array([np.fft.fft(win * x[i:i + window_size])
                     for i in range(0, len(x) - window_size, hop_size)],
                    dtype=np.complex64).T[0:window_size // 2 + 1]
