"""
    CUDA Support on Machines
    # reference link for CUDA -> https://developer.nvidia.com/cuda-zone

"""

import torch

print(torch.cuda.is_available()) # return either True or False

if torch.cuda.is_available():
    device = torch.device("cuda")   # Here in case CUDA support is available on Computer/Machine we will use it to solve problems
    # i.e. GPU will come in support of CPU
    X = torch.ones(5)
    Y = torch.ones_like(X, device=device) # Use GPU

