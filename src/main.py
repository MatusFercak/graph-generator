import matplotlib.pyplot as plt
from io import BytesIO


def main(context):
    if context.req.method == "GET":
        context.log(type(context.req.body))
        context.log(context.req.body)
        body = dict(context.req.body)
        context.log(body)
        context.log(type(body.x))
        context.log(type(body.y))
        context.log(type(body.x_label))
        context.log(type(body.y_label))
        context.log(type(body.title))

        plt.title(body.title)
        plt.xlabel(body.x_label)
        plt.ylabel(body.y_label)
        plt.plot(body.x, body.y)

        buf = BytesIO()
        plt.savefig(buf, format="png")
        return context.res.send(buf.getvalue())

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # # The `ctx.req` object contains the request data
    # if context.req.method == "GET":
    #     # Send a response with the res object helpers
    #     # `ctx.res.send()` dispatches a string back to the client
    #     return context.res.send(buf.getvalue())

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build Fast. Scale Big. All in One Place.",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )


# if __name__ == "__main__":
#     main(None)
#     pass
