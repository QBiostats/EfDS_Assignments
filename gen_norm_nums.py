import sys
import random
import statistics

def main():
    if len(sys.argv) != 5:
        print("Usage: python gen_norm_nums.py <num_samples> <mean> <stdev> <output_file>")
        return
    
    file_name = sys.argv[1]
    size = int(sys.argv[2])
    mu = float(sys.argv[3])
    sd = float(sys.argv[4])

    nums = [random.gauss(mu, sd) for _ in range(size)]

    with open(file_name, "w") as f:
        for n in nums:
            f.write(f"{n}\n")

    actual_mean = statistics.mean(nums)
    actual_sd = statistics.stdev(nums)

    print(f"Size: {size}")
    print(f"Mean: requested={mu}, generated = {actual_mean}")
    print(f"Stddev: requested={sd}, generated = {actual_sd}")

if __name__ == "__main__":
    main()