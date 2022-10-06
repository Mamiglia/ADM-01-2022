from collections import namedtuple

N = int(input())
Student = namedtuple('Student',input().split())
tot = 0
for _ in range(N):
    s = Student(*input().split())
    tot += int(s.MARKS)
print(f"{tot/N:.2f}")
