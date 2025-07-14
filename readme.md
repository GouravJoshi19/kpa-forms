
# 🚆 Wheel Specification Form API

This project is a backend RESTful API built with **FastAPI**, designed to collect and retrieve wheel specification forms with optional filters. The data is persisted in a **PostgreSQL** database using **SQLAlchemy ORM**.

---

## 🛠 Tech Stack

- **FastAPI** – High-performance web framework
- **SQLAlchemy** – ORM for database access
- **PostgreSQL** – Relational database
- **Pydantic** – Data validation and serialization
- **Uvicorn** – ASGI server for FastAPI
- **Python 3.10+**
- **PgAdmin** – GUI for managing PostgreSQL (optional)

---

## 🚀 Features

### 📌 APIs Implemented

#### 1. Submit Wheel Specification Form

- **Method:** `POST`
- **URL:** `/api/forms/wheel-specification`
- **Description:** Submits a new wheel specification form.
- **Request Body Example:**
```json
{
  "formNumber": "WHEEL-2025-002",
  "submitted_by": "user_id_124",
  "submittedDate": "2025-07-13",
  "fields": {
    "treadDiameterNew": "840mm",
    "lastShopIssueSize": "830mm",
    "condemningDia": "780mm",
    "wheelGauge": "1676mm",
    "variationSameAxle": "2mm",
    "variationSameBogie": "3mm",
    "variationSameCoach": "4mm",
    "wheelProfile": "WAP-4",
    "intermediateWWP": "yes",
    "bearingSeatDiameter": "140mm",
    "rollerBearingOuterDia": "200mm",
    "rollerBearingBoreDia": "120mm",
    "rollerBearingWidth": "50mm",
    "axleBoxHousingBoreDia": "150mm",
    "wheelDiscWidth": "100mm"
  }
}
```

---

#### 2. Get Wheel Specification Forms

- **Method:** `GET`
- **URL:** `/api/forms/wheel-specifications`
- **Query Parameters:**
  - `form_number` (optional)
  - `submitted_by` (optional)
  - `submitted_date` (optional, format: `YYYY-MM-DD`)
- **Description:** Returns a list of forms that match the given filters. If no filters are provided, all forms are returned.

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/GouravJoshi19/kpa-forms.git
cd kpa-forms.git
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database

- Install PostgreSQL and PgAdmin.
- Create a database (e.g. `kpa_forms`).
- Note your username, password, and port.

### 5. Create a `.env` file

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/kpa_forms
```

### 6. Run the App

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

---

## 🧪 Postman Collection

- ✅ All endpoints are included with working test data.
- [Download Postman Collection](https://drive.google.com/file/d/1AjeSziTXrW_RASy3domhz-nsiJ_dHa6Z/view?usp=sharing)

---

## 📺 Video Demonstrations

| Label              | Video Link                                      |
|--------------------|-------------------------------------------------|
| `project-features` | [Watch Video](https://drive.google.com/file/d/1dbbI5IVs-RoIz9MH-OYtT4lUM5s4ZcjJ/view?usp=sharing)   |
| `project-technical`| [Watch Video](https://drive.google.com/file/d/1aOM6pCxoeX6HgenosE7S-yVkikcV4Fe9/view?usp=sharing)   |


---

## ⚠️ Assumptions & Limitations

- No authentication implemented.
- `formNumber` must be unique.
- Required fields are validated only via Pydantic.
- Only JSON inputs accepted.

---

## 🎁 Bonus Implementations

- ✅ Field validation using Pydantic
- ✅ Environment-based configuration using `.env`
- ✅ Auto-generated Swagger documentation

---


