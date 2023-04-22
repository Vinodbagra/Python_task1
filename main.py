list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    merged_data = {}
    for data in list_1 + list_2:
        id = data.get("id")
        if id in merged_data:
            merged_data[id].update(data)
        else:
            merged_data[id] = data

    return list(merged_data.values())


list_3 = merge_lists(list_1, list_2)
print(list_3)
