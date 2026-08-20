# def all_thing_is_obj(object: any) ->int:
#     if isinstance(object,list):
#         print(f"List : {type(object)}")
#     elif isinstance(object,tuple):
#         print(f"Tuple : {type(object)}")
#     elif isinstance(object,set):
#         print(f"Set : {type(object)}")
#     elif isinstance(object,dict):
#         print(f"Dict : {type(object)}")
#     elif isinstance(object,str):
#         print(f"{object} is in the kitchen : {type(object)}")
#     else:
#         print("Type not found")
#         return 42
def all_thing_is_obj(object: any) -> int:
    Object_type = type(object)
    ret = None

    try:
        match object:
            case str():
                ret = f'{object} is in the kitchen : {Object_type}'
            case list():
                ret = f'List: {Object_type}'
            case tuple():
                ret = f'Tuple: {Object_type}'
            case set():
                ret = f'Set: {Object_type}'
            case dict():
                ret = f'Dict: {Object_type}'
            case _:
                ret = "Type not found"

        if ret is not None:
            print(ret)
    except Exception as e:
        print(f"Error: {e}")
    return 42

# ft_list = ["Hello","World!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}


# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))