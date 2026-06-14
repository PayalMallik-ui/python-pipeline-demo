# Simple Python script that does math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
if __name__ == "__main__":
    result1 = add(5, 3)
    result2 = subtract(10, 4)
    
    print(f"5 + 3 = {result1}")
    print(f"10 - 4 = {result2}")
    result3 = multiply(6, 7)
    print(f"6 * 7 = {result3}")
    print("✅ All calculations successful!")
    
    