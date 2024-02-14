#### 1. Read DB
import mysql.connector

# Replace with your MySQL connection details
host =  '10.8.0.1'
username = 'pere'
password = 'Nemomola5'
database_name =  'KOAMachines'

# Create a connection to the MySQL server
db_connection = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database_name
)

# Create a cursor to execute SQL commands
mycursor = db_connection.cursor()

# Now you can execute SQL queries
mycursor.execute("SELECT * FROM end_of_cycle where EMAIL_SENT = 0")

# Fetch the results
result = mycursor.fetchall()

# Close the connection when done
db_connection.close()


#### 2. & 3. Send alerts and log
# For now, let's hardcode the relationship between id_maquina and email list
id_maquina_info = {681: ('AA-202312-994', ['guillem.cobos@koabiotech.com', 'sira.mogas@koabiotech.com']),
                   1181: ('AA-000000-000', ['guillem.cobos@koabiotech.com']), 
                   489: ('AA-202311-992', ['guillem.cobos@koabiotech.com']),
                   506: ('AA-202310-001', ['guillem.cobos@koabiotech.com']),
                   592: ('AA-202312-003', ['guillem.cobos@koabiotech.com']),
                   599: ('AA-202312-002', ['guillem.cobos@koabiotech.com'])
                   }

from utils import sendEmail 
import logging

# Configure logging
logging.basicConfig(filename='database_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Send end of cycle email alerts, and log it!
for row in result:
    id_maquina, timestamp = row[0], row[1]
    sendEmail(email_receivers=id_maquina_info[id_maquina][1],
              serial_num=id_maquina_info[id_maquina][0],
              timestamp=timestamp)
    
    log_message = f"Maquina {id_maquina} acabó un ciclo en {timestamp}. Mail enviado a {id_maquina_info[id_maquina][1]}"
    logging.info(log_message)



#### 4. Update *EMAIL_SENT* in the table *end_of_cycle* on MariaDB
    # Create a connection to the MySQL server
db_connection = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database_name
)

# Create a cursor to execute SQL commands
mycursor = db_connection.cursor()

# Now you can execute SQL queries
mycursor.execute("UPDATE end_of_cycle SET EMAIL_SENT = 1")

# Commit transaction
db_connection.commit()

# Close the connection when done
db_connection.close()