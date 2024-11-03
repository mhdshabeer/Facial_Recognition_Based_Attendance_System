def send_attendance_email():
    import yagmail
    import os
    import datetime

    current_date = datetime.date.today().strftime("%B %d, %Y")
    attendance_dir = 'Attendance'

    # Change to the attendance directory
    os.chdir(attendance_dir)
    # Retrieve the most recent file
    sorted_files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    latest_file = sorted_files[-1]
    subject = f"Attendance Report for {current_date}"

    # Configure email settings
    yag = yagmail.SMTP("Your Email Credentials Here")
    recipient_email = 'Recipient Email Here'
    email_body = f'Attendance report sent to: {recipient_email}'

    # Send the email with the attachment
    yag.send(
        to=recipient_email,
        subject=subject,  # Email subject
        contents=email_body,  # Email body
        attachments=latest_file  # File to attach
    )
    print("Email sent successfully.")
