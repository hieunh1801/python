from pprint import pprint
"""
    sort trên một số trường có thể compare của đối tượng
    1. Sort trên 1 attribute
    2. Sort trên multiple attribute using lambda
"""

list_of_people = [
    {"name": "Hieu 1", "age": 22},
    {"name": "Hieu 2", "age": 23},
    {"name": "Hieu 3", "age": 24},
    {"name": "Hieu 4", "age": 25},
    {"name": "Hieu 5", "age": 26},
    {"name": "Hieu 6", "age": 25},
    {"name": "Hieu 7", "age": 24},
    {"name": "Hieu 8", "age": 23},
    {"name": "Hieu 9", "age": 26},
    {"name": "Hieu 2", "age": 20},
    {"name": "Hieu 1", "age": 20},
]
# 1. Sort on one attribute
sorted_list = sorted(list_of_people, key=lambda people: people["age"])
sorted_list = sorted(list_of_people, key=lambda people: people["name"])

# 2. Sort multiple attribute
sorted_list = sorted(list_of_people,
                     key=lambda people: (people["age"], people["name"]))
# đảo ngược tuổi  => -people["age"]
pprint(sorted_list)
