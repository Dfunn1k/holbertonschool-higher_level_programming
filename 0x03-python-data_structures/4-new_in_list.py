def new_in_list(my_list, idx, element):
    copy_list = []
    for items in my_list:
        copy_list.append(items)

    if idx < 0:
        return(copy_list)
    elif idx >= len(my_list):
        return(copy_list)
    else:
        copy_list[idx] = element
        return(copy_list)
