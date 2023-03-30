import numpy as np
import tensorflow as tf
from collections import deque
import random
import os

class DQNAgent:
    def __init__(self, state_size, action_size, model_path=None):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model_path = model_path
        self.model = self.build_model()

    def build_model(self):
        # Load the existing model if present, otherwise create a new one
        if self.model_path is not None and os.path.exists(self.model_path):
            model = tf.keras.models.load_model(self.model_path)
        else:
            model = tf.keras.Sequential()
            model.add(tf.keras.layers.Dense(24, input_dim=self.state_size, activation='relu'))
            model.add(tf.keras.layers.Dense(24, activation='relu'))
            model.add(tf.keras.layers.Dense(self.action_size, activation='linear'))
            model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save_model(self, model_path):
        self.model.save(model_path)
