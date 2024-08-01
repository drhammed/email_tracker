import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import uuid

# Load environment variables
load_dotenv()

def send_email(to_address):
    from_address = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    
    # Generate a unique email ID
    email_id = str(uuid.uuid4())

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Test Email with Tracking'
    msg['From'] = from_address
    msg['To'] = to_address

    #server
    server_address = '127.0.0.1:5000'  # we can use the actual IP/hostname if not running locally
    tracking_url = f'http://{server_address}/track/{email_id}.png'

    # HTML with the tracking image
    html = f'''
    <html>
    <body>
        <p>This is a test email with a tracking image.</p>
        <img src="{tracking_url}" alt="" width="1" height="1">
    </body>
    </html>
    '''
    part = MIMEText(html, 'html')
    msg.attach(part)

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

    print(f"Email sent to {to_address} with tracking ID {email_id}")

# Send a test email
send_email('hammedakande0@gmail.com')
