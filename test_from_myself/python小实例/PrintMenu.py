#PrintMenu.py
#格式化字符串实例
def printMenu(diction,width):
    #width=int(input("please enter width:"))

    price_width=10
    item_width=width-price_width

    header_format="%-*s%*s"
    item_format="%-*s%*.2f"

    print("="*width)
    print(header_format%(item_width,"Item",price_width,"Price"))
    print("="*width)
    
    for key,value in diction:
        print(item_format % (item_width,key,price_width,value))
   
    print("="*width)

def main():
    d={
       ("apple",23),
       ("pig",22.2),
       ("cat",15.6),
       ("monkey",25.3)
       }
    printMenu(d,20)

if __name__=="__main__":
    main()
