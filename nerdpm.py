#!/usr/bin/env python
import argparse
import inspect
from pmmodule import PMModule
import pmmodule

#from rev import Revelation

def print_module_cmds(module):
    for name, data in inspect.getmembers(module, predicate=inspect.ismethod):
        if name.startswith("cmd_"):
            print name[4:]
            print getattr(module, name).__doc__

        
parser = argparse.ArgumentParser(description="A password manager")
parser.add_argument("module")
parser.add_argument("parameter")

args = parser.parse_args()

""" WIP 
if args.module == "rev":
    module = Revelation(args.parameter)  
else:
    raise Exception("invalid module")"""

print "Welcome! \ntype 'help' if you need help, or 'list' to have a list of available commands"

module = pmmodule.PMModule()
while True:
    command = raw_input('> ').strip()
    if command == 'quit':
        break
    if command == 'list':
        print_module_cmds(module)
    else:
        attr = getattr(module, 'cmd_' + command)
        attr()
