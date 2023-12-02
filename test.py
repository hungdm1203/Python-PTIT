# # print("Hello world")
# # li=[2,4,7,5,7,8,9,3,7,2]
# # se=set(li)
# # print(se)
# # print(list(se))

# from itertools import groupby
# s=input()
# li=list(int(i) for i in s)
# gr=groupby(li)
# for i,j in gr:
#     print(f"({list(j)}, {i})",end=" ")
# number = 3.14159
# formatted_number = f"{number:.2f}"
# print(formatted_number)
# print(type(formatted_number))



# class User:
#     def __init__(self,first,last) -> None:
#         self.first=first
#         self.last=last

#     def describeUser(self):
#         return f"{self.first} {self.last}"
    
    
#     def greetUser(self):
#         print("hello User")

# class Admin(User):
#     def __init__(self, first, last, li) -> None:
#         super().__init__(first, last)
#         self.li=li
    
#     def toString(self):
#         print(f"{self.first} {self.last} {self.li}")
        


# admin=Admin("a","b",[1,2,3])
# admin.toString()







# class ThiSinh:
#     trangThai=""
#     def __init__(self,id,name, score,dt,kv) -> None:
#         self.id="TS{:02d}".format(id)
#         self.name=name
#         self.dt=dt
#         self.kv=kv
#         if dt=="Kinh":
#             if kv==1:
#                 self.score=score+1.5
#             elif kv==2:
#                 self.score=score+1
#             else: self.score=score
#         else:
#             if kv==1:
#                 self.score=score+1.5+1.5
#             elif kv==2:
#                 self.score=score+1+1.5
#             else: self.score=score+1.5

#         self.trangThai=self.setTrangThai()


#     def setTrangThai(self):
#         if(self.score<20.5):
#             return "Truot"
#         return "Do"
    
#     def __str__(self) -> str:
#         return f"{self.id} {self.name} {self.score} {self.trangThai}"
    
# n=int(input())
# ds=[]
# for i in range(1,n+1):
#     name=''
#     li=list(input().split())
#     name=" ".join(li)
#     name=name.title()

#     ts=ThiSinh(i,name,float(input()),input(),int(input()))
#     ds.append(ts)


# ds.sort(key=lambda i: i.id)
# ds.sort(key=lambda i: i.score,reverse=True)
# for i in ds:
#     print(i.__str__())


# n='4'
# print(int(n,16))

s="c06hc"
print(s[-2:])