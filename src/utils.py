import matplotlib.pyplot as plt
from io import BytesIO
from dataclasses import dataclass


@dataclass
class Data:
    x: list[str or int]
    y: list[str or int]
    x_label: str
    y_label: str
    title: str


def throw_if_missing(obj: object, keys: list[str]) -> None:
    """
    Throws an error if any of the keys are missing from the object

    Parameters:
        obj (object): Object to check
        keys (list[str]): List of keys to check

    Raises:
        ValueError: If any keys are missing
    """
    if missing := [key for key in keys if key not in obj or not obj[key]]:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    pass


def preprocess_data(obj: {"x": list or str, "y": list or str, "x_label": str, "y_label": str, "title": str}, data: Data) -> None:
    """
    Preprocess data for plotting.

    Parameters:
        obj (dict): A dictionary containing 'x', 'y', 'x_label', 'y_label', and 'title' keys.
        data (Data): An object to store preprocessed data.

    Raises:
        ValueError: If 'x' and 'y' have a different number of values.

    This function preprocesses data for plotting by converting 'x' and 'y' to lists if they are not already lists,
    and ensuring that 'x' and 'y' have the same number of values. It also assigns 'x_label', 'y_label', and 'title' to 'data'.
    """
    if type(obj['x']) == str and type(obj['x']) == str:
        data.x = obj['x'].split(',')
        data.y = obj['x'].split(',')
    else:
        data.x = list(obj['x'])
        data.y = list(obj['y'])

    if len(data.x) != len(data.y):
        raise ValueError(
            "Attributes 'x' and 'y' have a different number of values. To proceed, both attributes must have the same number of values.")

    data.x_label = str(obj['x_label'])
    data.y_label = str(obj['y_label'])
    data.title = str(obj['title'])


def generate_graf_png(data: Data) -> bytes:
    """
    Generate a PNG image of a plot based on provided data.

    Parameters:
        data (Data): An object containing data for plotting.

    Returns:
        bytes: PNG image data as bytes.

    The function takes a 'Data' object containing 'x' and 'y' data points, axis labels,
    and a title. It generates a plot using Matplotlib and saves it as a PNG image.
    The PNG image data is then returned as bytes.
    """
    plt.plot(data.x, data.y)
    plt.xlabel(data.x_label)
    plt.ylabel(data.y_label)
    plt.title(data.title)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    return buf.getvalue()
