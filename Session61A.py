import torch

X = torch.rand(5, 3)
print(X)

print()

Y = X.view(15)
print(Y)

P = torch.randn(1)
print(P)
print(P.item()) # works on sinlgle value tensors :)

print()

# print(X.item()) # error