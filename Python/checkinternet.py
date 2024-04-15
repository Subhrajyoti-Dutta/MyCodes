import tool

while True:
    try:
        tool.checkspeedtest()
        print("Passed: ",end="")
        tool.dateandtime().time()
        break
    except:
        print("Failed: ",end="")
        tool.dateandtime().time()