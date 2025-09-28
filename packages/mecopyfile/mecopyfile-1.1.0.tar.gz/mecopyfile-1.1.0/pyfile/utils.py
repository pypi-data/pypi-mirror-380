from enum import Enum

def flatten(base_list: list):
    result = []
    for element in base_list:
        if type(element) == list:
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

def convert_enum_values_to_str(enum_values: list[Enum | str]):
    return [x.value if type(x) != str else x for x in enum_values]
