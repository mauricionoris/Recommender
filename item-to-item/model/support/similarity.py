import numpy as np
from sklearn.metrics.pairwise import cosine_similarity;

parameters = {
     "matrix": None,
      "query": None,
      "dense": True
}

def run():
    S = cosine_similarity(parameters["matrix"],parameters["query"], parameters["dense"]);
    return S;

def run_jaccard():
    I = np.dot(parameters['matrix'][0].transpose(),  parameters['matrix'][1])
    U = parameters['matrix'].sum(axis=1).sum()
    #print('intersection={} \n union={}'.format(I,U))
    return I / U;
