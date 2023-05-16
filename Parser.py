
#################################### imports

import Scanner
from anytree import Node, RenderTree
import transitiondiagrams




#################################### main class



class Parser:

    def __init__(self ,scanner):
        self.main_node =Node("Program")
        self.scanner =scanner
        self.token=""
        self.messages=[]





    def diagram_transition(self,this_node,state,line):





        ############################################### final state handling
        # if we are in the final state of the program


        if len(transitiondiagrams.transition_diagrams[line][state]) == 0:
            return




        ###########################################first follow   (change the functionality of first follow set up)

        rented=False
        for trans in transitiondiagrams.transition_diagrams[line][state].keys():
            if self.token in transitiondiagrams.first[trans]:
                rented=True
                # add node to the tree in the left most child of the parent
                that_node=Node(trans,parent=this_node)
                if trans in transitiondiagrams.non_terminals:
                    self.diagram_transition(that_node,transitiondiagrams.starter_of_non_terminals[trans],trans)
                    #getting next token?
                    self.diagram_transition(this_node,transitiondiagrams.transition_diagrams[line][state][self.token],line)
                else:
                    self.token = self.scanner.get_next_token()

                    return



                # where is the epsilon transition?!



        if rented==False:  # error handling

            if self.token not in transitiondiagrams.follow[line]:

                #illegal token message

                error_message="illegal"+" "+self.token
                self.messages.append(error_message)

                #start over from this line

                self.token = self.scanner.get_next_token()
                self.diagram_transition(this_node, transitiondiagrams.starter_of_non_terminals[line],line)

            else:

                #missing line

                error_message="missing"+" "+line
                self.messages.append(error_message)

                #exit this line

                #fill this gap!








