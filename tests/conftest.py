import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()
#instantianing Faker

def generate_test_data(num_records):
    '''Operation mapping for Calculator and Calculation tests.
    It maps a key of a string to a value of a function'''
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        '''Iterates num_records of times to create individual
        test cases. The _ is like a placeholder'''
        c = Decimal(fake.random_number(digits=2))
        d = Decimal(fake.random_number(digits=2))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide:
            d = Decimal('1') if d == Decimal('0') else d
        
        try:
            if operation_func == divide and d == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield c, d, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"c", "d", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(c, d, op_name if 'operation_name' in meta.func.fixturenames else op_func, expected) for c, d, op_name, op_func, expected in parameters]
        metafunc.parametrize("c,d,operation,expected", modified_parameters)
