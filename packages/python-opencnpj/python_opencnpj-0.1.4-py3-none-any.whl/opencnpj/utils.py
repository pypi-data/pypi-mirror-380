import re

def return_number(char):
            """
            Receive a character, if number return itself, anything else return None
            """
            pattern = re.compile(r".*\D.*")
            if not pattern.match(char):
                return char
            
def format(cnpj: list):
            """
            Receive list of numbers and return a String formated as CNPJ
            """
            cnpj.insert(2, '.')
            cnpj.insert(6, '.')
            cnpj.insert(10, '/')
            cnpj.insert(15, '-')
            return ''.join(cnpj)