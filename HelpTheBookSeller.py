"""example from description
        b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        c = ["A", "B", "C", "W"]
        test.assert_equals(stock_list(b, c), "(A : 20) - (B : 114) - (C : 50) - (W : 0)")
        
        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")
        """

def stock_list(stocklist, categories):
    strng = ""
    for category in categories:
        count = 0
        for code in stocklist:
            if category == code[0]:
                count += (int(code.split(' ')[1]))

        if count != 0:
            isNotZero = True

        if category != categories[-1]:
            strng += "(" + category + " : " + str(count) + ") - "
        else:
            strng += "(" + category + " : " + str(count) + ")"

    return strng if stocklist and categories else ""

a = []
b = []

print(stock_list(a,b))