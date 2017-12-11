import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 17 # orange
coil_A_2_pin = 24 # yellow
coil_B_1_pin = 4  # pink
coil_B_2_pin = 23 # blue
 
# adjust if different
current_phase = 0
StepCount = 1
Seq = range(0, 8)
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]
 
# GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
# GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    global current_phase
    for i in range(steps):
        while True:
            setStep(Seq[current_phase][0], Seq[current_phase][1], Seq[current_phase][2], Seq[current_phase][3])
            current_phase += 1
            if current_phase >  7:
                current_phase = 0
            time.sleep(delay)
            break
 
def backwards(delay, steps):
    global current_phase
    for i in range(steps):
        while True:
            setStep(Seq[current_phase][0], Seq[current_phase][1], Seq[current_phase][2], Seq[current_phase][3])
            current_phase -= 1
            if current_phase < 0:
                current_phase = 7
            time.sleep(delay)
            break
 
if __name__ == '__main__':
    while True:
        delay = raw_input("Time Delay (ms)?")
        steps = raw_input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
 
