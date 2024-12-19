from gpiozero import LED, Buzzer
from time import sleep

# Set up GPIO pins as LEDs
red_led = LED(18)  # Pin 18 for red
yellow_led = LED(23)  # Pin 23 for yellow
active_buzzer = Buzzer(24) #Pin 24 for buzzer 

def menu():
    print("--- LED Control Menu ---")
    print("1. Blink Red LED")
    print("2. Blink Yellow LED")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    return choice

def control_led_and_buzzer():
    while True:
        choice = menu()  # Show the menu and get the user's choice

        if choice == '1':
            print("Blinking Red LED...")
            # Blink Red LED X times

            for i in range(20):
                red_led.on()  # Turn on red LED
                active_buzzer.on()
                sleep(0.1)      # Wait for x second


                red_led.off()  # Turn off red LED
                active_buzzer.off()
                sleep(0.1)      # Wait for x second

        elif choice == '2':
            print("Blinking Yellow LED...")
            # Blink Yellow LED Xtimes

            for i in range(5):
                yellow_led.on()  # Turn on yellow LED
                active_buzzer.on()
                sleep(1)         # Wait for x second

                yellow_led.off()  # Turn off yellow LED
                active_buzzer.off()
                sleep(1)         # Wait for x second

        elif choice == '3':
            print("Exiting program.")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice, please try again.")

# Run the program
control_led_and_buzzer()



"""
import RPi.GPIO as gpio
import time

# Set up GPIO mode and pins
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)

# Get user input
color = input("SCRIE ROSU SAU GALBEN: ").upper()  # Convert to uppercase for case-insensitivity

# Control the GPIO based on user input
if color == "ROSU":
    gpio.output(18, gpio.HIGH)  # Set pin 18 high
    time.sleep(3)
    gpio.output(18, gpio.LOW)   # Set pin 18 low to turn off after 3 seconds

elif color == "GALBEN":
    gpio.output(23, gpio.HIGH)  # Set pin 23 high
    time.sleep(3)
    gpio.output(23, gpio.LOW)   # Set pin 23 low to turn off after 3 seconds

# Clean up GPIO settings
gpio.cleanup()
"""
