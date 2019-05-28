
import setup
setup.load()

import manageFiles
import score

root = '/home/mnf/reachr/projects/RecommenderSystem/test'
manageFiles.parameters['path'] = root + '/support/similiars.json'

score.parameters['properties'] =  ["desc","titulo","area_atuacao"]
score.parameters['weights'] = {"desc":0.5, "titulo":0.4, "area_atuacao":0.1}
score.parameters['input'] = manageFiles.read()

manageFiles.write(score.run())
