from collections import deque

q = deque()

q.append(100)
q.append(200)
q.append(300)

print("Queue:", q)
print("Deleted:", q.popleft())
print("Front element:", q[0])
print("Queue after deletion:", q)
