mex1 = 'Hello!'
print(mex1)
print(type(mex1))

mex2 = "Welcome to Informatica"

print(mex1, mex2)

mex = mex1 + mex2
print(mex)

mex = mex1 + " " + mex2
print(mex)

n_corso = 13
mex = mex1 + ' ' + mex2 + 'corso n.' + str(n_corso)
print(mex)

mex = mex1*5
mex = mex1*n_corso
print(mex)

mex = (mex1+' ')*3
print(mex)
mex = (mex1+'\n')*3
print(mex)

print(len(mex))