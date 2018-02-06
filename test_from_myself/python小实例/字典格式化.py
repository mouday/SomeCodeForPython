#字典格式化
template='''<html>
<head></head>
<title>%(title)s</title>
</html>'''

d={"title":"name"}
print(template%d)

"""
<html>
<head></head>
<title>name</title>
</html>
"""
