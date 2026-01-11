import torch

def transpose_matrix(a) -> torch.Tensor:
    """
    Transpose a 2D matrix using PyTorch.
    
    Args:
        a: A 2D matrix (can be list, numpy array, or torch.Tensor)
    
    Returns:
        A transposed torch.Tensor
    """
    a_t = torch.as_tensor(a)
    # Your code here
    b_t = a_t.T
    return b_t
    
def main():
    a = torch.tensor([[1, 2, 3], [4, 5, 6]])
    b = transpose_matrix(a)
    print(f"transpose of a: {b}")

if __name__ == '__main__':
    main()
