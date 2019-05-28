
import setup
setup.load()

import reachrAPI
reachrAPI.parameters['url'] = 'https://jsonplaceholder.typicode.com/todos/1'

expected_ret = {
    'getVagas': {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
}

#-----------------------------------------

# Testes
ret = reachrAPI.getVagas();
assert(expected_ret['getVagas'] == ret.json()),'Erro no retorno das vagas';
print(ret.json());
