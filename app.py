from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from model import predict_disease, symptom_list
from database import init_db, add_doctor, add_patient, add_history, get_doctors, get_patients, get_patient_history, add_appointment, delete_doctor, update_doctor, verify_appointment, get_appointments, get_appointment, delete_patient, delete_appointment
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from datetime import datetime, timedelta
from mysql.connector import Error  # Import for database error handling

app = Flask(__name__)  # Fixed typo from _name_ to __name__
app.secret_key = "your_secret_key"  # Replace with a secure key

# Initialize database (MySQL)
init_db()

# Hardcoded admin credentials for demonstration (replace with database or secure auth in production)
ADMIN_CREDENTIALS = {
    "abhi": "abhi123"  # Updated to match your specified credentials
}

# Home/Dashboard - Loads first, redirects unauthenticated users to login
@app.route("/", methods=["GET"])
def index():
    if "role" not in session:
        return render_template("index.html")  # Show home for unauthenticated users
    if session["role"] == "patient":
        return render_template("index.html")
    elif session["role"] == "admin":
        return redirect(url_for("admin"))

# Login for both admin and patient (single endpoint)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role", "").strip()
        if role == "admin":
            admin_name = request.form.get("admin_name", "").strip()
            admin_password = request.form.get("admin_password", "").strip()
            if admin_name and admin_password and ADMIN_CREDENTIALS.get(admin_name) == admin_password:
                session["role"] = "admin"
                return redirect(url_for("admin"))
            else:
                flash("Invalid admin credentials! (Username: abhi, Password: abhi123)", "error")
        elif role == "patient":
            session["role"] = "patient"
            return redirect(url_for("index"))
        else:
            flash("Please select a role!", "error")
    return render_template("login.html")

# Symptom Analyzer (accessible only to authenticated patients)
@app.route("/symptom-analyzer", methods=["GET", "POST"])
def symptom_analyzer():
    if "role" not in session or session["role"] != "patient":
        return redirect(url_for("login"))
    
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")
        result = predict_disease(symptoms)
        return render_template("result.html", result=result)
    return render_template("symptom_analyzer.html", symptoms=symptom_list)


# Admin Interface (Dashboard) - accessible only to authenticated admins
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))
    
    if request.method == "POST":
        if "add_doctor" in request.form:
            try:
                add_doctor(
                    request.form["name"], request.form["email"], 
                    request.form["mobile"], request.form["specialization"]
                )
                flash("Doctor added successfully!", "success")
            except Error as e:
                flash(f"Error adding doctor: {str(e)}", "error")
        elif "add_patient" in request.form:
            try:
                add_patient(
                    request.form["name"], request.form["email"], 
                    request.form["mobile"], request.form["blood_group"], 
                    request.form["doctor_id"]
                )
                flash("Patient added successfully!", "success")
            except Error as e:
                flash(f"Error adding patient: {str(e)}", "error")
        elif "delete_doctor" in request.form:
            doctor_id = int(request.form.get("doctor_id", 0))
            if doctor_id:
                try:
                    delete_doctor(doctor_id)
                    flash("Doctor deleted successfully!", "success")
                except Error as e:
                    flash(f"Error deleting doctor: {str(e)}", "error")
        elif "update_doctor" in request.form:
            doctor_id = int(request.form.get("doctor_id", 0))
            if doctor_id:
                name = request.form.get("name", "").strip()
                email = request.form.get("email", "").strip()
                mobile = request.form.get("mobile", "").strip()
                specialization = request.form.get("specialization", "").strip()
                if name and email and mobile and specialization:
                    try:
                        update_doctor(doctor_id, name, email, mobile, specialization)
                        flash("Doctor updated successfully!", "success")
                    except Error as e:
                        flash(f"Error updating doctor: {str(e)}", "error")
        elif "delete_patient" in request.form:
            patient_id = int(request.form.get("patient_id", 0))
            if patient_id:
                try:
                    delete_patient(patient_id)
                    flash("Patient deleted successfully!", "success")
                except Error as e:
                    flash(f"Error deleting patient: {str(e)}", "error")
        elif "delete_appointment" in request.form:
            appointment_id = int(request.form.get("appointment_id", 0))
            if appointment_id:
                try:
                    delete_appointment(appointment_id)
                    flash("Appointment deleted successfully!", "success")
                except Error as e:
                    flash(f"Error deleting appointment: {str(e)}", "error")
        elif "verify_appointment" in request.form:
            appointment_id = int(request.form.get("appointment_id", 0))
            if appointment_id:
                try:
                    verify_appointment(appointment_id)
                    flash("Appointment verified successfully! Generating bill...", "success")
                    appointment = get_appointment(appointment_id)
                    if appointment:
                        try:
                            pdf_buffer = create_bill_pdf(appointment)
                            return send_file(
                                pdf_buffer,
                                as_attachment=True,
                                download_name=f"bill_{appointment_id}.pdf",
                                mimetype="application/pdf"
                            )
                        except Exception as e:
                            flash(f"Bill generation failed: {str(e)}", "error")
                            return redirect(url_for("admin"))
                    else:
                        flash("Appointment not found. Bill generation failed.", "error")
                except Error as e:
                    flash(f"Error verifying appointment: {str(e)}", "error")
    
    try:
        doctors = get_doctors()
        patients = get_patients()
        appointments = get_appointments()
    except Error as e:
        flash(f"Error fetching data: {str(e)}", "error")
        doctors, patients, appointments = [], [], []
    
    return render_template("admin.html", doctors=doctors, patients=patients, appointments=appointments)

@app.route("/history/<int:patient_id>")
def history(patient_id):
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))
    
    try:
        history = get_patient_history(patient_id)
    except Error as e:
        flash(f"Error fetching history: {str(e)}", "error")
        history = []
    
    return render_template("history.html", history=history, patient_id=patient_id)

# Logout route
@app.route("/logout")
def logout():
    session.pop("role", None)
    return redirect(url_for("login"))

# Appointment Booking (accessible only to authenticated patients)
@app.route("/book-appointment", methods=["GET", "POST"])
def book_appointment():
    if "role" not in session or session["role"] != "patient":
        return redirect(url_for("login"))
    
    try:
        doctors = get_doctors()
    except Error as e:
        flash(f"Error fetching doctors: {str(e)}", "error")
        doctors = []
    
    if request.method == "POST":
        name = request.form["name"].strip()
        age = request.form["age"].strip()
        gender = request.form["gender"].strip()
        problem = request.form["problem"].strip()
        doctor_id = int(request.form["doctor_id"])
        
        if name and age and gender and problem and doctor_id:
            try:
                add_appointment(name, age, gender, problem, doctor_id)
                flash("Appointment booked successfully!", "success")
                return render_template("appointment.html", doctors=doctors, show_success=True)
            except Error as e:
                flash(f"Error booking appointment: {str(e)}", "error")
        else:
            flash("Please fill all required fields!", "error")
    
    return render_template("appointment.html", doctors=doctors, show_success=False)

# Bill Generation Route
@app.route("/generate-bill/<int:appointment_id>")
def generate_bill(appointment_id):
    try:
        appointment = get_appointment(appointment_id)
        if not appointment:
            flash("Appointment not found!", "error")
            return redirect(url_for("admin"))
    except Error as e:
        flash(f"Error fetching appointment: {str(e)}", "error")
        return redirect(url_for("admin"))
    
    try:
        pdf_buffer = create_bill_pdf(appointment)
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"bill_{appointment_id}.pdf",
            mimetype="application/pdf"
        )
    except Exception as e:
        flash(f"Bill generation failed: {str(e)}", "error")
        return redirect(url_for("admin"))

def create_bill_pdf(appointment):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Header
    elements.append(Paragraph("Wingersofttouch - Biogenix Hospital", styles['Title']))
    elements.append(Paragraph("Healthcare Invoice", styles['Heading1']))
    
    # Billing Info
    data = [
        ["Billing To:", f"{appointment[2]} (Patient)"],
        ["Address:", "123 Health St, Anywhere, AnyCity, 12345"],
        ["Invoice No:", str(appointment[0])],
        ["Invoice Date:", appointment[7].strftime("%d %b %Y")],
        ["Due Date:", (datetime.now() + timedelta(days=30)).strftime("%d %b %Y")],
    ]
    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(table)
    
    # Items
    items = [
        ["Item Name", "Price", "Qty", "Total"],
        ["Medical Checkup", "$50.00", 1, "$50.00"],
        ["Consultation Fee", "$30.00", 1, "$30.00"],
        ["Medicine 1", "$10.00", 1, "$10.00"],
    ]
    items_table = Table(items, colWidths=[150, 100, 50, 100])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(items_table)
    
    # Totals
    sub_total = 90.00  # Sum of item totals
    tax = sub_total * 0.05  # 5% tax for demonstration
    total = sub_total + tax
    totals = [
        ["Sub Total", f"${sub_total:.2f}"],
        ["Tax (5%)", f"${tax:.2f}"],
        ["Total", f"${total:.2f}"],
    ]
    totals_table = Table(totals, colWidths=[250, 150])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(totals_table)
    
    # Signature
    elements.append(Paragraph("Signature: ____________________", styles['Normal']))
    
    # Footer
    elements.append(Paragraph("Wingersofttouch - Biogenix Hospital | +1-123-456-7890 | info@wingersofttouch.com", styles['Italic']))
    
    doc.build(elements)
    buffer.seek(0)
    return buffer

# New routes for additional pages
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/locations")
def locations():
    return render_template("locations.html")

@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/wellness_zone")
def wellness_zone():
    return render_template("wellness_zone.html")

if __name__ == "__main__":  # Fixed typo from _name_ and _main_ to __name__ and __main__
    app.run(debug=True)