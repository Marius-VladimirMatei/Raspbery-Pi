from gpiozero import LED, Buzzer
from time import sleep

# Set up GPIO pins as LEDsButton
red_led = LED(18)  # Pin 18 for red
yellow_led = LED(23)  # Pin 23 for yellow
active_buzzer = Buzzer(24) #Pin 24 for buzzer 

def menu():
    print("--- LED Control Menu ---")
    print("1. ROT")
    print("2. GELB")
    print("3. EXIT")
    choice = input("Enter your choice (ROT, GELB oder EXIT): ")
    return choice

def control_led_and_buzzer():
    while True:
        choice = menu()  # Show the menu and get the user's choice
       
        if choice == 'ROT':
            print("Blinking Red LED...")
            # Blink Red LED X times

            for i in range(20):
                red_led.on()  # Turn on red LED
                active_buzzer.on()
                sleep(0.1)      # Wait for x second


                red_led.off()  # Turn off red LED
                active_buzzer.off()
                sleep(0.1)      # Wait for x second
               
        elif choice == 'GELB':
            print("Blinking Yellow LED...")
            # Blink Yellow LED Xtimes

            for i in range(5):
                yellow_led.on()  # Turn on yellow LED
                active_buzzer.on()
                sleep(1)         # Wait for x second

                yellow_led.off()  # Turn off yellow LED
                active_buzzer.off()
                sleep(1)         # Wait for x second

        elif choice == 'EXIT':
            print("Exiting program.")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice, please try again.")

control_led_and_buzzer()