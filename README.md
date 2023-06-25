# pytorch-test

the results is different for the api ```torch.inverse``` when using ```torch.1.12.0``` and ```torch.2.0.1```, and here is the testing steps

## test using torch-1.12.0+cu116 and numpy-1.22.3
```
python test_torch_inv.py
```
two files ```test_np_1.22.3_float32.npy``` and ```test_np_1.22.3_float64.npy``` will be created and the terminal output (on my machine) is like
```
err: <class 'numpy.float32'> 0.00020217896
err: <class 'numpy.float64'> 3.814726312612038e-13
```

## test using torch-2.0.1+cu118 and numpy-1.24.3
```
python test_torch_inv.py
```
two files ```test_np_1.24.3_float32.npy``` and ```test_np_1.24.3_float64.npy``` will be created and the terminal output (on my machine) is like
```
err: <class 'numpy.float32'> 0.0004506111
err: <class 'numpy.float64'> 5.03597163969971e-13
```

## check ```np.linalg.inv```
```
import numpy as np
x1 = np.load('test_np_1.22.3_float32.npy')
x2 = np.load('test_np_1.24.3_float32.npy')
print(np.max(np.abs(x1-x2)))   # # expected output: 0.0

x1 = np.load('test_np_1.22.3_float64.npy')
x2 = np.load('test_np_1.24.3_float64.npy')
print(np.max(np.abs(x1-x2)))   # # expected output: 0.0
```


