import numpy as np
from dino_env import DinoEnv
from dino_agent import DQNAgent
import pygame
import time

EPISODES = 10000
BATCH_SIZE = 32
MODEL_PATH = 'dino_dqn_model.h5'  # Existing model file path

if __name__ == "__main__":
    try:
        env = DinoEnv()
        state_size = 3
        action_size = 2
        agent = DQNAgent(state_size, action_size, MODEL_PATH)
        for episode in range(EPISODES):
            state = env.reset()
            state = np.reshape(state, [1, state_size])
            done = False

            while not done:
                action = agent.act(state)
                next_state, reward, done = env.step(action)
                next_state = np.reshape(next_state, [1, state_size])
                agent.remember(state, action, reward, next_state, done)
                state = next_state

                if done:
                    print(f"Episode: {episode + 1}/{EPISODES}")

            if len(agent.memory) > BATCH_SIZE:
                agent.replay(BATCH_SIZE)

            # every 100 episodes, save the model in a folder named backup and save it as the date and time plus the episode number and also make it reload everything so the ram doesn't get full
            if episode % 10 == 0:
                agent.model.save(f'backup/{time.strftime("%Y%m%d-%H%M%S")}_{episode}.h5')
                

            # Check for 'c' keypress to exit and save the model
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    agent.model.save('dino_dqn_model.h5')
                    env.close()
                    pygame.quit()
                    quit()

        # Save the trained model after all episodes complete
        agent.model.save('dino_dqn_model.h5')
        env.close()
        pygame.quit()
    except Exception as e:
        print(f"Error: {e}")
        agent.save_model(MODEL_PATH)
        env.close()
        pygame.quit()
        quit()
