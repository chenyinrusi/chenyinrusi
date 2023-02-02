# -*- coding: utf-8 -*-
"""
Created on Fri 26 Mar 2021

@author: Jarry.Pan
"""

# for permutation and combination
def pc_output_description():
    print(
        '''
    Parameters to be used in function 'pc_output':
    
        *base - this is the list of parameters you want to insert permute or combine (must be in list form);
    
        *num - the Pick Number (default is to pick largest number), how many you want to pick out from the base;
    
        *mode - either 'permutation' (default) or 'combination', output in combination or permutation;
    
        *method - either 'unique' or 'order'(default), output in unique index order, or unique values;
    
        *print_results - either 'yes' (default) or 'no', print result in screen or not;
    '''
    )

def pc_output(base=['a', 'b', 'c'], num=None, mode='permutation', print_results='yes', method='order'):
    # check the base list type is a list
    if type(base) != type([]):
        print('Impossilbe input... The base should be list')
        exit()
    else:
        pass

    # check Pick number validity
    if num is None:
        num = len(base)
    if not isinstance(num, int):
        print('Impossilbe input... The Pick number should be an integer')
        exit()
    elif num > len(base):
        print('Impossilbe input... The Pick number is greater than the base number')
        exit()
    elif num == 0:
        print('Impossilbe input... The Pick number is Zero, you will get 0 if you do so')
        exit()
    elif num < 0:
        print('Impossilbe input... The Pick number is less than Zero')
        exit()
    else:
        pass

    index_list = []
    a_group = []
    temp_base = base

    for i in range(0, len(temp_base)):
        index_list.append(i)

    count = 0
    residual_list = tuple(index_list)
    for i in residual_list:
        temp_result_list = []
        temp_result_list.append(i)
        a_group.append(temp_result_list)
    count = 1
    while count < num:
        c_group = []
        for i in range(0, len(a_group)):
            a = a_group[i]
            for b in residual_list:
                c = []
                if b in a:
                    pass
                else:
                    c.append(b)
                    c = a + c
                    c_group.append(c)
        a_group = c_group
        count = count + 1

    index_group = []
    if mode == 'permutation':
        index_group = a_group
    elif mode == 'combination':
        c_group = []
        for i in a_group:
            i.sort()
            if i in c_group:
                pass
            else:
                c_group.append(i)
        index_group = c_group

    for i in index_group:
        for d in range(0, len(i)):
            i[d] = temp_base[i[d]]

    if method == 'unique':
        if mode == 'permutation':
            c_group = []
            for i in index_group:
                if i in c_group:
                    pass
                else:
                    c_group.append(i)
            index_group = c_group
        elif mode == 'combination':
            c_group = []
            for i in index_group:
                i.sort()
                if i in c_group:
                    pass
                else:
                    c_group.append(i)
            index_group = c_group
    elif method == 'order':
        pass
    else:
        print('incorrect method entered')
        exit()

    if print_results == 'yes':
        for i in index_group:
            print(i)
        print('Total ' + mode + ' count: ' + str(len(index_group)))

    return index_group

def product_combo_description():
    print(
        '''
        all args are in list format
        ---- e.g. product_combo([1,2],[4,5],['a','b'])
        '''
    )

def product_combo(*args):
    for i in args:
        if type(i) is list:
            pass
        else:
            print('Incorrect data type entered, only allow list type')
            exit()

    index_list = []
    segment_list = []
    for i in args:
        index_items = []
        segment_list.append(len(i))
        for j in range(0, len(i)):
            index_items.append(j)
        index_list.append(index_items)

    full_combo = 1
    for i in index_list:
        full_combo = len(i) * full_combo

    combo_div_list = []
    combo_div = full_combo + 0
    for i in segment_list:
        combo_div = combo_div / i
        combo_div_list.append(combo_div)

    result_index_list = []
    for i in range(0, full_combo):
        cal = i + 0
        result_element = []
        for j in combo_div_list:
            result_element.append(int(cal // j))
            cal = cal % j
        result_index_list.append(result_element)
    result_list = []
    for i in result_index_list:
        result_element = []
        for j in range(0, len(i)):
            result_element.append(args[j][i[j]])
        result_list.append(result_element)
    return result_list
