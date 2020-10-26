import p5 as p
from env import Env
from stable_baselines import DQN

e=None
obs=None
model=None
def setup():
    global e,model,obs
    
    p.size(800,600)
    e=Env(width,height)
    model = DQN.load("ball_blast_dqn_25000")
    obs = e.reset()

def draw():
    p.background(0)
#    r=0
#    if key_is_pressed:
#        if key=='RIGHT':
#            r=20
#        elif key=='LEFT':
#            r=-20
#        elif key=='r':
#            e.reset()
    action, _states = model.predict(obs)
    obs, rewards, dones, info = e.step(action)
    e.render()
    
p.run()
