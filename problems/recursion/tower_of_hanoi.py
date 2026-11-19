import sys

sys.setrecursionlimit(20000)

n = int(input())

src = "A"
aux = "B"
dest = "C"

moves = []

def occurance(n, src, aux, dest):
    if n == 0:
        return

    occurance(n - 1, src, dest, aux)
    moves.append(f"Move {src} to {dest}")
    occurance(n - 1, aux, src, dest)

def tower_of_hanoi(n, src, aux, dest):
    occurance(n, src, aux, dest)
    sys.stdout.write("\n".join(moves))

tower_of_hanoi(n, src, aux, dest)

# https://codeforces.com/group/DNruwPkRNA/contest/733421/problem/S
# 🚩 use python3 instead of pypy
