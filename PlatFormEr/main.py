import pygame as g
import random as r

print('preparing graphics...')
g.init()
font = g.font.SysFont("cambria", 16)

size = (800, 400)
sw, sh = size

clock = g.time.Clock()
tic = 0

d='Goodbye.'

screen = g.display.set_mode(size)
g.display.set_caption('§-PLATFORMER-§')

pl = g.Rect(int(sw/5)+25, int(sh*(4/5))-10, 20, 20)

imgs = {
    70: 'Assets/plat1.png',
    100: 'Assets/plat2.png',
    130: 'Assets/plat3.png'
}

enemis = [
    'Assets/spike.png',
    'Assets/keeper.png',
    'Assets/bat0.png'
    ]

class enemy:
    def __init__(self, x, y, type):
        self.o = g.Rect(x, y, 20, 20)
        self.health = 10
        self.type = type

def GenLevel():
    global platz
    global END
    for i in range(1, r.randint(50, 80)):
        doi = r.choice([70, 100, 130])
        gx, gy = (platz[len(platz)-1].x, platz[len(platz)-1].y)
        gx += r.randint(-300, 300)
        gy += r.randint(-45, 15)
        platz.append(g.Rect(gx, gy, doi, 15))
        if r.randint(1, 8) == 1:
            if score >= 10: bo = 2
            else: bo = 1
            bois.append(enemy(gx+20, gy-20, r.randint(0, bo)))
    
    gx, gy = (platz[len(platz)-1].x, platz[len(platz)-1].y)
    END = g.Rect(gx+25, gy-10, 30, 30)


def gameover():
    global d
    global deaths
    global run
    global DEFENCE
    global DAMAGE
    global inventory
    
    d = 'GAME OVER!'
    deaths += 1
    run = False
    
    if len(inventory) > 0: inventory.remove(r.choice(inventory))
    DAMAGE = 1
    DEFENCE = 0
    
    tic = 0
    j = 1
    
    for i in range(50):
        for ev in g.event.get():
            if ev.type == g.QUIT:
                run = False
                game = False
    
    
        screen.fill((50, 50, 250))
        
        for pe in platz:
            g.draw.rect(screen, (50, 50, 50), pe)
            screen.blit(g.image.load(imgs.get(pe.width, 'Assets/nn.png')), (pe.x, pe.y))
        
        for boi in bois:
            g.draw.rect(screen, (10, 10, 255), boi.o)
            screen.blit(g.image.load(enemis[boi.type]), (boi.o.x, boi.o.y))
        
        screen.blit(g.image.load(f'Assets/Death/{round(j)}.png'), (pl.x, pl.y))
        
        g.draw.rect(screen, (20, 255, 0), END)
        
        
        
        screen.blit(dude, (10, 10))
        
        g.display.flip()
        clock.tick(60)
        tic += 1
        if j <= 10: j += 0.49

deaths = 0
score = 0

inventory = []

drops_1 = [
    'sword',
    'sword',
    'shield',
    'shield',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'bigger sword',
    'bigger sword',
    'small shield',
    'small shield',
    'small sword',
    'small sword',
    'small sword',
    'GrowUp drug',
    'GrowUp drug',
    'GrowUp drug',
    'dust',
    'dust',
    'dust',
    'dust',
    'dust',
    'dust'
]

drops_2 = [
    'sword',
    'sword',
    'shield',
    'shield',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'omg XD XD omg wtf XD!!!!11!!1!12 potion',
    'bigger sword',
    'GrowUp drug',
    'GrowUp drug',
    'GrowUp drug',
    'dust',
    'dust',
    'dust',
    'dust',
    'wing membrane'
]

def damage(danno):
    global health
    global DEFENCE
    global bam
    
    if danno - DEFENCE >= 0: health -= (danno - DEFENCE)
    bam = True

def use(tin):
    global DAMAGE
    global DEFENCE
    global score
    
    if tin == 'sword':
        DAMAGE = 5
    if tin == 'shield':
        DEFENCE = 5
    if tin == 'omg XD XD omg wtf XD!!!!11!!1!12 potion':
        score += r.randint(1, 5)
        inventory.remove(tin)
    if tin == 'bigger sword':
        DAMAGE = 10
    if tin == 'small shield':
        DEFENCE = 2
    if tin == 'small sword':
        DAMAGE = 2
    if tin == 'GrowUp drug':
        if r.randint(0, 1) == 0: DAMAGE += r.randint(1, 5)
        else: DEFENCE += r.randint(1, 5)
        inventory.remove(tin)
    
    
def inven():
    global inventory
    global run
    global game
    global DEFENCE
    global DAMAGE
    
    selected = 0
    x = 250
    
    gud = True
    while gud:
        for ev in g.event.get():
            if ev.type == g.QUIT:
                run = False
                game = False
                gud = False
                
            if ev.type == g.KEYDOWN:
                if ev.key == g.K_UP:
                    if selected == 0: selected = len(inventory)
                    selected -= 1
                if ev.key == g.K_DOWN:
                    selected += 1
                    if selected == len(inventory): selected = 0
                
                if ev.key == g.K_i or ev.key == g.K_e:
                    gud = False
                
                if ev.key == g.K_u:
                    use(inventory[selected])
                    #inventory.remove(inventory[selected])
                
                if ev.key == g.K_t:
                    inventory.remove(inventory[selected])
                    
        
        screen.fill((100, 100, 100))
        screen.blit(font.render(f'INVENTORY   ({len(inventory)}/17)', True, (80, 255, 80)), (200, 10))
        screen.blit(font.render('use i to close, use u to equip/apply selected item, use t to throw selected item', True, (80, 255, 80)), (200, 20))
        
        screen.blit(font.render('STATS', True, (80, 255, 80)), (50, 45))
        screen.blit(font.render(f'damage: {DAMAGE}', True, (80, 255, 80)), (50, 65))
        screen.blit(font.render(f'defence: {DEFENCE}', True, (80, 255, 80)), (50, 85))
        
        y = 50
        if len(inventory) > 1:
            for i in range(len(inventory)-1):
                if i == selected: bing = font.render(inventory[i], True, (80, 255, 80))
                else: bing = font.render(inventory[i], True, (10, 200, 10))
                screen.blit(bing, (x, y))
                y += 20
        else:
            for i in inventory:
                if inventory.index(i) == selected: bing = font.render(i, True, (80, 255, 80))
                else: bing = font.render(i, True, (10, 200, 10))
                screen.blit(bing, (x, y))
                y += 20
        
        g.display.flip()
        clock.tick(60)


health = 50
DAMAGE = 1
DEFENCE = 0

class button:
    def __init__(self, rect, name):
        self.rect = rect
        self.name = name

def do(ds):
    global jen
    global bigboi
    global musikin
    
    if ds == 'play':
        jen = False
    elif ds == 'controls':
        bigboi = g.image.load('Assets/howtoplay.png')
    elif ds == 'credits':
        bigboi = g.image.load('Assets/credits.png')
    elif ds == 'toggle music':
        if musikin:
            musikin = False
            g.mixer.music.stop()
        else:
            musikin = True
            g.mixer.music.load('Assets/soundz/back.mp3')
            g.mixer.music.play(-1)
        

jen = True
bigboi = ''
game = True

def TitleScreen():
    global bigboi
    global jen
    global game
    
    buttonz = [
        button(g.Rect(100, 100, 130, 30), 'play'),
        button(g.Rect(100, 140, 130, 30), 'controls'),
        button(g.Rect(100, 180, 130, 30), 'credits'),
        button(g.Rect(100, 220, 130, 30), 'toggle music')
    ]

    mousebop = g.Rect(12, 12, 12, 12)
    while jen:
        mousebop.x, mousebop.y = g.mouse.get_pos()
        for ev in g.event.get():
            if ev.type == g.QUIT:
                game = False
                run = False
                jen = False
                break
            
            if ev.type == g.KEYDOWN and ev.key == g.K_x: bigboi = ''
            
            if ev.type == g.KEYDOWN and ev.key == g.K_ESCAPE: do('start') 
                
            if ev.type == g.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    for boi in buttonz:
                        if boi.rect.colliderect(mousebop):
                            do(boi.name)
                            
                    
        
        screen.fill((50, 50, 50))
        
        for boi in buttonz:
            gu = font.render(boi.name, True, (50, 255, 50))
            g.draw.rect(screen, (100, 100, 100), boi.rect)
            screen.blit(gu, (boi.rect.x, boi.rect.y))
        
        try: screen.blit(bigboi, (0, 0))
        except: 1+1
        
        g.display.flip()
        clock.tick(60)

musikin = False
TitleScreen()
jen = True

while game:
    xspid = 0
    
    bois = []
    
    health = 50
    atking = False
    
    startplat = g.Rect(int(sw/5), int(sh*(4/5)), 70, 15)
    platz = []
    platz.append(startplat)
    END = ''

    xspid = 0
    direction = 1
       
    ground = True
    run = True
    GenLevel()
    y = 0

    biggin = True
    bam = False

    batf = 0
    bata = 0
    ing = 0
    
    SALTO = 60
    while run:
        dude = font.render(f'health: {health}                          score: {score}                                 deaths:{deaths}', True,  (80, 250, 80))
        
        if health <= 0: gameover()
        
        hep = health
        
        for ev in g.event.get():
            if ev.type == g.QUIT:
                run = False
                game = False
                
            if ev.type == g.KEYDOWN:
                if ev.key == g.K_ESCAPE:
                    TitleScreen()
                    jen = True
                
                if ev.key == g.K_RIGHT or ev.key == g.K_d:
                    xspid = 5
                    direction = 1
                if ev.key == g.K_LEFT or ev.key == g.K_a:
                    xspid = -5
                    direction = -1
                if ev.key == g.K_SPACE:
                    atking = True
                if ev.key == g.K_UP or ev.key == g.K_w:
                    if ground:
                        END.y += SALTO
                        for p in platz:
                            p.y += SALTO
                            y -= SALTO
                        for boi in bois:
                            boi.o.y += SALTO
                
            if ev.type == g.KEYUP:
                if ev.key == g.K_RIGHT or ev.key == g.K_d:
                    xspid = 0
                if ev.key == g.K_LEFT or ev.key == g.K_a:
                    xspid = 0
                 
                if ev.key == g.K_i or ev.key == g.K_e:
                    if biggin:
                        biggin = False
                        inven()
                    else: biggin = True
                
                if ev.key == g.K_SPACE:
                    atking = False
        
        ground = False
        END.x -= xspid
        for p in platz:
            p.x -= xspid
            if pl.colliderect(p):
                ground = True
        
        for boi in bois:
            boi.o.x -= xspid
            if boi.type == 2:
                if abs(boi.o.x - pl.x) <= 50:
                    if boi.o.x >= pl.x: boi.o.x -= 2
                    else: boi.o.x += 2
                    if boi.o.y >= pl.y: boi.o.y -= 2
                    else: boi.o.y += 2
                else:
                    if batf == 0:
                        boi.o.x += r.randint(-6, 6)
                        boi.o.y += r.randint(-6, 6)
                        batf = r.randint(2, 8)
                    else:
                        batf -= 1
                    
                    if bata == 0:
                        if ing == 1: ing = 0
                        else: ing += 1
                        enemis[2] = f'Assets/bat{ing}.png'
                        bata = 10
                    else:
                        bata -= 1
                        
                    
            if pl.colliderect(boi.o):
                if boi.type == 0:
                    damage(53)
                    break
                elif boi.type == 1:
                    if atking:
                        atking = False
                        boi.health -= DAMAGE
                        
                    else:
                        damage(r.randint(1, 2))
                        break
                elif boi.type == 2:
                    if atking:
                        atking = False
                        boi.health -= DAMAGE
                        
                    else:
                        damage(r.randint(1, 4))
                        break
                    boi.o.x += r.randint(-20, 20)
                    boi.o.y += r.randint(-10, 10)
            
            
            
            if boi.health <= 0:
                if len(inventory) < 17: exec(f'inventory.append(r.choice(drops_{boi.type}))')
                bois.remove(boi)              
            
        if not ground:
            END.y -= 1
            for p in platz:
                p.y -= 1
                y += 1
            for boi in bois:
                boi.o.y -= 1
        
        if bam:
            fof = r.choice([-15, 15])
            for boi in bois:
                boi.o.x += fof
            for pe in platz:
                pe.x += fof
            END.x += fof
            bam = False
            xspid = 0
        
        #win/loose
        if y >= sh:
            gameover()
        
        if pl.colliderect(END):
            d = 'You Win!'
            score += 1
            run = False
        
        
        screen.fill((50, 50, 250))
        
        for pe in platz:
            g.draw.rect(screen, (50, 50, 50), pe)
            screen.blit(g.image.load(imgs.get(pe.width, 'Assets/nn.png')), (pe.x, pe.y))
        
        for boi in bois:
            screen.blit(g.image.load(enemis[boi.type]), (boi.o.x, boi.o.y))
        
        #g.draw.rect(screen, (20, 255, 0), END)
        screen.blit(g.image.load('Assets/end.png'), (END.x, END.y))
        screen.blit(g.image.load(f'Assets/pl{direction}.png'), (pl.x, pl.y))
        
        if hep != health: g.draw.rect(screen, (255, 10, 10), pl)
        
        screen.blit(dude, (10, 10))
        
        g.display.flip()
        clock.tick(60)
        tic += 1

    print(f'+===========+\n {d}\n+===========+')

    if d != 'Goodbye': print('next level!')
    
    
    