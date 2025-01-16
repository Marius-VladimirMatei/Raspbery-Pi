# Flame sensor that sends an email in flame detection

"""The flame sensor uses the IR light emitted by the flame in the range of 700 nanometers to 1100 nm
when the flame is detected the signal LED lights and the digital output pin goes to HIGH"""

# digital input device class needed to monitor the state of the flame sensor input pin for (HIGH(1)(flame detected) or LOW(0)(no flame)()
from gpiozero import DigitalInputDevice, LED
# simple mail transfer protocol
import smtplib

# multipurpose internet mail extensions (multipart needed for attachments)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import logging
from datetime import datetime


# Setup logging configuration
logging.basicConfig(filename="/home/Medeea/052583/py files/flame_detection_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

# Setup flame sensor using gpiozero on GPIO pin 17
#  VCC pin flame sensor - 5V pin; GND pin on RPI5; Digital Ouput DO pin - GPIO 17
FLAME_SENSOR_PIN = 17
flame_sensor = DigitalInputDevice(FLAME_SENSOR_PIN)

# Setup buzzer using gpiozero on GPIO pin 18 using LED class
# VCC pin 5V pin; GND pin on RPI5; Control pin of the buzzer - GPIO 18
BUZZER_PIN = 18
buzzer = LED(BUZZER_PIN) 

# Email configuration
sender_email = "learn.python.test.1234@gmail.com"
receiver_email = "052583@edu.szf.at"

# App Password for Gmail needed
password = "uzrplhppeswqvopt"

smtp_server = "smtp.gmail.com"
"""designated as standard port for mail submission by the Internet Assigned Numbers Authority
port 587 is specially for authenticated email submission => the client must log in using valid credentials
using port 587 the connection begins unencrypted. The STARTTLS command upgrades the connection so a secure one.
"""
smtp_port = 587


def send_email():
    """Function to send an email when the flame is detected"""
    subject = "Flame Detected Alert"
    body = f"Warning: A flame was detected by the sensor at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!"

    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish the server connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Encrypt the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent successfully.")
        logging.info(f"Email sent successfully to {receiver_email}.")
        
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        logging.error(f"Failed to send email: {e}")


# Monitors the flame sensor and sends email when flame is detected
print("Monitoring for flame detection...")

try:
    while True:
        # Check if the flame sensor is triggered
        if flame_sensor.is_active:  # If the sensor detects a flame (sensor output HIGH)
            print("Flame detected! Sending email and sounding the buzzer!")
            logging.info("Flame detected!")  # Log flame detection
            send_email()
            buzzer.on()  # Turn on the buzzer
            logging.info("Buzzer activated.")  # Log buzzer activation
            time.sleep(5)  # Keep the buzzer on for 5 seconds
            buzzer.off()  # Turn off the buzzer
            logging.info("Buzzer deactivated.")  # Log buzzer deactivation
            time.sleep(5)  # Wait for 5 seconds before checking again
        else:
            print("No flame detected.")
            logging.info("No flame detected.")  # Log no flame detection
        
        time.sleep(1)  # Delay before the next check

except KeyboardInterrupt:
    print("Program interrupted. Exiting")
    logging.info("Program interrupted by user.")  # Log when the program is interrupted
