from calculator.calculation import Calculation #using the class Calculation
from calculator.operations import add, subtract, multiply, divide #using the operations

class Calculator:

    @staticmethod
    def add(c,d):
        calculation = Calculation(c,d,add)  #variable calculation is the result of c,d, operation
        return calculation.result()     #obtained from operations.py

    @staticmethod
    def subtract(c,d):
        calculation = Calculation(c,d,subtract)
        return calculation.result()

    @staticmethod
    def multiply(c,d):
        calculation = Calculation(c,d,multiply)
        return calculation.result()
    @staticmethod
    def divide(c,d):
        calculation = Calculation(c,d,divide)
        return calculation.result()