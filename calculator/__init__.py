from calculator.calculation import Calculation #using the class Calculation
from calculator.operations import add, subtract, multiply, divide #using the operations

class Calculator:

    @staticmethod
    def add(c,d):  #grabs the result() from the parameters of Calculation
        return Calculation(c,d,add).result()

    @staticmethod
    def subtract(c,d):
        return  Calculation(c,d,subtract).result()

    @staticmethod
    def multiply(c,d):
        return Calculation(c,d,multiply).result()
    
    @staticmethod
    def divide(c,d):
        return Calculation(c,d,divide).result()