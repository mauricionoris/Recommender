
import manageFiles
import preprocessor
import similarity


parameters = {
    "index" : "",
    "properties" : [],
    "current_path": "",
    "new_path":  ""
}

def getProp(prop, list):
    ret = []
    for item in list:
        ret.append(item[prop])
    return ret;

def addFile(path, properties, index):
    manageFiles.parameters['path'] = path
    inputList = manageFiles.read()
    idx = getProp(index,inputList)
    corpus = {}
    for property in properties:
        corpus[property] = getProp(property, inputList)
    return idx, corpus, len(inputList)

def run():
    computed_similarity = []
    dataset = { "current": 0, "current_data": {}, "current_index": []
              , "new": 0    , "new_data": {}    , "new_index": []}

    dataset["current_index"], dataset["current_data"], dataset["current"] = addFile(parameters["current_path"],parameters["properties"], parameters["index"])
    dataset["new_index"], dataset["new_data"], dataset["new"] = addFile(parameters["new_path"],parameters["properties"], parameters["index"])

    for i in range(0,len(dataset["new_index"])):
        output = {"key": dataset["new_index"][i],"similars":[]}

        for prop in parameters["properties"]:
            preprocessor.parameters['corpus'] = [*dataset["current_data"][prop],*dataset["new_data"][prop]]
            X, Z = preprocessor.run()
            similarity.parameters['matrix'] = X
            S = similarity.run()[0:dataset["current"], dataset["current"]:]
            for j in range(0,S.shape[0]):
                item = {"key":dataset["current_index"][j], prop:S[j,i]}
                output['similars'] = setSimilarity(item, prop, output['similars'])
        computed_similarity.append(output)
    return computed_similarity

def setSimilarity(new_item, prop, output):
    for item in output:
        if item['key'] == new_item['key']:
            item[prop] = new_item[prop]
            return output
    output.append(new_item)
    return output
