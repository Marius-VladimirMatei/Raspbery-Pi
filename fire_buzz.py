# Flame sensor that send email in flame detection

# digital input device class needed to monitor the state of the flame sensor input pin for (HIGH(1) or LOW(0))
from gpiozero import DigitalInputDevice, LED
# simpe mail transfer protocol
import smtplib

# multipurpuse internet mail extensions (multipart needed for attachments)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Setup flame sensor using gpiozero on GPIO pin 17
FLAME_SENSOR_PIN = 17
flame_sensor = DigitalInputDevice(FLAME_SENSOR_PIN)

# Setup buzzer using gpiozero on GPIO pin 18 using LED class
BUZZER_PIN = 18
buzzer = LED(BUZZER_PIN)# Use App Password for authentication

# Email configuration
sender_email = "learn.python.test.1234@gmail.com"
receiver_email = "052583@edu.szf.at"
# App Password for Gmail needed
password = "uzrplhppeswqvopt"
smtp_server = "smtp.gmail.com"
"""designated as standard port for mail submission by the Internet Assigned Numbers Authority
port 587 is specially for authenticated email submission => the client must log in using valid credentials
using port 587 the connection begins unencripted. The STARTTLS command ugrades the connetion so a secure one.
"""
smtp_port = 587

def send_email():
    subject = "Flame Detected Alert"
    body = "Warning: A flame was detected by the sensor!"

    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish the server connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # used to encrypt the connection
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

try:
    print("Monitoring for flame detection...")
    while True:
        # Check if the flame sensor is triggered
        if flame_sensor.is_active:  # If the sensor detects a flame (sensor output LOW)
            print("Flame detected! Sending email and sounding the buzzer!")
            send_email()
            buzzer.on()  # Turn on the buzzer
            time.sleep(5)  # Keep the buzzer on for 5 seconds
            buzzer.off()  # Turn off the buzzer
            time.sleep(5)  # Wait for 5 seconds before checking again
        else:
            print("No flame detected.")
        
        time.sleep(1)  # Delay before the next check

except KeyboardInterrupt:
    print("Program interrupted")
