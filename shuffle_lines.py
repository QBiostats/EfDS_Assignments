import sys
import random

def shuffle_lines():
    if len(sys.argv) != 3:
        print("Error: use 'python shuffle_lines.py <inFileName> <outFileName>")
        return
    
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try: 
        with open(in_file, "r") as f:
            lines = f.readlines()

        if not lines:
            print(f"Warning: {in_file} is empty")
            return
        
        random.shuffle(lines)

        with open(out_file, "w") as f:
            f.writelines(lines)

        print(f"Done, the lines out {in_file} are shuffled")

    except FileNotFoundError:
        print(f"Error: The file '{in_file}' does not exist.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    shuffle_lines()
