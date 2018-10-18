from rows.utils import download_file
import pathlib

estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RO", "RS", "RR", "SC", "SE", "SP", "TO"]

data_path = pathlib.Path("data")
if not data_path.exists():
    data_path.mkdir()

CTF_path = pathlib.Path("data\\CTF") 
if not CTF_path.exists():
    CTF_path.mkdir()

AIDA_path = pathlib.Path("data\\AIDA")
if not AIDA_path.exists():
    AIDA_path.mkdir()

for UF in estados:
    download_file("http://dadosabertos.ibama.gov.br/dados/CTF/APP/"+UF+"/pessoasJuridicas.csv", filename="data\\CTF\\CTF-"+UF+".csv", progress=True)

download_file("http://dadosabertos.ibama.gov.br/dados/CTF/AIDA/pessoasJuridicas.csv", filename="data\\AIDA\\AIDA.csv", progress=True)
