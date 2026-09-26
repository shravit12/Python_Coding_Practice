# Python Coding Practice 🚀

Welcome to my Python practice repository! This collection contains various Python assignments, problem-solving scripts, and interactive applications built while mastering core Python concepts like user-defined functions, exception handling (`try-except`), and conditional logic.

---

## 📂 Project Structure & Assignments

### 1. Electricity Bill Calculator (`Question_One.py`)
* **Features:**
  * Takes customer name and consumed units as input with robust integer validation (`try-except` loop).
  * Slab-based electricity bill calculation:
    * First 100 units: ₹5 per unit
    * Next 100 units (101-200): ₹8 per unit
    * Above 200 units: ₹10 per unit
  * Automatically categorizes bills into **Low Bill**, **Medium Bill**, or **High Bill** and generates a clean summary report.

### 2. Employee Salary Management System (`Question_Two.py`)
* **Features:**
  * Takes employee name and basic salary with validation.
  * Calculates allowances using modular functions:
    * **HRA (House Rent Allowance):** 20% of basic salary
    * **DA (Dearness Allowance):** 15% of basic salary
  * Computes tiered tax based on basic salary (> ₹50,000 gets 10% tax, otherwise 5%).
  * Calculates final net salary and prints a detailed breakdown.

### 3. Student Report Card & Scholarship System (`Question_third.py`)
* **Features:**
  * Accepts student name and roll number (validated as integer).
  * Collects marks for 5 subjects with strict range validation (0 to 100 marks only).
  * Modular functions for calculating total marks, percentage, and grading (`A+`, `A`, `B`, `C`, `Fail`).
  * Automatically checks and displays **Scholarship Eligibility** (if percentage $\ge 85\%$).

### 4. ATM Machine Simulation (`Question_4.py`)
* Secure 4-digit PIN verification using strict digit-length checks (`isdigit()`).
* Initial balance setup and interactive menu for Check Balance, Deposit (minimum amount validation), and Withdrawal (with limit checks).

### 5. Number Analysis Tool (`Question5.py`)
* Accepts an integer input and analyzes it using separate modular functions:
  * Even/Odd & Positive/Negative/Zero check
  * Divisibility by both 5 and 11
  * Prime Number & Armstrong Number verification (with dynamic digit-length calculation).

### 6. Simple Login System & Menu (`Question_6.py`)
* Secure authentication (`admin` / `python123`) with a maximum of 3 login attempts and an **Account Locked** safety feature.
* Post-login interactive menu featuring a Simple Calculator, Even/Odd checker, and Largest of Three Numbers finder.

---

## 🛠️ Technologies Used
* **Language:** Python 3
* **Core Concepts:** User-defined functions, `while` loops, exception handling (`try-except`), conditional statements (`if-elif-else`), and list operations.

---
*Happy Coding! ✨*
