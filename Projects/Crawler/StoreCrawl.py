import csv
import sqlite3
import sys

def storeData(csvData: str):
    fromLinks = list()
    gottenLinks = list()

    rows = list()

    conn = sqlite3.connect('Crawler\StoredLinks.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "main"."Links"''')
    results = cursor.fetchall()

    alreadyStoredLinks = list()

    for row in results:
        alreadyStoredLinks.append(row[1])

    conn.commit()
    conn.close()

    if not csvData.endswith(".csv"):
        exit(-1)

    with open(csvData, newline='') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in csvReader:
            if len(row) != 0:
                rows.append(row)

    del rows[0]

    for z in range(len(rows)):
        string = rows[z][1]
        string_sem_aspas = string.strip('\"')
        lista = eval(string_sem_aspas)
        rows[z][1] = lista

    for z in range(len(rows)):
        if rows[z][0] in alreadyStoredLinks:
            rows[z][0] = rows[z][0]+"->canceled"
        for x in range(len(rows[z][1])):
            if rows[z][1][x] in alreadyStoredLinks:
                rows[z][1][x] = ''

    conn = sqlite3.connect('Crawler\StoredLinks.db')
    cursor = conn.cursor()

    for z in range(len(rows)):
        if not rows[z][0].endswith("->canceled"):
            cursor.execute('''INSERT INTO "main"."Links" ("LINK") VALUES (?)''', (rows[z][0],))
        else:
            rows[z][0] = rows[z][0][0:(len(rows[z][0])-10)]

        cursor.execute('SELECT "ID" FROM "main"."Links" WHERE "LINK" = ?', (rows[z][0],))

        last_id = cursor.fetchone()[0]
        
        for x in range(len(rows[z][1])):
            if rows[z][1][x] != '':
                cursor.execute('''INSERT INTO "main"."Links" ("LINK", "FROM") VALUES (?, ?)''', (rows[z][1][x], last_id,))

    results = cursor.fetchall()

    conn.commit()

    conn.close()