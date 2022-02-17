# !/usr/bin/python
# coding=utf-8
from flask import request,jsonify,session,render_template,make_response
from flask_restful import Resource,reqparse
import json
import sys
sys.path.insert(0, './functions')
import functions


class Loo(Resource):
    def get(self):
        pass
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        data = str(args['data'])
        loo = functions.loomain(data)
        del [[data]]
        return make_response(jsonify(loo), 200)
