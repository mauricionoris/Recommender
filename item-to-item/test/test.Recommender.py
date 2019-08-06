
import setup
setup.load()

import manageFiles
import recommender


recommender.parameters['threshold'] = 0.2
recommender.parameters['selection-step'] = 3
recommender.parameters['key'] = 'codigo'
recommender.parameters['inner-list'] = 'processo_seletivo'
recommender.parameters['candidates-list'] = 'candidatos'

root = '/home/mnf/reachr/projects/RecommenderSystem/test'
manageFiles.parameters['path'] = root + '/support/vagas.json'
recommender.parameters['input-jobs'] = manageFiles.read()

manageFiles.parameters['path'] = root + '/support/similiars.json'
recommender.parameters['input-similars'] = manageFiles.read()

output = recommender.run()
print(output)

manageFiles.parameters['path'] = root + '/support/recommendation.json'
manageFiles.write(output)
