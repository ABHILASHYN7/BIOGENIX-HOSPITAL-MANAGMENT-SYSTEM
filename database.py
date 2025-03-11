import mysql.connector
from datetime import datetime

def init_db():
    try:
        # First, connect to the MySQL server (no database specified)
        conn = mysql.connector.connect(
            host="localhost",
            user="medinsight_user",
            password="your_password"  # Replace with the password you set for medinsight_user
        )
        cursor = conn.cursor()

        # Check if the medinsight database exists, create it if not
        cursor.execute("CREATE DATABASE IF NOT EXISTS medinsight")
        cursor.execute("USE medinsight")

        # Create tables
        cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                          id INT PRIMARY KEY AUTO_INCREMENT,
                          name VARCHAR(255),
                          email VARCHAR(255),
                          mobile VARCHAR(20),
                          specialization VARCHAR(255))''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                          id INT PRIMARY KEY AUTO_INCREMENT,
                          name VARCHAR(255),
                          email VARCHAR(255),
                          mobile VARCHAR(20),
                          blood_group VARCHAR(10),
                          doctor_id INT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                          id INT PRIMARY KEY AUTO_INCREMENT,
                          patient_id INT,
                          disease VARCHAR(255),
                          comment TEXT,
                          timestamp DATETIME)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                          id INT PRIMARY KEY AUTO_INCREMENT,
                          patient_name VARCHAR(255),
                          age INT,
                          gender VARCHAR(10),
                          problem TEXT,
                          doctor_id INT,
                          timestamp DATETIME,
                          verified INT DEFAULT 0)''')
        
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        raise
    finally:
        conn.close()

def add_doctor(name, email, mobile, specialization):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doctors (name, email, mobile, specialization) VALUES (%s, %s, %s, %s)",
                   (name, email, mobile, specialization))
    conn.commit()
    conn.close()

def add_patient(name, email, mobile, blood_group, doctor_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, email, mobile, blood_group, doctor_id) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, mobile, blood_group, doctor_id))
    conn.commit()
    conn.close()

def add_history(patient_id, disease, comment):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO history (patient_id, disease, comment, timestamp) VALUES (%s, %s, %s, %s)",
                   (patient_id, disease, comment, timestamp))
    conn.commit()
    conn.close()

def add_appointment(patient_name, age, gender, problem, doctor_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO appointments (patient_name, age, gender, problem, doctor_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s)",
                   (patient_name, age, gender, problem, doctor_id, timestamp))
    conn.commit()
    conn.close()

def delete_doctor(doctor_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
    conn.commit()
    conn.close()

def update_doctor(doctor_id, name, email, mobile, specialization):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE doctors SET name = %s, email = %s, mobile = %s, specialization = %s WHERE id = %s",
                   (name, email, mobile, specialization, doctor_id))
    conn.commit()
    conn.close()

def verify_appointment(appointment_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET verified = 1 WHERE id = %s", (appointment_id,))
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    cursor.execute("DELETE FROM history WHERE patient_id = %s", (patient_id,))
    conn.commit()
    conn.close()

def delete_appointment(appointment_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = %s", (appointment_id,))
    conn.commit()
    conn.close()

def get_doctors():
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def get_patients():
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients

def get_patient_history(patient_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE patient_id = %s", (patient_id,))
    history = cursor.fetchall()
    conn.close()
    return history

def get_appointments():
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments ORDER BY id DESC LIMIT 10")
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def get_appointment(appointment_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="medinsight_user",
        password="your_password",
        database="medinsight"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id = %s", (appointment_id,))
    appointment = cursor.fetchone()
    conn.close()
    return appointment

if __name__ == "__main__":
    init_db()