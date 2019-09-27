import statistics

med = []
mod = []
all = []

n = int(input())
for i in range(n):
    a = input().split()
    result = [int(item) for item in a]
    all = all + result
    m = statistics.median(result)
    # m = int(m)
    med.append(m)
    mod.append(int(max(a, key=a.count)))

print(" ".join([str(i) for i in med]))
print(" ".join([str(i) for i in mod]))
print(statistics.median(med))
print(max(mod, key=mod.count))
print(statistics.median(all))
print(max(all, key=all.count))
