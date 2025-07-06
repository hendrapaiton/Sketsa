# Python Flet Dashboard

This project is a Desktop/Web Dashboard application built with [Flet](https://flet.dev/) and Python. It is developed for a radiology medical record dashboard.

## Features

- Modern dashboard interface
- Runs as a desktop or web application
- Easy to develop and customize

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hendrapaiton/sketsa.git
   cd sketsa
   ```

2. **Create a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Desktop Mode

```bash
python app.py
```

### Web Mode

```bash
flet run app.py --web
```

## Project Structure

```
.
├── ui
│   └── main.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

## References

- [Flet Documentation](https://flet.dev/docs/)
- [Flet Dashboard Example](https://github.com/flet-dev/examples)

---

License: [MIT](LICENSE)MIT
