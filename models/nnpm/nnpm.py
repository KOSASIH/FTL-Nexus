import torch
import torch.nn as nn
import torch.optim as optim

class NNPM(nn.Module):
    def __init__(self):
        super(NNPM, self).__init__()
        self.fc1 = nn.Linear(128, 256)  # Input layer (128) -> Hidden layer (256)
        self.fc2 = nn.Linear(256, 128)  # Hidden layer (256) -> Output layer (128)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Activation function for hidden layer
        x = self.fc2(x)
        return x

model = NNPM()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

# Use the trained model for predictive maintenance
def predict_maintenance(inputs):
    outputs = model(inputs)
    return outputs
