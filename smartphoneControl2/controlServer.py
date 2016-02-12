import cgi 
import RPi.GPIO as gpio 
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

EN = 18
#Motor 1 GPIO Pin
DIRL = 17
PWML = 27

#Motor 2 GPIO Pin
DIRR = 23
PWMR = 24

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/rccar':
            form = cgi.FieldStorage(fp=self.rfile, 
                                    headers=self.headers,
                                    environ={'REQUEST_METHOD':'POST'})
            cmd = form['cmd'].value
            print cmd

            if cmd == "GO":
                gpio.output(EN, gpio.HIGH)
                gpio.output(DIRL, gpio.HIGH)
                gpio.output(DIRR, gpio.HIGH)
                gpio.output(PWML, gpio.HIGH)
                gpio.output(PWMR, gpio.HIGH)                
            elif cmd == "LEFT":
                gpio.output(EN, gpio.HIGH)
                gpio.output(DIRL, gpio.LOW)
                gpio.output(DIRR, gpio.HIGH)
                gpio.output(PWML, gpio.HIGH)
                gpio.output(PWMR, gpio.HIGH)                
            elif cmd == "STOP":
                gpio.output(EN, gpio.LOW)
                gpio.output(DIRL, gpio.LOW)
                gpio.output(DIRR, gpio.LOW)
                gpio.output(PWML, gpio.LOW)
                gpio.output(PWMR, gpio.LOW)
            elif cmd == "RIGHT":
                gpio.output(EN, gpio.HIGH)
                gpio.output(DIRL, gpio.HIGH)
                gpio.output(DIRR, gpio.LOW)
                gpio.output(PWML, gpio.HIGH)
                gpio.output(PWMR, gpio.HIGH)                
            elif cmd == "BACK":
                gpio.output(EN, gpio.HIGH)
                gpio.output(DIRL, gpio.LOW)
                gpio.output(DIRR, gpio.LOW)
                gpio.output(PWML, gpio.HIGH)
                gpio.output(PWMR, gpio.HIGH)                

            self.send_response(100)
            self.send_header('Content-type', 'text/html')

            return

        return self.do_GET() 

gpio.setwarnings(False)
gpio.setmode( gpio.BCM ) 

#Pin Output Setup
gpio.setup(DIRL, gpio.OUT)
gpio.setup(DIRR, gpio.OUT)
gpio.setup(PWML, gpio.OUT)
gpio.setup(PWMR, gpio.OUT)
gpio.setup(EN, gpio.OUT)
#Pin Initialization
gpio.output(DIRL, gpio.LOW)
gpio.output(DIRR, gpio.LOW)
gpio.output(PWML, gpio.LOW)
gpio.output(PWMR, gpio.LOW)
gpio.output(EN, gpio.LOW)

server = HTTPServer(('', 8002), Handler).serve_forever()
