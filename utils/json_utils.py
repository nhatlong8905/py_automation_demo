import json
import time

def get_json_from_file(file_path):
    return json.load(open(file_path))

def create_json_file(path, file_name, data):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open(path+"/"+timestr+"_"+file_name, 'w') as f:
        json.dump(data,f, indent=4)

def remove_unicode_string(text):
    string_encode = text.encode("ascii", "ignore")
    return string_encode.decode().replace("\n", "")