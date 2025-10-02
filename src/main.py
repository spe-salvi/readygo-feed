import time
from config.config import *

def main():
    start = time.perf_counter()
    

    end = time.perf_counter()
    seconds = end - start
    elapsed = seconds / 60

    print(f'Elapsed time: {elapsed:.2f} minutes')

if __name__ == "__main__":
    main()