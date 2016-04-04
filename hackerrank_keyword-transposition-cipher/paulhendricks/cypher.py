#!/bin/python3
import numpy as np
import string


def fix_keyword(x):
    unique = []
    for i in x.upper():
        if i in unique:
            pass
        else:
            unique.append(i)
    return unique


def translate(raw_keyword, message):
    alphabet = string.ascii_uppercase
    keyword = fix_keyword(raw_keyword)
    n = len(keyword)
    keyword_sorted = np.unique(np.sort([i for i in keyword]))
    possible = np.array([i for i in alphabet if i not in keyword_sorted])
    arr = np.r_[keyword, possible]
    arr2 = [arr[i::n] for i in np.arange(n)]
    arr3 = {i: j for i, j in zip(keyword, arr2)}
    cipher_alphabet = []
    for i in keyword_sorted:
        cipher_alphabet = np.r_[cipher_alphabet, arr3[i]]
    cipher = {c: l for c, l, in zip(cipher_alphabet, alphabet)}
    solved = []
    for s in message:
        if s == ' ':
            solved.append(' ')
        else:
            solved.append(cipher[s])
    solved = ''.join(solved)
    return solved


def main():
    file_name = '../input.txt'
    with open(file_name, 'r') as f:
        x = f.read().strip().split('\n')
    t = int(x[0].strip())
    remainder = x[1:]
    for i in np.arange(0, t + 1, 2):
        print(translate(remainder[i], remainder[i + 1]))


if __name__ == '__main__':
    main()

