# BigDataWebULL
Proyecto para análisis de logs de servidores web de la ULL

Forma de ejecución

find . -name \*.gz -exec gzip -c -d {} \; | python3 ../map_campusvirtual_2.0.py 2013 | python3 ../reduce_campusvirtual_2.0.py | tee -a ../output2.csv

