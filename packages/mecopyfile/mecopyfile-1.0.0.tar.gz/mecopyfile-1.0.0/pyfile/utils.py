def flatten(base_list: list):
    result = []
    for element in base_list:
        if type(element) == list:
            result.extend(flatten(element))
        else:
            result.append(element)
    return result