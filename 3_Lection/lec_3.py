# def sum(x, y):
#     return x+y



# def mult(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a,b))
#     # return(op(a,b))

# calc(lambda x, y: x + y , 4, 5)


# list = []
# for i in range(1,101):
#     if(i%2) == 0:
#         list.append(i)

# print(list)

# def f(x):
#     return x**3


# list = [f(i) for i in range(1,21) if (i%2) == 0]
# print(list)

# def select(f, col):
#     return [f(x) fro x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x% 2, res)


# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10, li))
# print(li)



# data = list(map(int, input().split()))
# print(data)



# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)



# data = '1 2 3 4 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x,x**2), res))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# id = [22,33,44,55,66]

# print(list(zip(users,id)))


