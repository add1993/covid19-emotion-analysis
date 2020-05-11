import pandas as pd
import json
import collections

data = pd.read_json("nlp_train.json")

# Print the json file in pretty format
"""
input_file = open("nlp_train_pretty.json", "w")
with open("nlp_train.json") as f:
    input_dict = json.load(f)
dict_json = json.dumps(input_dict, indent=4)
input_file.write(dict_json)
"""

csv_file = open("nlp_train.csv", "w")

#new_file = open("nlp_train_clean.json", "w")
#json_dict = {}
#JArray = []
csv_file.write("body,anger,anticipation,disgust,fear,joy,love,optimism,pessimism,sadness,surprise,trust,neutral\n")
for index, values in data.iteritems():
    #json_dict.update(values)
    #JArray2 = collections.OrderedDict()
    #JArray2 = values
    #JArray.append(JArray2)
   
    line = ""
    for key, value in values.items():
        if key == "body":
            body = str(value)
            body = body.replace('\t','')
            body = body.replace('\n','')
            body = body.replace(',','')
            line = line + body
        elif key == "emotion":
            for emotion, label in value.items():
                line = line + ","+str(label)
                
    csv_file.write(line+"\n")
    
#dict_json = json.dumps(JArray)
#new_file.write(dict_json)

