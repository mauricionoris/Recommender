
import manageFiles
import requests

parameters = {'url':"",'submit':"",'dt_inicial':"20160101"}

#todo substituir stub pela chamada a API
root = '/home/mnf/reachr/projects/RecommenderSystem/test'

def getAllJobs():
    #response = requests.get(parameters['url'])
    #return response;
    obj = manageFiles.read(root + "/support/vagas.json")
    return manageFiles.write(obj)

def getJobToRecommend():
    obj = manageFiles.read(root + "/support/new_vaga.json")
    return manageFiles.write(obj)


def postJobRecommendation(data):
    return manageFiles.write(data)
