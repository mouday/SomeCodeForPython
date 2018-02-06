#ImageTest.py
#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
#类似于微信未读信息数量那种提示效果。

# 安装pillow  pip install Pillow

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# image=Image.open("image.jpg")
# image.show()
# image.save("image1.jpg")

text = u"5"

im = Image.open('./image.jpg')

dr = ImageDraw.Draw(im)
font = ImageFont.truetype('msyh.ttf', 35)

#设置x,y位置
dr.text((im.size[0]*0.85, im.size[1]*0.05), text, font=font, fill="#ff0000")

im.show()
im.save('result.jpg')
print("照片处理完成")