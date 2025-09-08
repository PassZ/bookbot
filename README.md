# BookBot - Text Analysis Tool

A Python-based text analysis tool designed to analyze literary works and provide detailed statistics about word counts and character frequency. BookBot processes text files and generates comprehensive reports about the content, making it perfect for literary analysis, content research, or educational purposes.

## 🚀 Features

- **Word Count Analysis**: Accurate word counting for any text file
- **Character Frequency Analysis**: Detailed breakdown of letter usage (a-z)
- **Sorted Results**: Character counts sorted by frequency (highest to lowest)
- **Multiple Book Support**: Analyze any text file with a simple command
- **Clean Output Format**: Professional, readable report format
- **Error Handling**: Robust file handling with clear error messages

## 📚 Included Books

The project comes with three classic literary works for analysis:

- **Frankenstein** by Mary Shelley
- **Moby Dick** by Herman Melville  
- **Pride and Prejudice** by Jane Austen

## 🛠️ Technology Stack

- **Python 3.x**
- **Pure Python** - No external dependencies required
- **File I/O** operations for text processing
- **Dictionary-based** character counting with sorting

## 📋 Prerequisites

- **Python 3.x** (any version)
- **Text files** to analyze (or use the included books)

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bookbot
```

2. No additional dependencies required! BookBot uses only Python standard library.

## 🎯 Usage

### Basic Usage
```bash
python main.py <path_to_book>
```

### Examples

**Analyze Frankenstein:**
```bash
python main.py books/frankenstein.txt
```

**Analyze Moby Dick:**
```bash
python main.py books/mobydick.txt
```

**Analyze Pride and Prejudice:**
```bash
python main.py books/prideandprejudice.txt
```

**Analyze your own text file:**
```bash
python main.py path/to/your/book.txt
```

### Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78195 total words
--------- Character Count -------
e: 11780
t: 8969
a: 8165
o: 7751
i: 7313
n: 6954
s: 6483
h: 5909
r: 5216
l: 4279
d: 3929
u: 3373
c: 2707
m: 2536
f: 2400
p: 2224
g: 2024
b: 1777
y: 1687
v: 1482
k: 1445
w: 1408
z: 434
x: 343
j: 291
q: 208
```

## 🏗️ Architecture

### Core Components

1. **Main Application (`main.py`)**
   - Command-line interface
   - File path validation
   - Orchestrates analysis workflow
   - Formats and displays results

2. **Statistics Module (`stats.py`)**
   - `get_number_of_words()` - Counts words using split() method
   - `get_character_counts()` - Analyzes character frequency
   - Sorting and formatting logic

### Analysis Functions

**Word Counting:**
- Uses Python's `split()` method for accurate word separation
- Handles whitespace and punctuation naturally
- Returns total word count as integer

**Character Analysis:**
- Creates dictionary for all letters (a-z)
- Case-insensitive counting (converts to lowercase)
- Sorts results by frequency (descending order)
- Displays formatted character frequency report

## 📊 Analysis Capabilities

### Word Count Features
- **Accurate Counting**: Handles various text formats and punctuation
- **Whitespace Handling**: Properly processes spaces, tabs, and newlines
- **Large File Support**: Efficiently processes books of any size

### Character Frequency Features
- **Complete Alphabet Coverage**: Analyzes all 26 letters (a-z)
- **Case Insensitive**: Treats uppercase and lowercase as same character
- **Sorted Output**: Results ordered by frequency for easy analysis
- **Zero Handling**: Shows characters with zero occurrences

## 📁 Project Structure

```
bookbot/
├── main.py                 # Main application entry point
├── stats.py               # Text analysis functions
├── books/                 # Sample books for analysis
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
└── README.md              # This file
```

## 🧪 Testing

Test with the included books:

```bash
# Test all three included books
python main.py books/frankenstein.txt
python main.py books/mobydick.txt
python main.py books/prideandprejudice.txt
```

Test error handling:
```bash
# Test with non-existent file
python main.py nonexistent.txt

# Test with invalid arguments
python main.py
```

## 📈 Use Cases

- **Literary Analysis**: Study character frequency patterns in literature
- **Content Research**: Analyze writing styles and vocabulary usage
- **Educational Projects**: Learn text processing and data analysis
- **Author Studies**: Compare writing patterns across different works
- **Language Learning**: Analyze text complexity and vocabulary

## 🔍 Technical Details

### Word Counting Algorithm
```python
def get_number_of_words(text):
    return len(text.split())
```
- Simple and efficient approach
- Handles multiple whitespace characters
- Works with various text encodings

### Character Counting Algorithm
```python
def get_character_counts(text):
    char_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
    return dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
```
- Dictionary-based counting for efficiency
- Case-insensitive processing
- Sorted output for readability

## 🚀 Future Enhancements

- Support for additional languages and character sets
- Statistical analysis (average word length, sentence count)
- Comparison tools for multiple books
- Export results to CSV or JSON format
- GUI interface for easier interaction
- Support for PDF and other document formats

## 📄 License

This project is part of the Boot.dev curriculum and is intended for educational purposes.

## 🤝 Contributing

This is a completed Boot.dev project. For learning purposes, feel free to fork and experiment with the code!

---

**Note**: BookBot demonstrates fundamental text processing concepts and can serve as a foundation for more advanced natural language processing applications.