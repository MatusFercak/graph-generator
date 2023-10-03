
from .utils import Data, throw_if_missing, preprocess_data, generate_graf_png

nessesery_keys = ["x", "y", "x_label", "y_label", "title"]


def main(context):
    try:
        if context.req.method == "GET":
            # @dataobject
            data: Data = Data()

            if context.req.path == "/":
                throw_if_missing(context.req.body, nessesery_keys)
                preprocess_data(context.req.body, data)

            if context.req.path == "/params":
                throw_if_missing(context.req.query, nessesery_keys)
                preprocess_data(context.req.query, data)

            graf: bytes = generate_graf_png(data)
            return context.res.send(graf)

    except ValueError as error:
        context.error(error.message)
        return context.res.json({"ok": False, "error": error.message}, 400)

    except Exception as error:
        context.error(str(error))
        return context.res.json({"ok": False, "error": str(error)}, 500)
