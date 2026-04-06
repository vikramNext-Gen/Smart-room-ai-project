import random

class SmartRoomEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.temperature = random.randint(20, 40)
        self.people = random.randint(0, 5)
        print("START")
        return self.state()

    def state(self):
        return {
            "temperature": self.temperature,
            "people": self.people
        }

    def step(self, action):
        reward = 0

        # Actions
        if action == 0:
            reward = -5
        elif action == 1:
            reward = 2
        elif action == 2:
            reward = 5
        elif action == 3:
            reward = 10

        # Smart condition
        if self.people == 0 and action != 0:
            reward -= 5

        # Environment change
        self.temperature -= action

        print(f"STEP | Action: {action} | State: {self.state()} | Reward: {reward}")

        return self.state(), reward


# -------- MAIN PROGRAM --------

env = SmartRoomEnv()

print("Initial State:", env.reset())

while True:
    action = input("Enter action (0-3) or q to quit: ")

    if action == 'q':
        print("END")
        break

    if not action.isdigit() or int(action) not in [0, 1, 2, 3]:
        print("Invalid input! Enter 0,1,2,3 or q")
        continue

    action = int(action)

    env.step(action)
