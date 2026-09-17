# ✈️ Flight Analytics Dashboard

A Streamlit web app for exploring and visualizing flight data — search flights between cities and view interactive analytics on airline distribution, busiest airports, and daily flight trends. Data is stored in a MySQL database hosted on AWS RDS.

🔗 **Live Demo:** _[[add your Streamlit Cloud link here once deployed]_](https://aws-rds-flight-analytics-tyyecn8rcvga6bmhdt47db.streamlit.app/)

---

## 📌 Features

- **Check Flights** — Search flights by source and destination city, and view airline, route, departure time, duration, and price.
- **Analytics Dashboard**
  - 🥧 Pie chart — flight distribution by airline
  - 📊 Bar chart — busiest airports by traffic
  - 📈 Line chart — daily flight frequency over time
- **About** — Overview of the app and tech stack.

---

## 🛠️ Tech Stack

| Layer          | Technology                          |
|-----------------|--------------------------------------|
| Frontend / UI   | [Streamlit](https://streamlit.io/)   |
| Database        | MySQL on [AWS RDS](https://aws.amazon.com/rds/) |
| Visualization    | [Plotly](https://plotly.com/python/) |
| Data Import      | Pandas + SQLAlchemy                 |
| Language         | Python 3.14                          |

---

## 📁 Project Structure

```
flights-sql-app/
├── app.py              # Streamlit UI — search flights & analytics dashboard
├── dbhelper.py          # DB class — handles all MySQL queries
├── import_to_rds.py     # One-time script to load CSV data into AWS RDS
├── crud.py              # (Additional CRUD utilities, if applicable)
├── requirements.txt     # Python dependencies
├── .env                 # Local environment variables (NOT committed — see setup)
└── .gitignore
```


---

## ⚙️ Setup & Installation

### 1. Clone the repository
\```bash
git clone https://github.com/Bhuwanyogii/aws-rds-flight-analytics.git
cd aws-rds-flight-analytics
\```

### 2. Create a virtual environment
\```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
\```

### 3. Install dependencies
\```bash
pip install -r requirements.txt
\```

### 4. Set up your own database
This project expects a MySQL database (locally or on AWS RDS) with a `flights` table. You can create your own instance and import data using:
\```bash
python import_to_rds.py
\```
Update the CSV path and connection details in `import_to_rds.py` to match your own setup.

### 5. Configure environment variables
Create a `.env` file in the project root (this file is gitignored and must be created manually):
\```
MYSQL_PASSWORD=your_mysql_password_here
\```
Update the `host`, `user`, and `database` values in `dbhelper.py` to point to your own MySQL instance.

### 6. Run the app
\```bash
streamlit run app.py
\```
The app will be available at `http://localhost:8501`.

---

## 📊 Data Source

_[Mention where the `flights.csv` dataset came from — e.g. a specific Kaggle dataset, and link it here.]_

---

## 🔒 Security Note

Database credentials are managed via environment variables (`.env`) and are **not** committed to this repository. If deploying (e.g. via Streamlit Community Cloud), store credentials using the platform's secrets manager instead of a plaintext file.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

**Bhuwan Yogi**
B.Tech Computer Science Engineering, Batch 2027



