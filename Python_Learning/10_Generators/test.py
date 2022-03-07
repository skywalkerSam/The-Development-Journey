# Testing...


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


list1 = make_list(10000)
print(list1)


'''
It's also generating numbers but, not efficiently! It's being stored in memory so, We'll have to wait before this process completes.
'''
