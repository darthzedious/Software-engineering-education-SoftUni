class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, milliliters):
        if self.content + milliliters < Glass.capacity:
            self.content += milliliters
            return f"Glass filled with {milliliters} ml"
        else:
            return f"Cannot add {milliliters} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
