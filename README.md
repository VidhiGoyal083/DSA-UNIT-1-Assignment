# Unit 1 Assignment – Recursion and Time Complexity


## 1. Recursive Factorial

### Problem
Compute the factorial of a number using recursion.

### Explanation
- Factorial of 0 is 1 (base case)
- For any n > 0, factorial(n) = n × factorial(n − 1)

### Time Complexity
O(n) – one recursive call for each value of n

### Space Complexity
O(n) – recursion stack grows to depth n

---

## 2. Recursive Fibonacci

### Problem
Compute the nth Fibonacci number using recursion.

---

### 2.1 Naive Recursive Fibonacci

### Explanation
- fib(0) = 0
- fib(1) = 1
- fib(n) = fib(n − 1) + fib(n − 2)

This approach is inefficient because the same Fibonacci values are recalculated multiple times.

### Time Complexity
O(2ⁿ) – exponential number of recursive calls

### Space Complexity
O(n) – recursion depth

---

### 2.2 Memoized Fibonacci

### Explanation
Previously computed Fibonacci values are stored in memory to avoid repeated calculations.

### Time Complexity
O(n) – each Fibonacci number is computed once

### Space Complexity
O(n) – memo table and recursion stack

---

## 3. Tower of Hanoi

### Problem
Move N disks from source peg to destination peg using an auxiliary peg.

### Explanation
1. Move n−1 disks to auxiliary peg
2. Move the largest disk to destination peg
3. Move n−1 disks from auxiliary to destination

---

### Trace for N = 3

Move disk 1 from A to C  
Move disk 2 from A to B  
Move disk 1 from C to B  
Move disk 3 from A to C  
Move disk 1 from B to A  
Move disk 2 from B to C  
Move disk 1 from A to C  

Total moves = 7

---

### Time Complexity
O(2ⁿ)

### Space Complexity
O(n)

---

## 4. Recursive Binary Search

### Problem
Search for an element in a sorted array using recursion.

### Explanation
At each step, the array is divided into two halves.

### Time Complexity
O(log n)

### Space Complexity
O(log n)

---

## Conclusion

All required recursive algorithms are implemented and analyzed according to Unit 1 syllabus.
