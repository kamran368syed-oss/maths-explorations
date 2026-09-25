"""
Fibonacci Numbers and the Golden Ratio

The Fibonacci sequence starts 1, 1 and each new number is the sum of the
two before it:
    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

If you divide each Fibonacci number by the one before it, the answers get
closer and closer to the golden ratio:
    phi = (1 + sqrt(5)) / 2 = 1.6180339887...

This program checks that numerically and draws a graph of it.
"""

import math
import matplotlib.pyplot as plt


def fibonacci(count):
    """Return a list of the first `count` Fibonacci numbers."""
    numbers = [1, 1]
    while len(numbers) < count:
        numbers.append(numbers[-1] + numbers[-2])
    return numbers[:count]


def main():
    phi = (1 + math.sqrt(5)) / 2
    count = 20
    fib = fibonacci(count)

    print(f"The first {count} Fibonacci numbers:")
    print(fib)
    print(f"\nThe golden ratio is {phi:.10f}\n")

    # Ratio of each number to the one before it
    ratios = []
    print(f"{'n':>3}  {'F(n+1) / F(n)':>15}  {'distance from phi':>18}")
    for i in range(1, count):
        ratio = fib[i] / fib[i - 1]
        ratios.append(ratio)
        print(f"{i:>3}  {ratio:>15.10f}  {abs(ratio - phi):>18.10f}")

    # Graph: the ratios settling down to phi
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, count), ratios, marker="o", label="F(n+1) / F(n)")
    plt.axhline(phi, color="red", linestyle="--", label=f"golden ratio = {phi:.5f}")
    plt.title("Ratios of consecutive Fibonacci numbers approach the golden ratio")
    plt.xlabel("n")
    plt.ylabel("Ratio")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/fibonacci_ratios.png", dpi=120)
    plt.close()

    print("\nGraph saved in the images folder.")


if __name__ == "__main__":
    main()
