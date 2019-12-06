a = [1,2,3] # 可变
b = 100 # 不可变
    
def test(m,n):
    print(id(m))
    print(id(n))

    m.append(4)
    n += 1

    print(id(m))
    print(id(n))
    print(m)
    print(n)

print(id(a))
print(id(b))
test(a,b)
print(a)
print(b)