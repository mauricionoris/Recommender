import json
import uuid

parameters = {'path':''}

def read(path=None):
    if path is None:
        path = parameters['path']
    with open(path) as json_file:
        return json.load(json_file)

def write(data, path=None):

    if path is None:
        path = "/tmp/{}.json".format(uuid.uuid4().hex)

    with open(path, 'w') as outfile:
        try:
            json.dump(data, outfile,ensure_ascii=False, indent=4)
            return path
        except:
            return 1
