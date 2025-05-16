import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(numbers).reshape(3, 3)
    
    calculations = {
        'mean': [
            arr.mean(axis=1).tolist(),      # rows
            arr.mean(axis=0).tolist(),      # columns
            arr.mean().item()               # flattened mean as scalar
        ],
        'variance': [
            arr.var(axis=1).tolist(),
            arr.var(axis=0).tolist(),
            arr.var().item()
        ],
        'standard deviation': [
            arr.std(axis=1).tolist(),
            arr.std(axis=0).tolist(),
            arr.std().item()
        ],
        'max': [
            arr.max(axis=1).tolist(),
            arr.max(axis=0).tolist(),
            arr.max().item()
        ],
        'min': [
            arr.min(axis=1).tolist(),
            arr.min(axis=0).tolist(),
            arr.min().item()
        ],
        'sum': [
            arr.sum(axis=1).tolist(),
            arr.sum(axis=0).tolist(),
            arr.sum().item()
        ]
    }
    
    return calculations
