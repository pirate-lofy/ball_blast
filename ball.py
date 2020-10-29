import p5 as p
import random as rnd
import math

class Ball:
    def __init__(self,cash,width,height,x,y,
                 angle,r=100):
        self.pos=p.Vector(x,y)
        self.r=r
        self.angle=angle
        self.cash=cash
        self.width=width
        self.height=height
        self.weight=(rnd.randint(1,self.r//2))
        
        self.alive=True
        self.color=123
        self.dumping=0.8
        self.v=p.Vector(5*math.cos(self.angle),
                        rnd.random()*5*math.sin(self.angle))
        self.a=p.Vector(0,2)
        
    
    
    def update(self):
        self.pos+=self.v
        self.v+=self.a
        self.off_board()
        if self.v.y<0:
            self.v*=0.9
        if self.v.y>0:
            self.v*=1.1
        
    def split(self):
        r=self.r/2
        if r<25:
            r=0
        angle1=-90
        angle2=-100
        x1=self.pos.x-50
        x2=self.pos.x+50
        y=self.pos.y-50
        return r,x1,x2,y,angle1,angle2
        
    def die(self):
        self.alive=False
        return self.split()
        
    
    def hit(self,obj):
        d=p.dist(self.pos,obj)
        if d<self.r:
            self.weight-=1
            if self.weight<=0:
                b=self.die()
                return b
    
    def off_board(self):
        if self.pos.x-self.r<0:
            self.pos.x=self.r
            self.v.x*=-self.dumping
        if self.pos.x+self.r>self.width:
            self.pos.x=self.width-self.r
            self.v.x*=-self.dumping
            
        if self.pos.y+self.r>self.height:
            self.pos.y=self.height-self.r
            self.v.y*=-1
        if self.pos.y-self.r<0:
            self.pos.y=self.r
        
    def cashing(self):
        self.cash.append(((self.pos.y,self.pos.y+self.r*0.7),
                          (self.pos.x-40,self.pos.x+self.r*0.7-30)))
    
    def render(self):
        p.fill(self.color)
        p.circle(self.pos,self.r)