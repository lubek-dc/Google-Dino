import os
import numpy as np
import tensorflow as tf
from dino_env import DinoEnv

def test_model(model_path):
    model = tf.keras.models.load_model(model_path)
    env = DinoEnv(None)
    state = env.reset()
    done = False
    while not done:
        state = np.reshape(state, [1, 3])
        action = np.argmax(model.predict(state))
        next_state, reward, done = env.step(action)
        state = next_state
    score = env.score
    env.close()
    return score

def load_blacklist(file_path):
    blacklist = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                model_file, score = line.strip().split(' | ')
                blacklist[model_file] = int(score)
    return blacklist

def save_to_blacklist(file_path, model_file, score):
    with open(file_path, 'a') as f:
        f.write(f"{model_file} | {score}\n")

def sort_scores(blacklist):
    return sorted(blacklist.items(), key=lambda x: x[1], reverse=True)

def save_sorted_scores(sorted_scores, file_path):
    with open(file_path, 'w') as f:
        for model_file, score in sorted_scores:
            f.write(f"{model_file} | {score}\n")

def main():
    backup_folder = 'backup'
    model_files = [f for f in os.listdir(backup_folder) if f.endswith('.h5')]
    blacklist_file = 'model_scores.txt'
    sorted_file = 'model_scores_sorted.txt'

    blacklist = load_blacklist(blacklist_file)

    for model_file in model_files:
        if model_file in blacklist:
            print(f"Skipping {model_file} (already in blacklist)")
            continue

        model_path = os.path.join(backup_folder, model_file)
        score = test_model(model_path)
        print(f"Tested {model_file} with score {score}")
        save_to_blacklist(blacklist_file, model_file, score)

    sorted_scores = sort_scores(blacklist)
    save_sorted_scores(sorted_scores, sorted_file)

if __name__ == "__main__":
    main()
