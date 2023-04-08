import pygame as pg

pg.init()

pg.display.set_caption("music")

pg.mixer.init()

WIDTH = 320
HEIGHT = 200
FPS = 60

playlist = ["./music/Story Of My Life (Sefon.me).mp3", "./music/John Legend - All Of Me (dizer.net).mp3"]
i = 0

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

background = pg.image.load("./images/mp3.jpeg")


pg.mixer.music.load(playlist[i])
pg.mixer.music.play(1)

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pg.mixer.music.pause()
            if event.key == pg.K_a:
                pg.mixer.music.unpause()
            if event.key == pg.K_RIGHT:
                pg.mixer.music.stop()
                i += 1
                if i >= len(playlist):
                    i = 0
                pg.mixer.music.load(playlist[i])
                pg.mixer.music.play(1)

            if event.key == pg.K_LEFT: 
                pg.mixer.music.stop()
                i -= 1
                pg.mixer.music.load(playlist[i])
                pg.mixer.music.play(1)


    screen.blit(background, (0,0))
    pg.display.flip()

pg.quit()