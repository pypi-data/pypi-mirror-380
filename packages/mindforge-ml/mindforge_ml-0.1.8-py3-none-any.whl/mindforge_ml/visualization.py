import matplotlib.pyplot as plt

def plot_losses(train_losses, val_losses=None):
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(train_losses, label="Train Loss")
    if val_losses is not None:
        plt.plot(val_losses, label="Val Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Training Curve")
    plt.legend()
    plt.show()

def plot_accuracy(train_accuracy, val_accuracy=None):
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(train_accuracy, label="Train Accuracy")
    if val_accuracy is not None:
        plt.plot(val_accuracy, label="Val Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.title("Training Curve")
    plt.legend()
    plt.show()

def plot_clusters(X_2d, clusters, method="PCA", cmap="viridis"):
    plt.figure(figsize=(7,6))
    plt.scatter(X_2d[:,0], X_2d[:,1], c=clusters, cmap=cmap, s=50)
    plt.colorbar(label="Cluster")
    plt.title(f"Patient Clusters ({method})")
    plt.xlabel("Dim 1")
    plt.ylabel("Dim 2")
    plt.show()

def plot_anomalies(errors, anomalies, threshold):
    # here, make the anomalies optional "errors, anomalies, threshold"
    plt.figure(figsize=(8,5))
    plt.hist(errors, bins=50, alpha=0.7)
    plt.axvline(threshold, color="red", linestyle="--", label="Threshold")
    # Highlight anomalous errors
    plt.hist(errors[anomalies], bins=50, alpha=0.6, color="orange", label="Anomalies")
    
    plt.title("Reconstruction Error Distribution")
    plt.xlabel("Error")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


def plot_prediction(prediction, probability):

    classes = list(probability.keys())
    probs = [float(v.strip('%')) for v in probability.values()]  # convert "92.34%" → 92.34

    plt.figure(figsize=(6,4))
    plt.bar(classes, probs, color="skyblue")
    plt.ylabel("Probability (%)")
    plt.title(f"Prediction: {prediction}")
    plt.ylim(0, 100)

    # Add labels on top of bars
    for i, v in enumerate(probs):
        plt.text(i, v+1, f"{v:.2f}%", ha='center')

    plt.show()

    return prediction, probability