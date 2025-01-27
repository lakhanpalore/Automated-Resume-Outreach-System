import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import logging
import re

# Set up logging
logging.basicConfig(filename='email_log.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def validate_email(email):
    email = email.strip().strip('.')
    # Basic regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return email
    else:
        logging.warning(f"Invalid email format: {email}")
        return None

def extract_name_from_email(email):
    """Extract a name from the email address."""
    try:
        username = email.split('@')[0]
        # Split username by non-alphanumeric characters to infer a name
        name_parts = re.split(r'[._-]', username)
        name_parts = [part.capitalize() for part in name_parts if part.isalpha()]
        return ' '.join(name_parts) if name_parts else ''
    except Exception as e:
        logging.error(f"Error extracting name from email: {email} - {e}")
        return ''

# Load the data from Sheet1
file_path = 'D:\python\Portals.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Email configuration
sender_email = "lakhanpalore@gmail.com"  # Replace with your email
sender_password = "dtxe vcng nkrp zrcd"  # Use environment variable for the password

# Subject and body of the email
subject = "Experienced Full Stack Java Developer Seeking New Opportunities: FT/W2"
body_template = """
Dear [Recipient's Name],

I hope this email finds you well. My name is Lakhan Palore, and I am an experienced Java Full Stack Developer with over 5 years of expertise in building scalable, high-performance applications and enterprise solutions. I am currently exploring full-time or W2 opportunities where I can bring my technical skills and experience to deliver impactful solutions.
My resume is attached for your reference. Please let me know if any opportunities align with my skills.

Thank you for your time and consideration.

Best regards,
Lakhan Palore
+1 (513) 302 3655
LinkedIn: https://www.linkedin.com/in/lakhanpalore/
"""

# Resume file path
resume_path = 'D:\python\lakhanresume.pdf'

# Set up the SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

except smtplib.SMTPAuthenticationError as e:
    print("Authentication failed: Check your email or app password.")
    print("Error details:", e)





# Iterate through the emails and send the email
for index, row in data.iterrows():
    recipient_email = validate_email(row['Email'])
    if recipient_email is None:
        continue

    # Extract recipient's name or leave it blank
    recipient_name = extract_name_from_email(recipient_email)

    # Customize email body
    email_body = body_template.replace("[Recipient's Name]", recipient_name if recipient_name else "")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(email_body, 'plain'))

    # Attach the resume
    try:
        with open(resume_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name='lakhanresume.pdf')
        part['Content-Disposition'] = 'attachment; filename="Lakhan_Palore_Resume.pdf"'
        msg.attach(part)
    except FileNotFoundError as e:
        logging.error(f"Resume file not found: {e}")
        print(f"Resume file not found: {e}")
        continue

    try:
        server.sendmail(sender_email, recipient_email, msg.as_string())
        logging.info(f"Email sent to {recipient_email}")
        print(f"Email sent to {recipient_email}")
    except smtplib.SMTPRecipientsRefused as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
        print(f"Failed to send email to {recipient_email}: {e}")

# Quit the server
server.quit()
