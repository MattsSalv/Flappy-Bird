
import pygame
import neat
import time
import os
import random
pygame.font.init()

#Dimensione delle finestra di gioco
WIN_WIDTH = 600             
WIN_HEIGHT = 800

#Nelle righe sottostanti vengono importante e ridemsnionate le immagini di gioco
BIRD_IMGS =  [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))  
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "bg.png")), (600, 900))

STAT_FONT = pygame.font.SysFont("comicsans", 50) #CAMBIARE FONT


#Creazione dell'uccellino
class Bird:                     
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25   #Valore massimo di rotazione (per non farlo mai andare a testa in giù)
    ROT_VEL = 20        #Velocità di rotazione dell'immagine dell'uccellino (quando sale/scende)
    ANIMATION_TIME = 5  #Ogni quanto cambia il frame e l'uccellino muove le ali

    def __init__(self, x, y):    #Inizializzazione dell'uccellino
        self.x = x  
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):             #Descrizione dei parametri di salto
        self.vel = -10.5    
        self.tick_count = 0
        self.height = self.y

    def move(self):             #Descrizione del movimento parabolico dell'uccellino, inclusa l'animazione di rotazione dell'immagine
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d 

        if d < 0 or self.y < self.height + 50:   
            if self.tilt < self.MAX_ROTATION:
                 self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL  

    def draw(self, win):                #Descrizione del battito di ali dell'uccellino
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)        
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):             #Associzione dell'immagine dell'uccellino alla maschera di collisione
        return pygame.mask.from_surface(self.img)    


#Creazione dei tubi
class Pipe:
    GAP = 200                      #Distanza costante tra un tubo ed il successivo   
    VEL = 5                        #Velocità costante di movimento del tubo

    def __init__(self, x):         #Inizializzazione del tubo
        self.x = x
        self.height = 0
        #self.gap = 100

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True) #Crea il tubo al contrario
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed=False
        self.set_height()

    def set_height(self):        #Gestisce l'altezza dei tubi
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):                #Descrive il movimento orizzontale regolare del tubo
        self.x -= self.VEL

    def draw(self, win):           #Disegno del tubo  
        win.blit(self.PIPE_TOP, (self.x, self.top))   
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom)) 

    def collide(self, bird):   #Le collisioni vengono gestite con le maschere della libreria pygame 
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)  
        bottom_mask =  pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))      
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        
        return False

    
#Creazione del terreno
class Base:
    VEL = 2.5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self,y):           #Inizializzazione del terreno
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):                 #Descrizione del movimento del terreno (coerente con il movimento dei tubi)
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH  

    def draw(self, win):           #Associazione dell'immagine all'elemento terreno
        win.blit(self.IMG, (self.x1, self.y))   
        win.blit(self.IMG, (self.x2, self.y))           

        
#Creazione della finestra complessiva di gioco
def draw_window(win, birds, pipes, base, score):

    win.blit(BG_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score " + str(score), 1, (255, 255, 255))   
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10)) 

    base.draw(win)    

    for bird in birds:
        bird.draw(win)

    pygame.display.update()


#Fitness function
def main(genomes, config):  

    nets = []
    ge = []
    birds = []

    #Creazione della rete neurale per ogni genoma
    for _, g in genomes:  
        g.fitness = 0 #Setto il valore del fitness di ogni genoma a 0
        net = neat.nn.FeedForwardNetwork.create(g, config) #creazione della rete neurale, passandogli il genoma e il file di configurazioned
        nets.append(net)
        birds.append(Bird(230, 350)) #creazione dell'uccellino relativo al genoma
        ge.append(g)



    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  #creazione della finestra di gioco
    clock = pygame.time.Clock()

    score = 0

    run = True          #Avvia il gioco

    while run:
            clock.tick(30) #Gestisce il framerate(rallenta il gioco)
            for event in pygame.event.get():  #Si occupa di gestire la chiusura della finestra di gioco
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            pipe_ind = 0
            if len(birds) > 0:
                if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width(): #RIGUARDARE
                    pipe_ind = 1
 
            else:   #Se non ho piu uccelli lascio il gioco
                run = False
                break  

            #Per ogni frame che l'uccellino avanza viene aumentato il fitness di 0.1
            for x, bird in enumerate(birds):
                bird.move()   
                ge[x].fitness += 0.1

                output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom))) #Attiviamo la rete neurale passandogli i valori(Ritorna un array)
                if output[0] > 0.5: #Posso mettere 0 perchè ho solo un neurone di uscita
                    bird.jump()



            base.move()
            add_pipe = False
            rem = []

            for pipe in pipes:

                pipe.move()

                for x,bird in enumerate(birds): #Gestisce le collisioni di ogni uccellino con i tubi, si occupa di rimuove gli uccellini che collidono
                    if pipe.collide(bird):
                        birds.pop(x)
                        nets.pop(x)
                        ge.pop(x)

                    if not pipe.passed and pipe.x < bird.x: #Controlla che se il singolo uccellino ha passato il tubo
                        pipe.passed = True    
                        add_pipe = True
            
                if pipe.x + pipe.PIPE_TOP.get_width() < 0: #Si occupa di rimuovere il tubo una volta che l'uccellino lo ha superato
                    rem.append(pipe)    

            if add_pipe:   #Se supera i tubi, il punteggio viene incrementato e il valore di fitness dell'uccellino viene incrementato di 5 
                score +=1
                for g in ge:
                pipes.append(Pipe(600)) #Aggiunge un nuovo pipe dopo che lo si è superato

            for r in rem:
                pipes.remove(r)

            for x, bird in enumerate(birds): #Controlla le collissioni del singolo uccellino con il suolo e che non vada oltre la parte superiore dello schermo
                if bird.y + bird.img.get_height() - 10 >= 730 or bird.y < -50:
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)    
                
            base.move()
            draw_window(win, birds, pipes, base, score) #Crea i vari oggetti sullo schermo   

def run(config_path):

    #Viene passato il path del file di configurazione e venogno settate le diverse proprietà
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    #Creazione della popolazione
    p = neat.Population(config) 

    #Opzionale: serve per visualizzare nella console le statistche
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    #configurazione della fitness function, 50 è il numero di volte che chiamerà la funzione main(numero massimo di generazioni)
    w = p.run(main,50)
    


if __name__ == "__main__":

    #Caricamento del file di configurazione

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)
