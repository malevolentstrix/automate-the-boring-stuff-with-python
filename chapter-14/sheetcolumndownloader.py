# "sheetcolumndownloader.py" of Chapter 14 of the book
# By JITHIN JOHN
import ezsheets
formsheet = ezsheets.Spreadsheet('https://forms.gle/iXbuTJFy6nhQ29MN7')
sheet1 = formsheet[0]
wanted = sheet1.getColumn(3)
print(wanted[1:wanted.index('')])
