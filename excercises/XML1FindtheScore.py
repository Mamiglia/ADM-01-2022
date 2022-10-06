

def get_attr_number(node):
    summa = len(node.attrib)
    for child in node:
        summa += get_attr_number(child)
    return summa

