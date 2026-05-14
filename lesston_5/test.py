# # some_var_1 = "var 1"
# # some_var_2 = "var 1"

# # res = some_var_1 is some_var_2
# # print(res)


# # some_str_1 = ""
# some_str_1 = None

# if some_str_1 is None:
#     print("hello")

# # bool_from_str = bool(some_str_1)


# # print(bool_from_str)


a: dict = {
    "a": {
        "a": ["1", "2", "3"],
    },
}

b: dict = {
    "a": {
        "a": ["1", "2", "3"],
    },
}

print(a.get("a"))
