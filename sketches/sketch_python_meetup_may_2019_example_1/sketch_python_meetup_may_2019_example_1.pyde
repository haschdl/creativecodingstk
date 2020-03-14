size(800, 800)

#0-255, RGB
background(255)
#0xFF0000

# rect(x, y, witdh, height)
fill(0, 0, 255, 80)
noStroke()

with pushMatrix():
    for j in range(0,3):
        s = 50
        ellipse(0,0,s,height)
        
        rect(s+10,0,s/4,height)
        rect(s+30,0,s/4,height)
        
        
        rect(s+50,0,s,height)
        
        
        for i in range(0,11):
            rect(s*4 + i*7,0,5,height)
        
        translate(s*6,0)

   
stroke(255,0,0)

beginShape()
#line(0,0,width,height)
curveVertex(0,0)
curveVertex(width,height)
curveVertex(0,300)
curveVertex(100,100)
endShape()
    
