import re


functions = { }
structurs = { }
ows = { }

def llparse_args(args):
    args_regex = r"(\d+|\"([\s\S]*?)\"|.*);+"
    res = re.findall(args_regex, args)
    arg_res = []

    for arg in res:
        if arg[0].startswith("\"") or arg[0].startswith("\'"):
            arg_res.append(arg[1])
        else:
            arg_res.append(int(arg[0]) if arg[0].isdigit() else arg[0])

    return arg_res

def llctype(own_args_parse=False, func_name=None):
    def llcargs(func):
        def _wrapper(text_args):
            if own_args_parse:func(text_args)
            else:func(*llparse_args(text_args))

        functions[func_name if func_name else func.__name__] = _wrapper
    return llcargs

def llcstruc(struct_name=None):
    def llcargs(func):
        def _wrapper(*args):
            func(*args)

        structurs[struct_name if struct_name else func.__name__] = _wrapper
    return llcargs

def llcows(ows_name=None):
    def llcargs(func):
        def _wrapper(code):
            func(code)

        ows[ows_name if ows_name else func.__name__] = _wrapper
    return llcargs
