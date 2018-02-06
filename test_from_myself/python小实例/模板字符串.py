from string import Template

s=Template("$x, ooxx $x")
s.substitute(x="good")
#'good, ooxx good!'
s=Template("it't good $$ $x")
s.substitute(x="ooxx")
#"it't good $ ooxx"
s=Template("is a ${x}good")
s.substitute(x="my")
#'is a mygood'
s=Template("is $one is $two")
d={}
d["one"]="good"
d["two"]="very"
s.substitute(d)
#'is good is very'
