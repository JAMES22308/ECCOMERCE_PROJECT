# 🛒 E-COMMERCE PROJECT

> ⚠️ **Disclaimer:** This project is for **logic-building purposes only**. It is **not vibe-coded** or fully production-ready. You may encounter grammar mistakes, syntax issues, or other unexpected errors. Please proceed with that in mind!

---

## 📋 Description

This is a **CLI-based eCommerce system** written in Python, supporting two types of users:

- **Admin**:
  - Can perform full **CRUD** operations on products.
  - Can **update the status** of user orders (`Processing`, `Shipped`, `Cancelled`, `Failed`, `Delivered`).
  - Can **register only once** to avoid multiple admin accounts.

- **User**:
  - Can register multiple accounts.
  - Can view product listings, view cart and place orders.
  - Can cancel orders. (still working on it)
  - Has a **displayed balance** in the system (virtual money). (still working on it)
  - Receives error messages for invalid actions (e.g. wrong credentials, ordering more than available stock).

---

## 🧪 Sample Accounts

You may use these example accounts when testing the system:

- **Admin Account:**
  - Email: `admin@gmail.com`
  - Password: `admin123`

- **User Account:**
  - Email: `user@gmail.com`
  - Password: `user123`

---

## 🚀 How to Run

Make sure you have **Python installed**. If not, download it from: https://www.python.org/downloads/

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/JAMES22308/ECCOMERCE_PROJECT.git
cd ECCOMERCE_PROJECT

# Windows
python main.py

#Linux/Mac
python3 main.py
