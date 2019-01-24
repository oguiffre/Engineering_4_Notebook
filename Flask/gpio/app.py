
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

          
@app.route("/", methods=["GET","POST"])

def index():
     msg = ['','']
     if request.method == "POST":
          msg[0] = request.form.get("redled")
          print(msg)
          print(request.form.get("redled"))
          if msg[0] == "ON":
               GPIO.output(17,GPIO.HIGH)

          else:
               GPIO.output(17,GPIO.LOW)

          msg[1] = request.form.get("blueled")
          print(msg)
          print(request.form.get("blueled"))
          if msg[1] == "ON":
               GPIO.output(27,GPIO.HIGH)
               
          else:
               GPIO.output(27,GPIO.LOW)
     else:
          msg[:] = ""
          
          
     return render_template("index.html", msg=msg)


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
