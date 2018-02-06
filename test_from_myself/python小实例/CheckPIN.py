#CheckPIN.py
#检查用户名和PIN码
database=[
	["admin","admin"],
	["guest","123456"],
	["ad","123456"],
	["temp","123abc"],
]

userName=input("user name:")
pin=input("PIN code:")
if [userName,pin] in database:
	print("Access granted")
else:
        print("user name or PIN error!")
