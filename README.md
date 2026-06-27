# Prodigy InfoTech Cybersecurity Internship - Task 4
# ⌨️ Simple Keylogger

A Python-based keylogger that records keyboard keystrokes and saves them to a text file. The application uses the `pynput` library to monitor keyboard events, log typed characters, and stop recording when the **ESC** key is pressed.

This project was developed as part of the **Prodigy Infotech Cyber Security Internship (Task 04)**.

## 🚀 Features

- Records keyboard keystrokes
- Saves keystrokes to a text file
- Logs letters, numbers, spaces, tabs, backspace, and enter keys
- Stops logging when the **ESC** key is pressed
- Lightweight command-line application
- Simple and easy-to-understand implementation

## 🛠️ Technologies Used

- Python 3
- pynput Library


## 📂 Project Structure

```text
PRODIGY_CS_04/
│
├── keylogger.py
├── key_log.txt
└── README.md
```

## ⚙️ How It Works

The program continuously listens for keyboard events.

- Normal characters are written directly to the log file.
- Special keys such as **Space**, **Enter**, **Tab**, and **Backspace** are recorded in a readable format.
- Pressing the **ESC** key safely stops the keylogger.

## 📦 Installation

### Clone the Repository

git clone https://github.com/anamikachauhan07/PRODIGY_CS_04.git
cd PRODIGY_CS_04

### Install Dependencies

pip install pynput

## ▶️ Usage

Run the program:
python keylogger.py

## 📝 Example Output

If the user types:

Hello123!

The log file may contain:

Hello123!

If the user presses **Tab**, **Backspace**, and **Enter**, the output may look like:

Hello[TAB][BACKSPACE]
World

## 🎯 Learning Objectives

This project demonstrates:

- Keyboard Event Monitoring
- File Handling in Python
- Event-Driven Programming
- Python Libraries (`pynput`)
- Basic Cyber Security Concepts
- Command-Line Application Development

## 👩‍💻 Author

**Anamika Chauhan**

Cyber Security Intern – Prodigy Infotech

GitHub: https://github.com/anamikachauhan07

## 📜 License

This project is created for educational purposes as part of the **Prodigy Infotech Cyber Security Internship (Task 04)**.
