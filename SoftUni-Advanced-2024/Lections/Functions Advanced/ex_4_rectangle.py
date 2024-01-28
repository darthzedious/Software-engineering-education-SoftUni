def rectangle(length, width):
    if not isinstance(width, int) or not isinstance(length, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2*length + 2 * width

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
