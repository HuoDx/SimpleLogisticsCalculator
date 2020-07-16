# CODE STYLE SUPER UGLY #
import copy
HP = 0.12
BP = 4.5
AB = 25
PNL = 15
def get_follwing_zeros(state, index):
    count = 0
    for i in range(index+1, len(state)):
        if state[i] == 0:
            count += 1
        else:
            break
    return count
def fast_simu(states):
    price = 0
    stock = 0
    order = 0
    strategy_table = []
    for i in range(12):
        if states[i] == 1:
            price += BP
            order = (1+get_follwing_zeros(states, i)) * AB
            strategy_table.append((1+get_follwing_zeros(states, i)) * AB)
        stock += order
        order = 0

        stock -= AB
        if stock > 0:
            price += stock * HP
        if stock < 0:
            price += PNL

    return price, strategy_table

min_value = None
min_seq = []
for i in range(4096):
    enum_list = []
    for character in str(bin(i))[2:14]:
        if character == '1':
            enum_list.append(1)
        else:
            enum_list.append(0)
    while len(enum_list) < 12:
        enum_list.append(0)

    if min_value is None:
        min_value = fast_simu(enum_list)[0]
    else:
        if min_value > fast_simu(enum_list)[0]:
            min_value = fast_simu(enum_list)[0]
            strategy = fast_simu(enum_list)[1]
            min_seq = copy.deepcopy(enum_list)
            counter = 0
            for i in range(len(min_seq)):
                if min_seq[i] == 1:
                    min_seq[i] = 'Order: %d'% strategy[counter]
                    counter += 1
                else:
                    min_seq[i] = 'Order: 0'
                   
                
print(min_value )
print('\nthen '.join(min_seq))
            
        
        
