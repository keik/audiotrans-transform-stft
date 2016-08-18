# -*- coding: utf-8 -*-

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


def test_repeatedly_transform_should_be_connected_smoothly():

    # 0 element array to 0 row matrix (= 0 / 1024)
    tr = STFTTransform()
    all_data = np.arange(4096)

    for s, col in zip(range(0, 4096, 1024),
                      [1, 4, 4, 4]):
        data = all_data[s:s + 1024]
        transformed = tr.transform(data)
        assert transformed.shape == (513, col)
