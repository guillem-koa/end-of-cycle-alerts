def sendEOCEmail(email_receivers, serial_num, timestamp):

    from email.message import EmailMessage
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    import ssl
    import smtplib

    email_sender = 'guillem.cobos@koabiotech.com'
    sender_alias = 'lab@koabiotech.com'  # Your alias email address
    email_password = 'yqeq lxsp vdxl nkni'

    subject = f'KOA Biotech - Alerta de Final de Ciclo⏰🔔' 
    body = f""" 
    <p>Estimado/a cliente/a,</p>
    <p>Le informamos de que su máquina Aquagar con número de serie {serial_num} ha alcanzado un final de ciclo el {timestamp}. </p>
    <p> Su máquina está preparada para analizar una nueva muestra.</p>
    """

    email_signature = """
    <p>Atentamente,</p>
    <p>Equipo de an&aacute;lisis y laboratorio.<br> &copy; 2024 KOA Biotech.</p>
    <p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqEEqzU6gsIyaAflx43K90fwr6f04EJZtLrGz9fC8_pOY4b19ayUC0SFt0muHUsf-9jQ&amp;usqp=CAU    " alt="" width="150" height="46" /></p>
    """

    em = MIMEMultipart()
    em['From'] = sender_alias
    em['To'] = ', '.join(email_receivers)
    em['Subject'] = subject

    # Attach the body of the email
    em.attach(MIMEText(body, 'html'))
    # Attach the HTML content to the email
    em.attach(MIMEText(email_signature, "html"))

    """ 
    # Attach an image
    attachment_path = 'pics/Resiembra 0005.png'
    with open(attachment_path, 'rb') as attachment:
        image = MIMEImage(attachment.read(), name = "Resiembra")
    em.attach(image)
    """

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receivers, em.as_string())

def sendMidcycleEmail(email_receivers, serial_num, timestamp):

    from email.message import EmailMessage
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    import ssl
    import smtplib

    email_sender = 'guillem.cobos@koabiotech.com'
    sender_alias = 'lab@koabiotech.com'  # Your alias email address
    email_password = 'yqeq lxsp vdxl nkni'

    subject = f'KOA Biotech - Alerta 24h de ciclo🕛🔔' 
    body = f""" 
    <p>Estimado/a cliente/a,</p>
    <p>Su máquina Aquagar con número de serie {serial_num} alcanzó 24h dentro de un ciclo el {timestamp}. </p>
    <p> Quedan 24h para completar el ciclo.</p>
    """

    email_signature = """
    <p>Atentamente,</p>
    <p>Equipo de an&aacute;lisis y laboratorio.<br> &copy; 2024 KOA Biotech.</p>
    <p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqEEqzU6gsIyaAflx43K90fwr6f04EJZtLrGz9fC8_pOY4b19ayUC0SFt0muHUsf-9jQ&amp;usqp=CAU    " alt="" width="150" height="46" /></p>
    """

    em = MIMEMultipart()
    em['From'] = sender_alias
    em['To'] = ', '.join(email_receivers)
    em['Subject'] = subject

    # Attach the body of the email
    em.attach(MIMEText(body, 'html'))
    # Attach the HTML content to the email
    em.attach(MIMEText(email_signature, "html"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receivers, em.as_string())


def get_id_maquina_info(db_connection):     
    # Create a cursor to execute SQL commands
    mycursor = db_connection.cursor()

    # Now you can execute SQL queries
    mycursor.execute("SELECT * FROM maquina")

    # Fetch the results
    result = mycursor.fetchall()

    # Close the connection when done
    db_connection.close()

    dict = {}
    for row in result:
        id, serial = row[0], row[3]
        dict[id] = (serial, ['guillem.cobos@koabiotech.com'])