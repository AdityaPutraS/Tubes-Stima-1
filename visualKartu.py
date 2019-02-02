import pyglet
import random
from util import lerp
# Variable koordinat & ukuran
w, h = 1000, 800


window = pyglet.window.Window(w, h, visible=False)

batch = pyglet.graphics.Batch()

spriteKartu = []
namaKartu = ['As'] + [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King']
tipeKartu = ['Hati', 'Keriting', 'Sekop', 'Wajik']

solusi = []
angka = []

label = []


def loadKartu(a, b, c, d):
    temp = {}
    global spriteKartu, batch, angka
    spriteKartu = []
    angka = [a, b, c, d]
    for k in angka:
        tipeRandom = random.choice(tipeKartu)
        nama = namaKartu[k-1] + ' ' + tipeRandom
        while(nama in temp):
            tipeRandom = random.choice(tipeKartu)
            nama = namaKartu[k] + tipeRandom
        pathKartu = 'static/img/kartu/' + nama + '.png'
        gambar = pyglet.image.load(pathKartu)
        gambar.anchor_x = gambar.width//2
        gambar.anchor_y = gambar.height//2
        spriteKartu.append(pyglet.sprite.Sprite(img=gambar))
    dx, dy = 0, 0
    for s in spriteKartu:
        s.update(x=s.image.anchor_x+dx, y=h-s.image.anchor_y-dy+50, scale=0.5)
        dx += 5
        dy += 5


durasiAnim1 = 1.5
fps = 60
noAnim = 1
t = 0


@window.event
def on_draw():
    global spriteKartu, label
    window.clear()
    for s in spriteKartu:
        s.draw()
    for l in label:
        l.draw()


def anim(dt):
    global spriteKartu, t, label, noAnim
    # if(noAnim == 1):
    #     done = True
    #     for i in range(4):
    #         if(t < durasiAnim1*fps):
    #             done = False
    #             xLama, yLama = spriteKartu[i].x, spriteKartu[i].y
    #             xBaru, yBaru = w/5 * (i+1), h/2
    #             spriteKartu[i].update(x=lerp(t,xLama,xBaru-xLama,durasiAnim1*fps),y=lerp(t,yLama,yBaru-yLama,durasiAnim1*fps))
    #             t += 1
    #     if(done):
    #         noAnim = 2
    # elif(noAnim == 2):
    #     label = []
    #     for i in range(4):
    #         ang = angka[i]
    #         label.append(pyglet.text.Label(str(ang),
    #                                 font_name='Times New Roman',
    #                                 font_size=36,
    #                                 x=w/5 * (i+1), y=h/2 - 100,
    #                                 anchor_x='center', anchor_y='center'))
    #     noAnim = 3
    for i in range(4):
        if(noAnim == (i+1)):
            if(t < durasiAnim1*fps):
                xLama, yLama = spriteKartu[i].x, spriteKartu[i].y
                xBaru, yBaru = w/5 * (i+1), h/2+100
                spriteKartu[i].update(
                        x=lerp(t, xLama, xBaru-xLama, durasiAnim1*fps), 
                        y=lerp(t, yLama, yBaru-yLama, durasiAnim1*fps))
                t += 1
            if(t >= durasiAnim1*fps*1/2):
                label.append(pyglet.text.Label(str(angka[i]),
                                               font_name='Times New Roman',
                                               font_size=36,
                                               x=w/10 * 2*(i+1), y=h/2 - 100,
                                               anchor_x='center', anchor_y='center'))
                if(noAnim < 4):
                    label.append(pyglet.text.Label(str(solusi[i]),
                                                font_name='Times New Roman',
                                                font_size=36,
                                                x=w/10 * (2*(i+1)+1), y=h/2 - 100,
                                                anchor_x='center', anchor_y='center'))
                elif(noAnim == 4):
                    label.append(pyglet.text.Label('=',
                                                font_name='Times New Roman',
                                                font_size=36,
                                                x=w/10 * (2*(i+1)+1), y=h/2 - 100,
                                                anchor_x='center', anchor_y='center'))
                t = 0
                noAnim = i+2
    if(noAnim == 5):
        hasil = str(angka[0])+solusi[0]+str(angka[1])+solusi[1]+str(angka[2])+solusi[2]+str(angka[3])
        hasil = eval(hasil)
        label.append(pyglet.text.Label(str(hasil),
                                            font_name='Times New Roman',
                                            font_size=36,
                                            x=w/2, y=h/2 - 150,
                                            anchor_x='center', anchor_y='center'))


def visualisasiSolusi(arrSolusi):
    global solusi
    solusi = arrSolusi[1::2] #Operator solusi
    a,b,c,d = arrSolusi[::2] #Angka solusi
    loadKartu(a,b,c,d)
    window.set_visible()
    pyglet.clock.schedule_interval(anim, 1/fps)
    pyglet.app.run()
    
# if __name__ == '__main__':
#     loadKartu(13,2,1,6)
#     pyglet.clock.schedule_interval(anim, 1/fps)
#     pyglet.app.run()
