import re
import pandas as pd
from validate_docbr import CPF, CNPJ
import requests

class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta")

class DocCpf:
    def __init__(self, documento):
        documento = str(documento)  
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")
    
    def __str__(self):
        return self.format()

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        documento = str(documento)  
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")
        
    def __str__(self):
        return self.format()

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
