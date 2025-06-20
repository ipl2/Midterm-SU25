# pylint: disable=unused-import, disable=comparison-with-callable

'''Special file in pytest that holds configuration, hooks, and fixtures. They
are shared amongst many test files. It is reusable and customizable within tests'''
from decimal import Decimal
import pytest
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
        c = Decimal(fake.random_number(digits=2))
        d = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide:
            d = Decimal('1') if d == Decimal('0') else d

        try:
            if operation_func == divide and d == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(c, d)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield c, d, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''Adds custom CLI to pytest'''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''Parametrize tests with c, d, expected only for selected test modules'''
    allowed_modules = {
        "test_calculation",
        "test_calculations",
        "test_calculator",
        "test_main",
        "test_operations",
    }

    # Extract module name without path and extension
    module_name = metafunc.module.__name__.split('.')[-1]

    # Only parametrize if the module is allowed and fixtures exist in the test
    if module_name in allowed_modules and {"c", "d", "expected"}.issubset(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (c, d, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for c, d, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("c,d,operation,expected", modified_parameters)
