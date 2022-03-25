import sys,pygame

class BallGame:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("李雨佳好可爱")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit

            pygame.display.flip

if __name__=='_main_':
    ballGame=BallGame()
    ballGame.run_game