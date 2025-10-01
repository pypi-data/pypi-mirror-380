# sf-tensor

Minimal start of a Python package for functionality related to the services offered by SF Tensor.
This will include functionality to interact with SF Tensor's API endpoints for metric logging and more.

Updates will arrive in the next days and weeks ;)


## Installation

Install with:

```bash
pip install sf-tensor
```

## Usage

```python
from sf_tensor import logAccuracy
import torch
from torch import nn

model = nn.Sequential(nn.Linear(4, 2))
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.CrossEntropyLoss()
x = torch.randn(64, 4)
y = torch.randint(0, 2, (64,))
for _ in range(5):
    opt.zero_grad(); o = model(x); (loss_fn(o, y)).backward(); opt.step()
    logAccuracy((o.argmax(1) == y).float().mean().item())
```


