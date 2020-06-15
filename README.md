# Opening, reading, changing and closing files as well as error handling with python

## Error Handling: Try, Except, Else and Finally
The try block is the code that might have exceptions. (The try block essentially runs a test, exceptions are failures of this test). When an exception is caught then the following except block is executed.

The except block is the code that runs given the type of exception. There can be multiple except blocks and typically except blocks contain error messages.

The else block is ran if there are no exceptions. Essentially, the code that was intended to be ran before realising possible exceptions

The finally code block is always ran regardless if there are any exceptions raised.

### example (Also check the run file)
```python

try:

except:

else:

finally:


```
## opening files
To open a file the open method gives access to that. We use the with statement to aid error handling by encapsulating preparation and cleanup tasks.

### example (Also check the run file)
```python
#1
file = open("file_name.txt")

data = file.read()

print(data)

file.close()

# another way to do this
#2
with open("file_name.txt") as file:
    data = file.read()

print(data)

```
In #1 we have opened the file and stored it as the variable file, read the open file in data. Printed the contents of the file. Then closed it at the end.

In #2 we accomplish the same thing by using the with statement to refer to opening of the file as an object.

### using the optionals to the open method
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# The open method with all its defaults and optionals
open(file_name, "r") # r mode is use toread the file on open
open(file_name, "w") # w mode is used to write into the file on open
open(file_name, "a") # a mode is used to append to end of the file if it exists
open(file_name, "a+") # the plus symbol (can be used to with all kinds of modes) opens the file for updating ie. reading and writing.
```

## reading and changing files

list of the different ways to change files:

## closing files 
