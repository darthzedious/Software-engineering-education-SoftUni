class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.new_count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.new_count <= 0:
            raise StopIteration
        self.new_count -= 1

        return self.new_count


#  not passing in judge but still correct
class DictionaryIterator:
    def __init__(self, dictionary: dict):  # {1: "1", 2: "2"}
        self.items = dictionary.items() # dictionary.items() => dict_items([(1, "1"), (2, "2")])

    def __iter__(self):
        return iter(self.items)


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")