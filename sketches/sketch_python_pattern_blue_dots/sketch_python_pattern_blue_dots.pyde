def setup():
    size(800,800)


def draw():
    noStroke()
    background(255)
    
    
    thin = 4
    medium = 20
    thick = 80
    
    for i in range(0,10):
        # one thick, three medium, one thick, 9 small
        rectWithDots(0,0,thick,height)
        
        s = medium*1.5
        rectWithDots(thick+s,0,medium,height)
        rectWithDots(thick+2*s,0,medium,height)
        rectWithDots(thick+3*s,0,medium,height)
        
        for j in range(0,10):
            rectWithDots(250,0,thin,height)
            translate(thin*2,0)
        
        translate(400,0)

def rectWithDots(x, y, w, h):
    with pushMatrix():
        translate(x,y)
        dot_size = 2.
    
        n_dots_y = int( h / dot_size) 
        n_dots_x = int( w / dot_size)
        
        inc_y =   h / n_dots_y
        inc_x =   w / n_dots_x
        
        y = 0
        for i in range(0,n_dots_y+1):
            x = 0
            for j in range(0,n_dots_x+1):
                if ((i*n_dots_x + j) % 6 == 0):
                    fill(80,200)
                else:
                    fill(0,0,255, 200)
                
                rect(x,y,dot_size,dot_size)            
                x = j*inc_x + noise(j*.1, i*0.1, millis()*.001)
            y += inc_y
        
        #rect(x, y, w, h)
    



from datetime import datetime

def keyPressed():
    if key == 'S' or key == 's':
        saveSketch()
        
 
# example on how to save Processing sketch in Python mode
# copy and paste to your sketch
def saveSketch():
    s = datetime.now().strftime('%Y%m%d%H%M%S_.%f')  
    save(str.format("/out/sketch_{0}.jpg", s ))
