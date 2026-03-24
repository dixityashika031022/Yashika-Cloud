num = 153
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** 3
    temp = temp // 10

if sum_val == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
