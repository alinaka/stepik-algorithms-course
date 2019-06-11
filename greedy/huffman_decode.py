import sys


def huffman_decode(dictionary, string):
    sequence = ''
    result = ''
    for s in string:
        sequence += s
        if sequence in dictionary:
            result += dictionary[sequence]
            sequence = ''
    return result


def main():
    k, l = map(int, sys.stdin.readline().split())
    dictionary = {}
    for _ in range(k):
        letter, code = sys.stdin.readline().strip().split(": ")
        dictionary[code] = letter
    string = sys.stdin.readline()
    result = huffman_decode(dictionary, string)
    print(result)


if __name__ == "__main__":
    main()