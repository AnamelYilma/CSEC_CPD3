n, k = map(int, input().split())
s = input().split()

names = []
for i in range(n):
    names.append("Name" + str(i + 1))

for i in range(n - k + 1):
    if s[i] == "NO":
        names[i + k - 1] = names[i]

print(' '.join(names))
