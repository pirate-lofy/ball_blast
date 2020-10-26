import p5 as p
from tank import Tank
from ball import Ball
import random as rnd
import numpy as np
import cv2 as cv
import gym
from gym import spaces

class Env(gym.Env):
    '''
    RL stuff
    '''
    
    metadata = {'render.modes': ['human']}
    
    def __init__(self,width,height):
        super(Env,self).__init__()
        
        self.balls=[]
        self.min_balls=5
        self.reward=0
        self.width=width
        self.height=height
        self.size=(height,width,1)
        
        
        self.observation_space=spaces.Box(0,255,self.size)
        self.action_space=spaces.Discrete(2)
        
        self.cash=[]
        self.tank=Tank(self.width/2,self.height-90,
                       30,90,self.cash)
        self.generate_ball()
        
    
    def generate_ball(self,x=None,
                      y=40,a=-80,r=100):
        if x is None:
            x=rnd.randint(0,self.width)
        b=Ball(self.cash,self.width,self.height,
               x,y,a,r)
        self.balls.append(b)

    def check_balls(self):
        i=0
        while i<len(self.balls):
            ball=self.balls[i]
            for fire in self.tank.fires:
                b=ball.hit(fire)
                if b is not None:
                    rad,x1,x2,y,angle1,angle2=b
                    if rad:
                        self.reward+=1
                        self.generate_ball(x1,y,angle1,rad)
                        self.generate_ball(x2,y,angle2,rad)
                        break
            
            if ball.alive==False:
                self.destroy_ball(i)
            
            if len(self.balls)<self.min_balls:
                self.generate_ball()
            
            i+=1
    
    def destroy_ball(self,idx):
        self.balls.pop(idx)
    
    def render_balls(self):
        for ball in self.balls:
            ball.render()
    
    def update_balls(self):
        for ball in self.balls:
            ball.update()
    
    def is_done(self):
        return self.tank.hit(self.balls)
        
        
    def generate_data(self):
        print('generate')
        data=np.zeros(self.size,dtype=np.uint8)
        for tp in self.cash:
            a,b=tp[0],tp[1]
            a=tuple(map(round,a))
            a=tuple(map(int,a))
            b=tuple(map(round,b))
            b=tuple(map(int,b))
            if a[0]<0 or a[1]<0:
                continue

            data[a[0]:a[1],
                      b[0]:b[1]]=[255]
        
#        data=data.reshape((*self.size,1))
        return data

    def show(self,img):
        cv.imshow('cv',img)    
        if cv.waitKey(1)==27:
            exit()                  
        
    def cashing(self):
        self.tank.cashing()
        for ball in self.balls:
            ball.cashing()
          
            
    def render(self):
        self.tank.render()
        self.render_balls()
        p.text(str(self.reward),(700,30))

    def update(self,r):
        self.tank.update(r)
        self.update_balls()   
        self.check_balls()
        
    def reset(self):
        self.cash.clear()
        self.balls.clear()
        self.reward=0
        self.tank=Tank(self.width/2,self.height-90,
                       30,90,self.cash)
        self.generate_ball()
        data=self.generate_data()
        return data


    def step(self,r):
        self.update(r)
        done=self.is_done()
        self.cashing()
        data=self.generate_data()
        self.cash.clear()
        return data,self.reward,done,{}
