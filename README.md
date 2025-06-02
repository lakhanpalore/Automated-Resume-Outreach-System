# 📧 Automated Resume Outreach System

A **Python automation tool** to send personalized emails in bulk using data from an Excel spreadsheet. It’s ideal for recruiters, job seekers, educators, or anyone who needs to contact multiple people with customized content and attachments.


## 📝 Overview

This project automates the process of:

- Reading recipient names and emails from an Excel sheet.
- Generating personalized email messages.
- Sending those emails via an SMTP server (like Gmail).
- Logging every successfully sent email to `email_log.log`.

📄 Example use case: Sending your resume and a personalized message to a list of job portals or recruiters.

---

## 📂 Project Structure
![image](https://github.com/user-attachments/assets/05472d02-bb56-4c27-9809-02456f1a8a83)

Automated-Emails/
├── Auto update name script.py # Main script for email sending
├── Portals.xlsx # Excel file with names and emails
├── email_log.log # Log file of sent emails
├── lakhanresume.pdf # Resume/attachment to be sent
├── testjjk.py # Optional testing script
├── ~$Portals.xlsx # Temporary Excel cache (can ignore)
├── README.md


YAML`
---

## 🛠 Features

- ✅ Read data from `.xlsx` using `pandas`
- ✅ Customize email body per recipient
- ✅ Attach resume or any file
- ✅ Log each email sent
- ✅ Configurable sender, subject, and SMTP settings

---

## 📸 Screenshots

### 📊 Sample Excel Input (`Portals.xlsx`)

| Name      | Email               |
|-----------|---------------------|
| John Doe  | john.doe@email.com  |
| Jane Smith| jane.smith@email.com|



---

### 💌 Terminal Output

![image](https://github.com/user-attachments/assets/e50cbf04-bff6-4ea9-8997-da77412ffe8e)

```text
2024-01-15 10:30:42 | Email sent to: john.doe@email.com
2024-01-15 10:31:01 | Email sent to: jane.smith@email.com




