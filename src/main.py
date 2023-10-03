
import utils

nessesery_keys = ["x", "y", "x_label", "y_label", "title"]


def main(context):
    try:
        if context.req.method == "GET":
            # @dataobject
            data: utils.Data = utils.Data()

            if context.req.path == "/":
                utils.throw_if_missing(context.req.body, nessesery_keys)
                utils.preprocess_data(context.req.body, data)

            if context.req.path == "/params":
                utils.throw_if_missing(context.req.query, nessesery_keys)
                utils.preprocess_data(context.req.query, data)

            graf: bytes = utils.generate_graf_png(data)
            return context.res.send(graf)

    except Exception as error:
        context.error(error.message)
        return context.res.json({"ok": False, "error": error.message}, 400)
