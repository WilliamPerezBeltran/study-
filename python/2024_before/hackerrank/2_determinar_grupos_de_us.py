# s: a string describing his path
# determinar cuantos grupos de Us mayores o iguales a 2 hay   

def countingValleys(s):
    rta = 0
    count = 0
    position = 0 
    first_time = True
    for x in range(len(s)):
        if s[x] == 'D':
            if first_time:
                position = x
                first_time = False
                count+=1
            else:
                if x - position == 1:
                    count+=1
                    if count>=2:
                        rta +=1 
                else:
                    first_time = True
        else:
            count = 0
            first_time = True
    return rta

def test(got,expeted):
    if got == expeted:
        pref='OK'
    else:
        pref='X'
    print(" {} got {}, expeted {}".format(pref, repr(got), repr(expeted)))      

def main():
    test(countingValleys('UDDDUDUU'),1)
    test(countingValleys('UDDDUDUUDDUDDDU'),3)
    test(countingValleys('DUDUDUDUDUDUDUDUDDDUDDDUDDDUDDDDD'),5)

if __name__=='__main__':
	main()

