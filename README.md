# 🎯 EleQuizSystem - Digital Electronics Quiz Application

A Python-based interactive quiz system designed to test and improve knowledge of **Digital Electronics**. This application features randomized questions, score tracking, performance analysis, and result persistence.

---

## 📋 Features

- ✨ **Interactive Quiz Interface** - User-friendly command-line quiz experience
- 🔀 **Randomized Questions** - Questions are shuffled each round for variety
- 📊 **Score Tracking** - Automatic tracking and storage of quiz results
- 📈 **Performance Analysis** - Evaluates performance based on score averages
- 💾 **CSV Export** - Results saved in Excel-compatible CSV format
- 🔁 **Multiple Attempts** - Play multiple rounds and track progress over time
- ✅ **Answer Validation** - Immediate feedback for correct/incorrect answers

---

## 📁 Project Structure

```
EleQuizSystem/
├── quizsys.py              # Main application file (4.1 KB)
├── questions.txt           # Quiz questions database (1.1 KB)
├── quiz_results.csv        # Saved quiz results (Excel-compatible)
├── quiz_results.txt        # Text format results
└── README.md               # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| **quizsys.py** | Core application containing all classes and logic |
| **questions.txt** | Question database with multiple-choice options (pipe-delimited format) |
| **quiz_results.csv** | Stores player results with timestamps |
| **quiz_results.txt** | Alternative text format for results |

---

## 🏗️ Architecture

### Core Classes

#### **Question**
```python
class Question:
    - text: str           # Question text
    - options: tuple      # 4 answer options (A, B, C, D)
    - answer: str         # Correct answer key
```

#### **Player**
```python
class Player:
    - name: str           # Player name
    - score_history: list # List of all scores
```

#### **Quiz**
```python
class Quiz:
    - questions: list     # Quiz questions
    - score: int          # Current quiz score
    - asked: set          # Tracks asked questions
    - Methods:
      - ask_question()    # Presents question & validates answer
      - start()           # Runs the complete quiz
```

### Key Functions

| Function | Description |
|----------|-------------|
| `load_questions_from_file()` | Reads questions from `questions.txt` |
| `save_results()` | Saves player score to CSV file with timestamp |
| `analyze_performance()` | Analyzes score history and provides feedback |
| `main()` | Main application loop |

---

## 🎮 Usage

### Prerequisites
- Python 3.x
- No external dependencies required (uses only built-in modules)

### Running the Application

```bash
python quizsys.py
```

### Workflow

1. **Start Quiz**
   ```
   ===== DIGITAL ELECTRONICS QUIZ SYSTEM =====
   Enter your name: [Your Name]
   ```

2. **Answer Questions**
   ```
   -----------------------------------
   Which of the following gates are designated as universal gates?
   A) OR, NOT, AND
   B) NOR, NAND
   C) XOR, NOR, NAND
   D) AND, NAND
   Your answer (A/B/C/D): B
   ✔ Correct!
   ```

3. **View Results**
   ```
   ===== QUIZ FINISHED =====
   Your Score: 8/9
   
   ===== PERFORMANCE ANALYSIS =====
   Previous Scores: [8]
   Average Score: 8.00
   Excellent understanding of Digital Electronics!
   ```

4. **Play Again**
   ```
   Do you want to play another round? (y/n): y
   ```

---

## 📝 Question Format

Questions are stored in `questions.txt` using a pipe-delimited format:

```
[Question Text]|[Option A]|[Option B]|[Option C]|[Option D]|[Correct Answer]
```

### Example
```
Which Boolean law states that A + AB = A?|A) Distributive law|B) Absorption law|C) De Morgan's law|D) Associative law|B
```

### Adding Custom Questions

Edit `questions.txt` and add lines following the format above:
- Separate each field with `|`
- Answer must be a single character: `A`, `B`, `C`, or `D`
- One question per line

---

## 📊 Results Storage

### CSV Format (`quiz_results.csv`)
Results are automatically saved with timestamps:

```csv
Player,Score,Date
John Doe,8,2026-04-27 15:30:45
Jane Smith,7,2026-04-27 15:45:20
```

### Performance Feedback

- **Average Score > 7**: "Excellent understanding of Digital Electronics!"
- **Average Score > 4**: "Good performance, needs improvement in some areas."
- **Average Score ≤ 4**: "Needs more practice!"

---

## 🔧 Technical Details

### Technologies Used
- **Language**: Python 3.x
- **Modules**: 
  - `random` - Question shuffling
  - `os` - File operations
  - `csv` - Result storage
  - `datetime` - Timestamp generation

### Key Features Implementation

**Randomization**
```python
random.shuffle(self.questions)  # Shuffles question order
```

**Duplicate Prevention**
```python
self.asked = set()  # Tracks asked questions
```

**Score Persistence**
```python
csv.writer()  # Saves results in CSV format with timestamps
```

---

## 📚 Digital Electronics Topics Covered

The current question set includes:

- ✅ Universal Logic Gates (NOR, NAND)
- ✅ Boolean Algebra & Laws
- ✅ Karnaugh Maps (K-maps)
- ✅ Flip-Flops (J-K Toggle)
- ✅ Combinational Circuits
- ✅ Decoders & Multiplexers
- ✅ Logic Families (TTL, ECL, CMOS)
- ✅ XOR/EX-NOR Gates
- ✅ Counter Circuits

---

## 🚀 Future Enhancements

- [ ] GUI interface using tkinter/PyQt
- [ ] Question difficulty levels
- [ ] Category-based quizzes
- [ ] Leaderboard system
- [ ] Detailed statistics and graphs
- [ ] Question timer/timeout feature
- [ ] Mobile app version
- [ ] Database backend (SQLite/PostgreSQL)

---

## 📋 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Shaktiman** - [GitHub Profile](https://github.com/shaktimaann)

---

## 🤝 Contributing

Contributions are welcome! To add more questions or improve the system:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

---

## 📞 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/shaktimaann/EleQuizSystem/issues).

---

**Happy Learning! 🎓**
