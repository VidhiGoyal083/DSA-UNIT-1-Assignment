# Recursive Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Naive Recursive Fibonacci
def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)


# Memoized Fibonacci
def fibonnaci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonnaci_memo(n - 1, memo) + fibonnaci_memo(n - 2, memo)
    return memo[n]


# Tower of Hanoi
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# Recursive Binary Search
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


# Example Test Runs
if __name__ == "__main__":
    print("Factorial of 7:", factorial(7))
    print("Fibonacci of 8 (naive):", fibonnaci(8))
    print("Fibonacci of 8 (memoized):", fibonnaci_memo(8))

    print("\nTower of Hanoi for N=3:")
    hanoi(3, 'A', 'B', 'C')

    arr = [1, 3, 5, 7, 9, 11]
    print("\nBinary Search result:", binary_search(arr, 0, len(arr)-1, 7))

    