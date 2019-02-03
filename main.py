from solver import solve24,score
#from visualKartu import visualisasiSolusi

#if __name__ == '__main__':
def main(angka, file=None):
    #angka = [int(i) for i in input('Masukan 4 angka kartu : ').split(' ')]
    ekspresi = []
    ekspresi.append('%d%c%d%c%d%c%d')
    ekspresi.append('((%d%c%d)%c%d)%c%d')
    ekspresi.append('(%d%c%d)%c(%d%c%d)')
    ekspresi.append('(%d%c(%d%c%d))%c%d')
    ekspresi.append('%d%c((%d%c%d)%c%d)')
    ekspresi.append('%d%c(%d%c(%d%c%d))')
    evalEkspresi = []
    for e in ekspresi:
        evalEkspresi.append([solve24(angka, exprStr=e),e])
    evalEkspresi.sort(key = lambda s : score(s[1]%tuple(s[0])),reverse=True)
    for e in evalEkspresi:
        sol = e[1] % tuple(e[0])
        strTulis = sol + ' = ' + str(eval(sol)) + ' .Score = ' + str(score(sol)) + '\n'
        if(file==None):
            print(strTulis)
        else:
            file.write(strTulis)
    #visualisasiSolusi(solusi)

if __name__ == '__main__':
    fil = open('Data1.txt','w')
    for a in range(1,14):
        print(a)
        for b in range(1,14):
            for c in range(1,14):
                for d in range(1,14):
                    angka = [a,b,c,d]
                    fil.write('=========================\n')
                    main(angka,file=fil)
    fil.close()
    print('Done')
