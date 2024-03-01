import pygame
import random
#Colors
BLACK = (0,0,0)
WHITE=(255,255,255)
OFFWHITE=(250,250,250)
RED=(191, 48, 70)
BLUE = (52, 128, 235)
GRAY=(128,128,128)
YELLOW=(255,255,0)
PINK=(255,22,148)

#global variables
global winner
global RedTeamCounter
global BlueTeamCounter
global InnocentCounter
global AssassinTrigger
global windowx
global windowy

#Global Variables
winner="BLACK"
RedTeamCounter=0
BlueTeamCounter=0
InnocentCounter=0
AssassinTrigger=False

pygame.init()

#Dimensions
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
windowx=screen.get_width()
windowy=screen.get_height()
#Window Size
print("X: "+str(windowx)+" Y: "+str(windowy))

#List Initialisation
buttonOrder=[]
redlog=[]
bluelog=[]

#Button Parameters
buttonspacex=buttonsizex=windowx//7
buttonspacey=buttonsizey=windowy//9
buttonindentx=(windowx-(buttonsizex*5))/2
buttonindenty=(windowy-(buttonsizey*7))/2
fontStyle="Ariel"
fontSize=buttonsizey//2
fontsize2=buttonsizey
cluefontsize=fontsize2
font=pygame.font.SysFont(fontStyle, fontSize)
cluefont=pygame.font.SysFont(fontStyle, cluefontsize)

screencolor=BLACK
filebank=open("CodeNames.txt","r")
wordbanktemp=[line.strip() for line in filebank]
filebank.close()
wordbank=[]

while len(wordbank)<25:
    word=random.choice(wordbanktemp)
    if word not in wordbank:
        wordbank.append(word)

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color=color
        self.basecolor=GRAY
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.animation=0
        self.increase=False
        self.clicked=False

    def ButtonClick(self):

        if self.clicked==False:
            self.clicked=True
            self.basecolor=self.color
            self.increase=True
            return True
        else:
            return False

    def draw(self,screen,outline=True):
        if self.increase:
            self.animation+=0.5

        if self.animation>=self.height:
            self.animation=self.height

        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(screen, self.basecolor, (self.x,self.y,self.width,self.height),0)
        pygame.draw.rect(screen, GRAY, (self.x,self.y,self.width,self.height-self.animation),0)


        if self.text!='':
            pygame.font.init()
            text=font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x+(self.width/2-text.get_width()/2), self.y+(self.height/2-text.get_height()/2)))


    
    def buttonend(self):
        pygame.draw.rect(screen, self.basecolor, (self.x,self.y,self.width,self.height),0)

    def getcolor(self):
        return self.color
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
    def getwidth(self):
        return self.width
    
    def getheight(self):
        return self.height

    def gettext(self):
        return self.text

    def getcolor(self):
        return self.color

class PrivateButton():
    def __init__(self, color, x,y,width,height,team, text='',):
        self.color=color
        self.basecolor=GRAY
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.animation=0
        self.increase=False
        self.leftx=x
        self.lefty=y
        self.rightx=width
        self.righty=height
        self.clickteam=team
    def draw(self,screen,outline=True):
        if self.increase:
            self.animation+=0.5

        if self.animation>=self.height:
            self.animation=self.height

        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(screen, self.basecolor, (self.x,self.y,self.width,self.height),0)
        pygame.draw.rect(screen, GRAY, (self.x,self.y,self.width,self.height-self.animation),0)


        if self.text!='':
            pygame.font.init()
            text=font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x+(self.width/2-text.get_width()/2), self.y+(self.height/2-text.get_height()/2)))


    
    def endscreen(self):
            global windowx
            global windowy
            global fontsize2
            x_max=windowx
            x_min=0
            y_max=windowy
            y_min=0
            proportionscaler=1
            fontcolor=self.color

            if self.leftx>x_min:
                # self.leftx+=-(self.leftx-x_min)/proportionscaler
                self.leftx+=-proportionscaler
            else:
                self.leftx=0
            if self.rightx<x_max:
                # self.rightx+=(x_max-self.rightx)/proportionscaler
                self.rightx+=proportionscaler*2
            else:
                self.rightx=windowx
            if self.lefty>y_min:
                # self.lefty+=-(self.lefty-y_min)/proportionscaler
                self.lefty+=-proportionscaler
            else:
                self.lefty=0
            if self.righty<y_max:
                # self.righty+=(y_max-self.righty)/proportionscaler
                self.righty+=proportionscaler*2
            else:
                self.righty=windowy

            # if self.leftx-x_min<10:
            #     self.leftx=x_min
            # if x_max-self.rightx<10:
            #     self.rightx=x_max
            # if self.lefty-y_min<10:
            #     self.lefty=y_min
            # if y_max-self.righty<10:
            #     self.righty=y_max


            #round all values to the nearest integer


            pygame.draw.rect(screen, BLACK, (self.leftx,self.lefty,self.rightx,self.righty),0)          


            if self.leftx==x_min and self.rightx==x_max and self.lefty==y_min and self.righty==y_max:

                if self.color==RED:
                    winner="RED"
                elif self.color==BLUE:
                    winner="BLUE"
                elif self.color==YELLOW:
                    winner=self.clickteam
                else:
                    winner="BYSTANDERS L"



                font3=pygame.font.SysFont("Arial", fontsize2*2)
                font2=pygame.font.SysFont("Arial", fontsize2)
                text=font3.render(winner+" WINS!", 1,fontcolor)
                
                screen.blit(text, (windowx/2-text.get_width()/2, windowy/4-text.get_height()/2))
                score=font2.render("Score:", 1, fontcolor)
                screen.blit(score, (windowx/2-score.get_width()/2, windowy*5/8-score.get_height()/2))

                scoretext=font2.render("Red: "+str(RedTeamCounter)+" Blue: "+str(BlueTeamCounter), 1, fontcolor)
                screen.blit(scoretext, (windowx/2-scoretext.get_width()/2, windowy*3/4-scoretext.get_height()/2))

def generateSpyMasterBoard():

    spymasterscreen=pygame.display.set_mode((windowx, windowy))
    spymasterscreen.fill(WHITE)
    
    pygame.display.flip()
    colorlist=[YELLOW,RED,RED,RED,RED,RED,RED,RED,RED,RED,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,BLUE,
               BLUE,BLUE,OFFWHITE,OFFWHITE,OFFWHITE,OFFWHITE,OFFWHITE,OFFWHITE]
    
    #draw a 5x5 grid of colored squares
    for i in range(5):
        for j in range(5):
            squarecolor=random.choice(colorlist)
            buttonOrder.append(squarecolor)
            colorlist.remove(squarecolor)
            pygame.draw.rect(spymasterscreen, squarecolor, (i*buttonspacex+buttonindentx,j*buttonspacey+buttonindenty,buttonsizex,buttonsizey),0)
            pygame.draw.rect(spymasterscreen, BLACK, (i*buttonspacex+buttonindentx,j*buttonspacey+buttonindenty,buttonsizex,buttonsizey),1)
            spymasterscreen.blit(font.render(wordbank[i*5+j], 1, BLACK), (i*buttonspacex+buttonindentx+(buttonsizex/2-font.render(wordbank[i*5+j], 1, BLACK).get_width()/2), 
                                                                          j*buttonspacey+buttonindenty+(buttonsizey/2-font.render(wordbank[i*5+j], 1, BLACK).get_height()/2)))
    pygame.display.flip()

def GameStats(RedTeamCounter, BlueTeamCounter, InnocentCounter, AssassinTrigger):
    print("Red: "+str(RedTeamCounter))
    print("Blue: "+str(BlueTeamCounter))
    print("Innocent: "+str(InnocentCounter))
    print("Assassin: "+str(AssassinTrigger))

def codenamesGame(buttonOrder):
    buttonlist=[]
    global RedTeamCounter
    global BlueTeamCounter
    global InnocentCounter
    global AssassinTrigger
    global cluefont
    done=False
    endtrigger=False
    cluetext=""

    for i in range(5):
        for j in range(5):
            buttonlist.append(Button(buttonOrder[i*5+j], i*buttonspacex+buttonindentx, j*buttonspacey+buttonindenty, buttonsizex, buttonsizey, wordbank[i*5+j]))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
                if event.key == pygame.K_BACKSPACE:
                    cluetext=cluetext[:-1]
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    cluetext+=chr(event.key).upper()
                if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    cluetext+=chr(event.key)
                if event.key == pygame.K_SPACE:
                    cluetext+=" "
                if event.key == pygame.K_RETURN:
                    cluetext=""
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                click=pygame.mouse.get_pressed()

                if click[0]==1:
                    #left
                    print("Left click:RED")
                    clickteam="BLUE"
                if click[2]==1:
                    #right
                    print("Right click:BLUE")
                    clickteam="RED"

                for button in buttonlist:
                    if button.x<mouse[0]<button.x+button.width and button.y<mouse[1]<button.y+button.height:
                        success=button.ButtonClick()
                        if success:
                            if button.getcolor()==YELLOW:
                                AssassinTrigger=True

                                if not(endtrigger):
                                    endbutton=PrivateButton(button.getcolor(), button.x, button.y, button.width, button.height,clickteam, button.gettext())
                                endtrigger=True
                            if button.getcolor()==RED:
                                RedTeamCounter+=1
                                if RedTeamCounter==9:
                                    if not(endtrigger):
                                        endbutton=PrivateButton(button.getcolor(), button.x, button.y, button.width, button.height,clickteam, button.gettext())
                                    endtrigger=True                 
                            if button.getcolor()==BLUE:
                                BlueTeamCounter+=1
                                if BlueTeamCounter==9:
                                    if not(endtrigger):
                                        endbutton=PrivateButton(button.getcolor(), button.x, button.y, button.width, button.height,clickteam, button.gettext())
                                    endtrigger=True                       
                            if button.getcolor()==OFFWHITE:
                                InnocentCounter+=1
                            GameStats(RedTeamCounter, BlueTeamCounter, InnocentCounter, AssassinTrigger)


        #drawing time
        screen.fill(WHITE)



        #Border
        pygame.draw.rect(screen, BLACK, (0,windowy-buttonindenty*2,windowx,windowy),0)
        cluerender=cluefont.render(cluetext, 1, YELLOW)
        #Draw a text box for the text
        screen.blit(cluerender, (windowx/2-cluerender.get_width()/2, windowy*8/9-cluerender.get_height()/2))

        for button in buttonlist:
            button.draw(screen, BLACK)

        if AssassinTrigger or RedTeamCounter==9 or BlueTeamCounter==9:
            endbutton.endscreen()



        pygame.display.flip()

def SortWords():
    screen = pygame.display.set_mode((640, 480))
    wordfile=open("codenameswords.txt", "r")
    finalwords=open("CodenamesWordsSorted.txt", "w")

    
    for line in wordfile:
        #Write display the line on the screen in WHITE
        screen.fill(WHITE)
        line=line.strip()
        text=font.render(line, 1, (0,0,0))
        screen.blit(text, (320-text.get_width()/2, 240-text.get_height()/2))
        pygame.display.flip()
        #If the user presses left click, write the word to the file otherwise if the user presses right click, don't write the word to the file and move to the next word
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        finalwords.write(line)
                        done=True
                    elif event.button==3:
                        done=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

    wordfile.close()
    finalwords.close()

def main():

    generateSpyMasterBoard()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done=True
    codenamesGame(buttonOrder)
    pygame.quit()

main()