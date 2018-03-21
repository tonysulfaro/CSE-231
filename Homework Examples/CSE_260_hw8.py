import math

def sequence(n):
    if n == 0:
        return 1
    return (sequence(n-1) + 2)

def main():
    n = 2
    print(sequence(n))

if __name__ == "__main__":
    main()