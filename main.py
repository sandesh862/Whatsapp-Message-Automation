from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials (for production, load these from environment variables or a secure store)
account_sid = 'AC03ad989396d9388aaedc1b7ed7ac83a'
auth_token = '019ce21e3d60bfa04e232c315063a7bc'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send a WhatsApp message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f"An error occurred: {e}")

# User inputs
name = input("Enter the recipient's name: ")
recipient_number = input("Enter the recipient's WhatsApp number (with country code): ")
message_body = input(f"Enter the message you want to send to {name}: ")

# Parse date and time inputs
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

try:
    # Combine date and time into a datetime object
    scheduled_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    # Calculate delay in seconds
    time_difference = scheduled_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print("The specified time is in the past. Please enter a future date and time.")
    else:
        print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")
        # Wait until the scheduled time
        time.sleep(delay_seconds)
        # Send the message
        send_whatsapp_message(recipient_number, message_body)
except ValueError as ve:
    print("Invalid date/time format. Please enter the correct format.")
