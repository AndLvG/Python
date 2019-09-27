import statistics
a = input().split()
b = 0
k = 0
result = [float(item) for item in a]
for i in a:
    b += len(i)
m = statistics.median(result)
m = float(m)
print(statistics.mean(result), m)