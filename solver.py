
""" INFORMASI :
Untuk semua cara solvingnya bisa ditulis disini, kalau ada cara solving lain
tinggal buat fungsi baru aja, kalau bisa tolong jelasin juga algoritma bagaimana
secara jelas supaya nanti gampang buat laporannya hehe...
"""

def score(solusi,pengaliTotal = 5, pengaliOperator = 1):
    plus = solusi.count('+')*5
    kurang = solusi.count('-')*4
    kali = solusi.count('*')*3
    bagi = solusi.count('/')*2
    kurung1 = solusi.count('(')
    kurung2 = solusi.count(')')
    if(kurung1 != kurung2):
        return -10000
    else:
        try:
            delta24 = abs(eval(solusi)-24)
        except ZeroDivisionError:
            delta24 = 10000000
        operator = plus+kurang+kali+bagi-kurung1
        return operator*pengaliOperator-delta24*pengaliTotal

def solve24(angka,exprStr = '%d%c%d%c%d%c%d', pengaliTotal = 5, pengaliOperator = 1):
    operator = ['+','+','+']
    arrSolusi = [0 for i in range(7)] 
    arrSolusi[::2] = [0,0,0,0]
    arrSolusi[1::2] = operator
    sisaInput = {}
    for a in angka:
        if(a in sisaInput):
            sisaInput[a] += 1
        else:
            sisaInput[a] = 1
    #Persiapan greedy
    pilihan = []
    availOperan = ['+','-','*','/']
    for a in angka:
        for op in availOperan:
            weight = 0
            value = 0
            pilihan.append([op,a,value,weight])
    #Greedy, Terinspirasi 1-0 Knapsack Greedy
    start = True
    idx = 0
    while(sum(sisaInput.values()) > 0):
        #Update value,weight
        for p in pilihan:
            tempArrSolusi = arrSolusi
            if(start):
                tempArrSolusi[idx] = p[1]
            else:
                tempArrSolusi[idx*2-1] = p[0]
                tempArrSolusi[idx*2] = p[1]
            solusi = exprStr % tuple(tempArrSolusi)
            p[2] = score(solusi,pengaliTotal=pengaliTotal,pengaliOperator=pengaliOperator)
            try:
                p[3] = abs(eval(solusi)-24)
            except ZeroDivisionError:
                p[3] = 10000000
            #Menghindari div by zero
            if(p[3] == 0):
                p[3] = 10**-10
        #Selesai update value,weight
        #Sort sesuai value/weight
        pilihan.sort(key = lambda wv : wv[2]/wv[3], reverse = True)
        #Ambil yang pertama kalo masih bisa diambil angkanya
        terpilih = pilihan[0]
        while(sisaInput[terpilih[1]] == 0):
            del pilihan[0]
            terpilih = pilihan[0]
        #Masuk ke solusi
        if(start):
            arrSolusi[idx] = terpilih[1]
        else:
            arrSolusi[idx*2-1] = terpilih[0]
            arrSolusi[idx*2] = terpilih[1]
        sisaInput[terpilih[1]] -= 1
        del pilihan[0]
        start = False
        idx += 1
    return arrSolusi


def solve(a,b,c,d, pengaliTotal = 5, pengaliOperator = 1):
    '''
    Menggunakkan algoritma greedy 1-0 knapsack
    Dengan tujuan memaksimalkan nilai dengan weight maksimal 24
    Algoritma bekerja dengan cara looping
    Tiap loop nilai weight dan value tiap pilihan solusi diupdate
    
    Pada awalnya semua kemungkinan (operan, angka) di generate dengan operan = [+,-,*,/] dan
    angka = angka input [a,b,c,d]

    Lalu , weight dari salah satu kemungkinan X akan diupdate dengan rumus
     Weight Baru = nilai Solusi jika X diambil

    Lalu, value dari salah satu kemungkinan X akan diupdate dengan rumus
     Value Baru = Skor dari operator * A - perbedaan solusi jika X diambil dengan 24 * B
     dimana A = pengali untuk Operator, B = pengali untuk nilai Total
     Sweet spot nya : A = 1, B = 5
     Jika diset A > B, maka algoritma akan menghasilkan persamaan dengan mementingkan skor
     dari operator terlebih dahulu

    NB : UNTUK SEMENTARA, ALGO INI TIDAK MEMBUAT PERSAMAAN YANG BERISI KURUNG
    '''
    solusi = ''
    total = 0
    sisaInput = {a : 0,b: 0,c:0,d:0}
    arrSolusi = []
    for x in [a,b,c,d]:
        sisaInput[x] += 1
    operan = ['+','-','*','/']
    nilai = [5,4,3,2]
    pilihan = []
    for x in [a,b,c,d]:
        for op in operan:
            weight = 0
            value = 0
            tup = [op,x,weight,value]
            pilihan.append(tup)
    #print(pilihan)
    #Simulasi penghitungan nilai dengan
    #Nilai = abs(24-total)*pengaliTotal + bonusOperan - banyakPasangKurung
    start = True
    while(sum(sisaInput.values()) > 0):
        #Update weight & value
        # print('===================')
        # print(pilihan)
        # print('===================')
        for p in pilihan:
            if(start):
                p[2] = p[1]
            else:
                p[2] = eval('%d%c%d' % (total,p[0],p[1]))
            p[3] = nilai[operan.index(p[0])]*pengaliOperator-abs(24-p[2])*pengaliTotal  - 0 #0 = banyakPasangKurung, ga pake kurung sekarang
            if(p[2] == 0):
                p[2] = (10**-10)
        if(start):
            start = False
        #Sort sesuai weight/value
        pilihan.sort(key = lambda wv : wv[3]/wv[2], reverse = True)
        # print('++++++++++++++++++++')
        # print(pilihan)
        # print('++++++++++++++++++++')
        # print('')
        #Ambil yang pertama kalo masih bisa diambil angkanya
        terpilih = pilihan[0]
        if(sisaInput[terpilih[1]] > 0):
            #Masuk ke solusi
            solusi += '%c%d' % (terpilih[0],terpilih[1])
            arrSolusi += [terpilih[0],terpilih[1]]
            total = terpilih[2]
            sisaInput[terpilih[1]] -= 1
        #Masuk/gamasuk, tetep di hapus
        # print(arrSolusi)
        # print('')
        # print('')
        del pilihan[0]
    print(solusi[1:],' = ',eval(solusi[1:]))
    return arrSolusi[1:]
