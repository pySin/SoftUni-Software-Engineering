# Matrix of palindromes


def call_functions():
    rows, cols = [int(x) for x in input().split()]
    for i in range(rows):
        for j in range(cols):
            j = j + i
            ascii_a = ord("a")
            word = chr(ascii_a + i) + chr(ascii_a + j) + chr(ascii_a + i)
            print(word, end=" ")
        print()


if __name__ == "__main__":
    call_functions()
