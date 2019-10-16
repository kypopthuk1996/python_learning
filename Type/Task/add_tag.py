#!/usr/bin/python3
import os
import json

pathJsonScript = '/Users/dmitrijminor/tests'
tag = " \'Tags\': [\"ssw\",\"ecss3.14\"],"
vrs = " \'InitVrs\': [{\'NodeName\': \'ecss-node-3.14\',\'NodeVrs\': \'3.14.2.33\' }],"
res = 0

def loadjson(path):
    res = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                if '.json' in entry.name:
                    res.append(path + '/' + entry.name)
            else:
                res.extend(loadjson(path + '/' + entry.name))
    return res

def add_new_to_json(str1, str2, data, list):
    srh = int(str(data).find(','))+1
    new_data = str(data)[:srh] + tag + vrs + str(data)[srh:]
    with open(list, 'w') as j_file:
        j_data = json.dumps(eval(new_data), ensure_ascii=False, indent=2)
        print(j_data)
        j_file.write(j_data)
    return j_file

listpath = loadjson(pathJsonScript)
for list1 in listpath:
    try:
        with open(list1, 'r') as test:
            data = json.load(test)
            add_new_to_json(tag, vrs, data, list1)
        res = res + len(data['Tests'])
    except Exception as e:
        pass
