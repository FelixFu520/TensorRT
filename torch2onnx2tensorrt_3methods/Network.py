# -*- coding: utf-8 -*-
import torch.nn as nn
import torch.nn.functional as F
from Config import Config
import torch

class Net(nn.Module):
    '''
    卷积网络结构
    '''

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, kernel_size=5)
        self.conv2 = nn.Conv2d(20, 50, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(800, 500)
        self.fc2 = nn.Linear(500, 10)
        self.config = Config()

    def forward(self, x):
        x = F.max_pool2d(self.conv1(x), kernel_size=2, stride=2)
        x = F.max_pool2d(self.conv2(x), kernel_size=2, stride=2)
        x = x.view(-1, 800)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x)

# class Net(torch.nn.Module):
#     def __init__(self, num_classes=10,):
#         super(Net, self).__init__()
#         self.layer1 = torch.nn.Conv2d(1,16,3)
#         self.layer2 = torch.nn.Conv2d(16,64,5)
#         self.relu = torch.nn.ReLU()
        
#         # TAKE CARE HERE
#         # Ceil_mode must be False, because onnx eporter does NOT support ceil_mode=True
#         self.max_pool = torch.nn.MaxPool2d(kernel_size=3, stride=1, ceil_mode=False) 
#         self.avg_pool = torch.nn.AdaptiveAvgPool2d((1,1)) 
        
#         self.fc = torch.nn.Linear(64,num_classes)

       
#     def forward(self, X_in):
#         x = self.layer1(X_in)
#         x = self.relu(x)
#         x = self.max_pool(x)
#         x = self.layer2(x)
#         x = self.relu(x)
#         x = self.avg_pool(x)
        
#         # Such an operationt is not deterministic since it would depend on the input and therefore would result in errors
#         length_of_fc_layer = x.size(1) 
#         x = x.view(-1, length_of_fc_layer)
        
#         x = self.fc(x)
#         return x
if __name__ == '__main__':
    net = Net()
    print(net)