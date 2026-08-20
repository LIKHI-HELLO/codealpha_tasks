# Secure Coding Review

## Project Overview

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

The purpose of this project is to perform a security assessment of a Python-based login application, identify common software vulnerabilities, analyze their potential impact, and implement secure coding practices to mitigate those risks.

Secure coding is an essential part of software development that helps protect applications from cyberattacks, data breaches, and unauthorized access.

---

## Objective

The main objectives of this project are:

- Identify security vulnerabilities in application code
- Analyze the risks associated with insecure coding practices
- Demonstrate secure coding techniques
- Improve application security
- Promote cybersecurity awareness among developers

---

## Application Description

The reviewed application is a simple login system developed using Python and SQLite.

The application allows users to:

- Register an account
- Log in using a username and password
- Validate user credentials

Two versions of the application were developed:

### 1. Vulnerable Application
Contains intentionally insecure coding practices for educational purposes.

### 2. Secure Application
Implements security controls and follows secure coding principles.

---

## Technologies Used

- Python
- SQLite
- bcrypt
- GitHub

---

## Vulnerabilities Identified

### 1. Hardcoded Credentials

**Description:**
Sensitive credentials are directly stored in source code.

**Risk:**
If the source code is exposed, attackers can easily obtain login credentials.

**Severity:**
High

---

### 2. SQL Injection

**Description:**
User input is directly concatenated into SQL queries.

**Risk:**
Attackers can manipulate database queries, bypass authentication, or access sensitive data.

**Severity:**
High

---

### 3. Plain Text Password Storage

**Description:**
Passwords are stored without encryption or hashing.

**Risk:**
Compromise of the database exposes all user passwords.

**Severity:**
High

---

### 4. Missing Input Validation

**Description:**
User input is accepted without proper validation.

**Risk:**
Unexpected input may cause application errors or security issues.

**Severity:**
Medium

---

### 5. Detailed Error Messages

**Description:**
Internal system errors are displayed to users.

**Risk:**
Attackers may gather useful information about the application.

**Severity:**
Medium

---

### 6. Weak Password Policy

**Description:**
Passwords are accepted without enforcing minimum security requirements.

**Risk:**
Weak passwords increase the likelihood of unauthorized access.

**Severity:**
Medium

---

## Security Improvements Implemented

The secure version of the application includes:

### Parameterized Queries

Prevents SQL Injection attacks by separating user input from SQL statements.

### Password Hashing

Uses bcrypt to securely hash passwords before storing them in the database.

### Input Validation

Validates user inputs before processing.

### Secure Error Handling

Displays generic error messages to prevent information disclosure.

### Password Policy Enforcement

Ensures passwords meet minimum security requirements.

---

## Files Included

### vulnerable_app.py

Contains intentionally vulnerable code used to identify and analyze security weaknesses.

### secure_app.py

Contains the improved version implementing secure coding practices.

### Secure_Coding_Review_Report.pdf

Detailed report documenting vulnerabilities, risks, remediation techniques, and security recommendations.

---

## Learning Outcomes

Through this project, the following concepts were learned:

- Secure Coding Principles
- SQL Injection Prevention
- Password Security
- Authentication Security
- Input Validation
- Secure Error Handling
- Risk Assessment
- Software Security Review

---

## Future Enhancements

The application can be further improved by implementing:

- Multi-Factor Authentication (MFA)
- Account Lockout Mechanism
- Session Management
- Role-Based Access Control
- Security Logging and Monitoring
- Automated Security Testing

---

## Conclusion

The Secure Coding Review successfully identified multiple security vulnerabilities within the login application and demonstrated practical mitigation techniques. By implementing secure coding practices such as parameterized queries, password hashing, input validation, and secure error handling, the overall security of the application was significantly improved.

Secure software development is critical for protecting systems, data, and users from modern cyber threats.

---

## Internship Information

**Internship:** CodeAlpha Cyber Security Internship

**Task:** Task 3 – Secure Coding Review

**Submitted By:** Gandamalla Likitha
