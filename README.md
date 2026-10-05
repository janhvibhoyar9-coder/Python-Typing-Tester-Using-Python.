# ⌨️ Typing Tester Using Python

## 📌 Project Description

Typing Tester is a simple Python-based project developed to test and improve a user's typing skills. The program provides a random sentence and measures the user's typing speed, accuracy, time taken, and number of errors.

The project is divided into four Python modules to make the code simple, organized, and easy to understand.

---

## 🎯 Objectives

* To calculate typing speed in Words Per Minute (WPM).
* To calculate typing accuracy.
* To measure the time taken to type a sentence.
* To count typing errors.
* To provide basic performance feedback.
* To understand Python modules and functions.

---

## ✨ Features

* 🎲 Random sentence selection
* ⏱️ Typing time calculation
* ⌨️ WPM calculation
* 🎯 Accuracy calculation
* ❌ Error counting
* 🏆 Performance evaluation
* 📦 Modular Python structure

---

## 🗂️ Project Structure

```text
typing-tester-python/
│
├── main.py
├── sentences.py
├── typing_test.py
├── result.py
└── README.md
```

### Module Description

| File             | Description                                    |
| ---------------- | ---------------------------------------------- |
| `main.py`        | Main program that connects all modules         |
| `sentences.py`   | Stores sentences and selects a random sentence |
| `typing_test.py` | Calculates time, WPM, accuracy, and errors     |
| `result.py`      | Displays the final result                      |
| `README.md`      | Project documentation                          |

---

## 🛠️ Technologies Used

* **Python**
* `time` module
* `random` module

No external libraries are required.

---

## 📊 How WPM is Calculated

WPM stands for **Words Per Minute**.

The formula used is:

```text
WPM = (Number of Words / Time Taken in Seconds) × 60
```

For example, if a user types 20 words in 30 seconds:

```text
WPM = (20 / 30) × 60
    = 40 WPM
```

---

## ⚙️ How the Project Works

```text
Start
  ↓
Select Random Sentence
  ↓
Display Sentence
  ↓
Start Timer
  ↓
User Types Sentence
  ↓
Stop Timer
  ↓
Calculate WPM
  ↓
Calculate Accuracy
  ↓
Count Errors
  ↓
Display Result
  ↓
End
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd typing-tester-python
```

### 3. Run the program

```bash
python main.py
```

If `python` does not work, try:

```bash
py main.py
```

---

## 💻 Sample Output

```text
================================
        TYPING TESTER
================================

Type the following sentence:
Practice makes a person perfect.

Press Enter to start...

Start typing: Practice makes a person perfect.

================================
          TEST RESULT
================================
Time Taken : 6.25 seconds
WPM        : 57.60
Accuracy   : 100.0 %
Errors     : 0
Performance: Excellent!
================================
```

---

## 📚 Python Concepts Used

* Python functions
* Modules and imports
* Lists
* Strings
* `if-elif-else`
* Loops
* `random.choice()`
* `time.time()`
* Basic mathematical calculations
* User input and output

---

## 🔮 Future Improvements

The project can be improved by adding:

* Different difficulty levels
* 30-second and 60-second typing tests
* Multiple rounds
* High-score storage
* Typing history
* More sentences
* Graphical User Interface (GUI)
* User login and profiles
* Leaderboard

---

## 👨‍💻 Project Type

**Academic / College Mini Project**

**Project Title:** Typing Tester Using Python

---

## 📝 Conclusion

The Typing Tester project provides a simple way to measure typing speed and accuracy using Python. It helped in understanding important Python concepts such as modules, functions, lists, loops, conditional statements, and time calculation. Dividing the project into four modules makes the program easier to understand, maintain, and modify.
