import time
import onnxruntime as ort
import numpy as np

def test(session, data, target):
    start = time.time()
    output = session.run([], {"input": data})[0]
    end = time.time()
    print(f"Time: {end - start:.4f} seconds")

    pred = output.argmax(axis=1, keepdims=True)
    correct = np.sum(pred.flatten() == target)
    print(f"Accuracy: {correct}/{1000} ({100.*correct/1000:.0f}%)")

def main():
    # Load data
    npzfile = np.load("data/mnist_test_1000.npz")
    data, target = npzfile["data"], npzfile["target"]

    # Load model
    session = ort.InferenceSession("models/mnist_cnn.onnx")

    # Benchark inference
    test(session, data, target)

if __name__ == '__main__':
    main()
