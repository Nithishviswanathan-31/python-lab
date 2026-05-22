## Exp 09 — File handling

Programs demonstrating reading, writing, and processing text files in Python.

| File | Description |
|------|-------------|
| 09a_copy_file.py | Copies content from one text file to another |
| 09b_word_count.py | Counts total words, unique words, and word frequency in a file |
| 09c_longest_word.py | Finds and displays the longest word in a given text file |

## Concepts used
- open() with modes: 'r', 'w', 'a'
- read(), readline(), readlines(), write()
- split() for tokenising words
- Iterating over file contents
- Exception handling for FileNotFoundError

## Sample output

**09a — Copy file**
```
Source file      : input.txt
Destination file : output.txt
File copied successfully!
```

**09b — Word count**
```
Total words   : 48
Unique words  : 31
Most frequent : 'the' appears 5 times
```

**09c — Longest word**
```
File          : sample.txt
Longest word  : 'Krishnagiri' (11 characters)
```