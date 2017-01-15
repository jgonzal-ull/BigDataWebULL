#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import collections

def reduce():
    lines = 0
    logs_mensuales = dict()

    lugar = {"monitorizar": 0,"redirigir": 1, "interno": 2, "externo": 3}
    tipo = {"externo": 0, "Cableada": 1, "Wifi": 2}

    for line in sys.stdin:
        lines += 1
        campos = line.split(";")
        anio = campos[0]
        mes = campos[1]
        dia = campos[2]
        hora = campos[3]
        sistema = campos[4]
        aplicacion =campos[5]
        ip0 = campos[6]
        ip1 = campos[7]
        ip2 = campos[8]
        ip3 = campos[9]
        valor = campos[10]
        clave_anio_mes = anio+mes
        if clave_anio_mes in valores:
            valores[clave_anio_mes] += int(valor)
        else:
            logs_mensuales[clave] = int(valor)
    print("Anio;Mes;Dia;Hora;Monitorizar;Redirigir;Interno;Externo;Externo;Cableada;Wifi")
    itemssalida = collections.OrderedDict(sorted(valores.items()))
    for indice in itemssalida:
        print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}".format(anio, indice[4:6], indice[6:8], indice[8:10], valores[indice][0], valores[indice][1], valores[indice][2], valores[indice][3],tipos[indice][0], tipos[indice][1], tipos[indice][2]))
    return lines


def main():
    val = reduce()
    if str(val).isdigit():
        print('Reduce procesadas ' + str(val) + ' líneas', file=sys.stderr)
    else:
        print('Error: brake:  ' + val , file=sys.stderr)
    return 0

if __name__ == '__main__':
    main()


def imprime_logs_mensuales():
    global
    for clave, valor in logs:
        print("Mes: %d: %d logs" % (clave, valor))