
def divide(num1, num2):
    try:
        return (num1/num2)
    except ZeroDivisionError:
        return "\nYou're causing singularity, try again ! \n"


print(divide(4, 2))
