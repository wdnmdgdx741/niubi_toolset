# coding: utf-8
import base64

a = 'wIDIgACIgACIgAyIK0wIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMiCNoQD'
b='jMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjMyIjoQDjACIgACIgACIggDM6EDM6AjMgAzMtMDMtEjM'
c='t0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0iCNMyIjMyIjMyIjMyI'
d='6AjMgAzMtMDMtEjMwIjO0eZ62ep5K0wKrQWYwVGdv5EItAiM1Aydl5mK6M6jlfpqnrQDt0SLt0SL'
e='t0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLt0SLK0AIdZavo75mlvlCNMTM6EDM'
f='z0yMw0SMyAjM6Q7lpb7lmrQDrsCZhBXZ09mTg0CIyUDI3VmbqozoPW+lqeuCN0SLt0SLt0SLt0SL'
g='sxWZld1V913e7d2ZhFGbsZmZg0lp9iunbW+Wg0lp9iunbW+Wg0lp9iunbW+WK0wMxoTMwoDMyACM'
h='DN0QDN0QDlWazNXMx0Wbf9lRGRDNDN0ard0Rf9VZl1WbwADIdRampDKilvFIdRampDKilvVKpM2Y'
i='==QIhM0QDN0Q'

a=a[::-1]
b=b[::-1]
c=c[::-1]
d=d[::-1]
e=e[::-1]
f=f[::-1]
g=g[::-1]
h=h[::-1]
i=i[::-1]
s = (a+b+c+d+e+f+g+h+i)

with open("1.txt","wb")as f:
    f.write(base64.b64decode(s))