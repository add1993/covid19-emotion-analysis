import pandas as pd
import process_data as prcs
import constants as c

"""
    This function reads the data from json file. Converts that into pandas daraframe. It also flattens any nested json columns.
    
    Attributes
    ----------
    
    path : str
        the path of the input file name
    header: list[str]
        the name of the nested columns which needs to be flattened 
"""


def read_input_file(path, header, attributes, clean, map_label = False):
    data = pd.read_json(path)
    data = data.loc[:, attributes]
    if header is not None:
        for col_name in header:
            flattened_data =  pd.json_normalize(data[col_name])
            header_names = flattened_data.columns
            for i in header_names:
                data[i] = flattened_data[i]
        data = data.drop(columns=header)
        if clean == True:
            data = prcs.clean_data(data, c.LABELS)
        if map_label == True:
            data = prcs.map_label(data, c.LABEL_MAP, c.LABELS)
    return data


