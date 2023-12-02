# tim tu thuan nghich dai nhat
import collections

def check(s):
    if s==s[::-1]: return True
    return False

class Word:
    def __init__(self,w,vl,id) -> None:
        self.w=w
        self.vl=vl
        self.id=id
        self.l=len(w)

    def __str__(self) -> str:
        return f"{self.w} {self.vl}"

ip=open("VANBAN.in",'r')
word=ip.read().split()
res=collections.Counter(word).most_common()
a=[]
for i in res:
    if check(i[0]): a.append(Word(i[0],i[1],word.index(i[0])))

a.sort(key=lambda i:(-i.l,i.id))
for i in a:
    if i.l==a[0].l: print(i)
    else: break

