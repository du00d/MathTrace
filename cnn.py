import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms


class Net(nn.Module):
    
    def __init__(self, input_shape, vocab):
        super().__init__()
        self.n_classes = len(vocab)
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.AvgPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 3)
        self.fc1 = nn.Linear(115200, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, self.n_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.flatten(start_dim=1)   # flatten features
#         print(x.shape)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.sigmoid(x)    
    
    def decode(self, x):
        return x