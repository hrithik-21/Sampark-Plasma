import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size
f=os.listdir("static/img")
ff="static/img/"+str(f[0])
print(getSize(ff))