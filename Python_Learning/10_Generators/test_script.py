
def fibonacci_num(num):
    a = 0
    b = 1
    fibonacci_nums = []
    for i in range(num):
        fibonacci_nums.append(a)
        temp = a    
        a = b
        b = temp + b


for x in fibonacci_num(21):
    print(x)