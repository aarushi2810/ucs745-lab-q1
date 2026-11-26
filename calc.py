def calculate(a, b, op="*"):
    """
    Calculator function supporting multiple operations.
    op='+'  -> addition
    op='-'  -> subtraction
    op='*'  -> multiplication (default, kept from feature-multiply)
    op='/'  -> division
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


if __name__ == "__main__":
    print(calculate(3, 4, op="*"))  # 12  (multiply)
    print(calculate(3, 4, op="-"))  # -1  (subtract)
    print(calculate(3, 4, op="+"))  #  7  (add)
