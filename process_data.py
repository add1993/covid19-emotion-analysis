import pandas as pd

"""
    

    This function reads the data from json file. Converts that into pandas daraframe. It also flattens any nested json columns.
    
    Attributes
    ----------
    
    data : dataframe
        the data that needs to be cleaned row-wise. If none of the labels are True, then this function will drop that row.
    labels: list[str]
        list of the labels

"""

def clean_data(data, labels):
    valid = 'valid'
    data[valid] = False
    for i in labels:
        data[valid] = data[valid] | data[i]
    data = data[data[valid] == True]
    data = data.drop(columns = [valid])
    return data


"""


    This function maps the labels. Given the mapping information, it can convert it to one format to another format. Like category to int

    Attributes
    ----------

    data : dataframe
        the data that needs to be cleaned row-wise. If none of the labels are True, then this function will drop that row.
    mapping : dict
        this is the mapping information
    labels: list[str]
        list of the labels
    

"""

def map_label(data, mapping, labels):
    for i in labels:
        data[i] = data[i].map(mapping)
    return data
