# Penambahan
x = 5
y = 7
print(x+y)

# Pengurangan
x = 9
y = 3
print(x-y)

# Perkalian
x = 9
y = 32
print(x * y)

# Pembagian
a = 20
b = 0
if b == 0 :
    print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")

# Modulus
a = 39
b = 2
print(a%b)

# Fibonacci (n)
n = 5
def fibonancci(n):
    if n <= 1:
        return n
    else:
        return fibonancci(n - 1) + fibonancci(n - 2)

for i in range(n):
    print(fibonancci(n-i))