import random
def pc(x=10):
    print(f'''SON TOP O'YINI
Men 1 dan {x} gacha bo'lgan bir son o'yladim. Topishga urinib ko'ring!''')
    sanagich=0
    son=random.randint(1,x)
    while True:
        sanagich+=1
        javob=int(input(">>> "))
        if javob>son:
            print("Kichikroq son kiriting!")
        elif javob<son:
            print("Kattaroq son kiriting!")
        elif javob==son:
            print(f"Tabriklayman siz {sanagich} ta urinishda topdingiz.")
            break
        else:
            print("Iltimos faqat son kiriting")
    return sanagich

def user(x):
    input('''Endi siz bir son o'ylang va istalgan tugmani bosing. Men topaman.''')
    sanagich=0
    top=x
    bottom=1
    while True:
        sanagich+=1
        if top!=bottom:
            pc=random.randint(bottom,top)
        else:
            pc=bottom
        javob=input(f"""Siz {pc} ni o'ylagan bo'lsangiz kerak.
To'g'ri(T), Men o'ylagan son bundan kattaroq(+), Men o'ylagan son bundan kichikroq(-)""")
        if javob.capitalize()=="T":
            print(f"Men {sanagich} ta urinishda topdim!")
            break
        elif javob=="+":
            bottom=pc+1
        elif javob=="-":
            top=pc-1
        else:
            print("Iltimos faqat yuqorida aytilgan belgilarni kiriting!")
    return sanagich

def play(x):
    a=pc(x)
    b=user(x)
    javob=True
    while javob:
        if a==b:
            print("Durrang")
        elif a<b:
            print("Siz yutdingiz. Tabriklayman!")
        else:
            print("Men yutdim!")
        javob=int(input("Yana o'ynaymizmi? Ha(1), Yo'q(0)"))



play(20)




