# 测试jinja2
from jinja2 import Template

template = Template("Hello {{ name }}!")
html = template.render(name="World")

print(template)
print(html)

"""
<Template memory:2d2c1d0>
Hello World!
"""