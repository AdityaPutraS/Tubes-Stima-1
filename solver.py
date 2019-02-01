

""" INFORMASI :
Untuk semua cara solvingnya bisa ditulis disini, kalau ada cara solving lain
tinggal buat fungsi baru aja, kalau bisa tolong jelasin juga algoritma bagaimana
secara jelas supaya nanti gampang buat laporannya hehe...
"""

def solve(a,b,c,d, pengaliTotal = 5):
    #Menggunakkan algoritma greedy 1-0 knapsack
    #Dengan tujuan memaksimalkan nilai dengan weight maksimal 24
    solusi = ''
    total = 0
    sisaInput = {a : 0,b: 0,c:0,d:0}
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
    while(sum(sisaInput.values()) > 0):
        #Update weight & value
        for p in pilihan:
            p[2] = eval('%d%c%d' % (total,p[0],p[1]))
            p[3] = abs(24-p[2])*pengaliTotal + nilai[operan.index(p[0])] - 0 #0 = banyakPasangKurung, ga pake kurung sekarang
        #Sort sesuai weight/value
        pilihan.sort(key = lambda wv : wv[2]/wv[3], reverse = True)
        #Ambil yang pertama kalo masih bisa diambil angkanya
        terpilih = pilihan[0]
        if(sisaInput[terpilih[1]] > 0):
            #Masuk ke solusi
            solusi += '%c%d' % (terpilih[0],terpilih[1])
            total = terpilih[2]
            sisaInput[terpilih[1]] -= 1
        #Masuk/gamasuk, tetep di hapus
        del pilihan[0]
    print(solusi[1:],' = ',eval(solusi[1:]))
