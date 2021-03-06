from py3270 import Emulator
import time

# use x3270 with visible window
em = Emulator(visible=True)

# changed to a differnt address
em.connect('192.168.1.100')

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
