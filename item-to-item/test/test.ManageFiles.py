
import setup
setup.load()

import manageFiles

expected_ret = {

}

# Teste Leitura
ret = manageFiles.read('./support/vagas.json')
print(ret);
assert(isinstance(ret,list)),'Erro ao abrir arquivo JSON';

# Teste Gravação
ret = manageFiles.write(ret);
print(ret);
assert(ret != 1),'Erro ao gravar arquivo JSON';
