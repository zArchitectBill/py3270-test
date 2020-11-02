from py3270 import Emulator
import time

# use x3270 so you can see what is going on
em = Emulator(visible=True)

em.connect('192.168.1.95')

if em.is_connected() :
    em.wait_for_field()
    em.send_string('L TSO',ypos=24,xpos=1)
    em.send_enter()
    em.send_string('ibmuser',ypos=2,xpos=1)
    em.send_enter()
    em.send_string('<PASSWORD>')
    em.send_enter()
    time.sleep(5)
    em.save_screen('/home/bill/devel/py3270-test/test.out')
    em.terminate()
