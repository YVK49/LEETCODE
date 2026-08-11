import sys


def solve(s):
    n = len(s)

    valid_even_ways = 0
    for start_val in ["0", "1"]:
        is_valid = True
        for i in range(0, n, 2):
            expected = start_val if (i // 2) % 2 == 0 else str(1 - int(start_val))
            if s[i] != "?" and s[i] != expected:
                is_valid = False
                break
        if is_valid:
            valid_even_ways += 1

    valid_odd_ways = 0
    for start_val in ["0", "1"]:
        is_valid = True
        for i in range(1, n, 2):
            expected = start_val if (i // 2) % 2 == 0 else str(1 - int(start_val))
            if s[i] != "?" and s[i] != expected:
                is_valid = False
                break
        if is_valid:
            valid_odd_ways += 1

    return valid_even_ways * valid_odd_ways


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1

    out = []
    for _ in range(t):
        pos += 1          # the n line; len(s) gives the same thing
        s = data[pos]
        pos += 1
        out.append(solve(s))

    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
