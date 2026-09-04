# p2_koroglu.py
# Problem 2 - Pythagorean Numbers


def find_Pythagorean(n):
    """Return a list of tuples (a, b, c) with 0 < a, b, c <= n and a^2 + b^2 = c^2."""
    triples = []

    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a * a + b * b == c * c:
                    triples.append((a, b, c))

    return triples


def main():
    n = int(input("Enter a positive integer n: "))

    if n <= 0:
        print("Sorry, n has to be a positive integer.")
        return

    result = find_Pythagorean(n)

    if len(result) == 0:
        print("There are no Pythagorean triples with sides up to", n)
    else:
        print("Pythagorean triples with sides up to", n, ":")
        for triple in result:
            print(triple)
        print("Found", len(result), "triples.")


main()