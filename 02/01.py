"""
1. Выяснить тип результата выражений:

15 * 3
15 / 3
15 // 2
15 ** 2
"""

expression = [
    15 * 3,
    15 / 3,
    15 // 2,
    15 ** 2,
    ]

for exp in expression:
    print(type(exp))