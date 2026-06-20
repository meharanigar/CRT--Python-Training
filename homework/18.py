#cycle rotation
n,k = int(input().split())
arr = list(map(int, input().split()))
it = iter(arr)
s =0
for i in range(k):
    try:
        s += next(it)
    except StopIteration:
        it = iter(arr)
        s += next(it)
print(s)


#password

def pass_gen(s):
    while True:
        for ch in s:
            yield ch

s = input()
k = int(input())

g = pass_gen(s)

password = ""

for _ in range(k):
    password += next(g)

print(password)



#generator
n = int(input())

students = [input().split() for _ in range(n)]

def attendance_check(func):
    def wrapper(name, p, m):
        if int(p) >= 75 and int(m) <= 2:
            return f"{name} Allowed"
        return f"{name} Not Allowed"
    return wrapper

@attendance_check
def student(name, p, m):
    pass

for name, p, m in students:
    print(student(name, p, m))