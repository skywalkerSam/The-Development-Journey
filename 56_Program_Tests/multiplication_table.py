"""
Developer: skywalkerSam
Purpose: Multiplication Table Program
Stardate: 12021352.13:14

"""

print("""
            *************************************************
                >_    MULTIPLICATION TABLE PROGRAM

*************************************************************************
""")


def main():
    attempt = 1
    try:
        number = int(input("Enter a number: "))
        while (attempt <= 10):
            result = (f"{number} X {attempt} = {number*attempt}")
            attempt = attempt + 1 
            print(result)
    
    except:
        print("\n\t\t\tEnter a valid operation & Try Again!\t\t\t\n\n")

    return result


main()








