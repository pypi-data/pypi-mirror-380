from yetanotherpackage import sum

def main() -> None:
    print("Hello from yetanotherpackage!")
    result = sum.funky_sum(3, 5)
    print(f"The funky sum of 3 and 5 is: {result}")
    result = sum.funky_sum(250, 5)
    print(f"The funky sum of 250 and 5 is: {result}")
