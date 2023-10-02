import matplotlib.pyplot as plt
from .utils import check
from io import BytesIO


def main(context):
    if context.req.method == "GET":
        try:
            check(context)
            body = dict(context.req.body)
            plt.plot(body["x"], body["y"])
            plt.title(body["title"])
            plt.xlabel(body["x_label"])
            plt.ylabel(body["title"])

            buf = BytesIO()
            plt.savefig(buf, format="png")
            return context.res.send(buf.getvalue())

        except Exception as error:
            context.error(error)
            return context.res.json({"ok": False, "error": error.message}, 400)
