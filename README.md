# 🛒 Brazilian E-Commerce Backend System (PostgreSQL + FastAPI)

## 👨‍💻 Created by: Ruthveek M R

This is an **end-to-end backend project** developed as part of my internship at **Moptra Infotech** (June–July 2025). It utilizes the [Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data) to build a complete ETL + Database + API pipeline.

The project demonstrates how real-world multilingual data can be cleaned, structured into a relational schema, and exposed securely through APIs.

---

## 🚀 Project Goals

- Clean & Normalize complex multilingual datasets
- Create a relational schema in PostgreSQL
- Perform full ETL and enforce integrity constraints
- Build modular RESTful APIs using FastAPI
- Test data insertions, updates, deletions via Swagger UI
- Prepare data for future dashboarding (e.g., Tableau)

---

## 📁 File Structure

```bash
📦 Project Root/
├── App/                           # Additional components
├── Apps/                          # Additional modules
├── Advanced/                      # Advanced features
├── moptra_database.txt            # Logs of my DB issues + fixes
├── moptra_notebook.ipynb          # Python notebook used for cleaning
├── moptra_copyable_database_script.txt # Final DB creation script
├── crud.py / crud.cpython-313.pyc
├── database.py / database.cpython-313.pyc
├── models.py / models.cpython-313.pyc
├── schemas.py / schemas.cpython-313.pyc
├── main.py / main.cpython-313.pyc
└── README.md                      # 📄 This file
```bash
---
## 📦 Dataset Used

- 🟢 **Original Source:**  
  [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)

- 🧼 **Cleaned Dataset Folder (Google Drive):**  
  [Click to Access](https://drive.google.com/drive/folders/1eSFTg8MJwj-mSJb2_WmrcsmOd76oM6_f?usp=drive_link)

---

## 🔧 Technologies Used

| Layer            | Tools/Libraries                        |
|------------------|----------------------------------------|
| ETL & Cleaning   | Python, pandas, Excel, deep_translator |
| Database         | PostgreSQL                             |
| ORM & API        | FastAPI, SQLAlchemy, Pydantic          |
| Interface        | Swagger/OpenAPI                        |
| Environment      | Uvicorn, pgAdmin, VS Code, Jupyter     |

---

## ⚙️ Steps Implemented

### 🔹 1. Data Cleaning

- Converted **Latin-1 → UTF-8** using Python  
- Fixed inconsistent city names using Excel functions like `UNIQUE()`, `FIND()`, `REPLACE()`, `TRANSLATE()`  
- Skipped full translation of Portuguese reviews due to API quota (will revisit later)

### 🔹 2. Database Modeling

- Created **8+ normalized tables** in PostgreSQL  
- Enforced **primary keys**, **foreign keys**, and **constraints** (`NOT NULL`, `UNIQUE`)  
- Logged every correction in **`moptra_database.txt`**

### 🔹 3. RESTful API with FastAPI

- `models.py` → SQLAlchemy DB Models  
- `schemas.py` → Pydantic Validation Schemas  
- `crud.py` → Reusable CRUD Logic  
- `main.py` → FastAPI Application & Swagger Integration  
- ✅ All endpoints tested via Swagger:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 How to Run

### 🔸 Prerequisites

- Python 3.11+  
- PostgreSQL (with DB name: `moptra_ecommerce`)  
- Virtual Environment (recommended)

### 🔸 1. Install dependencies

pip install -r requirements.txt

### 🔸 2. Run the FastAPI server

uvicorn main:app --reload

### 🔸 Open Swagger UI

Go to 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Key Learnings
- Tackled real-world ETL issues from multilingual datasets  
- Gained hands-on practice with constraint design and enforcement  
- Understood relational schemas and foreign key challenges  
- Wrote clean modular REST APIs across 8+ tables  
- Maintained a full debug & learning log in `moptra_database.txt`  

---

## 🧠 Reflection
> “This project taught me more about real-world backend development than any theory.  
> From encoding issues to API batching limits, it pushed me into scenarios where I had to debug, research, and solve problems end-to-end.”  
>  
> — **Ruthveek M R**

---

## 🙏 Acknowledgements
I sincerely thank **Moptra Infotech** for giving me this opportunity to work on a real-world problem with full ownership and creative freedom.

---

## 📬 Contact
- 📧 Email: [ruthmys123@gmail.com](mailto:ruthmys123@gmail.com)  
- 🔗 LinkedIn: [linkedin.com/in/ruthveek](https://linkedin.com/in/ruthveek)  
- 💻 GitHub: [github.com/RuthveekMR](https://github.com/RuthveekMR)

---

## ⭐ Like this project?
Feel free to **fork**, **star ⭐**, or **clone** the repo.  
Contributions and suggestions are always welcome!

---

## 📌 GitHub Repository Info
- **Repository Name:** `moptra-ecommerce-postgresql-api`
- **Description/About:**  
  > End-to-end multilingual e-commerce backend system using PostgreSQL and FastAPI, built during my internship at Moptra Infotech. Includes ETL, relational schema design, and full REST API tested with Swagger.

