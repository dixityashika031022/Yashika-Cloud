a = 12
b = 18

x = a
y = b

while b != 0:
    a, b = b, a % b

hcf = a
lcm = (x * y) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
