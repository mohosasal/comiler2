import Scanner
import Parser


class Compiler:







    if __name__ == "__main__":

        scanner=Scanner("input.txt")
        parser=Parser(scanner)

        parser.diagram_transition(parser.main_node,"Program")



