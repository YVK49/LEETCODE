import sys


def solve(n: int, s: str) -> int:
    valid_even_ways = 0
    valid_odd_ways = 0

    for start_val in ["0", "1"]:
        is_valid = True
        for i in range(0, n, 2):
            expected = start_val if (i // 2) % 2 == 0 else str(1 - int(start_val))
            if s[i] != "?" and s[i] != expected:
                is_valid = False
                break
        if is_valid:
            valid_even_ways += 1

    for start_val in ["0", "1"]:
        is_valid = True
        for i in range(1, n, 2):
            expected = start_val if ((i - 1) // 2) % 2 == 0 else str(1 - int(start_val))
            if s[i] != "?" and s[i] != expected:
                is_valid = False
                break
        if is_valid:
            valid_odd_ways += 1

    return valid_even_ways * valid_odd_ways


def main():
    line = sys.stdin.readline()
    if not line:
        return

    t = int(line.strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        print(solve(n, s))


if __name__ == "__main__":
    main()