from wxpy import *

bot=Bot()

my_friend=bot.friends().search("彭世瑜")[0]

my_friend.send("hello wechat!")

my_friend.send_image("表情包.png")