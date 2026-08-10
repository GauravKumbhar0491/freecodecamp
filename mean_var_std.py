import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    data = np.asarray(numbers).reshape(3, 3)

    def statistics(operation):
        return [
            operation(data, axis=0).tolist(),
            operation(data, axis=1).tolist(),
            operation(data).item()
        ]

    return {
        "mean": statistics(np.mean),
        "variance": statistics(np.var),
        "standard deviation": statistics(np.std),
        "max": statistics(np.max),
        "min": statistics(np.min),
        "sum": statistics(np.sum)
    }

