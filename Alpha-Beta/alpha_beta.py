import numpy as np
def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    
    symbol = alternate_symbol(chosen_symbol)
    nodes_generated = []
    i = 0
    symbol_indice=[]
    for n in node:
        if (n==0):
            symbol_indice.append(i)
    
        i+=1

    num = 0   
    while(num< len(symbol_indice):
        new_children = node.copy()          
        new_children[symbol_indice[num]]=symbol
        nodes_generated.append(new_children)
    
        print(new_children)       
        num+=1

    print("child")
    return nodes_generated
    

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol, alpha, beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
      game_result = is_game_over(node)
   # print(node)
    #Verifica si el juego ya terminó
    
    if game_result[0]:
       # print("termino",node)
        if game_result[1] is None:
            return (0,node)
            #return 0
        else:
            return (-infinty,node) if is_maximizing_player_turn else (infinty,node)
            #return -infinty if is_maximizing_player_turn else infinty
    
    children = generate_children(node, chosen_symbol)
    #print("generate")
    if(is_maximizing_player_turn):
        max_child= -infinty
        for child in children:
            child_actual=mini_max_ab(child,not is_maximizing_player_turn,alternate_symbol(chosen_symbol),alpha,beta)
            var= child_actual[0]
            var2= child_actual[1]
            max_child= max(var,max_child)            
            alpha= max(alpha,var)
            if beta <= alpha:
                break
        return (max_child,var2)
       # return max_child
    else:
        min_child= infinty
        for child in children:
            child_actual= mini_max_ab(child, not is_maximizing_player_turn,alternate_symbol(chosen_symbol),alpha,beta)
            var= child_actual[0] 
            var2= child_actual[1] 
            min_child= min(var,min_child)
            beta = min(var,beta)
            if beta <= alpha:
                break
        return (min_child,var2)
        #return min_child


def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    children_results = list(map(
        lambda child: [
            mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
            child
        ],
        children
    ))

    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)