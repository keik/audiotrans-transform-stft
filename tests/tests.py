# -*- coding: utf-8 -*-

import sys
import numpy as np
from audiotrans_transform_stft import STFTTransform


def test_accept_arg_of_verbose():
    STFTTransform(['-v'])  # no error would be raised


def test_int_array_should_transform_to_matrix_formed_properly_shape():
    sys.argv[1:] = '-w 1024 -H 256'.split()

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
