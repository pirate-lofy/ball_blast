from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import CnnPolicy
from stable_baselines import DQN
from env import Env

e=Env(800,600)
model = DQN(CnnPolicy, e, verbose=2)
model.learn(total_timesteps=50000)
model.save("ball_blast_dqn_50000")
