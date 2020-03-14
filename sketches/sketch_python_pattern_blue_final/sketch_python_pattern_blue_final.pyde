size(800,800)

noStroke()
background(255)
fill(0,0,255, 40)

thin = 2
medium = 10
thick = 40



for i in range(0,10):
    # one thick, three medium, one thick, 9 small
    rect(0,0,thick,height)
    
    s = 20
    rect(thick+s,0,medium,height)
    rect(thick+2*s,0,medium,height)
    rect(thick+3*s,0,medium,height)
    
    for j in range(0,10):
        rect(150,0,thin,height)
        translate(5,0)
        
    translate(180,0)
