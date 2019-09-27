alpha = input()
shift = int(input())

if abs(shift) > len(alpha):
    if shift > 0:
        shift = shift - len(alpha)
    else:
        shift = shift + len(alpha)

print(len(alpha))

print(alpha[shift:] + alpha[:shift])
print(alpha)
print(alpha[-shift:] + alpha[:-shift])

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# -27
