import gym
from stable_baselines3 import PPO
from dino_gym_env import DinoGymEnv

# Create the custom Dino game environment
env = DinoGymEnv()

# Create the PPO agent
model = PPO("MlpPolicy", env, verbose=1)

# Train the agent
model.learn(total_timesteps=100000)

# Save the trained model
model.save("ppo_dino")
