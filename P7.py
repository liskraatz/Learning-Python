# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 09:19:16 2026

"""
# Lisa Kraatz


# Miles

def distance():
    print('\n')
    mil = float(input('Enter miles: '))
    print('\n')
    km = (mil * 1.609344)
    print('Miles entered: ', mil, '\nKilometers:', km)
    return
    
# Temperature

def temp():
    print('\n')
    f = float(input('Enter Fahrenheit: '))
    print('\n')
    c = (f -32)* (5/9)
    print('Fahrenheit entered: ', f, '\nCelsius: ', c)
    return
    
# Weight

def weight():
    print('\n')
    lb = float(input('Enter Pounds: '))
    print('\n')
    kg = lb * 0.45359237
    print('Pounds entered: ', lb, '\nKilograms: ', kg)
    return
    

# Main

def main():
    distance()
    temp()
    weight()
    return
    
    
main()
    