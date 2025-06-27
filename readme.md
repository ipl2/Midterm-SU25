# Midterm

## Install

1. clone
2. pip install -r requirements.txt


## Testing 

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## Run Application

1. python main.py


## Features

1. Interactive CLI
2. add, subtract, multiply, divide
3. Error handling: division by zero, invalid input, etc.

## Usage

>>> add 5 4
Result: 9

>>> divide 4 0
2025-06-27 09:25:47,422 - ERROR - Error in executing 'divide': Cannot divide by zero.impleFormatter
Error in executing.

>>> subtract
2025-06-27 09:26:10,246 - ERROR - Error in executing 'subtract': Two arguments are required.impleFormatter
Error in executing.

>>> multiply f g
2025-06-27 09:26:31,200 - ERROR - Error in executing 'multiply': Invalid decimal input.impleFormatter
Error in executing.

>>> ajkdhfh
2025-06-27 09:27:09,120 - WARNING - Unknown command entered ajkdhkfh.impleFormatter
Unknown command.

## Menu
Commands available:
- add
- clear_history
- delete_history
- divide
- load_history
- menu
- multiply
- save_history
- subtract