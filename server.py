from flask import Flask, request, jsonify
from flask.ext.restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import argparse

parser = reqparse.RequestParser()

saved_vids = ('ycYewhiaVBk', '0UHwkfhwjsk', 'kcpUO8K_rek')
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

context = ('cert.pem', 'key.pem')

@app.route('/query', methods=['POST'])
class Model(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('link', type=str, required=True, help="link to query.")
        args = parser.parse_args()
        try:
            return args['link'] in saved_vids
        except Exception as e:
            print (e)
            return

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

@app.errorhandler(500)
def raiseError(error):
    return error

if __name__ == '__main__':
    #----------- Parsing Arguments ---------------
    p = argparse.ArgumentParser()
    p.add_argument("--host", help="Host name (default: 0.0.0.0)")
    p.add_argument("--port", help="Port (default: 5000)")
    args = p.parse_args()
    host = args.host if args.host else "0.0.0.0"
    port = int(args.port) if args.port else 5000
    api.add_resource(Model, '/query')
    app.run(host=host, port=port, ssl_context=context)