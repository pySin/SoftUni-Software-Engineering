phrase = "Thene+xtdayat12£"
if phrase.isalnum():
    print("isallnum() gets them all")

for sym in phrase:
    if not sym.isalnum():
        print("Non num symbol")
