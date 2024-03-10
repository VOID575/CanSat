import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

ssid = 'Livebox-F19D'
password = '18F1A0F99C5397259144510369'
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    ip = wlan.ifconfig()[0]
    print(f'Conneted on {ip} !')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection

connect()

from microdot import Microdot, Response
from mutemplate import render_template

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
async def index(request):
    return 'Hello, world!'

@app.route('/main', methods=['GET'])
async def index(req):
    return render_template('index.html')

@app.errorhandler(404)
def not_found(req: Request):
    res = None
    if req.method == 'OPTIONS':
        res = Response(res)
        res.headers["Access-Control-Allow-Origin"] = '*'
        res.headers["Access-Control-Allow-Methods"] = '*'
        res.headers["Access-Control-Allow-Headers"] = '*'
        res.headers["Access-Control-Allow-Credentials"] = 'true'
        res.headers["Access-Control-Max-Age"] = '86400'
        return res


app.run(debug=True, port = 80)