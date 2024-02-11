def start_spring(**example_objects):
    data = {}
    for key, value in example_objects.items():
        if value not in data.keys():
            data[value] = []
        data[value].append(key)

    sorted_collection = dict(sorted(data.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []

    for type, collection in sorted_collection.items():
        result.append(f"{type}:")
        for item in sorted(collection):
            result.append(f"-{item}")

    return "\n".join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}

print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}

print(start_spring(**example_objects))

