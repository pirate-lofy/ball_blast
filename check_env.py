from stable_baselines.common.env_checker import check_env
from env import Env

env = Env(800,600)
# It will check your custom environment and output additional warnings if needed
check_env(env)