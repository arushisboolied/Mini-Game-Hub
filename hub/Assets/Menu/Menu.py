import pygame
import sys
from Level import Level


class Menu:
    def __init__(self,Resolution=(1280,720)):
        pygame.init()
        pygame.font.init()
        self.Resolution=Resolution
        self.character=0
        self.screen=pygame.display.set_mode(Resolution,pygame.RESIZABLE)
        self.clock=pygame.time.Clock()
        self.level=Level()
        

    def event_handler(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e and self.level.player.check_zones():
                self.level.settings_toggle()

    def run(self):
        running=True
        
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()
                else:
                    self.event_handler(event)

            self.screen.fill("black")
            self.level.run()
            #self.screen.blit(self.Menu_png,(0,0))
            pygame.display.update()
            

Menu().run()