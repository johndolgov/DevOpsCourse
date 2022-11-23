import pathlib


def generate_index(is_ready: bool):
    message="We are ready" if is_ready else "We are not ready"

    template = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1> {message} </h1>
    </body>
    </html>"""

    with open(pathlib.Path("../content/index.html").resolve(), "w+") as index:
        index.write(template)