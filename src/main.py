
from .utils import Data, throw_if_missing, preprocess_data, generate_graf_png

nessesery_keys = ["x", "y", "x_type", "y_type", "x_label", "y_label", "title"]


def main(context):
    try:
        if context.req.method == "GET" and context.req.path == "/graph.png":
            # @dataobject with Deafult values
            data: Data = Data(
                x=[1, 2, 3, 4, 5],
                y=['1', '2', '3', '4', '5'],
                x_type="int",
                y_type="int",
                x_label="x-label",
                y_label="y-label",
                title="Deafult title")

            if context.req.body:
                throw_if_missing(context.req.body, nessesery_keys)
                preprocess_data(context.req.body, data)

            else:
                throw_if_missing(context.req.query, nessesery_keys)
                preprocess_data(context.req.query, data)

            graf: bytes = generate_graf_png(data)
            return context.res.send(graf, 200, {
                "content-type": "image/png"
            })

        else:
            return context.res.json({"ok": False, "message": "Try GET method and follow instruction -> https://github.com/MatusFercak/graf-generator"}, 405)
    except Exception as error:
        context.error(str(error))
        return context.res.json({"ok": False, "error": str(error)}, 400)
