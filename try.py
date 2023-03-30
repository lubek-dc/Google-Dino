import gym
import numpy as np
import tensorflow as tf
from dino_env import DinoEnv

# Load the pre-trained model
model_path = 'dino_dqn_model.h5'
model = tf.keras.models.load_model(model_path)

# Create the Dino game environment
env = DinoEnv(None)

# Play the game using the pre-trained model
state = env.reset()
done = False
while not done:
    # Choose the next action using the pre-trained model
    state = np.reshape(state, [1, 3])
    action = np.argmax(model.predict(state))
    
    # Update the game state based on the chosen action
    next_state, reward, done = env.step(action)
    state = next_state
#print the score
print(env.score)
# Close the game environment
env.close()
