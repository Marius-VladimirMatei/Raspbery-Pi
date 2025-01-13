from gpiozero import DigitalInputDevice, LED
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Setup flame sensor using gpiozero
FLAME_SENSOR_PIN = 17  # Change to the GPIO pin you're using for the flame sensor
flame_sensor = DigitalInputDevice(FLAME_SENSOR_PIN)

# Setup buzzer using gpiozero (connected to GPIO 18)
BUZZER_PIN = 18  # Change to the GPIO pin you're using for the buzzer
buzzer = LED(BUZZER_PIN)  # Use LED class to control the buzzer

# Email configuration
sender_email = "learn.python.test.1234@gmail.com"
receiver_email = "052583@edu.szf.at"
password = "uzrplhppeswqvopt"  # Use the App Password for Gmail
smtp_server = "smtp.gmail.com"
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
        server.starttls()  # Encrypt the connection
        server.login(sender_email, password)  # Use App Password for authentication
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
            print("Flame detected! Sending email and sounding the buzzer...")
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
