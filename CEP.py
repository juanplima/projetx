class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!!")
        
    def __str__(self):
        return self.format_cep()  
    
    def cep_e_valido(self, cep):
        return len(cep) == 8
    
    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def acesso_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        r.raise_for_status()  
        dados = r.json()
        
        if 'erro' in dados:
            raise ValueError("CEP não encontrado.")
        
        bairro = dados.get('bairro', 'Não informado')
        localidade = dados.get('localidade', 'Não informado')
        uf = dados.get('uf', 'Não informado')
        
        return bairro, localidade, uf


def salvar_dados_excel(dados, nome_arquivo="dados_validos.xlsx"):
    df = pd.DataFrame(dados)
    df.to_excel(nome_arquivo, index=False)
    print(f"Dados salvos em {dados}")


dados = []
