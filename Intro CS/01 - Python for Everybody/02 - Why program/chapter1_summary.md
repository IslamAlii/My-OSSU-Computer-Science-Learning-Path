# Chapter: Introduction

This file provides a comprehensive summary of the key concepts covered in the introduction chapter, where we explore the fundamentals of programming. In this chapter, we lay the groundwork for understanding the world of programming, with a specific focus on Python. Below, you'll find an overview of the topics we explored.

## Date: [1/10/2023]

### Topics Covered

During this session, I explored several key topics:

1. **Why Learn Programming?**
   - Understanding the importance and relevance of programming in today's world.

2. **Computer Hardware Architecture**
   - Learning about the components and structure of computer hardware.

3. **Understanding Programming from high-level view**
   - Gaining insights into the high-level view of programming and its concepts.

4. **Reserved Words for Python Language**
   - Familiarizing myself with reserved keywords specific to the Python programming language:
    - `and`
     - `as`
     - `assert`
     - `break`
     - `class`
     - `continue`
     - `def`
     - `del`
     - `elif`
     - `else`
     - `except`
     - `False`
     - `finally`
     - `for`
     - `from`
     - `global`
     - `if`
     - `import`
     - `in`
     - `is`
     - `lambda`
     - `None`
     - `nonlocal`
     - `not`
     - `or`
     - `pass`
     - `raise`
     - `return`
     - `True`
     - `try`
     - `while`
     - `with`
     - `yield`

5. **Conversing with Python**
   - Interacting with the Python programming environment.

6. **Distinguishing between interpreters and compilers in programming:**
     - **Interpreter**: An interpreter executes a program line by line, translating and executing each line as it goes. It's like having a conversation where you understand and respond to each sentence as it's spoken.
     - **Compiler**: A compiler translates the entire program into machine code all at once, creating a standalone executable. It's like writing a letter, translating it into a different language, and then sending it, so it can be read without further translation.


7. **Writing a Program**
   - The process of creating a program, including its structure and components.

8. **What is a Program?**
   - Defining the concept of a computer program and its role in computing.

9. **Running a Words Program (Dr. Chuck)**
   - Executing a program written with Dr. Chuck's guidance.

10. **The Building Blocks of Programs**
    - Identifying the fundamental elements that make up a program, including:
      - **Input:** Get data from the “outside world”. This might be reading data from a file, or even some kind of sensor like a microphone or GPS. In our initial programs, our input will come from the user typing data on the keyboard.
      - **Output:** Display the results of the program on a screen or store them in a file or perhaps write them to a device like a speaker to play music or speak text.
      - **Sequential Execution:** Perform statements one after another in the order they are encountered in the script.
      - **Conditional Execution:** Check for certain conditions and then execute or skip a sequence of statements.
      - **Repeated Execution:** Perform some set of statements repeatedly, usually with some variation.
      - **Reuse:** Write a set of instructions once and give them a name and then reuse those instructions as needed throughout your program.

11. **Types of Errors**
    - Understanding various types of programming errors that can occur, including:
      - **Syntax Errors:** These errors occur when there are issues with the structure or syntax of your code. The Python interpreter can't understand your code due to typos or missing elements. Remember to carefully check your code for correct syntax.
      - **Semantic Errors:** Errors in the meaning of a program. These errors may not result in syntax errors or crashes but can lead to unintended behavior. Careful code review and testing are essential to catch semantic errors.
      - **Logic Errors:** Logic errors are the trickiest to spot. They occur when your code runs without errors, but it doesn't produce the desired outcome. Debugging and thorough testing are essential to identify and fix logic errors.

12. **Debugging Techniques**
    - Debugging is the process of identifying and fixing errors in a program. Effective debugging techniques include:
       - **Reading:** Examine your code, read it back to yourself, and check that it says what you meant to say.
      - **Running:** Experiment by making changes and running different versions. Often if you display the right thing at the right place in the program, the problem becomes obvious, but sometimes you have to spend some time to build scaffolding.
      - **Ruminating:** Take some time to think! What kind of error is it: syntax, semantic? What information can you get from the error messages, or from the output of the program? What kind of error could cause the problem you’re seeing? What did you change last, before the problem appeared?
      - **Retreating:** At some point, the best thing to do is back off, undoing recent changes, until you get back to a program that works and that you understand. Then you can start rebuilding.

13. **Assignment Submission**
    - Finaly as part of the session, I completed an assignment that is required. 



## Glossary

- **Bug**: An error in a program.
- **Central Processing Unit**: The heart of any computer. It is what runs the software that we write; also called “CPU” or “the processor”.
- **Compile**: To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.
- **High-Level Language**: A programming language like Python that is designed to be easy for humans to read and write.
- **Interactive Mode**: A way of using the Python interpreter by typing commands and expressions at the prompt.
- **Interpret**: To execute a program in a high-level language by translating it one line at a time.
- **Low-Level Language**: A programming language that is designed to be easy for a computer to execute; also called “machine code” or “assembly language”.
- **Machine Code**: The lowest-level language for software, which is the language that is directly executed by the central processing unit (CPU).
- **Main Memory**: Stores programs and data. Main memory loses its information when the power is turned off.
- **Parse**: To examine a program and analyze the syntactic structure.
- **Portability**: A property of a program that can run on more than one kind of computer.
- **Print Function**: An instruction that causes the Python interpreter to display a value on the screen.
- **Problem Solving**: The process of formulating a problem, finding a solution, and expressing the solution.
- **Program**: A set of instructions that specifies a computation.
- **Prompt**: When a program displays a message and pauses for the user to type some input to the program.
- **Secondary Memory**: Stores programs and data and retains its information even when the power is turned off. Generally slower than main memory. Examples of secondary memory include disk drives and flash memory in USB sticks.
- **Semantics**: The meaning of a program.
- **Semantic Error**: An error in a program that makes it do something other than what the programmer intended.
- **Source Code**: A program in a high-level language.

## Exercises and Solutions

### Exercise 1: What is the function of the secondary memory in a computer?

**Answer:** c) Store information for the long term, even beyond a power cycle

### Exercise 2: What is a program?

**Answer:** A program is a set of instructions that specifies a computation.

### Exercise 3: What is the difference between a compiler and an interpreter?

**Answer:** A compiler translates a program written in a high-level language into a low-level language all at once, while an interpreter executes a program in a high-level language by translating it one line at a time.

### Exercise 4: Which of the following contains “machine code”?

**Answer:** c) Python source file

### Exercise 5: What is wrong with the following code:

```python
>>> primt 'Hello world!'
File "<stdin>", line 1
  primt 'Hello world!'
                     ^
SyntaxError: invalid syntax
>>>
```

**Answer**: There is a syntax error in the code. The correct statement should be print('Hello world!').

### Exercise 6: Where in the computer is a variable such as “x” stored after the following Python line finishes?

```python
x = 123
```

**Answer: b) Main Memory**

### Exercise 7: What will the following program print out:

```python
x = 43
x = x - 1
print(x)
```

**Answer**: b) 42

### Exercise 8: Explain each of the following using an example of a human capability: (1) Central processing unit, (2) Main Memory, (3) Secondary Memory, (4) Input Device, and (5) Output Device. For example, “What is the human equivalent to a Central Processing Unit”?

**Answer:** (1) The Central Processing Unit (CPU) in a computer is analogous to the brain in a human. It performs calculations and processes instructions, much like how the brain processes thoughts and commands.

(2) Main Memory is like a person's short-term memory, where temporary information is stored and easily accessible for immediate use.

(3) Secondary Memory is akin to a person's long-term memory, where information is stored for the long term, even beyond power cycles, similar to how humans store knowledge and experiences.

(4) An Input Device is comparable to human sensory organs, such as eyes and ears, as it receives external information and feeds it into the computer.

(5) An Output Device is like a person's voice or hands, as it allows the computer to communicate or interact with the external world.

### Exercise 9: How do you fix a “Syntax Error”?

**Answer:** To fix a "Syntax Error," you need to review your code for any syntax mistakes and correct them. Syntax errors occur when the code does not conform to the rules and structure of the programming language. Common fixes include checking for missing or mismatched parentheses, quotes, colons, or other syntax elements.


