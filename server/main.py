from argparse import ArgumentParser
from flask import Flask, render_template

from generate_index import generate_index


def main():
    app = Flask(__name__, template_folder="../content")

    @app.route("/")
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--is_ready', required=True)
    args, unknown = parser.parse_known_args()
    print(args.is_ready)
    print(unknown)
    is_ready = args.is_ready.lower() == "true"

    generate_index(is_ready)
    main().run(host='0.0.0.0', port=8080)