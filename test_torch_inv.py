import torch
import numpy as np



def test_inv(dtype):
    x = np.load('test_x.npy')
    x = x.astype(dtype)
    x = torch.from_numpy(x)

    x2t = torch.inverse(x)
    x2 = np.linalg.inv(x.numpy())

    err = np.max(np.abs(x2 - x2t.numpy()))

    print('err:', dtype, err)

test_inv(np.float32)
test_inv(np.float64)
