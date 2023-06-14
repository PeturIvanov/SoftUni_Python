def start_spring(**kwargs):
    collection = {}
    result = []

    for spring_name, spring_type in kwargs.items():
        if spring_type not in collection:
            collection[spring_type] = []

        collection[spring_type].append(spring_name)

    sorted_collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))

    for spring_type, data in sorted_collection:
        result.append(f"{spring_type}:")
        result.append('\n'.join([f"-{el}" for el in sorted(data)]))

    return '\n'.join(result)




example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))