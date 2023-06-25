import torch
import numpy as np


def test_inv(dtype, dtype_str):
    x = np.load('test_x.npy')
    x = x.astype(dtype)
    x = torch.from_numpy(x)

    x2t = torch.inverse(x)
    x2 = np.linalg.inv(x.numpy())

    err = np.max(np.abs(x2 - x2t.numpy()))
    np.save('test_np_%s_%s.npy' % (np.__version__, dtype_str), x2)

    print('err:', dtype, err)

test_inv(np.float32, 'float32')
test_inv(np.float64, 'float64')
