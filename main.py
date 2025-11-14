def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def main():
    # Test the functions
    num1 = 10
    num2 = 5
    num3 = 10
    num4 = 2
    
    print(f"Adding {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtracting {num2} from {num1}: {subtract(num1, num2)}")
    print(f"Multiplication")
    print(f"Division")

if __name__ == "__main__":
    main()