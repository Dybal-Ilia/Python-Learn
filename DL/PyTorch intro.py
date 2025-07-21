import torch

tensor = torch.tensor([[[2, 3], [4, 5]], [[6, 7], [8, 9]]],
                      dtype = torch.float32, requires_grad=True)
print(f"Tensor type = {tensor.dtype}")
print(f"Tensor shape = {tensor.shape}")
print(f"Tensor dimensions = {tensor.ndim}")

print(type(tensor[0, 0, 0]))

print(tensor[0, 0, 0].item())


torch_zeros = torch.zeros([2, 3, 2])
print(torch_zeros)

print(torch.cuda.is_available())


tensor = torch.tensor([1., 2., 3.], requires_grad=True)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tensor = tensor.to(device)