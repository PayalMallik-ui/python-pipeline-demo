# Simple Python script that does math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return a ** b
if __name__ == "__main__":
    result1 = add(5, 3)
    result2 = subtract(10, 4)
    result3 = multiply(6, 7)
    
    print(f"5 + 3 = {result1}")
    print(f"10 - 4 = {result2}")
    print(f"6 * 7 = {result3}")
    result4 = divide(20, 4)
    print(f"20 / 4 = {result4}")
    result5 = power(2, 8)
    print(f"2 ^ 8 = {result5}")
    print("✅ All calculations successful!")
    