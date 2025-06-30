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

add 5 4  
Result: 9

divide 4 0  
2025-06-27 09:25:47,422 - ERROR - Error in executing 'divide': Cannot divide by zero.impleFormatter  
Error in executing.

subtract  
2025-06-27 09:26:10,246 - ERROR - Error in executing 'subtract': Two arguments are required.impleFormatter  
Error in executing.

multiply f g  
2025-06-27 09:26:31,200 - ERROR - Error in executing 'multiply': Invalid decimal input.impleFormatter  
Error in executing.

ajkdhfh  
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

## Design Patterns

### Command pattern
Command pattern is used when defining the common interface Command for all the operations like Addcommand, SubtractCommand, SaveHistoryCommand, etc. Each of the operations implement this interface. Execution is run dynamically and dependent on the user's input.

Link:  
[Command Abstract Class and CommandHandler](https://github.com/ipl2/Midterm-SU25/blob/main/app/commands/__init__.py)  
[Example of usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/plugins/add/__init__.py)  

### Factory Pattern
Factory pattern is used in the class CommandFactory where it dynamically creates command instances and injects dependencies (command_handler) when it is needed. The command logic is separate from the execution logic.  

Link:  
[Class Command Factory](https://github.com/ipl2/Midterm-SU25/blob/main/app/factory.py)  

### Facade Pattern
Facade pattern is used in the class HistoryFacade which manages history operations (loading, deleting, saving, logging). It separates the data handling used through pandas from command classes. The logic is encapsulated for command classes.

Link:  
[Class HistoryFacade](https://github.com/ipl2/Midterm-SU25/blob/main/calculator/history_facade.py)  
[Example of usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/plugins/csv/__init__.py)  

### Singleton Pattern
Singleton pattern is used in HistoryFacade ensuring there is only one history object throughout the app. History is kepy centralized here.  

Link:  
[Singleton used here](https://github.com/ipl2/Midterm-SU25/blob/main/calculator/history_facade.py#L7-L11)  

### Strategy Pattern
Strategy pattern is used in the arithmetic operations (AddCommand, DivideCommand) as it implements the Command interface but uses different operations to execute it. The CommandHandler chooses which strategy to use based on the input.  

Link:  
[Example of usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/plugins/divide/__init__.py)  

## Environment Variables
Environment variables are used to configure where thr app stores or retrieves the calculator history. The DATA_DIR holds the hisotry files. The HISTORY_FILE stores the calculator history.  

Link:  
[Example of usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/plugins/csv/__init__.py#L11-L23)  

## Logging
Logging is used to track the registration of plugin, execution of commands, errors, and system exits. It is configured with fallback support. It helps to debug parts of the program that needs attention rather than crashing it.  

Link:  
[CommandHandler execution of logs](https://github.com/ipl2/Midterm-SU25/blob/main/app/commands/__init__.py)  

## Execption Handling

### EAFP
EAFP is used when plugins are loading. The app will assume that the plugin exists and will catch the error is it does not.  

Link:  
[Loading plugins EAFP usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/__init__.py#L37-L43)  

### LBYL
LBYL is used to check if the .env file or the logging config file exists before it even tries to use it.  

Link:  
[Checking .env file and logging config LBYL usage](https://github.com/ipl2/Midterm-SU25/blob/main/app/__init__.py#L21-L27)  

## Midterm Paper

[Read the Midterm Paper](https://docs.google.com/document/d/18gssYBFLmrn6g98iAhlxDEe7EDPnb-jFc2iQT6SK0yg/edit?usp=sharing)

## Midterm Video

[Watch the Midterm Presentation](https://drive.google.com/file/d/1cmqSwB1w5FOf-qS-x_Pp59WAdT3mnIQX/view?usp=sharing)