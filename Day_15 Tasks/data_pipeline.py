import time
import numpy as np
import pandas as pd


# Decorator to measure and print execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f}s")
        return result
    return wrapper


# Generator streaming valid numeric lines while skipping malformed entries
def stream_numbers(file_path):
    with open(file_path, "r") as f:
        for line in f:
            text = line.strip()
            if not text:
                continue
            try:
                yield float(text)
            except ValueError:
                print(f"Skipping invalid data: {text}")


@measure_time
def run_pipeline(file_path):
    values = list(stream_numbers(file_path))
    arr = np.array(values, dtype=float)
    summary_df = pd.DataFrame({
        "Count": [len(arr)],
        "Mean": [np.mean(arr)],
        "Std": [np.std(arr)]
    })
    return summary_df


result = run_pipeline("numbers.txt")
print(result)