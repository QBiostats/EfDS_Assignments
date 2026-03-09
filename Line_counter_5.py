import sys

if __name__ == "__main__":
    fileName = sys.argv[1]

    lineCnt = 0
    with open(fileName, mode = "r") as f:
        for l in f:
            lineCnt += 1
    print(f"Number of lines in {fileName} is {lineCnt}")

