hash_table = [None for i in range(101)]
colisions = []
n_entries = 0

def jhash(key_str):
    temporal_sum = 0
    for i in range(len(key_str)):
        temporal_sum += ord(key_str[i])*(i+1)
    return (19 * temporal_sum) % 101


def add_entry(idx,str):
    global n_entries
    hash_table[idx] = str
    n_entries += 1
    return


def rm_entry(idx):
    global n_entries
    hash_table[idx] = None
    n_entries -= 1
    if idx in colisions:
        colisions.remove(idx)
    return


def t_add(str_val):
    global n_entries
    idx_ins = jhash(str_val)
    # Comprobar que la palabra no sea la misma que algunas de las que causaron colisiones
    for x in colisions:
        if hash_table[x] == str_val:
            return #se trata de una palabra que ya esta insertada en otra posicion debido a una colision

    if hash_table[idx_ins] is None:
        add_entry(idx_ins, str_val)
        #print("insert "+str_val + " at:"+str(idx_ins))
    else:
        if hash_table[idx_ins] == str_val:
            return  # se trata de la misma palabra
        else:
            # La entrada esta ocupada, hay que usar resolucion de colisiones.
            for j in range(1, 20):
                colision_index = (idx_ins + j*j + 23 * j) % 101
                if hash_table[colision_index] is None:
                    add_entry(colision_index, str_val)
                    colisions.append(colision_index)
                    #print("insert " + str_val + " at:" + str(colision_index))
                    return
                elif hash_table[colision_index] == str_val:
                    return
    return


def t_del(str_val):
    idx_ins = jhash(str_val)
    if hash_table[idx_ins] == str_val:
        rm_entry(idx_ins)
        #print("delete " + str_val + " at:" + str(idx_ins))
    else:  #Pueden pasar dos cosas, que la palabra no exista o que haya sido insertada en otro indice por una colision
        for j in range(1, 20):
            colision_index = (idx_ins + j * j + 23 * j) % 101
            if hash_table[colision_index] == str_val:
                rm_entry(colision_index)
                #print("delete " + str_val + " at:" + str(colision_index))
                return
    return


n_test_cases = int(input())
for i in range(n_test_cases):
    n_operations = int(input())

    for j in range(n_operations):
        line = input()
        str_entry = line[4:].rstrip()

        if len(str_entry) != 0 and ord(str_entry[0]) != 32:
            if line[0] == 'A':
                t_add(str_entry)
            else:
                t_del(str_entry)

    print(n_entries)
    # Print the hash table in order
    for idx in range(101):
        if hash_table[idx] is not None:
            print(str(idx)+":"+hash_table[idx])

    # Clear table
    n_entries = 0
    hash_table = [None for i in range(101)]
    colisions = []