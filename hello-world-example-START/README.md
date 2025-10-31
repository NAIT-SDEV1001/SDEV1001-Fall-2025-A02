# Hello World!

In this example, we'll get a little familiar with using Python in the terminal.

## Why?

It's important to understand how to get your code running so that you can run your code on any computer. This is especially important when you're working on a team and you need to share your code with others.

## Steps
### 1. Open your terminal and navigate to the folder where you'll be keeping your notes.
### 2. type `python` in the terminal and you should see something like this:
```
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**IMPORTANT NOTE**: If you don't see this you should go to the Python website and download the latest version of Python. You can find the download link [here](https://www.python.org/downloads/).

### 3. Type `print("Hello World!")` and you should see something like this:
```
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World!")
Hello World!
>>> 
```

Congratulations! You've just run your first Python program!

This was done in the "Python Interpreter" which is a program that allows you to run Python code. This is a great way to test out small snippets of code, but it's not a great way to write a program.

### 4. Exit the Python Interpreter by typing `exit()` and pressing enter.

### 5. Create a new file called `hello_world.py` and open it in your text editor, we'll be using [Visual Studio Code](https://code.visualstudio.com/) in this course.
- in your terminal, double-check that `hello_world.py`` exists by typing `ls` if you're on Mac and `dir` if you're on Windows and pressing enter. You should see something like this (on Windows):
```
C:\path\to\your\project> dir
 Volume in drive C is Windows
 Volume Serial Number is 4445-6B5C

 Directory of C:\path\to\your\project

05/26/2023  10:54 AM    <DIR>          .
05/26/2023  10:54 AM    <DIR>          ..
05/26/2023  10:54 AM                 0 hello_world.py
05/26/2023  10:53 AM             2,241 README.md
               2 File(s)          2,241 bytes
               2 Dir(s)  243,710,267,392 bytes free
```
Note: On Mac it looks pretty similar, the most important thing is that you have a file called `hello_world.py` in your project folder.

### 6. Type `print("Hello World!")` into your `hello_world.py` file and save it.
- You can also add a comment to your file by typing `#` and then your comment. Comments are ignored by the Python Interpreter and are used to explain what your code is doing.
- Your file `hello_world.py` should look something like this:
```python
# My First Python Program
print("Hello World!")
```

### 7. Run your project by typing `python hello_world.py` and pressing enter. You should see something like this:
```
C:\path\to\your\project> python hello_world.py
Hello World!
```

Congratulations! You've just run your first Python program from a file!

### 8. Let's take a look at what an error looks like because you'll be seeing a lot of them. Change your `hello_world.py` file to look like this:
- Let's make a mistake and see what happens.
```python
# My First Python Program
print("Hello World!"   # removed the closing parenthesis
```
- As you can see here I removed your closing parenthesis `)` from the `print` function. This is a common mistake that you'll make when you're first starting out.
- Let's see what happens when we try to run this program.
```
C:\path\to\your\project> python hello_world.py
```
The output you'll see looks something like this
```python
  File " C:\path\to\your\project\hello_world.py", line 2
    print("Hello World!"
         ^
SyntaxError: '(' was never closed
```
- This is the "traceback" and is telling us we have an error called a `SyntaxError` and it's telling you that you have a problem with your syntax. In this case, it's telling you that you forgot to close your parenthesis `)`. We'll learn more about this later.
- Something really important to note here is that it tells us the line to look at. This is really helpful when you're trying to figure out what's wrong with your code. So here it tells us our error is on line 2 of the file `hello_world.py`.

### 9. Let's fix our program and go on to the next example!
- Let's add the closing parenthesis `)` back to our `print` function (on line 2) in our `hello_world.py` file.
```python
# My First Python Program
print("Hello World!")
```

## Conclusion

We'll be doing this essentially every day in this course. You'll be writing code, running it, and fixing errors. This is a very important skill to learn and will help you become a better programmer.
