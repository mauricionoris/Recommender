
import setup
setup.load()

import manageFiles
manageFiles.parameters['path'] = './support/vagas.json'
inputList = manageFiles.read() # Le o arquivo

corpus = []
for doc in inputList: # captura a descrição
    corpus.append(doc["desc"])

import preprocessor
preprocessor.parameters['corpus'] = corpus

X, Z = preprocessor.run()

print (X)
print (Z)

output_file = []
for i in range(0,X.shape[0]):
     output = {"titulo": "", "texto": "", "tokens": []}
     output["titulo"]='Código: {} - Título: {}'.format(inputList[i]["codigo"],inputList[i]["titulo"])
     output["texto"] = corpus[i]
     for j in range(0,X.shape[1]):
        if X[i,j] > 0:
            token = {"item":Z[j],"tfidf":X[i,j]}
            output['tokens'].append(token)
     output_file.append(output)

manageFiles.parameters['path'] = './support/processed.json'
manageFiles.write(output_file)
