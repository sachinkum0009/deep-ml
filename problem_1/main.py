import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    # Dimension mismatch check
    if a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)
    # Your implementation here

    c_t = torch.matmul(a_t, b_t)
    return c_t

def main():
    a, b = torch.tensor([[1,2,3],[2,4,5],[6,8,9]], dtype=torch.float), torch.tensor([1,2,3], dtype=torch.float) 
    c_t = matrix_dot_vector(a, b)
    print(f"c_t is {c_t}")

if __name__ == '__main__':
    main()
