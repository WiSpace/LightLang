import re
import llc

last = False
funs = { }
vars = { }
classes = { }

@llc.llctype(func_name="output")
def output(*text):
    print(*text)

@llc.llcstruc(struct_name="if")
def if_(if_evnt, code):
    global last
    last = eval(if_evnt)
    if last:
        code.run()

@llc.llcstruc(struct_name="else")
def else_(_, code):
    global last
    if not last:
        code.run()

@llc.llcstruc(struct_name="space")
def space(_, code):
    code.run()

@llc.llcows(ows_name="v")
def var(text):
    global vars
    v = text.split('=')
    val = re.findall(r"(\d+|\"([\s\S]*?)\"|.*)", v[1])
    if val[0]=='':valr = val[1]
    else:
        if val[0].isdigit():
            valr = int(val[0])
        else:
            valr = val[0]
    vars[v[0]] = valr

@llc.llcstruc(struct_name="f")
def fun(name, code):
    global funs
    n = re.findall(r"(.*)\(([\s\S]*?)\)", name)[0]
    funs[n[0]] = [code, llc.llparse_args(n[1])]

@llc.llcows(ows_name="f")
def fun_start(name):
    global funs, vars
    name, args = name.split(':', 1)
    args = llc.llparse_args(args)
    n = 0
    for arg in args:
        vars[funs[name.strip()][1][n]] = arg
        n+=1
    funs[name.strip()][0].run()

@llc.llctype(func_name="output-var")
def outputvar(*varrs):
    for i in varrs:
        print(vars[i])

@llc.llcstruc(struct_name="obj")
def obj_class(class_name, code):
    global classes
    print(class_name)
    print(99)
    classes[class_name] = code
    print(classes)

@llc.llctype(func_name="class-init")
def class_init(name):
    global classes
    print(classes)
    print(101)
    classes[name].run()
