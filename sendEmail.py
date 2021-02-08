import smtplib, ssl

# Function to start server and send email
def sendEmail(message):
    # Email server info
    smtp_server = 'smtp.gmail.com'
    port = 587  # For starttls
    # Your email
    sender_email = ''
    # Recipient email
    reciever_email = ''
    # Your email password
    password = ''
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        # Start email server
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, reciever_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 