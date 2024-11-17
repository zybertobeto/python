import itertools
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook


dr = [[1, 2, 3, 4, 5, 6],
      [13, 14, 15, 16, 17, 18],
      [25, 26, 27, 28, 29, 30],
      [37, 38, 39, 40, 41, 42],
      [49, 50, 51, 52, 53, 54],
      [61, 62, 63, 64, 65, 66],
      [73, 74, 75, 76, 77, 78],
      [85, 86, 87, 88, 89, 90],
      [97, 98, 99, 100, 101, 102],
      [109, 110, 111, 112, 113, 114]]

cr = [[7, 8, 9, 10, 11, 12],
      [19, 20, 21, 22, 23, 24],
      [31, 32, 33, 34, 35, 36],
      [43, 44, 45, 46, 47, 48],
      [55, 56, 57, 58, 59, 60],
      [67, 68, 69, 70, 71, 72],
      [79, 80, 81, 82, 83, 84],
      [91, 92, 93, 94, 95, 96],
      [103, 104, 105, 106, 107, 108],
      [115, 116, 117, 118, 119, 120]]

for (a, b) in itertools.zip_longest(dr, cr):
    dr_cr = (a, b)

    print(dr_cr)

wb = openpyxl.load_workbook('Tests.xlsx')
ws = wb.active

for x in dr_cr:
    ws.append(x)

wb.save('Tests.xlsx')
