from __future__ import print_function
from os import walk
import re
from pathlib import Path

class Func:
    def __init__(self, n):
        self.nome = n
        self.ret = []

class Controller:
    def __init__(self, n):
        self.nome = n
        self.functions = []

controllers_path = '../Documentos/convenios-teste/app/Http/Controllers'
views_path = '../Documentos/convenios-teste/resources/views'
files_path = []
dir_path = []
controllers = []
for (dirpath, dirnames, filenames) in walk(controllers_path):
    dir_path.extend(dirnames)
    files_path.extend(filenames)
    break
for f_path in files_path:
    path = Path(controllers_path+'/'+f_path)
    file = path.open('r')
    controllers.append(Controller(path.stem))
    f = file.readlines()
    for line in f:
        if re.findall(r'public function ([a-zA-Z0-9_]*)\(([a-zA-Z0-9_$, ]*)\)', line):
            controllers[len(controllers)-1].functions.append(Func(line.replace('\n', '')))
        elif re.findall(r'return ([a-zA-Z0-9_]*)\(([a-zA-Z0-9_$, ]*)\)', line):
            returns = re.findall(r'view\(([a-zA-Z0-9_]*)\)', line)
            print(returns)
            print("->"+line)
            for r in returns:
                r = r.replace('\'', '')
                r = r.replace('"', '')
                r = r.replace('.', '/')
                view = Path(views_path+'/'+r.encode('utf8')+".blade.php")
                print(view)
                if view.exists():
                    controllers[len(controllers)-1].functions[len(controllers[len(controllers)-1].functions)-1].ret.append(views.stem)

print('@startuml')
for c in controllers:
    print(c.nome+'{')
    for f in c.functions:
        print(f.nome)
        for r in f.ret:
            print('r->'+r)
    print('}')
print('@enduml')
