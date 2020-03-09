# Ejemplo basado en: https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
# Git: https://github.com/edenau/minimal-blockchain


import datetime # tratamiento timestamps
from MinimalChain import MinimalChain


# se inicia la cadena y se agregan 20 bloques
c = MinimalChain()
for i in range(1,20+1):
    c.add_block(f'Datos del bloque {i}')


# Se obtienen los atributos de ciertos bloques
print('--- Atributos de un determinado bloque')
print('Bloque 3 - Timestamp:',c.blocks[3].timestamp)
print('Bloque 7 - Datos:',c.blocks[7].data)
print('Bloque 9 - Hash:',c.blocks[9].hash)


# se obtiene el número de bloques de la cadena
print('--- Atributo de la cadena de bloques')
print('Bloques que contiene la cadena:', c.get_chain_size())


# se verifican todos los bloques de la cadena
print('--- Verificación de todos los bloques de la cadena')
print(c.verify())


# copia de la cadena completa
print('--- Lógica Fork')
c_forked = c.fork('latest')
print('Fork: cadena igual a la original:',c == c_forked)


c_forked.add_block('Datos nuevo bloque que solo afecta a la cadena Fork')
print(c.get_chain_size(), c_forked.get_chain_size())


# pruebas provocando errores
print('--- Modificaciones Fork para provocar errores')
c_forked = c.fork('latest')
# Error 1: la verificación será errónea porque se modifica el index y el hash del bloque ya no coincide
c_forked.blocks[9].index = -9
c_forked.verify()


c_forked = c.fork('latest')
# Error 2: la verificación será errónea porque se modifica el timestamp y el hash del bloque ya no coincide
c_forked.blocks[16].timestamp = datetime.datetime(2000, 1, 1, 0, 0, 0, 0)
c_forked.verify()


c_forked = c.fork('latest')
# Error 3: la verificación será errónea porque se modifica el previous_hash y el hash del bloque ya no coincide
c_forked.blocks[5].previous_hash = c_forked.blocks[1].hash
c_forked.verify()