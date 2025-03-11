# BIOGENIX-HOSPITAL-MANAGMENT-SYSTEM

2.1 Introduction


2.1.1 Background
The Biogenix Hospital Management System is a web-based application designed to streamline healthcare operations, enhance patient care, and improve administrative efficiency in a hospital setting. Built using Flask (a Python web framework), MySQL for database management, and enhanced with HTML/CSS/JavaScript for an interactive user interface, the system addresses the growing need for digitized healthcare solutions. The project was inspired by the increasing demand for automated symptom analysis, appointment booking, and patient management in modern hospitals. The homepage  serves as the entry point, offering features like symptom analysis and appointment booking, with a visually appealing design featuring animations and a branded logo.

2.1.2 Objectives
The primary objectives of the Biogenix Hospital Management System are:

To provide an intuitive platform for patients to analyze symptoms and receive preliminary disease predictions.
To enable seamless appointment booking and management for patients and administrators.
To facilitate admin functionalities, including doctor and patient record management, appointment verification, and bill generation.
To ensure a secure and user-friendly interface with role-based access (patient and admin).
To integrate dynamic visual elements (e.g., particle animations, confetti, and sparkles) to enhance user engagement.
2.1.3 Significance of the Project
This project holds significant value in the healthcare domain by reducing manual workload, minimizing errors in patient data management, and improving accessibility to healthcare services. The symptom analysis feature, powered by a dataset of 132 symptoms and multiple diseases (e.g., Fungal Infection, Allergy, GERD), offers a preliminary diagnostic tool, while the appointment and billing systems enhance operational efficiency. The use of modern web technologies and animations makes it appealing to a tech-savvy audience, potentially increasing patient adoption rates.

2.2 Project Overview


2.2.1 Project Scope
The scope of the Biogenix Hospital Management System includes:

A patient-facing interface for symptom analysis and appointment booking.
An admin dashboard for managing doctors, patients, appointments, and generating bills.
A database to store patient history, doctor details, and appointment records.
Interactive features such as animated backgrounds, button hover effects, and a chatbot interface.
Support for multiple pages (e.g., About, Contact, Locations, Career, Wellness Zone) to provide comprehensive hospital information.


2.2.2 Technical Requirements
Frontend: HTML, CSS (with animations), JavaScript (for particle, confetti, and sparkle effects).
Backend: Python with Flask framework, MySQL for database management.
Database: Tables for doctors, patients, history, and appointments with CRUD operations.
External Libraries: ReportLab for PDF bill generation, pandas for data handling.
Hardware: Standard web server with sufficient memory and processing power.


2.2.3 Roles and Responsibilities
Developer: Designed and implemented the Flask application, database schema, and frontend styling.
Data Analyst: Prepared symptom and disease datasets (e.g., symptom_data.csv, disease_info.csv).
UI/UX Designer: Created the animated homepage and ensured a responsive design across devices.
Tester: Validated functionality, including login, symptom analysis, and bill generation.


2.3 Methodology
2.3.1 Documentation Strategy
Documentation was maintained using inline comments in the code (e.g., Flask routes, database functions) and external files (e.g., CSS, JavaScript). The project report serves as a comprehensive overview.


2.3.2 Collaboration with Technical Teams
Collaboration involved integrating frontend animations with backend logic and ensuring database consistency through iterative testing with mock data.

2.3.3 Review and Revision Process
Code and design were reviewed weekly, with revisions made based on feedback to enhance usability and performance (e.g., optimizing animation performance on mobile devices).

2.4 Technical Contributions


2.4.1 Documentation Tools and Techniques
Tools like pandas were used to create CSV files for symptoms and diseases, while ReportLab generated PDF bills. Documentation followed a structured format as seen in this report.

2.4.2 Document Creation and Maintained
Documents were created using Python scripts and manually updated in the report. Maintenance involved version control of code files.

2.4.3 Documentation Quality Assurance
Quality was ensured through peer reviews and testing the accuracy of generated reports (e.g., bills matching appointment data).

2.5 Use Case Scenario


2.5.1 Background
A patient logs into the Biogenix Hospital Management System, selects symptoms (e.g., itching, skin rash), receives a predicted disease (e.g., Fungal Infection), and books an appointment. An admin verifies the appointment and generates a bill.

2.5.2 Use Case Description
Patient Login: The patient accesses the homepage, selects "Login" as a patient, and is redirected to the symptom analyzer.
Symptom Analysis: The patient checks symptoms from a grid, submits them, and receives a disease prediction with precautions and medications.
Appointment Booking: The patient books an appointment by filling out a form, which is stored in the database.
Admin Verification: The admin logs in, views the appointment, verifies it, and generates a PDF bill using ReportLab.
Outcome: The patient receives the bill, and the appointment is recorded in the history.

2.5.3 Conclusion
The Biogenix Hospital Management System successfully integrates patient care and administrative tasks, offering a scalable solution for hospital management. Future enhancements could include AI-driven symptom analysis and mobile app support.


# IMAGES 


HOMEPAGE:
![1](https://github.com/user-attachments/assets/ecacec8a-2d59-46eb-b1ce-a36bf4aebbfc)

PATIENT INTERFACE:
![3](https://github.com/user-attachments/assets/d5cfde13-4b72-4cf1-bad5-070a49f3aa01)

ADMIN DASHBOARD:

![8](https://github.com/user-attachments/assets/f9e4a1d3-c0a5-400a-b4b7-4397588260fd)
![9](https://github.com/user-attachments/assets/f729d204-fced-4452-a06c-4a4bc33c8912)

# Functions

Admin

Signup their account. Then Login (No approval Required).
Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
Can view/book/approve Appointment (approve those appointments which is requested by patient).


Patient
Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
Can view assigned doctor's details like ( specialization, mobile, address).
Can view their booked appointment status (pending/confirmed by admin).
Can book appointments.(approval required by admin)
Can view/download Invoice pdf (Only when that patient is discharged by admin).

HOW TO RUN THIS PROJECT

Download This Project Zip Folder and Extract it
Install Necessary libraries
Make sure sql is connected
Open Terminal and Execute Following Command:
run app.py
