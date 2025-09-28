import pygame
import pygame.camera
try:
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
running = True
camerapos = [0,0]
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
class Sound(pygame.mixer.Sound):
    pass
class Sprite:
    def __init__(self,imgpath,pos=[0,0],scale = [64,64], camaffect=True, rotation = 0):
        self.image = _loadimage(imgpath)
        self.children = []
        self.pos = pos
        self.scale = scale
        self.rotation = rotation
        self.camaffect = camaffect
        self.update = connect._defaultfunc
        self.success = True if self.image else False
    def add(self):
        sprites.append(self)
    #def destroy(self):
    #   sprites.remove(self)
    def move(self,dx,dy):
        self.pos[0] += dx
        self.pos[1] += dy
    def iscolliding(self,other):
        if self.success:
            meow1 = pygame.transform.scale(self.image, self.scale).get_rect() # type: ignore
            meow1.topleft = self.pos
            meow2 = pygame.transform.scale(other.image, other.scale).get_rect()
            meow2.topleft = other.pos
            return meow1.colliderect(meow2)
    def rotate(self, angle):
        self.rotation += angle
    def _draw(self, screen:pygame.Surface):
        if self.success:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(self.image, self.scale), self.rotation), (self.pos[0] - camerapos[0], self.pos[1] - camerapos[1])) # type: ignore
    def _drawab(self, screen:pygame.Surface):
        if self.success:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(self.image, self.scale), self.rotation), self.pos) # type: ignore
class Line:
    def __init__(self, p1=(0,0), p2=(0,20), color="red", camaffect=True, width=4):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.camaffect = camaffect
        self.width = width
    def add(self):
        lines.append(self)
    def _draw(self,screen):
        pygame.draw.line(screen, self.color, (self.p1[0] - camerapos[0], self.p1[1] - camerapos[1]), (self.p2[0] - camerapos[0], self.p2[1] - camerapos[1]), self.width)
    def _drawab(self,screen):
        pygame.draw.line(screen, self.color, self.p1, self.p2, self.width)
class Rectangle:
    def __init__(self, pos=[0,0],size=[20,20],color='red',camaffect=True, draw=True):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.camaffect=camaffect
        self.draw = draw
    def add(self):
        rects.append(self)
    def _draw(self, screen):
        # Create a new pygame.Rect object with the adjusted position
        adjusted_rect = pygame.Rect(self.rect.x - camerapos[0], self.rect.y - camerapos[1], self.rect.width, self.rect.height)
        pygame.draw.rect(screen, self.color, adjusted_rect)
    def _drawab(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
class Text:
    def __init__(self, text="MEoooow",pos=[0,0], size=20, color="red",camaffect=True):
        self.pos = pos
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.text = text
        self.camaffect = camaffect
    def add(self):
        texts.append(self)
    def _draw(self,screen):
        meow = self.font.render(self.text,False,self.color)
        screen.blit(meow, (self.pos[0] - camerapos[0], self.pos[1] - camerapos[1]))
    def _drawab(self,screen):
        meow = self.font.render(self.text,False,self.color)
        screen.blit(meow, self.pos)
class Circle:
    def __init__(self,pos=[0,0], color="red", radius=10, camaffect=True) -> None:
        #pygame.draw.circle(screen,"blue",(0,0),10)
        self.pos = pos
        self.color = color
        self.radius = radius
        self.camaffect = camaffect
    def add(self):
        circles.append(self)
    def _draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.pos[0] - camerapos[0], self.pos[1] - camerapos[1]), self.radius)
    def _drawab(self,screen):
        pygame.draw.circle(screen,self.color,self.pos,self.radius)

def mainloop():
    global running,screen
    screen = pygame.display.set_mode(window.size, pygame.RESIZABLE if window.resizeable else 0)
    pygame.display.set_caption(window.title)
    pygame.display.set_icon(window.icon)
    keydown = False
    mousedown = False
    key = None
    clock = pygame.time.Clock()
    while running:
        if mouselocked:
            pygame.mouse.set_pos((window.size[0] / 2, window.size[1] / 2))
        connect.onupdate()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                connect.onkeypress(event.key)
                keydown = True
                key = event.key
            if event.type == pygame.KEYUP:
                keydown = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                connect.onmouseclicked((pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1]))
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
            if event.type == pygame.MOUSEMOTION:
                connect.onmousemove(event.pos)
            if event.type == pygame.QUIT:
                if _quit:
                    running = False
        if mousedown:
            connect.onmousedown((pygame.mouse.get_pos()[0] + camerapos[0], pygame.mouse.get_pos()[1] + camerapos[1]))
        if keydown:
            connect.onkeydown(key)
        screen.fill(window.screencolor)
        for sp in sprites:
            if sp.camaffect:
                sp._draw(screen)
            else:
                sp._drawab(screen)
            sp.update(event)
        for sp in lines:
            if sp.camaffect:
                sp._draw(screen)
            else:
                sp._drawab(screen)
        for sp in rects:
            if sp.draw:
                if sp.camaffect:
                    sp._draw(screen)
                else:
                    sp._drawab(screen)
        for sp in texts:
            if sp.camaffect:
                sp._draw(screen)
            else:
                sp._drawab(screen)
        for sp in circles:
            if sp.camaffect:
                sp._draw(screen)
            else:
                sp._drawab(screen)
        pygame.display.flip()
        clock.tick(window.fps)
if __name__ == "__main__":
    meow = Sprite("baby.jpeg",[0,0],(290,290), rotation=45)
    meow.add()
    e = Line(width=4, camaffect=False)
    e.add()
    rea = Rectangle()
    rea.add()
    Text(color="blue").add()
    setmouse(mouses.RESIZEALL, True)
    def _meow(k):
        if k == pygame.K_w:
            camerapos[1] -= 3
        if k == pygame.K_a:
            camerapos[0] -= 3
        if k == pygame.K_s:
            camerapos[1] += 3
        if k == pygame.K_d:
            camerapos[0] += 3
        
    connect.onkeydown = _meow
    mainloop()