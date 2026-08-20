def NULL_not_found(object: any) -> int:
    try:
        match object:
            case None:
                print(f"Nothing: {object} {object.__class__}")
            case float() if object != object:
                print(f"Cheese: {object} {object.__class__}")
            case int() if object == 0:
                print(f"Zero: {object} {object.__class__}")
            case str() if object == "":
                print(f"Empty: {object.__class__}")
            case bool() if object is False:
                print(f"Fake: {object} {object.__class__}")
            case _:
                print("Type not Found")
                return 1
    except Exception as e:
        print(f"Error: {e}")

    return 0


# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))