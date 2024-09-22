import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

# Function to simulate a sine wave data stream with added noise
def generate_data_stream(l = 1000, scale_factor = 2, seasonality = 80, noise = 0.02, anomaly_probability = 0.03):
    """
    Function to generate a streaming sine wave data with noise and random anomalies.
    """
    for i in range(l):
        y = scale_factor * np.sin(i/seasonality)+(np.random.randn() * noise)        #sin curve with random noise
        if np.random.rand() < anomaly_probability:          # adding random anomaly to the curve
            y *= 2
        yield y
        time.sleep(0.01)

def z_score_algorithm(window, value, threshold):
    """
    Function to calculate Z-score of given value with respect to nearby values and identify anomalies
    """
    mean = np.mean(window)
    std_dev = np.std(window)

    # avoid division by zero in the case of zero standard deviation
    if std_dev == 0:
        return False, 0
    
    z_score = (value - mean) / std_dev

    # return True if the Z-score is above the threshold (anomaly detected)
    return abs(z_score) > threshold, z_score

def detect_anomalies(data_stream, window_size=24, threshold=4):
    """
    Function to detect anomalies in a real-time streaming data using Z-Score algorithm and sliding window.
    """
    anomalies = []                                          # storing indices of anomalies for visualization
    window = deque(maxlen=window_size)                     # sliding window to provide context of recent data points
    for i, data_point in enumerate(data_stream):
        if len(window) < window_size:
            # Fill the initial rolling window
            window.append(data_point)
        else:
            # perform Z-score anomaly detection
            is_anomaly, z_score = z_score_algorithm(window, data_point, threshold)

            if is_anomaly:
                print(f"Anomaly detected at index {i}: Value = {data_point}, Z-Score = {z_score:.2f}")
                anomalies.append(i)
            
            # update rolling window
            window.append(data_point)
        yield data_point, anomalies


def real_time_plot(data_stream):
    """
    Function to plot the data stream in real-time and highlight the detected anomalies.
    """
    x, y = [], []
    plt.ion()
    fig, ax = plt.subplots()

    for i, (value, anomalies_list) in enumerate(data_stream):
        x.append(i)
        y.append(value)
        
        ax.clear()
        ax.plot(x, y, label="Data Stream")
        
        # highlight anomalies on the plot
        anomaly_values = [y[idx] for idx in anomalies_list]
        anomaly_indices = [x[idx] for idx in anomalies_list]
        ax.scatter(anomaly_indices, anomaly_values, color='red', label="Anomalies", zorder=5)
        
        # labels and legend
        ax.set_title("Real-Time Data Stream with Anomaly Detection")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.grid(True)  # Add grid for better visualization
        ax.legend()

        # added pause to simulate real-time plotting
        plt.pause(0.05)
    
    plt.ioff()  # Turn off interactive mode
    plt.show()

def main():
    data_stream = generate_data_stream()
    processed_stream = detect_anomalies(data_stream)
    real_time_plot(processed_stream)

if __name__ == "__main__":
    main()