import setup
setup.load()

import reachrAPI
import manageFiles

import processor
import score
import recommender

processor.parameters['index'] = "codigo"
processor.parameters['properties'] = ["desc","titulo","area_atuacao"]

processor.parameters['new_path'] = reachrAPI.getJobToRecommend()
processor.parameters['current_path'] = reachrAPI.getAllJobs()

print(processor.parameters['new_path'])
print(processor.parameters['current_path'])

score.parameters['properties'] =  ["desc","titulo","area_atuacao"]
score.parameters['weights'] = {"desc":0.3, "titulo":0.6, "area_atuacao":0.1}
score.parameters['input'] = processor.run()

recommender.parameters['threshold'] = 0.2
recommender.parameters['selection-step'] = 2
recommender.parameters['key'] = processor.parameters['index']
recommender.parameters['inner-list'] = 'processo_seletivo'
recommender.parameters['candidates-list'] = 'candidatos'

recommender.parameters['input-jobs'] = manageFiles.read(processor.parameters['current_path'])
recommender.parameters['input-similars'] = score.run()

ret = reachrAPI.postJobRecommendation(recommender.run())
print(ret)
