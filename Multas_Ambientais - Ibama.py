from rows.utils import download_file
import pathlib

estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RO", "RS", "RR", "SC", "SE", "SP", "TO"]

data_path = pathlib.Path("data")
if not data_path.exists():
    data_path.mkdir()

for UF in estados:
    download_file("https://dadosabertos.ibama.gov.br/dados/SICAFI/"+UF+"/Quantidade/multasDistribuidasBensTutelados.csv", filename="data\\"+UF+".csv", progress=True)