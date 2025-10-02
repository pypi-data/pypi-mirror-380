#!/usr/bin/env python3

"""
python_package_tree.py is a  free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

import os
import sys
import ast
from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_LIGHT
import click


class Parentage(ast.NodeTransformer):
    # current parent (module)
    parent = None

    def visit(self, node):
        # set parent attribute for this node
        node.parent = self.parent
        # This node becomes the new parent
        self.parent = node
        # Do any work required by super class 
        node = super().visit(node)
        # If we have a valid node (ie. node not being removed)
        if isinstance(node, ast.AST):
            # update the parent, since this may have been transformed 
            # to a different node by super
            self.parent = node.parent
        return node

class ClassLister(ast.NodeVisitor):
    
    def __init__(self):
        self.class_dict = {}
        self.class_ = False

    def visit(self, node):

        if isinstance(node, ast.ClassDef):
            self.class_ = self.visit_ClassDef(node)
            self.class_dict[self.class_] = {}
            #print(f'{node.name} is CLASS')

        if isinstance(node,ast.FunctionDef) and isinstance(node.parent, ast.Module):
            #print(f'{node.name} as ROOT')
            self.func_ = self.visit_FunctionDef(node)
            self.class_ = False
            self.class_dict[self.func_] = {}

        if  isinstance(node,ast.FunctionDef) and isinstance(node.parent, ast.ClassDef):
            #print(f'{node.name} IN CLASS {self.class_}')
            self.func_ = self.visit_FunctionDef(node)
            self.class_dict[self.class_][self.func_] = {}

        elif  isinstance(node,ast.FunctionDef) and isinstance(node.parent, ast.FunctionDef):
            self.func_ = self.visit_FunctionDef(node)
            #print(f'{node.name} IN {node.parent.name}')
            if self.class_:
                try:
                    self.class_dict[self.class_][node.parent.name][node.name] = {}
                except KeyError:
                    self.class_dict[self.class_][node.parent.name] = {}
                    self.class_dict[self.class_][node.parent.name][node.name] = {}
            else:
                try:
                    self.class_dict[node.parent.name][node.name] = {}
                except KeyError:
                    self.class_dict[node.parent.name] = {}
                    self.class_dict[node.parent.name][node.name] = {}

        self.generic_visit(node)

        return self.class_dict

    def visit_ClassDef(self, node):
        return f'\033[36mclass: {node.name}\033[0m'

    def visit_FunctionDef(self, node):
        return node.name

# Recursive count keys of dictionnary
def count_keys(dict_, counter=0):
    for each_key in dict_:
        if isinstance(dict_[each_key], dict):
            # Recursive call
            counter = count_keys(dict_[each_key], counter + 1)
        else:
            counter += 1
    return counter

# Create a hierarchical data structure of files and directories
# for asciitree
def list_files_recursive(path='.',exclude_list=None, no_recursion=False):
    file_info_dict = {}
    for root, dirs, files in os.walk(path):

        cont = False
        for dirname in root.split(os.path.sep):
            if dirname == '.':
                dirname = os.path.basename(os.getcwd())
            if dirname in exclude_list:
                cont = True
                continue

            if cont: continue
            #current_dict = current_dict.setdefault(dirname, {})
        if cont: continue 
        for filename in files:
            if filename.startswith('.'): continue
            if not filename.endswith('.py'): continue
            fname = filename if root == '.' else f'{root[2:]}/{filename}'
            #en vert
            fname = f'\033[92m{fname}\033[0m'
            with open(f'{root}/{filename}', 'r') as fp:
                try:
                    tree = ast.parse(fp.read())
                except Exception as e:
                    input(f'{filename}, {e}')
                #tree = ast.parse(fp.read())
                tree = Parentage().visit(tree)
                cl = ClassLister()
                file_info_dict.update({fname: cl.visit(tree)})

        if no_recursion: break

    return file_info_dict
    
@click.command(context_settings={ 'help_option_names': ['-h', '--help'] })
@click.argument('path', required=False, default=None)
@click.option('--exclude_dir', required=False, default=None, help='Comma separated (WITHOUT spaces) list of directory names to exclude, default=None')
@click.option('-o', 'outfile', required=False, default=None, help='Output file name, default=None')
@click.option('--no_recursion', '-n', is_flag=True, required=False, default=None, help='Do not explore directories')
def main(path, exclude_dir, outfile, no_recursion):
    """
    Tree-like display of directories, files, classes and functions of a python project. The argument PATH may be a dirname or a filename
    
    Without argument, explore from current directory

    Depth exceeding 2 (def in def in def) or class in def will be badly displayed
    """
    
    if not path : path = '.'
    exclude_list = ['__pycache__', 'yap.egg-info', '.git' ]
    try:
        exclude_list += exclude_dir.split(',')
    except AttributeError: pass

    if os.path.isfile(path):
        if not path.endswith('.py'):
            sys.exit("\tI only handle .py files")
        
        with open(path, 'r', encoding='utf-8') as fp:
            tree = ast.parse(fp.read())
            tree = Parentage().visit(tree)
            tree_dict = { path: ClassLister().visit(tree) }

    else:
        file_info_dict = list_files_recursive(path=path, exclude_list=exclude_list, no_recursion=no_recursion)
        path = os.path.basename(os.getcwd()) if path == '.' else path
        tree_dict = {path: file_info_dict}
    

    if count_keys(tree_dict) > 1000 and not outfile:
        sys.exit(f'Very long output ({count_keys(tree_dict)} lines), may no fit in terminal, \nUse:\n   python_package_tree -o python_package_tree.output')

        
    tr = LeftAligned()    
    box_tr = LeftAligned(draw=BoxStyle(gfx=BOX_LIGHT,
                                       horiz_len=3,
                                       indent=3))
    if tree_dict:
        if outfile:
            with open(outfile, 'w') as out_h:
                print(box_tr(tree_dict), file=out_h)
        else:
            print(box_tr(tree_dict))

if __name__ == '__main__': main()

