# -*- coding: utf-8 -*-
"""receive and print a int value.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zybaiL_uLzNLgidenRZ1j9mKdGrrFb6Y
"""

try:
  x = int(input('pick a integer number: '))
  print(x)
except ValueError:
  print('thats not a integer number.')

