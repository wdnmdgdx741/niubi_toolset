import requests

url = ["http://198.16.1.10:8007/ngobvt.txt", "http://198.16.1.10:8007/djphb/vzzekv.txt",
       "http://198.16.1.10:8007/dqgz/vucymx.txt", "http://198.16.1.10:8007/flfx/xlvcez.txt",
       "http://198.16.1.10:8007/gjgy/zprfad.txt", "http://198.16.1.10:8007/gzap/hnnuvn.txt",
       "http://198.16.1.10:8007/gzzd/seovln.txt", "http://198.16.1.10:8007/hsdt/icmyoc.txt",
       "http://198.16.1.10:8007/hswh/ciudfo.txt", "http://198.16.1.10:8007/hszt/qpphzi.txt",
       "http://198.16.1.10:8007/ldjh/ikkvbc.txt", "http://198.16.1.10:8007/qnfc/jaordm.txt",
       "http://198.16.1.10:8007/sxdj/imiobi.txt", "http://198.16.1.10:8007/txl/pmctmz.txt",
       "http://198.16.1.10:8007/xqgk/wcpaof.txt", "http://198.16.1.10:8007/xzzx/nzaegd.txt",
       "http://198.16.1.10:8007/yjyk/xnkpia.txt", "http://198.16.1.10:8007/zbxx/hguraw.txt",
       "http://198.16.1.10:8007/hacker.txt"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Referer": "http://198.16.1.10:8007/"
}

for i in url:
    resp = requests.delete(url=i, headers=headers)
    if resp.status_code == 200:
        print("ok")
    else:
        print(i)