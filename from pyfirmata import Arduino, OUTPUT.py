from pyfirmata import Arduino, OUTPUT
import time

# Define the Arduino board and serial port (usually '/dev/ttyACM0' on Linux or 'COMX' on Windows)
board = Arduino('COM5')  # Replace with your actual serial port

# Set pin 13 as an OUTPUT
pin = board.get_pin('d:13:o')

# Blink the LED 5 times
for _ in range(5):
    pin.write(1)  # Turn the LED on
    time.sleep(1)  # Wait for 1 second
    pin.write(0)  # Turn the LED off
    time.sleep(1)  # Wait for 1 second

# Close the connection to the Arduino
board.exit()
