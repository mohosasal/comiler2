
#################################### imports

import Scanner
from anytree import Node, RenderTree
import transitiondiagrams




#################################### main class



class Parser:

    def __init__(self ,node_0,parser):
        self.main_node =Node("Program")
        self.scanner = Scanner.Scanner()
        self.token=""





    def diagram_transition(self,this_node,state,line):





        ############################################### final state handling
        # if we are in the final state of the program


        if len(transitiondiagrams.transition_diagrams[line][state]) == 0:
            return




        ###########################################first follow   (change the functionality of first follow set up)

        rented=False
        for trans in transitiondiagrams.transition_diagrams[line][state].keys():
            if self.token in first[trans]:
                rented=True
                # add node to the tree in the left most child of the parrent
                that_node=Node(trans,parent=this_node)
                if trans in transitiondiagrams.non_terminals:
                    self.diagram_transition(that_node,transitiondiagrams.starter_of_non_terminals[trans],self.token,trans)
                    #getting next token?
                    self.diagram_transition(this_node,transitiondiagrams.transition_diagrams[line][state][self.token],self.token,line)
                else:
                    self.token = self.scanner.get_next_token()

                    return



        if rented==False:  # error handling

            if token not in follow[line]:
                pass
                #illegal token message
                #start over from this line
            else:
                #missing line
                #exit this line








