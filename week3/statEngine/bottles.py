from bottle import route, run, template, response, request
import json

@route('/')
@route('/hello')
@route('/hello/<name>')
def index(name="Pardner"):
    return template('<div>Hello, {{person}}!</div>', person=name)

@route('/<thing>/<id:int>')
def thing(thing, id):
    return template('Are you looking for {{object}} with id {{id}}',
                    Object=thing, id=id)



@route('/data/hello')
def data_hello():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = { 'noun': 'world', 'thing': "Hello"}

    return json.dump(resp_data)




@route('/data/2.5/forecast')
def get_forecast():
    lat = request.query.lat
    lon = request.query.lon

    return template('<div>Lat: {{lat}}, lon: {{lon}}',
                    lat=lat, lon=lon)



run(host='localhost', port=8080)
