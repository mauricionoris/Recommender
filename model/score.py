

parameters = {
    'properties' : ["desc","titulo","area_atuacao"],
    'weights'    : {"desc":0.3, "titulo":0.6, "area_atuacao":0.1},
    'input' : None
}

def run():

    output = []
    for item in parameters['input']:
        for subitem in item['similars']:
            total = 0
            for w in parameters['weights']:
                total += subitem[w]*parameters['weights'][w]
            subitem['score'] = total
        item['similars'].sort(key=lambda x: x['score'], reverse=True)
        output.append(item)
    return output
