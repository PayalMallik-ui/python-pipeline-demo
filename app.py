# Simple Python script that does math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    result1 = add(5, 3)
    result2 = subtract(10, 4)
    
    print(f"5 + 3 = {result1}")
    print(f"10 - 4 = {result2}")
    print("✅ All calculations successful!")