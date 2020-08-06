import numpy as np
import pandas as pd

print ('reading and importing excel data to dataframe')
Bk1=pd.read_excel('Superstore.xlsx', sheet_name='Orders')
print('Done reading and copying to dataframe')

print('Sorting by selected columns')
Customer = pd.DataFrame(Bk1,columns = ['Order ID','Country','Product ID'])
print('Done sorting by selected columns')

#Bk1 Show the whole excel book

#Customer Show only selected columns

print('Data ready to export')
fname = input('Name of new workbook - ')

print('Exporting to the new workbook')
Customer.to_excel('{fname}.xlsx')
print('Done writing and exporting to new Excel workbook')
