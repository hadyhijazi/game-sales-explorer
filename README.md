# 🎮 Game Sales Explorer

A full-stack web application developed with **Python**, **FastAPI**, **Pandas**, **HTML**, **CSS**, and **JavaScript** to explore and analyze video game sales data.

---

# 📌 Project Overview

The objective of this project is to build a REST API capable of serving and processing video game sales data stored in a CSV file. A responsive frontend communicates with the backend through HTTP requests, allowing users to search, filter, sort, and explore games interactively.

---

# 🚀 Features

- Search games by name
- Filter by platform
- Filter by genre
- Sort by:
  - Top Sales
  - Newest
  - Oldest
- Interactive game details page
- Responsive card-based interface
- About page
- Swagger API documentation

---

# 🛠 Technologies Used

### Backend

- Python
- FastAPI
- Pandas
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- Swagger UI

---

# 📂 Project Structure

```text
GameSalesExplorer/
│
├── data/
│   └── vgsales.csv
│
├── frontend/
│   ├── home.html
│   ├── index.html
│   ├── game.html
│   ├── about.html
│   └── images/
│
├── main.py
├── data_loader.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/game-sales-explorer.git
```

Navigate to the project:

```bash
cd game-sales-explorer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

---

# 🌐 API Documentation

Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive documentation for all API endpoints.

---

# 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home endpoint |
| GET | `/games` | Retrieve all games |
| GET | `/games/search` | Search games by name |
| GET | `/games/filter` | Filter and sort games |
| GET | `/games/platform/{platform}` | Filter by platform |
| GET | `/games/genre/{genre}` | Filter by genre |
| GET | `/games/year/{year}` | Filter by year |
| GET | `/games/publisher/{publisher}` | Filter by publisher |
| GET | `/stats` | Dataset statistics |

---

# 💻 Frontend

The frontend communicates with the FastAPI backend using JavaScript's `fetch()` API.

Features include:

- Search bar
- Platform filter
- Genre filter
- Sorting options
- Responsive game cards
- Dynamic game details page
- Navigation bar
- About page

---

# 🖼 Game Covers

The original dataset does not include game cover images.

To improve the user interface, cover images were manually selected and stored locally inside the `frontend/images/` directory.

---

# 🎯 Concepts Practiced

- REST API development
- HTTP requests
- JSON responses
- FastAPI routing
- Pandas data processing
- CSV handling
- Filtering and sorting
- Dynamic frontend rendering
- URL parameters
- Frontend/backend communication
- Responsive web design
- Git version control

---

# 📷 Screenshots

Add screenshots of:

- Home page
- Explorer page
- Game details page
- Swagger UI

---

# 🔮 Future Improvements

- Real-time game database
- User authentication
- Favorites system
- Shopping cart
- SQL database integration
- Admin dashboard

---

# 👨‍💻 Author

Developed as a full-stack learning project using Python, FastAPI, Pandas, HTML, CSS, and JavaScript.
