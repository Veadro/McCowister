from flask import Flask, request, jsonify, render_template
import RPi.GPIO as GPIO

# Set up Flask
app = Flask(__name__)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the motor driver
IN1 = 17
IN2 = 18
PWM_PIN = 18  # PWM pin for speed control (must be a pin that supports PWM)

# Set up the GPIO pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Set up PWM on the PWM_PIN with a frequency of 1000Hz
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)  # Start PWM with 0% duty cycle

# Initialize speed
current_speed = 50
pwm.ChangeDutyCycle(current_speed)

def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def motor_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

@app.route('/motor/forward', methods=['POST'])
def api_motor_forward():
    motor_forward()
    return jsonify(status="Motor moving forward", speed=current_speed)

@app.route('/motor/backward', methods=['POST'])
def api_motor_backward():
    motor_backward()
    return jsonify(status="Motor moving backward", speed=current_speed)

@app.route('/motor/stop', methods=['POST'])
def api_motor_stop():
    motor_stop()
    return jsonify(status="Motor stopped")

@app.route('/motor/faster', methods=['POST'])
def api_motor_faster():
    global current_speed
    if current_speed < 100:
        current_speed += 10
        pwm.ChangeDutyCycle(current_speed)
    return jsonify(status="Speed increased", speed=current_speed)

@app.route('/motor/slower', methods=['POST'])
def api_motor_slower():
    global current_speed
    if current_speed > 0:
        current_speed -= 10
        pwm.ChangeDutyCycle(current_speed)
    return jsonify(status="Speed decreased", speed=current_speed)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
