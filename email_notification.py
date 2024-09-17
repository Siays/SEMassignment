import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# Replace these with your Gmail credentials
GMAIL_USER = 'khokj-wm21@student.tarc.edu.my'
GMAIL_PASSWORD = '021202011465'

def send_email(recipient, subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = formataddr(('TARUMT FOCS', GMAIL_USER))
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

