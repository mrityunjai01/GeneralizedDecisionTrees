import numpy as np
from constants import NO_SAMPLES
class Node:
    def __init__(self, left=None, right=None, c_tilde = np.ones(NO_SAMPLES)):
        self.right = right
        self.left = left
        self.c_tilde = c_tilde
    def forward(self):
        if (self.right is not None and self.left is not None):
            return c_hat_left * self.left.forward() + c_hat_right * self.right.forward()
        else:
            return self.activation(self.w.mm(self.x) + self.b)
    
