nessesery_data = {
    "x": list,
    "y": list,
    "x_label": str,
    "y_label": str,
    "title": str
}


def check(context) -> None:
    """
    Throws an error if any of the keys are missing from the object

    Parameters:
       context (__main__.Context): communication object

    Raises:
        ValueError: If any keys are missing
        ValueError: If any keys have an incorrect data type
        ValueError: Arrays have different lengths
    """
    body = dict(context.req.body)

    missing = list()
    invalid = list()

    for key in body.keys():
        if key not in nessesery_data.keys():
            missing.append(key)
        elif type(body[key]) != nessesery_data[key]:
            invalid.append(
                f"The key has an incorrect data type, it should be a {nessesery_data[key]}, but it is {type(body[key])}\n")

    if missing:
        raise ValueError(f"Missing required values: {', '.join(missing)}")
    if invalid:
        raise ValueError(f"Invalid data types: \n {''.join(invalid)}")
    if len(body["x"]) != len(body["y"]):
        raise ValueError(
            f"Arrays have different lengths. X:{len(body['x'])} ,Y:{len(body['y'])}")
    pass
