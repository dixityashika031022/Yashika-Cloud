stack = []

text = "Yashika"

for ch in text:
    stack.append(ch)

reverse = ""
while stack:
    reverse += stack.pop()

print("Original String:", text)
print("Reversed String:", reverse)
