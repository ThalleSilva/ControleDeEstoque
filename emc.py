from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import Error
from openpyxl import Workbook
import os



banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="emc"
)

def abrir_adicionar():
    tela_adicionar.show()

def abrir_excluir():
    tela_excluir.show()

def abrir_pers():
    tela_consultaP.show()





def consulta_personalizada():
    tela_resulP.show()
    setor = tela_consultaP.comboBox.currentText()
    info = tela_consultaP.comboBox_2.currentText()
    modelo = tela_consultaP.comboBox_3.currentText()
    
    if setor == "Setor 1" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 1" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 1" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                    FROM controle
                    WHERE setor = 'Setor 1' AND tipo IN ('Monitor', 'Computador')
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 1' AND tipo = 'Monitor'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 1' AND tipo = 'Computador'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 1'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 1' AND tipo = 'Monitor'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 1' AND tipo = 'Computador'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 1" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 1'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))















    if setor == "Setor 2" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 2" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 2" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                    FROM controle
                    WHERE setor = 'Setor 2' AND tipo IN ('Monitor', 'Computador')
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 2' AND tipo = 'Monitor'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 2' AND tipo = 'Computador'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                    FROM controle
                    WHERE setor = 'Setor 2'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 2' AND tipo = 'Monitor'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 2' AND tipo = 'Computador'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 2" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                    FROM controle
                    WHERE setor = 'Setor 2'
                    GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))















    if setor == "Setor 3" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 3" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 3" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                        FROM controle
                        WHERE setor = 'Setor 3' AND tipo IN ('Monitor', 'Computador')
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 3' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 3' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 3'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 3' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 3' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 3" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 3'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))





        




    if setor == "Setor 4" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 4" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 4" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                        FROM controle
                        WHERE setor = 'Setor 4' AND tipo IN ('Monitor', 'Computador')
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 4' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 4' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 4'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 4' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 4' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 4" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 4'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))










    if setor == "Setor 5" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 5" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 5" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                        FROM controle
                        WHERE setor = 'Setor 5' AND tipo IN ('Monitor', 'Computador')
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 5' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 5' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 5'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 5' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 5' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 5" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 5'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))












    if setor == "Setor 6" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 6" AND tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE setor = "Setor 6" AND tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                        FROM controle
                        WHERE setor = 'Setor 6' AND tipo IN ('Monitor', 'Computador')
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 6' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 6' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE setor = 'Setor 6'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 6' AND tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 6' AND tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 6" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE setor = 'Setor 6'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



        







    if setor == "Setor 7" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 7" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 7" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 7' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 7' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 7' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 7'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 7' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 7' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 7" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 7'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))















    if setor == "Setor 8" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 8" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 8" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 8' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 8' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 8' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 8'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 8' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 8' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 8" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 8'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
















    if setor == "Setor 9" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 9" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 9" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 9' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 9' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 9' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 9'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 9' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 9' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 9" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 9'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))








        








    if setor == "Setor 10" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 10" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 10" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 10' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 10' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 10' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 10'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 10' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 10' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 10" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 10'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

















    if setor == "Setor 11" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 11" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 11" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 11' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 11' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 11' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 11'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 11' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 11' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 11" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 11'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))















    if setor == "Setor 12" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 12" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 12" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 12' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 12' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 12' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 12'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 12' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 12' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 12" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 12'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))















    if setor == "Setor 13" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 13" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 13" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 13' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 13' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 13' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 13'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 13' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 13' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 13" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 13'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))











    if setor == "Setor 14" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 14" AND tipo = "Monitor"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                          FROM controle
                          WHERE setor = "Setor 14" AND tipo = "Computador"
                          GROUP BY setor;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                       FROM controle
                       WHERE setor = 'Setor 14' AND tipo IN ('Monitor', 'Computador')
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 14' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 14' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                       FROM controle
                       WHERE setor = 'Setor 14'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 14' AND tipo = 'Monitor'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 14' AND tipo = 'Computador'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Setor 14" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                       FROM controle
                       WHERE setor = 'Setor 14'
                       GROUP BY setor, tipo;
                       """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))











    if setor == "Todos" and info == "Valor" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE tipo = "Monitor"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Valor" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, sum(valor) AS total_valor
                        FROM controle
                        WHERE tipo = "Computador"
                        GROUP BY setor;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Valor" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, SUM(valor) AS total_valor
                        FROM controle
                        WHERE tipo IN ('Monitor', 'Computador')
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        WHERE tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) Quantidade
                        FROM controle
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(3)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade'])

        for i in range(len(dados_lidos)):
            for j in range(3):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Valor e Quantidade" and modelo == "Monitor":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE tipo = 'Monitor'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Valor e Quantidade" and modelo == "Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        WHERE tipo = 'Computador'
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    if setor == "Todos" and info == "Valor e Quantidade" and modelo == "Monitor e Computador":
        cursor = banco.cursor()
        cursor.execute("""SELECT setor, tipo, count(tipo) 'Quantidade', sum(valor) 'Valor Total'
                        FROM controle
                        GROUP BY setor, tipo;
                    """)
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_resulP.tableWidget.setRowCount(len(dados_lidos))
        tela_resulP.tableWidget.setColumnCount(4)

        tela_resulP.tableWidget.setHorizontalHeaderLabels(['Setor', 'Tipo', 'Quantidade', 'Valor Total'])

        for i in range(len(dados_lidos)):
            for j in range(4):
                tela_resulP.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))






















def abrir_auditoria():
    tela_auditoria.show()
    
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM auditoria")
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_auditoria.tableWidget.setRowCount(len(dados_lidos))
        tela_auditoria.tableWidget.setColumnCount(6)

        for i in range(len(dados_lidos)):
            for j in range(6):
                tela_auditoria.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except Error as e:
        print("Erro ao carregar dados:", e)

def gerar_excel():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM controle"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.title = "Produtos Cadastrados"

    ws.append(["ID", "CÓDIGO", "PRODUTO", "TIPO", "SETOR", "DATA", "VALOR"])

    for linha in dados_lidos:
        ws.append(linha)

    
    caminho_arquivo = os.path.join(os.path.expanduser("~"), "Desktop", "Relatorio_EMC.xlsx")
    wb.save(caminho_arquivo)
    print("Excel FOI GERADO COM SUCESSO na Área de Trabalho!")
    tela_aviso.show()

def abrir_produtos():
    tela_produtos.show()
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM controle")
        dados_lidos = cursor.fetchall()
        cursor.close()

        tela_produtos.tableWidget.setRowCount(len(dados_lidos))
        tela_produtos.tableWidget.setColumnCount(7)

        for i in range(len(dados_lidos)):
            for j in range(7):
                tela_produtos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except Error as e:
        print("Erro ao carregar dados:", e)

def cadastrar():
    tela_adicionar.label.setText("") 
    codigo = tela_adicionar.lineEdit.text()
    tipo = tela_adicionar.lineEdit_2.text()
    setor = tela_adicionar.lineEdit_3.text()
    modelo = tela_adicionar.lineEdit_4.text()
    data = tela_adicionar.lineEdit_5.text()
    valor = tela_adicionar.lineEdit_6.text()
    
    print(codigo, tipo, setor, modelo, data, valor)

    try:
        codigo = int(codigo)
        valor = float(valor)  

        cursor = banco.cursor()
        insert = "INSERT INTO controle (emc_num, descricao, tipo, setor, data_alocacao, valor) VALUES (%s, %s, %s, %s, %s, %s)"
        dados = (codigo, modelo, tipo, setor, data, valor)
        
        cursor.execute(insert, dados)
        banco.commit()
        cursor.close()
        tela_adicionar.label.setText("Cadastrado com sucesso!") 

    except Error as e:
        print("Erro ao inserir dados:", e)
        tela_adicionar.label.setText("Erro ao inserir dados.") 

def excluir():
    codigoExcluir = tela_excluir.lineEdit.text()

    try:    
        cursor = banco.cursor()

        codigoExcluir = int(codigoExcluir)
        delete = "DELETE FROM controle WHERE emc_num = %s;"
        dados = (codigoExcluir,)
        cursor.execute(delete, dados)
        banco.commit()
        cursor.close()  

        tela_excluir.label.setText("Produto excluído com sucesso!") 

    except Error as e:
        print("Erro ao excluir dados:", e)
        tela_excluir.label.setText("Erro ao excluir dados.") 

app = QtWidgets.QApplication([])
tela_inicial = uic.loadUi("tela_inicial.ui")
tela_adicionar = uic.loadUi("adicionar.ui")
tela_excluir = uic.loadUi("excluir.ui")
tela_produtos = uic.loadUi("produtos.ui")
tela_auditoria = uic.loadUi("auditoria.ui")
tela_aviso = uic.loadUi("aviso.ui")
tela_consultaP = uic.loadUi("consultaPers.ui")
tela_resulP = uic.loadUi("resul_pers.ui")


tela_produtos.pushButton.clicked.connect(abrir_pers)
tela_inicial.pushButton_2.clicked.connect(abrir_auditoria)  
tela_inicial.pushButton_3.clicked.connect(gerar_excel)  
tela_inicial.pushButton_4.clicked.connect(abrir_adicionar)
tela_inicial.pushButton_5.clicked.connect(abrir_excluir)
tela_inicial.pushButton.clicked.connect(abrir_produtos)
tela_adicionar.pushButton.clicked.connect(cadastrar)
tela_excluir.pushButton.clicked.connect(excluir)
tela_consultaP.pushButton.clicked.connect(consulta_personalizada)

tela_inicial.show()
app.exec()
