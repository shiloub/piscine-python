def all_thing_is_obj(data: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }
    type_name = type_names.get(type(data), "Type not found")
    if type_name == "String":
        print(f"{data} is in the kitchen : {type(data)}")
    elif type_name != "Type not found":
        print(f"{type_name} : {type(data)}")
    else:
        print(type_name)
    return(42)