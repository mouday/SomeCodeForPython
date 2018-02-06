#FormatData.py
#功能：格式化日期
'''
year:2017
month(1-12):9
day(1-31):11
September 11th. 2017
'''
def getFormatData(year,month,day):
    if month<=0 or month>12:
        return '0'
    if day<=0 or day >31:
        return "0"
    months=["January",
            "February",
            "March",
            "Apirl",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]

    endings=["st","nd","rd"]+17*["th"]\
            +["st","nd","rd"]+7*["th"]\
            +["st"]
   
    monthNumber=int(month)
    dayNumber=int(day)

    monthName=months[monthNumber-1]
    ordinal=str(day)+endings[dayNumber-1]

    return monthName+" "+ordinal+". "+str(year)

def main():  
    year=int(input("year:"))
    month=int(input("month(1-12):"))
    day=int(input("day(1-31):"))
    print(getFormatData(year,month,day))

if __name__=="__main__":
    main()
