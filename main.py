from solver import solve
from visualKartu import visualisasiSolusi

if __name__=='__main__':
    a,b,c,d = [int(i) for i in input('Masukan 4 angka kartu : ').split(' ')]
    solusi = solve(a,b,c,d)
    visualisasiSolusi(solusi)