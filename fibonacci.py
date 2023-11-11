def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def main(nterms):
    result = fibonacci(nterms)
    print(f"Fibonacci sequence up to {nterms} terms: {result}")

if __name__ == "__main__":
    import sys
    nterms = int(sys.argv[1]) if len(sys.argv) > 1 else 5  # Default to 5 if not provided
    main(nterms)


