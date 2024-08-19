def greeting_user():
    print('Hello world!')
# greeting_user()

def aoa():
    print('Asalam o Alaekum, All the way from Pakistan')
# aoa()


def aoa(name):
    print(f'Asalam o Alaekum, {name}!,Kaifa Haluk?')
# aoa('Ahmed')

def aoa(name='Meray Payaray Bhai'):
    print(f"Asalam o Alaekum, {name}! kaifa Haluk?")
# aoa()


def square(number):
    return number*number
result = square(8)
# print(result)



# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(3))


# Lambda Function

def x(a):
    return a + 5
# print(x(5))

x = lambda a: a + 5
# print(x(5))

def y(a,b):
    return a*b
# print(y(4,5))

y = lambda a,b: a+b/5
# print(y(4,5))


# 1
sum_list = lambda lst: sum(lst)
# print(sum_list([1,2,3,4]))

# 2
access_tuple = lambda t: t[2]
# print(access_tuple((1,2,3)))

# 3
add_to_set =lambda s,x: s.union(x)
# print(add_to_set({1,2,3},{3,4}))


# 4
get_value = lambda d, k: d.get(k,'Key not found')
# print(get_value({'name':'Ahmed','age':25},'address'))

# 5
reverse_string =lambda s:s[::-1]
print(reverse_string('String'))
