import os
import requests

from datetime import date

os.chdir("S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/")

 

 



 

sciezka = 'https://dane.imgw.pl/datastore/getfiledown/Oper/Snieg/'

data = date.today().strftime("%Y_%m_%d")

calosc = f"{sciezka}Pokrywa_sniezna{data}.pdf"

print(calosc)

 

response = requests.get(calosc)

pdf_filename = f"2.pokrywa_sniezna.pdf"

with open(pdf_filename, "wb") as pdf_file:

    pdf_file.write(response.content)
