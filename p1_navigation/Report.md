# Report for Project 1 of the Udacity Deep Reinforcement Learning course.

This report provides a short description of my implementation.

## Learing Algorithm

A Deep Reinforcement Agent was developed to solve the task of collecting as many yellow bananas as possible.
The implementation is based on the "Deep Q-Learning Algorithm", which has already been implemented in a previous exercise.

The Deep Q-Learning Algorithm represents the optimal action value function as a neural network rather than a table/matrix like in normal Q-Learning.
Since reinforcement learning is very unstable when neural networks are used to represent action values, it is common to use techniques like "Experience Replay" and "Fixed Q-Targets".

"Experience Replay" is implemented by a replay buffer, which is used to store experience while executing a policy in an environment.
The replay buffer stores the most recent experiences, including the state, action, reward, next state, and done, in a size-limited queue.
During training, a subset of the experiences is sampled from the replay buffer to "replay" the agent's experiences.

"Fixed Q-Targets" are implemented by a second neural network, which is called target network.
Instead of using the policy network a second time to calculate the target Q-Values, we use the temporarily fixed target network.
The target network is a clone of the policy network, has its own weights and is only updated from time to time with the weights of the policy network.

**Learing Algorithm Steps**
1. Init the agent with state and action size:
   - Init policy network and optimizer
   - Init target network
   - Init replay buffer
2. For each episode:
   1. Get the initial state by resetting the environment
   2. For each step
      1. Select an action with epsilon-greedy strategy
         - exploration: random action
         - exploitation: based on policy network
      2. Execute the selected action in the environment
      3. Observe next state, reward and if it's a final state.
      4. Store experience in the replay buffer
      5. Learn from observed experiences every `UPDATE_EVERY` steps
         1. Sample random experiences from replay buffer
         2. Obtain state action values from policy network for current state
         3. Obtain next state values from target network for next state
         4. Calculate expected state action values based on next state values
         5. Calculate the loss between state action values and expected state action values
         6. Update policy network weights to minimize loss
         7. Update target network weights with policy network weights

**Agent Hyperparameters**
```
BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate
UPDATE_EVERY = 4        # how often to update the network
```

**Neural Network Hyperparameters**
```
STATE_SIZE = 37
ACTION_SIZE = 4
```

**Neural Network Architectures**
```
QNetwork(
  Linear(in_features=STATE_SIZE, out_features=64)
  ReLU()
  Linear(in_features=64, out_features=64)
  ReLU()
  Linear(in_features=64, out_features=ACTION_SIZE)
)
```

## Plot of Rewards

The environment reached an average reward of 13 over the last 100 episodes in episode 522 and was therefore solved in episode 422.

![rewards](rewards.png)

## Ideas for Future Work

- Try different network architectures
- Implement DQN extensions
  - double DQN
  - dueling DQN
  - prioritized experience replay
- Use up-to-date software
