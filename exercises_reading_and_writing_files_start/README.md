# Exercises: File Reading and Writing

## Exercise 1
1. Create a file named `file_reader.py`.
2. In that file, create a function named `read_file` that takes in a filename as a parameter and returns a list of lines from the file.
   - Use a `with open(filename, 'r') as f:` block.
   - Use a loop to print each non-empty line and strip extra spaces.
   - Keep track of the number of non-empty lines.
3. Create another file named `file_summary.py`.
4. In `file_summary.py`, import the `read_file` function from `file_reader.py`.
5. In the main program, ask the user for a filename (e.g., `data.txt`) and then call the imported `read_file` function.
6. After displaying the lines, print the total count of non-empty lines at the end.
7. The output should look like the following:

```
$ python file_summary.py
Enter filename: data.txt
Line 1: Python Basics
Line 2: Reading and Writing Files
Line 3: Loops and Conditions
Total non-empty lines: 3
```

---

## Exercise 2


1. Create a new file named `file_writer.py`.
2. In that file, create a function named `write_to_file` that takes two parameters:
- filename
- lines (a list of strings)

3. The function should:
- Use a with `open(filename, 'w') as f:` block to create or overwrite the file.
- Write each line from the list to the file, adding a newline \n after each one.
- Print a message like:
Successfully wrote 3 lines to filename.txt

4. Create another function in the same file named `append_to_file` that takes the same parameters but:
- Opens the file in append mode ('a').
- Adds each new line at the end of the file.
- Print a message like:
Successfully appended 2 lines to filename.txt

5. Create another file named `file_editor.py`.

6. In `file_editor.py`:
- Import both functions (`write_to_file` and `append_to_file`) from `file_writer.py`.
- Ask the user for:
A filename (e.g., notes.txt)
Whether they want to write or append
Then ask how many lines they want to add.
Collect the input lines in a list using a loop.
Call the appropriate function based on the user’s choice.

7. Sample run
- (writing new file):
$ python file_editor.py
Enter filename: notes.txt
Do you want to write or append? write
How many lines? 3
Enter line 1: Python is fun
Enter line 2: File handling is powerful
Enter line 3: Let's learn more!
Successfully wrote 3 lines to notes.txt

- appending to same file:
$ python file_editor.py
Enter filename: notes.txt
Do you want to write or append? append
How many lines? 2
Enter line 1: Adding more notes...
Enter line 2: Keep learning!
Successfully appended 2 lines to notes.txt

**Tip:** Always use `with open()` to handle files safely and automatically close them after use.
