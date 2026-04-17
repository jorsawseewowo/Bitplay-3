def longest_consecutive_ones(n: int) -> int:
    count = 0
    while n != 0:
        n = n & (n << 1)
        count += 1
    return count
if __name__ == "__main__":
    num = int(input("Enter your number: "))
    result = longest_consecutive_ones(num)
    print("Longest consecutive 1’s length:", result)
