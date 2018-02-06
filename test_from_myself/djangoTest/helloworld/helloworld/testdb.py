from django.http import HttpResponse
from blog.models import Test

# 添加数据
def insertdb(request):
    test=Test(name="nood")  # 创建对象
    test.save()  # 相当于SQL中的INSERT
    return HttpResponse("保存成功！")

# 获取
def getdb(request):
    lst=Test.objects.all()
    datas=[]
    for l in lst:
        datas.append(l.name)
    datas="|".join(datas)
    return HttpResponse(datas)

# 更新
def updatedb(request):
    row=Test.objects.get(id=1)
    row.name="Tom"
    row.save()
    return HttpResponse("修改成功！")

# 删除
def deletedb(request):
    row=Test.objects.get(id=1)
    row.delete()
    return HttpResponse("删除成功！")