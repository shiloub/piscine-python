import math
def NULL_not_found(data: any) -> int:
    name_types = {
        int: "Zero",
        float: "Cheese",
        str: "Empty",
        bool: "Fake"
    }

    if data is None:
        type_name = "Nothing"
    else:
        type_name = name_types.get(type(data))
    if (type_name != "Type not found" and data is None) or (type(data) is int and data == 0) or (type(data) is float and math.isnan(data)) or (type(data) is bool and data == False) or (type(data) is str and data == ""):
        print(f"{type_name}: {data} {type(data)}")
    else:
        print("Type not found")
        return(1)
    return (0)
