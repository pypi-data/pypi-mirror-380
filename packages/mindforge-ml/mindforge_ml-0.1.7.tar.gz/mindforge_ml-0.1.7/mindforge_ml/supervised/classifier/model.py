import torch
import torch.nn as nn

class IntentClassifierLayer(nn.Module):
  def __init__(self, input_dim, hidden=64, num_classes=4):
    super(IntentClassifier, self).__init__()
    self.model = nn.Sequential(
        nn.Linear(input_dim, 128),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(128, hidden),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(hidden, 32),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(32, num_classes)
    )

  def forward(self, x):
    return self.model(x)



class IntentClassifier:
    def __init__(self, input_dim, device=None):
       self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
       self.model = IntentClassifierLayer(input_dim).to(self.device)
       self.criterion = nn.CrossEntropyLoss()
       self.optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-4)


    def fit(self, X_train, y_train, X_val, y_val, epochs=50, verbose=True):
       
        self.train_losses = []
        self.train_accuracies = []
        self.val_losses = []
        self.val_accuracies = []

        for epoch in range(epochs):
            # Training 
            self.model.train()
            total_loss = 0
            total_accuracy = 0
            total_batch = 0

            y_preds = self.model(X_train)
            loss = self.criterion(y_preds, y_train)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            preds = torch.argmax(y_preds, dim=1)
            accuracy = (preds == y_train).float().mean().item()

            total_loss += loss.item()
            total_accuracy += accuracy
            total_batch += 1


        avg_loss = total_loss / total_batch
        avg_accuracy = total_accuracy / total_batch

        self.train_losses.append(avg_loss)
        self.train_accuracies.append(avg_accuracy)


        if X_val and y_val:
           # validation
            self.model.eval()
            with torch.inference_mode():
                total_val_loss = 0
                total_val_accuracy = 0
                total_val_batch = 0
                
                y_val_preds = self.model(X_val)

                val_loss = self.criterion(y_val_preds, y_val)
                val_preds = y_val_preds.argmax(dim = 1)

                val_accuracy = (val_preds == y_val).float().mean().item()

                total_val_loss += val_loss.item()
                total_val_accuracy += val_accuracy
                total_val_batch += 1

                avg_val_loss = total_val_loss / total_val_batch
                avg_val_accuracy = total_val_accuracy / total_val_batch

                self.val_losses.append(avg_val_loss)
                self.val_accuracies.append(avg_val_accuracy)
                
            if verbose:
                if (epoch + 1) % 10 == 0:
                    print(f"Epoch [{epoch+1}/{epochs}] || Loss: {self.avg_loss:.4f} || Val Loss: {self.avg_val_loss:.4f} || Accuracy: {self.avg_accuracy:.4f} || Val Acc: {self.avg_val_accuracy:.4f}")
                    

    def predict(self, X_input, idx2label):
        self.model.eval()
        # Forward pass
        with torch.inference_mode():
            y_preds = self.model(X_input)

            # Get probabilities
            probs = torch.softmax(y_preds, dim=1).cpu().numpy()[0]

            # Get prediction index + label
            predicted_idx = torch.argmax(y_preds, dim=1).item()
            prediction = idx2label[predicted_idx]

            # Format probabilities for each class
            probability = {idx2label[i]: f"{prob*100:.2f}%" for i, prob in enumerate(probs)}

            return prediction, probability
        
    def save(self, path="intent_classifier_model.pth"):
        torch.save(self.model.state_dict(), path)

    def load(self, path="intent_classifier_model.pth"):
        self.model.load_state_dict(torch.load(path, map_location=self.device))
        self.model.to(self.device)