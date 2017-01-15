#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import argparse
import sys


def check_params():
    parser = argparse.ArgumentParser(description='Process bank files \
            and report stadistical information.')
    parser.add_argument('year', metavar='N', type=int, nargs='*',
                        help='Four digits for the year of log file')
    params = parser.parse_args()
    return params.year[0]


def map(year):
    lines = 0
    error = 0
    meses = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12" }
    dias = {" 1": "01", " 2": "02", " 3": "03", " 4": "04", " 5": "05", " 6": "06", " 7": "07", " 8": "08",
            " 9": "09", "10": "10", "11": "11", "12": "12", "13": "13", "14": "14",
            "15": "15", "16": "16", "17": "17", "18": "18", "19": "19", "20": "20", "21": "21", "22": "22", "23": "23",
            "24": "24", "25": "25", "26": "26", "27": "27", "28": "28", "29": "29", "30": "30", "31": "31"}
    horas = {"00": "00", "01": "01", "02": "02", "03": "03", "04": "04", "05": "05", "06": "06", "07": "07", "08": "08",
             "09": "09", "10": "10", "11": "11", "12": "12", "13": "13", "14": "14",
             "15": "15", "16": "16", "17": "17", "18": "18", "19": "19", "20": "20", "21": "21", "22": "22", "23": "23"}

    for line in sys.stdin:
        lines += 1
        mes = meses.get(line[0:3], "Error")
        dia = dias.get(line[4:6], "Error")
        hora = horas.get(line[7:9], "Error")
        if mes == "Error":
            error += 1
            return ("Error mes" + line)
        if dia == "Error":
            error += 1
            return ("Error dia " + line)
        if hora == "Error":
            error += 1
            return ("Error hora " + line)

        campos = line.split()
        server = campos[3]
        aplicacion = campos[4]
        ip = campos[5].split(".")

        if len(ip) == 1:
            cadena_ip = ip[0] + ";0;0;0"
        elif len(ip) == 2:
            cadena_ip = ip[0] + ";" + ip[1] + ";0;0"
        elif len(ip) == 3:
            cadena_ip = ip[0] + ";" + ip[1] + ";" + ip[2] + ";0"
        else:
            cadena_ip = ip[0] + ";" + ip[1] + ";" + ip[2] + ";" + ip[3]

        print("{0};{1};{2};{3};{4};{5};{6};1".format(year, mes, dia, hora, server, aplicacion, cadena_ip))
    return lines


def main():
    val = map(check_params())
    if str(val).isdigit():
        print('Map procesadas ' + str(val) + ' líneas', file=sys.stderr)
    else:
        print('Error: brake:  ' + val, file=sys.stderr)
    return 0


if __name__ == '__main__':
    main()
