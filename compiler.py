from scanner import MyFuckingScanner
from parser import MyParser
from anytree import Node, RenderTree

if __name__ == "__main__":
    scanner = MyFuckingScanner("input.txt")
    parser = MyParser(scanner)
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
        f.write(parser.messages)
    f.close()





