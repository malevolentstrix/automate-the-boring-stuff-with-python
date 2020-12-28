# PRACTICE PROBLEM OF CHAPTER 4 "COMMA CODE"
# BY JITHIN JOHN
def comma(passed) : 
    newstring = ""
    for i in passed[:-2]:
        newstring = newstring + i + ", "
    newstring = newstring + string[-2] + ' and ' + string[-1]
    print(newstring)
string = ['apples', 'bananas', 'tofu', 'cats']
comma(string)