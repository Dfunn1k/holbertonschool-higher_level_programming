<p align="center">
<img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" height="200px" width="700px">
</p>

#
# 0x01. Python - if/else, loops, functions

## Learning Objectives

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements

### Python Scripts

* Allowed editors: `vi, vim, emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file at the root of the repo, containing a description of the repository
* A `README.md` file, at the root of the folder of this project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

### C Scripts

* Allowed editors: `vi`, `vim`, `emacs`.
* All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`.
* All your files should end with a new line.
* Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl).
* You are not allowed to use global variables.
* No more than 5 functions per file.
* You are not allowed to use the standard library. Any use of functions like `printf`, `puts`, etc… is forbidden.
* In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples.
* The prototypes of all your functions and the prototype of the function `_putchar` should be included in your header file called `main.h`.
* Don’t forget to push your header file.
* All your header files should be include guarded

#
## Tasks 

#

### 0-positive_or_negative.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the `number` stored in the variable `number` is positive or negative.
* You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import, random. randint` do. Please do not touch this code
* The output of the program should be:
  * The number, followed by
    * if the number is greater than 0: `is positive`
    * if the number is 0: `is zero`
    * if the number is less than 0: `is negative`
  * followed by a new line

### 1-last_digit.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the `number` stored in the variable `number`.
* You can find the source code [here](https://intranet.hbtn.io/rltoken/e9k9---MJXcMmIjlMdlBpw)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import, random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
* The output of the program should be:
  * The string `Last digit of`, followed by
  * The number, followed by
  * The string `is`, followed by the last digit of `number`, followed by
    * if the last digit is greater than 5: the string `and is greater than 5`
    * if the last digit is 0: the string `and is 0`
    * if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  * followed by a new line

### 2-print_alphabet.py
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
*  You can only use one `print` function
*  You can only use one loop in your code
*  You are not allowed to store characters in a variable
*  You are not allowed to import any module

### 3-print_alphabt.py
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
Print all the letters except `q` and `e`
* You can only use one print function
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

### 4-print_hexa.py
Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
* You can only use one print function
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

### 5-print_comb2.py
Write a program that prints numbers from `0` to `99`.
* Numbers must be separated by `,`, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 `print` functions
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

### 6-print_comb3.py
Write a program that prints all possible different combinations of two digits.
* Numbers must be separated by `,`, followed by a space
* The two digits must be different
* `01` and `10` are considered the same combination of the two digits `0` and `1`
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 `print` functions
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module* 

### 7-islower.py
Write a function that checks for lowercase character.
* Prototype: `def islower(c):`
* Returns `True` if `c` is lowercase
* Returns `False` otherwise
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`

### 8-uppercase.py
Write a function that prints a string in uppercase followed by a new line.
* Prototype: `def uppercase(str):`
* You can only use no more than 2 `print` functions
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`

### 9-print_last_digit.py
Write a function that prints the last digit of a number.
* Prototype: `def print_last_digit(number):`
* Returns the value of the last digit
* You are not allowed to import any module

### 10-add.py
Write a function that adds two integers and returns the result.
* Prototype: `def add(a, b):`
* Returns the value of `a + b`
* You are not allowed to import any module

### 11-pow.py
Write a function that computes a to the power of b and return the value.
* Prototype: `def pow(a, b):`
* Returns the value of `a ^ b`
* You are not allowed to import any module

### 12-fizzbuzz.py
Write a function that prints the numbers from 1 to 100 separated by a space.
* For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
* For numbers which are multiples of both three and five print `FizzBuzz`.
* Prototype: `def fizzbuzz():`
* Each element should be followed by a space
* You are not allowed to import any module

### 100-print_tebahpla.py
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
* You can only use one `print` function
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

### 101-remove_char_at.py
Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”)
* Prototype: `def remove_char_at(str, n):`
* You are not allowed to import any module

### 102-magic_calculation.py
Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:

	3         0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  	4        12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  	5     >> 16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  	6        28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  	7     >> 36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
