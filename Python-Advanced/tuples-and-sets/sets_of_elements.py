# Sets of elements


n, m = (int(x) for x in input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

print(*(n_set & m_set), sep="\n")

