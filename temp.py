#import p5 as p
#from env import Env
#
#e=None
#def setup():
#    global e
#    p.size(800,600)
#    e=Env(width,height)
#
#def draw():
#    p.background(0)
#    r=0
#    if key_is_pressed:
#        if key=='RIGHT':
#            r=20
#        elif key=='LEFT':
#            r=-20
#        elif key=='r':
#            e.reset()
#    
#    e.render()
#    e.step(r)
#    
#p.run()



#
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import CnnPolicy
from stable_baselines import DQN
from env import Env

e=Env(800,600)
model = DQN(CnnPolicy, e, verbose=2)
model.learn(total_timesteps=25000)
model.save("ball_blast_dqn_25000")

del model # remove to demonstrate saving and loading

model = DQN.load("ball_blast_dqn_25000")

obs = e.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = e.step(action)
    e.render()
