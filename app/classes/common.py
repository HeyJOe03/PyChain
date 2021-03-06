def list_to_str(given_list: list) -> str:
    if len(given_list) == 0:
        return "[]"
    if type(given_list[0]) == list:
        for sub_list in given_list:
            list_to_str(sub_list)

    def call_str(o):
        return str(o)

    str_list_iter = map(call_str, given_list)
    list_str = list(str_list_iter)

    return str(list_str)


def list_to_dict(given_list: list) -> list:
    if len(given_list) == 0:
        return []
    if type(given_list[0]) == list:
        for sub_list in given_list:
            list_to_dict(sub_list)

    def call_as_dict(o):
        return o.to_dict()

    dict_list_iter = map(call_as_dict, given_list)
    list_dict = list(dict_list_iter)

    return list_dict
