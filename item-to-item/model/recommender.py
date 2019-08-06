

parameters = {
    'input-similars': None,
    'input-jobs' : None,
    'threshold': 0,
    'selection-step':0,
    'key': '',
    'inner-list': '',
    'candidates-list':''
}

def getsimilars():
    reco = []
    for item in parameters['input-similars']:
        keylist = list(filter(lambda x : x['score'] >= parameters['threshold'], item['similars']))
        reco.append({'key': item['key'], 'similars': list(map(lambda x : x['key'],keylist)) })
    return reco

def recommend(job):
    obj = {'key':job['key'], 'candidates':[]}
    for key in job['similars']:
        rec = list(filter(lambda x : x[parameters['key']] == key, parameters['input-jobs']))[0]
        obj['candidates'] = rec[parameters['inner-list']][parameters['selection-step']][parameters['candidates-list']]
    return obj

def run():
    recommendation = []
    for job in getsimilars():
        print(job)
        recommendation.append(recommend(job))
    return recommendation
