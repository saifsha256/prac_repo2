def main():
    num1 = int(input("Enter first number? "))
    num2 = int(input("Enter second number? "))
    
    print(add(num1, num2))

def add(x: int, y: int) -> int:
    return x + y

if __name__ == "__main__":
    main()