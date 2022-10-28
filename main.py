import sys, os.path, re
import json, importlib, argparse

path_to_this_file = os.path.join(*os.path.abspath(__file__).split("\\")[:-1])
sys.path.insert(0, path_to_this_file)
sys.path.insert(0, os.path.join(path_to_this_file, "lib"))
sys.path.insert(0, "lib/")

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to file")
parser.add_argument("-c", help="add path to config file", default="std.json")
args = parser.parse_args()

litef, lites, liteo = dict(), dict(), dict()

with open(args.path, 'r', encoding="utf-8") as f:coder = f.read()

with open(args.c, 'r', encoding="utf-8") as f:
    for i in json.loads(f.read()):
        lib = importlib.import_module(i)

        for lfname, lffun in lib.llc.functions.items():litef[lfname] = lffun
        for lsname, lsfun in lib.llc.structurs.items():lites[lsname] = lsfun
        for loname, lofun in lib.llc.ows.items():liteo[loname] = lofun

struct, own_syntax, function = r"\$\(([\s\S]*?)\):([\s\S]*?)<(([\s\S]*?)*)>\.?|\@\(([\s\S]*?)\):([\s\S]*?)\{(([\s\S]*?)*)\}\.?", r"(.*)>(.*).?", r"(\S*)\(([\s\S]*?)\)\.?"
comment, comment2 = r"//.*", r"\$\(comment\)\<[^>]*>"

def re_get(regex, code):
    res = re.findall(regex, code)
    code = re.sub(regex, "", code)

    return res, code


def analyze(code):
    code = re.sub(comment2, "", re.sub(comment, "", code))
    structures, code = re_get(struct, code)
    own_syntax_l, code = re_get(own_syntax, code)
    functions, code = re_get(function, code)
    return functions, structures, own_syntax_l

class CodeLL:
    def __init__(self, lst):
        self.lst = lst
    
    def run(self):
        start_code(*self.lst)

def start_code(functions, structures, own_syntax_l):
    for st_ in structures:
        if st_[0] in list(lites.keys()):lites[st_[0]](st_[1], CodeLL(analyze(st_[2].strip())))
        else:print(f"warning: unknow stucture with name <{st_[0]}>")

    for fun in functions:
        if fun[0] in list(litef.keys()):litef[fun[0]](fun[1])
        else:print(f"warning: unknow function with name <{fun[0]}>")

    for os_el in own_syntax_l:
        if os_el[0] in list(liteo.keys()):liteo[os_el[0]](os_el[1])
        else:print(f"warning: unknow obj with name <{os_el[0]}>")

start_code(*analyze(coder))
