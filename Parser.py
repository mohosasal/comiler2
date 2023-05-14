
#################################### imports

import Scanner
from anytree import Node, RenderTree
import transitiondiagrams

#################################### setting dfa s




#################################### first follow


#################################### main class



class Parser:

    def __init__(self ,node_0,parser):
        self.main_node =Node("Program")
        self.parser=parser
        self.token=""





    def diagram_transition(self,this_node,state,line):





        ############################################### final state handling
        # if we are in the final state of the program


        if state is final_state:
            return




        ###########################################first follow   (change the functionality of first follow set up)

        rented=False
        for trans in transition_diagram[state]:

            if self.token in first[trans]:
                rented=True
                # add node to the tree in the left most child of the parrent
                that_node=Node(trans,parent=this_node)
                if trans is not terminals:
                    self.diagram_transition(that_node,first_state_of_node,token,trans)
                    #getting next token?
                    self.diagram_transition(this_node,next_state_of_this_state,next_token,line)

                else:
                    #token= get next token
                    return



        if rented==False:  # error handling

            if token not in follow[line]:
                pass
                #illegal token message
                #start over from this line
            else:
                #missing line
                #exit this line








