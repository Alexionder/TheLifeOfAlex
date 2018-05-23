from urllib2 import urlopen
from bs4 import BeautifulSoup
import Tkinter as tkinter

top = tkinter.Tk()
var = tkinter.StringVar()
text1 = tkinter.Text(top)
text2 = tkinter.Text(top)

resultLabel = tkinter.Label(top, textvariable=var)

def get_value(name):
    name = name.replace(" ", "+")
    response = urlopen('https://www.cardmarket.com/en/Magic/Products/Singles/Dominaria/' + name)

    soup = BeautifulSoup(response.read(), from_encoding=response.headers.getparam('charset'))

    for line in soup.find('td', {'class': 'outerRight col_Odd col_1 cell_2_1'}).stripped_strings:
        line = float(line[:-2].replace(',', '.'))
        return line

def Submit():
    var.set("Error")
    print "Calculating"
    cards1 = []
    sum1 = 0
    cards2 = []
    sum2 = 0
    for line in text1.get(1.0, tkinter.END).splitlines():
        if line != "":
            cards1.append(line)

    for line in text2.get(1.0, tkinter.END).splitlines():
        if line != "":
            cards2.append(line)

    for card in cards1:
        sum1 += get_value(card)

    for card in cards2:
        sum2 += get_value(card)

    if sum1 < sum2:
        equalizer = " < "
    elif sum1 > sum2:
        equalizer = " > "
    else:
        equalizer = " = "

    var.set(str(sum1) + equalizer + str(sum2))
    print "Done"


'''
card = str(raw_input("Your card: "))
print(get_value(card))
'''


submitButton = tkinter.Button(top, text="Submit", command=Submit)
text1.pack(side=tkinter.LEFT, fill=tkinter.X)
text2.pack(side=tkinter.RIGHT, fill=tkinter.X)
resultLabel.pack(side=tkinter.BOTTOM)
submitButton.pack(side=tkinter.BOTTOM)
top.mainloop()