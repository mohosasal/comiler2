from MyFuckingScanner import MyFuckingScanner
from MyParser import MyParser
from anytree import Node, RenderTree

if __name__ == "__main__":
    scanner = MyFuckingScanner("input.txt")
    parser = MyParser(scanner)
    parser.diagram_transition(parser.main_node, 0, "Program")
    for pre, fill, node in RenderTree(parser.main_node):
        print("%s%s" % (pre, node.name))
    print(parser.messages)




    # handling outputs
