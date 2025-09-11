# Hi or Low game

In this example, we're going to make a game that you get a random number and you have to guess if the next number is going to be higher or lower than the current number.

## Why is this important?

We're going to compare numbers in this example and this is a very common thing to do in programming. 

We're also going to use the `random` module to generate a random number. The `random` module is a part of "python the standard library", we'll be talking a lot more about this in the future here.

## What are we going to do?

We're going to make a game where you get a random number (between 1 and 100) and you have to enter a number and guess if your number is going to be higher or lower than the current number.

## Steps

### 1. create a new file called `high_or_low.py`
### 2. using the `random` module, generate a random number between 1 and 100. 
```python
import random

# Generate a random integer between a range
random_number = random.randint(1, 100)
print(F"random number {random_number}")
```
- `random` is a module that is part of the standard library in python.
  - There's a whole bunch of modules that are part of the standard library, we'll be talking about them in the future. [You can take a look here](https://docs.python.org/3/library/index.html) if you're interested.
- Now if you run this program, you'll get a random number between 1 and 100. The output should look like below.
```
$ python hi_or_low.py
random number 95
```
- Note where the `95` should be different every time.

### 3. Let's get the users' guess from the input
We've done this a few times so we should start to get comfortable with this.
```python
import random

# Generate a random integer between a range
random_number = random.randint(1, 100)
print(F"random number {random_number}")

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)

print(F"user guess {user_guess}")
```
- Now if you run this program, you'll get a random number between 1 and 100 and you'll be asked to guess a number between 1 and 100. The output should look like the output below.
```
$ python hi_or_low.py
random number 50
Guess a number between 1 and 100: 50
user guess 50
```
### 4. Let's compare the user's guess to the random number
- we're going to use an if statement with three conditions and and else statement.
  - if the user's guess is higher than the random number, we'll print "higher than the number"
  - if the user's guess is lower than the random number, we'll print "lower than the number"
  - if the user's guess is the same as the random number, we'll print "you got the number"
  - the else statement will catch any other condition that we didn't account for.
```python
import random

# Generate a random integer between a range
random_number = random.randint(1, 100)
print(F"random number {random_number}")

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)

print(F"user guess {user_guess}")

# Compare the user input to the random number
if user_guess == random_number:
    print("You guessed the number!")
elif user_guess > random_number:
    print("higher than the number!")
elif user_guess < random_number:
    print("lower than the number!")
else: 
    print("sorry I couldn't compute that.")
```
- You can see above that we're using three different types of operators.
  - `==` is the equality operator
  - `>` is the greater than operator
  - `<` is the less than operator
- Let's see what we get if guess the number exactly.
```
$ python hi_or_low.py
random number 81
Guess a number between 1 and 100: 81
user guess 81
You guessed the number!
```
- Let's see what we get if we guess a higher number
```
$ python hi_or_low.py
random number 81
Guess a number between 1 and 100: 97
user guess 97
higher than the number!
```
- Let's see what we get if we guess a lower number
```
$ python hi_or_low.py
random number 13
Guess a number between 1 and 100: 10
user guess 10
lower than the number!
```
So you can see here that we've taken into account all the possible conditions that could happen, but we haven't checked if the thinks their guess is higher or lower than the number!

### 5. Let's check if the user thinks their guess is higher or lower than the number
- Let's ask the user if they think their number is higher or lower than the number.
```python
import random

# Generate a random integer between a range
random_number = random.randint(1, 100)
print(F"random number {random_number}")

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(F"user guess {user_guess}")

# Ask the user if they think they are higher or lower than the number
high_low_input = input("Do you think you are higher or lower than the number? (h/l) ")

# other code here removed for brevity
```
### 6. Let's store whether the guess was high or low in a variable
- We're going to use a string to store whether the guess was high, low or correct and remove the print statements.
```python
# other code here removed for brevity

# Ask the user if they think they are higher or lower than the number
high_low_input = input("Do you think you are higher or lower than the number? (h/l) ")

result = ""

# Compare the user input to the random number
if user_guess == random_number:
    result = "correct"
elif user_guess > random_number:
    result = "high"
elif user_guess < random_number:
    result = "low"
else: 
    result = "error"
```
### 7. Let's check if the user was correct about their guess.
- Below our current if statements we're going to create another if statement to see if the user is correct about their guess.
```python
# other code removed for brevity

# Is user correct?
if result == "high" and high_low_input == "h":
    print("You are correct it's high!")
elif result == "low" and high_low_input == "l":
    print("You are correct it's low!")
else: 
    print('You are wrong and this is rigged...')
```
- You can see in the above that we're using the `and` operator to check if both conditions are true.
  - Go through and print out the result of the following operators so that we can see the differences between them and a good understanding of what they do.
    - `==` checks if something is equal to something else returns `True` or `False`
    - `and` checks if both conditions are true returns `True` or `False` 
    - `or` checks if either condition is true returns `True` or `False`
- Let's take a look at some output where the user is correct.
```
$ python hi_or_low.py
random number 32
Guess a number between 1 and 100: 1
user guess 1
Do you think you are higher or lower than the number? (h/l) l
You are correct it's low!
```
- Let's take a look at the output where the user is incorrect
```
$ python hi_or_low.py
random number 86
Guess a number between 1 and 100: 87
user guess 87
Do you think you are higher or lower than the number? (h/l) l
You are wrong and this is rigged...
```


### 8. Remove the print statement at the start and move it to the end so the user can't guess correctly.
We don't want our user to know the number before guessing!

## Conclusion

Here we've taken a bit of a different approach to the problem and we've used a few different operators to compare numbers. We've also used the `random` module to generate a random number.
