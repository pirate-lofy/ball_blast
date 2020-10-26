import p5 as p

class Tank:
    def __init__(self,x,y,w,h,cash):
        self.h=h
        self.w=w
        self.width=x*2
        self.pos=p.Vector(x,y)
        self.fires=[]
        self.cash=cash

    def make_fire(self):
        f=p.Vector(self.pos.x+15,self.pos.y)
        return f
    
    def update_fires(self):
        i=0
        while i<len(self.fires):
            self.fires[i].y-=25
            if self.fires[i].y<0:
                self.fires.pop(i)
            i+=1

    def render_fires(self):
        for fire in self.fires:
            p.fill(123)
            self.cash.append(((fire.y,fire.y+7),
                          (fire.x,fire.x+7)))
        
            p.circle(fire,10)

    def update(self,dx):
        if dx==0:
            dx=20
        elif dx==1:
            dx=-20
        self.pos.x+=dx
        
        if self.pos.x<0:
            self.pos.x=0
        if self.pos.x+self.w>self.width:
            self.pos.x=self.width-self.w
        
        f=self.make_fire()
        self.fires.append(f)
        self.update_fires()
        
    def cashing(self):
        self.cash.append(((self.pos.y,self.pos.y+self.h),
                          (self.pos.x,self.pos.x+self.w)))
        
        
    def render(self):
        p.fill(255)
        p.rect(self.pos.x,self.pos.y,self.w,self.h)
        self.render_fires()


    def hit(self,balls):
        for ball in balls:
            d1=p.dist(ball.pos,self.pos)
            npos=p.Vector(self.pos.x,self.pos.y)
            npos.x+=self.w
            d2=p.dist(ball.pos,npos)
            
            if d1<(ball.r*0.5) or d2<(ball.r*0.5):
                print(d1,d2)
