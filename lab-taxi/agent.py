import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.alpha = 1.0
        self.epsilon = 0.005
        self.gamma = 1.0
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        
    def get_epsilon_greedy_probs(self, state):
        best_a = np.argmax(self.Q[state])
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        policy_s[best_a] = 1 - self.epsilon + (self.epsilon / self.nA)
        return policy_s

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # get action probabilities with epsilon greedy strategy
        policy_s = self.get_epsilon_greedy_probs(state)
        
        # select random action based on policy for current state
        action = np.random.choice(np.arange(self.nA), p=policy_s)
        
        return action

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.Q[state][action] = self.Q[state][action] + self.alpha * (
            reward + self.gamma * np.dot(
                self.Q[next_state],
                self.get_epsilon_greedy_probs(next_state)
            ) - self.Q[state][action]
        )