import code_gen
from scanner import MyFuckingScanner
from parser import MyParser
from anytree import Node, RenderTree
from code_gen import *
if __name__ == "__main__":
    scanner = MyFuckingScanner("input.txt")
    code_gen=Code_gen(scanner)
    parser = MyParser(scanner,code_gen)
    parser.diagram_transition(parser.main_node, 0, "Program")
    output = ''
    for pre, fill, node in RenderTree(parser.main_node):
        output = output + "%s%s" % (pre, node.name)
        output = output + '\n'
        # print("%s%s" % (pre, node.name))
    output = output.replace("'", '')
    f = open('parse_tree.txt', 'w', encoding="utf-8")
    f.write(output)
    f.close()
    f = open('syntax_errors.txt', 'w', encoding='utf-8')
    if len(parser.messages) == 0:
        f.write('There is no syntax error.')
    else:
        f.write('\n'.join(parser.messages))
    f.close()

    output=""
    for i in range(len(code_gen.pb)):
        output+=(code_gen.pb[i])+"\n"

    f = open('output.txt', 'w', encoding="utf-8")
    f.write(output)
    f.close()







