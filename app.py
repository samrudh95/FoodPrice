#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:52:12 2018

@author: samjagad
"""

import urllib
import jsom 
import os
from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    print("Request:")
    print(json.dumps(req,indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(req,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action")!= "price":
        return()
    result = req.get("result")
    parameters = result.get("parameters")
    food = parameters.get("food-name")
    cost = {'Burger':'100','Pizza':'200'}
    speech = "The price of " + food + " is " + str(cost[food])
    print("Response:")
    print (speech)
    return {
        "speech": speech
        "displayText": speech,
        "source": ""
        }