import setup
setup.load()

import manageFiles
import processor
import similarity

root = '/home/mnf/reachr/projects/RecommenderSystem/test'

processor.parameters['index'] = "codigo"
processor.parameters['properties'] = ["desc","titulo","area_atuacao"]
processor.parameters['current_path'] = root + "/support/vagas.json"
processor.parameters['new_path'] = root + "/support/new_vaga.json"

computed_similarity = processor.run()

manageFiles.parameters['path'] = root + '/support/similiars.json'
manageFiles.write(computed_similarity)

#test jaccard

import pandas as pd
similarity.parameters['matrix'] = pd.DataFrame([[1,0,1,0,1],[0,0,1,1,1]], columns=list('ABCDE')).transpose()
print(similarity.run_jaccard());
