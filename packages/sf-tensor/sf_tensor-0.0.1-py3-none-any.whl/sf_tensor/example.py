from . import logAccuracy

import torch
from torch import nn


model = nn.Sequential(nn.Linear(4, 2))
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.CrossEntropyLoss()

inputs = torch.randn(64, 4)
targets = torch.randint(0, 2, (64,))

for _ in range(5):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = loss_fn(outputs, targets)
    loss.backward()
    optimizer.step()

    accuracy = (outputs.argmax(1) == targets).float().mean().item()
    logAccuracy(accuracy)