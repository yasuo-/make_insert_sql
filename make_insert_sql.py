# coding: utf-8

import csv
import sys

SQL_FILE = "data.sql"

def get_insert_sql(data):
    print(type(data))
    return "INSERT INTO table_name (id, text1, text2) " \
            "VALUES ({0}, {1}, {2});\n".format(*data)

def main():
    data_file = sys.argv[1]
    with open(data_file, "rt") as fr, open(SQL_FILE, "w") as fw:
        for data in csv.reader(fr):
            fw.write(get_insert_sql(data))


if __name__ == '__main__':
    main()