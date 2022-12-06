#! python3
# find sdk-web

import os


for pasta, subpasta, file in os.walk('C:\\'):

    #Após o if, coloque as característica do arquivo ou pasta que deseja encontrar.
    #Após o in, segue a lógia. Se procurar um aquivo, coloque 'file', se preocura uma pasta, coloque 'pasta'
    if 'chromedriver.exe' in pasta:
        print(file)
print('Finished')
