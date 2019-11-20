from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os, json
from laterals import Laterals
from abborders import AbbOrders

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/laterals')
def route_laterals():
    l = Laterals()
    return json.dumps({'laterals': l.lats})


@app.route('/lat/orders')
def route_lat_orders():
    orders = AbbOrders()
    orders_detail = orders.get_orders()
    return json.dumps({'orders': orders_detail})

@app.route('/lat/orders/summary')
def route_lat_orders_summary():
    orders = AbbOrders()
    orders_data = orders.get_orders_summary()
    return json.dumps({'summary': orders_data})

@app.route('/lat/orders/<lateral>')
def route_lat_one_lat(lateral):
    one_lat = request.view_args['lateral']
    orders = AbbOrders()
    orders_detail = orders.get_orders(lateral=one_lat)
    return json.dumps({'orders': orders_detail})

@app.route('/lat/orders/summary/<lateral>')
def route_lat_one_lat_summary(lateral):
    one_lat = request.view_args['lateral']
    orders = AbbOrders()
    orders_data = orders.get_orders_summary(lateral=one_lat)
    return json.dumps({'summary': orders_data})


if __name__ == '__main__':
    app.run()
