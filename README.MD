# README

## Overview
This project contains a reinforcement learning agent that learns to play the Google Chrome's Dino game. The agent uses Deep Q-Networks (DQNs) and a custom Pygame-based environment to learn how to jump over cacti and avoid obstacles in the game.

## Installation
1. Clone the repository to your local machine.
2. Ensure you have Python 3.6 or later installed.
3. Install the required packages using pip: `pip install pygame tensorflow stable-baselines3 numpy pyperclip`
4. Run the `train_dino.py` script to train the DQN agent.
## Explanation

### Inputs
The Dino game agent takes in three inputs as its state: the distance to the next cactus, the height of the Dino's jump, and the current game speed. These inputs are passed to the agent's neural network to predict the best action to take.

### Outputs
The agent outputs one of two actions: either to jump or to do nothing. The agent uses a Deep Q-Network (DQN) to learn how to choose the best action given the current state.

### Model Architecture
The DQN agent uses a simple neural network with the following layers:

- Input layer with 3 units, corresponding to the 3 state inputs
- Two hidden layers, each with 24 units and ReLU activation
- Linear output layer with 2 units (one for jumping, one for doing nothing)

The model is trained using the Mean Squared Error (MSE) loss function and the Adam optimizer. The agent also uses experience replay and epsilon-greedy exploration to improve its performance.

## Showcase
This is training so it uses random jumps so the ai can learn quicker thats why it jumps so often

https://user-images.githubusercontent.com/70327203/228851868-399e0e84-a0ce-401d-a9bc-a560f7880393.mp4

