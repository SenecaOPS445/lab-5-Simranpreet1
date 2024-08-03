#!/usr/bin/env python3
# Author ID: 167976216

def add(number1, number2):
    try:
        
        if isinstance(number1, str) and number1.isdigit():
            number1 = float(number1)
        if isinstance(number2, str) and number2.isdigit():
            number2 = float(number2)
        
        return number1 + number2
    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                   
    print(add('10', 5))                   
    print(add('abc', 5))                  
    print(read_file('seneca2.txt'))     
    print(read_file('file10000.txt'))   
