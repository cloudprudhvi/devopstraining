### Shell Script Basics

---

### **1: Understanding the Shell Environment**

#### **What is a Shell?**
- **Definition**: A shell is a user interface that provides access to various services of a computer's operating system, available in graphical or command-line forms.
- **Functionality**: Shells interpret commands, enabling interaction with the system through scripts or direct input.

#### **Different Types of Shells**
- **Bash (Bourne Again SHell)**: The most common default shell on Linux systems, used for the majority of scripting tasks.
- **Zsh (Z Shell)**: Known for its enhanced features over Bash, such as improved auto-completion and globbing capabilities.
- **Others (Korn Shell, C Shell, etc.)**: Useful in specific contexts; C Shell is favored in certain environments due to its C-like syntax.

---

### **2: Creating Your First Shell Script**

#### **Writing and Executing a Script**
- **Creating a Script File**
   - Use a text editor like `nano` or `vim` to create a new file and write your script. Start with the shebang line, followed by commands. For example:
     ```bash
     #!/bin/bash
     echo "Hi, Mom!"
     ```

- **Making the Script Executable**
   - Modify the script's permissions to make it executable with `chmod`:
     ```bash
     chmod +x script.sh
     ```
   - Run the script by its path:
     ```bash
     ./script.sh
     ```

#### **Shell Script Structure and Syntax**
- **Basic Syntax Elements**
  - **Comments**: Begin with `#`, useful for adding descriptions and notes, except for the shebang.
  - **Echo Command**: Displays text or variable values.

#### **Using the Read Command**
- **Purpose**: The `read` command is used in shell scripts to capture input from the user.
- **Usage**: You can prompt the user for input, which is then stored in a variable for further use within the script.
- **Example**:
  - This script asks for the user's name and then greets them:
    ```bash
    #!/bin/bash
    echo "What is your name?"
    read name
    echo "Hi, $name!"
    ```
### Understanding Variables and Command-Line Arguments in Shell Scripts

---

### **Variables in Shell Scripts**

#### **What are Variables?**
- **Definition**: Variables in shell scripting store data that can be used and manipulated within the script. They are placeholders or references that can hold different values throughout the execution of the script.
- **Declaring Variables**: Variables in shell scripts do not need to be declared with any type. A variable is created the moment you assign a value to it.
- **Syntax**:
  ```bash
  # Assigning a value to a variable
  name="Prudhvi"
  echo $name
  ```
### Variable Types

- **Local Variables**: Defined within a script and accessible only within that shell session.
- **Environmental Variables**: Defined for the current shell and inherited by any child shells or processes. Common examples include PATH, HOME, and USER.
- **Positional Parameters**: Special variables that store command-line arguments to a script. $1, $2, etc., represent each argument.

### Best Practices for Using Variables

- **Quotes in Variables**: Always use quotes around variables to handle spaces and special characters in the value.
  ```bash
  # Correct Usage
  echo "User name: $name"
  ```
### Using Command-Line Arguments with Variables

#### What are Command-Line Arguments?
- **Definition**: Command-line arguments are inputs provided to the script at the time of execution, which allow users to pass additional data to the script without hardcoding values.

#### Accessing Command-Line Arguments via Variables
- **Positional Variables**: $0 (script name), $1, $2, etc., represent the arguments in the order they are passed.
- **Counting Arguments**: $# gives the number of command-line arguments passed.
- **All Arguments**: $* or $@ is used to reference all arguments passed to the script.

#### Example Usage
- **Script Using Variables and Command-Line Arguments**:
  ```bash
  #!/bin/bash
  # This script echoes the first two command-line arguments and a variable
  user_defined="Myvalue"
  echo "First argument: $1"
  echo "Second argument: $2"
  echo "User defined variable: $user_defined"
  ```
### Handling User Input

- **Reading Input During Execution**: Besides using command-line arguments, scripts can prompt the user during execution using the `read` command, storing the input in a variable:
  ```bash
  echo "Enter your name:"
  read user_name
  echo "Hello, $user_name!"
  ```

### Conditional Statements in Shell Scripting

Conditional statements allow you to make decisions in your scripts based on conditions. They are essential for making scripts dynamic and responsive to different situations.

#### **If Statement**
The `if` statement performs a command and checks its exit status. If the exit status is `0` (true), the commands inside the `if` block are executed.

```bash
# Syntax of if statement
if [ condition ]
then
  # Commands to execute if the condition is true
fi
```
### Else Statement

The `else` statement is used to execute commands when the `if` condition is false.

#### Syntax

```bash
# Syntax of if-else statement
if [ condition ]
then
  # Commands if the condition is true
else
  # Commands if the condition is false
fi
```

### Elif Statement

The `elif` (else if) statement is used to specify a new condition to test if the first condition is false.

#### Syntax

```bash
# Syntax of if-elif-else statement
if [ condition1 ]
then
  # Commands if condition1 is true
elif [ condition2 ]
then
  # Commands if condition2 is true
else
  # Commands if both conditions are false
fi
```

#### **Script Example with Numeric Comparison**

This script prompts the user for a number and checks if it is greater than, less than, or equal to 10.

```bash
#!/bin/bash
# Prompt user for a number
echo "Please enter a number:"
read number

# Numeric comparison
if [[ $number -gt 10 ]]
then
  echo "The number $number is greater than 10."
elif [[ $number -lt 10 ]]
then
  echo "The number $number is less than 10."
else
  echo "The number is exactly 10."
fi
```
### Loops in Shell Scripting

Loops allow you to execute a set of commands repeatedly under certain conditions. This can be extremely useful for automating repetitive tasks.

#### **For Loop**

The `for` loop iterates over a list of items and performs commands for each item in the list.

```bash
# Syntax of a for loop
for item in list
do
  # Commands to execute for each item
done
```
### Example Usage of For Loop
This example shows a `for` loop that prints each item in a list.

```bash
#!/bin/bash
# List of names
names="chiranjeevi balakrishna Nagarjuna Venkatesh"

# For loop that prints each name in the list
for name in $names
do
  echo "Hello, $name!"
done
```

### Shell Script to Determine Even or Odd Status of Positional Arguments

#### Script Using Individual Positional Parameters `$1`

```bash
#!/bin/bash

# This script checks if each provided positional argument is even or odd using $1, $2, etc.

# Checking $1
if [ $(($1 % 2)) -eq 0 ]
then
    echo "$1 is even"
else
    echo "$1 is odd"
fi
```

# This script checks if each provided positional argument is even or odd using $@

```bash
#!/bin/bash
for num in "$@"
do
    if [ $(($num % 2)) -eq 0 ]
    then
        echo "$num is even"
    else
        echo "$num is odd"
    fi
done
```

### While Loop
The `while` loop continues to execute a set of commands as long as the given condition is true.

```bash
# Syntax of a while loop
while [ condition ]
do
  # Commands to execute as long as condition is true
done
```
### Example Usage of While Loop
This example demonstrates a `while` loop that asks the user for input until they enter "stop".

```bash
#!/bin/bash
# Initialize variable
echo "Enter Input only stop is allowed"
read input

# While loop that runs until the user enters "stop"
while [[ $input != "stop" ]]
do
  echo "Enter 'stop' to quit:"
  read input
  echo "You entered: $input"
done
```
