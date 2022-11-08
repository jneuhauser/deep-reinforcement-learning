import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_shape, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_shape Tulpe[int]: Shape of each state (batch, height, width, depth) or (height, width, depth)
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"

        print(f"state_shape = {state_shape}, action_size = {action_size}, seed = {seed}")

        # Inspired by https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

        self.conv1 = nn.Conv2d(state_shape[-1], 16, kernel_size=3, stride=2)
        self.bn1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=2)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3, stride=2)
        self.bn3 = nn.BatchNorm2d(32)

        # Number of Linear input connections depends on output of conv2d layers
        # and therefore the input image size, so compute it.
        def conv2d_size_out(size, kernel_size = 3, stride = 2):
            return (size - (kernel_size - 1) - 1) // stride  + 1
        last_conv_out_height = conv2d_size_out(conv2d_size_out(conv2d_size_out(state_shape[-3])))
        last_conv_out_width = conv2d_size_out(conv2d_size_out(conv2d_size_out(state_shape[-2])))
        linear_input_size = 32 * last_conv_out_height * last_conv_out_width
        print(f"last_conv_out_height = {last_conv_out_height}, last_conv_out_width = {last_conv_out_width}, linear_input_size = {linear_input_size}")
        self.fc1 = nn.Linear(linear_input_size, action_size)

    def forward(self, x):
        """Build a network that maps state -> action values."""

        if len(x.shape) > 4:
            x = x.reshape(-1, *x.shape[-3:])

        # channel last -> channel first
        x = x.transpose(1, 3)

        x = self.conv1(x)
        x = self.bn1(x)
        x = F.relu(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = F.relu(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = F.relu(x)

        #x = x.view(x.size(dim=0), -1)
        x = x.flatten(start_dim=1)
        x = self.fc1(x)

        return x

if __name__ == '__main__':
    state_shape = (10, 84, 84, 3)

    net = QNetwork(state_shape, 4, 0)

    x = torch.rand(state_shape)

    print(type(x), x.shape)

    y = net(x)

    print(type(y), y.shape)
