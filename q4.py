# -*- coding: utf-8 -*-
"""q4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/106E6TEkYznUNRiXrIhbesnWtdNGdAUyB
"""

def string_reverse(s):

    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    return s[::-1]


print(string_reverse("Hello World"))
print(string_reverse("Python"))