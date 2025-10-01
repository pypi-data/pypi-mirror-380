import pygame
import pygame.camera
import math
try: # stiching
    from . import window,connect,keys,log,mouses
except:
    import window,connect,keys,log,mouses
log.info(f"Backends: {pygame.camera.get_backends()}")
pygame.init()
pygame.camera.init()
print("PYGAME_INIT")
_quit = True
sprites = []
lines = []
rects = []
texts = []
circles = []
drawqueue = []
updatequeue = []
running = True

camerapos = [0,0]
camerazoom = 1.0
screen = None
camallowed = True
cams = pygame.camera.list_cameras()
log.info(f"Cameras: {cams}")
def hidemouse():
    pygame.mouse.set_visible(False)
def showmouse():
    pygame.mouse.set_visible(True)
def setmouse(mouse, system = False):
    if not system:
        pygame.mouse.set_cursor(mouse)
    else:
        pygame.mouse.set_system_cursor(mouse)
mouselocked = False
if not cams:
    log.error("Attach a camera to your device")
    camallowed = False
webcamsize = (640,480)
webcam = pygame.camera.Camera(cams[0])
def takepicturetofile(path="photo.jpg"):
    if camallowed:
        webcam.start()
        pygame.time.wait(1000)  # 1 second delay
        pygame.image.save(webcam.get_image(), path)
        webcam.stop()
def getmousepos():
    return (pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1])
def changemusic(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)
def stopmusic():
    pygame.mixer.music.stop()
def screenshot(path="screenshot.png"):
    pygame.image.save(screen,path) # type: ignore
def quit_app():
    exit(0)
def _loadimage(path):
    try:
        return pygame.image.load(path)
    except Exception as e:
        log.error(f"Could not load {path}: {e}")
        return None

# im lazy
class Sound(pygame.mixer.Sound):
    pass

# sprite
class Sprite:
    def __init__(self,imgpath,pos=[0,0],scale = [64,64], camaffect=True, rotation = 0,removecolor=None):
        self.image = _loadimage(imgpath)
        self.children = []
        self.pos = pos
        self.scale = scale
        self.rotation = rotation
        self.camaffect = camaffect
        self.update = connect._defaultfunc
        self.visible = True if self.image else False
        self.removecolor = removecolor
    def add(self):
        drawqueue.append(self)
    def changeimg(self,path):
        self.image = _loadimage(path)
        self.visible = True if self.image else False
    def move(self,dx,dy):
        self.pos[0] += dx
        self.pos[1] += dy
    def iscolliding(self,other):
        if self.visible:
            meow1 = pygame.transform.scale(self.image, self.scale).get_rect() # type: ignore
            meow1.topleft = self.pos
            meow2 = pygame.transform.scale(other.image, other.scale).get_rect()
            meow2.topleft = other.pos
            return meow1.colliderect(meow2)
    def rotate(self, angle):
        self.rotation += angle
    def _draw(self, screen:pygame.Surface):
        if self.visible:
            screen.blit(
                pygame.transform.rotate(
                    pygame.transform.scale(
                        self.image,  # type: ignore
                        (abs(self.scale[0] * camerazoom), abs(self.scale[1] * camerazoom))
                    ), 
                    self.rotation
                ), 
                (
                    (self.pos[0] - camerapos[0]) * camerazoom,
                    (self.pos[1] - camerapos[1]) * camerazoom
                )
            )
    def _drawab(self, screen:pygame.Surface):
        if self.visible:
            screen.blit(
                pygame.transform.rotate(
                    pygame.transform.scale(
                        self.image, self.scale # type: ignore
                    ), 
                    self.rotation
                ), 
                self.pos
            )
class Line:
    def __init__(self, p1=(0,0), p2=(0,20), color="red", camaffect=True, width=4,visible=True):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.camaffect = camaffect
        self.width = width
        self.visible = visible
    def add(self):
        drawqueue.append(self)
    def _draw(self,screen):
        if self.visible:
            pygame.draw.line(
                screen, 
                self.color, 
                (
                    (self.p1[0] - camerapos[0]) * camerazoom, 
                    (self.p1[1] - camerapos[1]) * camerazoom
                ), 
                (
                    (self.p2[0] - camerapos[0]) * camerazoom, 
                    (self.p2[1] - camerapos[1]) * camerazoom
                ), 
                self.width
            )
    def _drawab(self,screen):
        if self.visible:
            pygame.draw.line(
                screen, 
                self.color, 
                self.p1, 
                self.p2, 
                self.width
            )
class Rectangle:
    def __init__(self, pos=[0,0],size=[20,20],color='red',camaffect=True, visible=True):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.camaffect=camaffect
        self.visible = visible
    def add(self):
        drawqueue.append(self)
    def _draw(self, screen):
        # Create a new pygame.Rect object with the adjusted position
        if self.visible:
            adjusted_rect = pygame.Rect(
                (self.rect.x - camerapos[0]) * camerazoom,
                (self.rect.y - camerapos[1]) * camerazoom,
                abs(self.rect.width * camerazoom),
                abs(self.rect.height * camerazoom)
            )
            pygame.draw.rect(
                screen, 
                self.color, 
                adjusted_rect
            )
    def _drawab(self,screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)

# text
class Text:
    def __init__(self, text="MEoooow",pos=[0,0], size=20, color="red",camaffect=True,visible=True):
        self.pos = pos
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.text = text
        self.camaffect = camaffect
        self.visible = visible
    def add(self):
        drawqueue.append(self)
    def _draw(self,screen):
        if self.visible:
            meow = self.font.render(self.text,False,self.color)
            screen.blit(
                pygame.transform.scale(
                    meow,  # type: ignore
                    (abs(meow.get_width() * camerazoom), abs(meow.get_height() * camerazoom))
                ), 
                (
                    self.pos[0] - camerapos[0], 
                    self.pos[1] - camerapos[1]
                )
            )
    def _drawab(self,screen):
        if self.visible:
            meow = self.font.render(self.text,False,self.color)
            screen.blit(meow, self.pos)

# circle
class Circle:
    def __init__(self,pos=[0,0], color="red", radius=10, camaffect=True,visible=True) -> None:
        #pygame.draw.circle(screen,"blue",(0,0),10)
        self.pos = pos
        self.color = color
        self.radius = radius
        self.camaffect = camaffect
        self.visible = visible
    def add(self):
        drawqueue.append(self)
    def _draw(self,screen):
        if self.visible:
            pygame.draw.circle(
                screen, 
                self.color, 
                (
                    (self.pos[0] - camerapos[0]) * camerazoom, 
                    (self.pos[1] - camerapos[1]) * camerazoom
                ), 
                abs(self.radius * camerazoom)
            )
    def _drawab(self,screen):
        if self.visible:
            pygame.draw.circle(screen,self.color,self.pos,self.radius)
class Button:
    def __init__(self, size=50, text="Mrow?", color="blue", hovercolor="red", pos=[0,0], textcolor="white", camaffect=False, onclick=lambda: print("clicked")) -> None:
        self.text = Text(text,pos,size,textcolor,camaffect,True)
        m = self.text.font.render(text,True, "white")
        self.hovercolor = hovercolor
        self.color = color
        self.rect = Rectangle([pos[0] - 10, pos[1] - 10], [m.get_width() + 10, m.get_height() + 10], color, camaffect, True)
        self.onclick = onclick
    def add(self):
        self.rect.add()
        self.text.add()
        updatequeue.append(self)
    def _update(self,event):
        if self.rect.rect.collidepoint(pygame.mouse.get_pos()):
            self.rect.color = self.hovercolor
            setmouse(mouses.HANDPOINT)
        else:
            self.rect.color = self.color
            setmouse(mouses.NORMAL)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.rect.collidepoint(event.pos):
                self.onclick()
#   IMPORTANT
def mainloop():
    global running,screen
    screen = pygame.display.set_mode(window.size, pygame.RESIZABLE if window.resizeable else 0 or pygame.FULLSCREEN if window.fullscreen else 0)
    pygame.display.set_caption(window.title)
    pygame.display.set_icon(window.icon)
    mousedown = False
    clock = pygame.time.Clock()
    while running:
        if mouselocked:
            pygame.mouse.set_pos((window.size[0] / 2, window.size[1] / 2))
        connect.onupdate()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                connect.onkeypress(event.key)
            if event.type == pygame.KEYUP:
                connect.onkeyup(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                connect.onmouseclicked((pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1]))
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
            if event.type == pygame.MOUSEMOTION:
                connect.onmousemove((pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1]))
            if event.type == pygame.MOUSEWHEEL:
                connect.onmousescroll((event.x,event.y))
            if event.type == pygame.QUIT:
                if _quit:
                    running = False
                    connect.onquit()
            for item in updatequeue:
                item._update(event)
            connect.oneventupdate(event)
        if mousedown:
            connect.onmousedown((pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1]))
        kes = pygame.key.get_pressed()
        connect.onkeydown(kes)
        screen.fill(window.screencolor)
        for item in drawqueue:
            if item.camaffect:
                item._draw(screen)
            else:
                item._drawab(screen)
        pygame.display.flip()
        clock.tick(window.fps)
def calculate_sprite_distance(sp1:Sprite, sp2:Sprite):
    """
    Calculates the Euclidean distance between the centers of two Sprite objects.
    """
    meow1 = pygame.transform.scale(sp1.image, sp1.scale).get_rect() # type: ignore
    meow2 = pygame.transform.scale(sp2.image, sp2.scale).get_rect() # type: ignore
    center1_x, center1_y = meow1.center
    center2_x, center2_y = meow2.center

    dx = center1_x - center2_x
    dy = center1_y - center2_y

    distance = math.hypot(dx, dy)
    return distance
# test
if __name__ == "__main__":
    rea = Rectangle(camaffect=False)
    rea.add()
    meow = Sprite("baby.jpeg",[0,0],(290,290), rotation=45)
    meow.add()
    meow2 = Sprite("oil.png",[0,0],(290,290), rotation=45)
    meow2.add()
    butt = Button()
    butt.add()
    Circle([100,100]).add()
    txt = Text(color="blue", pos=[100,100])
    txt.add()
    e = Line(width=4, camaffect=True)
    e.add()
    #setmouse(mouses.HANDPOINT, False)
    def _meow(k):
        global txt,camerapos
        #meow.rotate(1)
        camerapos = meow.pos
        e.p1 = meow.pos
        e.p2 = meow2.pos
        if k[keys.W]:
            meow.pos[1] -= 1
            #meow.changeimg("fish.png")
        if k[keys.A]:
            meow.pos[0] -= 1
        if k[keys.S]:
            meow.pos[1] += 1
        if k[keys.D]:
            meow.pos[0] += 1
    def _meow2(scroll):
        global camerazoom
        camerazoom -= (scroll[1] * 0.1)
        
    connect.onkeydown = _meow
    connect.onmousescroll = _meow2
    mainloop()