def main():
     
    a, b = enter_nums()
    
    print(add(a, b))
    print(subtrt(a, b))
    

# Making code more efficient, adding input function for entering number
def enter_nums():
    num1 = int(input("Enter first number? "))
    num2 = int(input("Enter second number? "))
    return num1, num2


def add(x: int, y: int) -> int:
    return x + y

# Adding Subtraction function that will subtract 2 number
def subtrt(x: int, y: int) -> int:
    return x - y

if __name__ == "__main__":
    main()