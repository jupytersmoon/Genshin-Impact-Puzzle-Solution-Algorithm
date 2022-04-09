# Function
def count(x, y):
    if x == y:
        return 0
    elif (x % 3) > y:
        return x + y - abs(y - x)
    else:
        return y - (x % 3)


def step(z, move):
    if z + move < 4:
        return z + move
    else:
        return (z + move) % 3


# Input
a = int(input("Insert the value for A: "))
b = int(input("Insert the value for B: "))
c = int(input("Insert the value for C: "))
d = int(input("Insert the value for D: "))

# Main
while a != b or a != c or a != d:
    if a == b:
        if b == c:
            tap = count(b, d)
            print("Tap B ", tap, " time(s)")
            a = step(a, tap)
            b = step(b, tap)
            c = step(c, tap)
        else:
            tap = count(c, b)
            print("Tap D ", tap, " time(s)")
            c = step(c, tap)
            d = step(d, tap)
    elif c == d:
        if c == b:
            tap = count(c, a)
            print("Tap C ", tap, " time(s)")
            b = step(b, tap)
            c = step(c, tap)
            d = step(d, tap)
        else:
            tap = count(b, c)
            print("Tap A ", tap, " time(s)")
            a = step(a, tap)
            b = step(b, tap)
    else:
        tap1 = count(c, d)
        tap2 = count(b, a)
        if tap1 < tap2:
            print("Tap B ", tap1, " time(s)")
            a = step(a, tap1)
            b = step(b, tap1)
            c = step(c, tap1)
        else:
            print("Tap C ", tap2, " time(s)")
            b = step(b, tap2)
            c = step(c, tap2)
            d = step(d, tap2)

print("The puzzle is complete:", a, b, c, d)
