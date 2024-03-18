def get_info(search, **kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"
    # if search in kwargs.keys():
    #     print(kwargs[search])
    # else:
    #     print("Not here")


print(get_info(**{"name": "George", "town": "Sofia", "age": 26}))
