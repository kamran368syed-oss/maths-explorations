"""
Collatz Conjecture Explorer

The rule:
    - If a number is even, halve it.
    - If a number is odd, multiply it by 3 and add 1.
    - Repeat until you reach 1.

The Collatz conjecture says that every positive whole number eventually
reaches 1. It has been checked by computer for enormous numbers, but
nobody has ever proved it is always true.

This program counts how many steps each starting number takes to reach 1
and draws some graphs of the results.
"""

import matplotlib.pyplot as plt


def next_number(n):
    """Apply the Collatz rule once."""
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(n):
    """Return the full list of numbers visited, starting at n and ending at 1."""
    sequence = [n]
    while n != 1:
        n = next_number(n)
        sequence.append(n)
    return sequence


def count_steps(n):
    """Return how many steps it takes for n to reach 1."""
    return len(collatz_sequence(n)) - 1


def main():
    # 1. Show one example sequence
    example = 27
    sequence = collatz_sequence(example)
    print(f"Starting at {example}:")
    print(sequence)
    print(f"It takes {count_steps(example)} steps to reach 1.")
    print(f"The highest number it reaches is {max(sequence)}.\n")

    # 2. Count steps for every starting number up to a limit
    limit = 10000
    starts = list(range(1, limit + 1))
    steps = [count_steps(n) for n in starts]

    longest = max(steps)
    longest_start = starts[steps.index(longest)]
    print(f"Checked every number from 1 to {limit}: all of them reach 1.")
    print(f"The number that takes the most steps is {longest_start} "
          f"({longest} steps).")

    # 3. Graph: the path of one starting number
    plt.figure(figsize=(10, 5))
    plt.plot(sequence, marker=".")
    plt.title(f"Collatz sequence starting at {example}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.grid(True)
    plt.savefig("images/collatz_path_27.png", dpi=120)
    plt.close()

    # 4. Graph: steps needed for every starting number
    plt.figure(figsize=(10, 5))
    plt.scatter(starts, steps, s=1)
    plt.title(f"Steps to reach 1 for starting numbers 1 to {limit}")
    plt.xlabel("Starting number")
    plt.ylabel("Number of steps")
    plt.grid(True)
    plt.savefig("images/collatz_steps.png", dpi=120)
    plt.close()

    print("\nGraphs saved in the images folder.")


if __name__ == "__main__":
    main()
