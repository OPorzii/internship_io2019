""" 
PIYAWAT CHOEYCHIT
"""

import json,xmltodict
 
def convert_to_json(file_path):
    """ Function's Convert data frome XML to JSON """
    # Read XML to String value
    with open(file_path, 'r') as f:
        xmlString = f.read()

    # Write String to Json file
    new_path = file_path.replace(".xml", ".json")
    with open(new_path, 'w') as outfile:
        data = xmltodict.parse(xmlString, attr_prefix='')['current']
        json.dump(data, outfile, indent=4)
        print("Convert Success!!")
        print("Output = ",new_path)
    
print("Enter XML File path:", end=" ")
convert_to_json(input())
