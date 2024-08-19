
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
