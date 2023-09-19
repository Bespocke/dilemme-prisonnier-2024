def cian(i,moi,lui,elle,memoire):
    if i==0 :
        memoire.append(0)
        return 1
    if lui[i-1]==1 and elle[i-1]==1 :
        return 1
    if lui[i-1]+elle[i-1]==1  :
        memoire[0]+=1
        if memoire[0]%3!=0 :
            return 1
        else :
            return 0

    else :
        return 0

def pasnils(i,moi,lui,elle,memoire):
    if i==0 :
        return 1
    if lui[i-1]==1 and elle[i-1]==1 :
        return 1
    else:
        return 0

def nilsnonplus(i,moi,lui,elle,memoire):
    if i==0 :
        return 1
    if lui[i-1]+elle[i-1]>0  :
        return 1
    else :
        return 0

def avare(i,moi,lui,elle,memoire):
    if i==0:
        return 1
    if i==1:
        return 1
    if lui[i-1]+elle[i-1]==2 :
        if lui[i-2]+elle[i-2]>0 :
            return 0
        else:
            return 1

    if lui[i-1]+elle[i-1]==1 :
        return rd.randint(0,1)
    if lui[i-1]+elle[i-1]==0 :
        return 0
