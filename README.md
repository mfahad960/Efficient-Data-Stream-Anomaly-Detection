
# Efficient Data Stream Anomaly Detection

## Overview

This project focuses on detecting anomalies in a real-time data stream. The data stream is simulated using a sine wave with added noise, and random anomalies are injected to test the detection system. Anomalies are detected using the **Z-Score algorithm**, which flags data points that deviate significantly from the mean of recent data points.

The project is implemented using **Python 3.x**, with a real-time visualization of the data stream and anomalies.

## Project Objectives

1. **Algorithm Selection**: The **Z-Score algorithm** was chosen for anomaly detection due to its simplicity and efficiency for stationary data streams.
2. **Data Stream Simulation**: A function simulates real-time streaming data using a sine wave with random noise and anomalies.
3. **Anomaly Detection**: The system identifies anomalies based on deviations from the normal pattern in real-time using a sliding window for context.
4. **Optimization**: The solution is optimized for speed and efficiency using Python’s built-in functions and a sliding window technique.
5. **Visualization**: Real-time visualization is implemented to display the streaming data and highlight any detected anomalies.

## Z-Score Algorithm

The **Z-Score** method detects anomalies by calculating how many standard deviations a data point is from the mean of the recent data (stored in a sliding window). If a data point’s Z-Score exceeds a set threshold, it is flagged as an anomaly.

### Z-Score Formula:
\[
Z = \frac{X - \mu}{\sigma}
\]
Where:
- \(X\) is the data point,
- \(\mu\) is the mean of the sliding window,
- \(\sigma\) is the standard deviation of the sliding window.

The algorithm is effective for detecting spikes or unusual deviations in normally distributed or stationary data, but it may struggle with non-stationary data (concept drift).

## Features

- **Real-Time Data Simulation**: A sine wave with noise and random anomaly injection.
- **Z-Score Based Anomaly Detection**: Efficient detection of anomalies based on statistical deviation.
- **Real-Time Visualization**: Continuous plotting of data and marking detected anomalies.
- **Performance Optimization**: Sliding window implemented with `deque` for efficient rolling window management.

## Installation

To run this project, you need **Python 3.x** and the following libraries:

1. **Numpy** (for mathematical operations)
2. **Matplotlib** (for real-time plotting)

You can install the required libraries using `pip`:

```bash
pip install numpy matplotlib
```

### File Structure

- `main.py`: Contains the main logic for data stream simulation, anomaly detection, and real-time plotting.
- `README.md`: This file, describing the project setup, usage, and explanation of the algorithm.

## Running the Project

1. Clone the repository or download the project files.
2. Install the required libraries using `pip`.
3. Run the `main.py` file using Python:

```bash
python main.py
```

This will simulate a real-time data stream and detect anomalies as they occur.

## How It Works

1. **Data Stream Generation**: The system generates a noisy sine wave using the `generate_data_stream()` function, where 3% of the values are randomly chosen to be anomalies (amplified by a factor of 2).
   
2. **Sliding Window**: The system uses a rolling window of recent data points to compute the mean and standard deviation for anomaly detection.

3. **Anomaly Detection**: The **Z-Score** is calculated for each new data point. If the Z-Score exceeds the threshold (default is 4), the data point is flagged as an anomaly.

4. **Real-Time Plot**: The data points are plotted in real-time using **Matplotlib**, with anomalies highlighted in red.

## Code Breakdown

### Key Functions

- `generate_data_stream()`: Simulates a continuous data stream with a sine wave and noise. Occasional anomalies are injected.
- `z_score_algorithm()`: Calculates the Z-Score for a data point and determines if it’s an anomaly.
- `detect_anomalies()`: Applies the Z-Score algorithm to the data stream and stores the indices of detected anomalies.
- `real_time_plot()`: Plots the data stream in real-time, marking anomalies as red points.

### Error Handling and Edge Cases

- **Division by Zero**: In case the standard deviation of the window is zero (when all data points are the same), the Z-Score is set to zero, and no anomaly is flagged.
- **Real-Time Simulation**: Data is streamed with a 0.01-second delay to mimic real-time behavior, handled by `time.sleep()`.

## Customization

You can customize several parameters:
- **Window Size**: The size of the sliding window for the Z-Score calculation.
- **Threshold**: The Z-Score threshold for flagging anomalies (default is 4).
- **Anomaly Probability**: The likelihood of injecting an anomaly into the data stream.

Example:

```python
data_stream = generate_data_stream(length=5000, scale_factor=3, seasonality=100, noise=0.05, anomaly_probability=0.05)
processed_stream = detect_anomalies(data_stream, window_size=30, threshold=3)
```

## Limitations

- **Stationarity**: The Z-Score method assumes the data follows a stationary distribution. It may not adapt well to concept drift or non-stationary data.
- **Simplicity**: While efficient for simple outlier detection, more complex techniques (e.g., Isolation Forest, LOF) might be needed for advanced anomaly detection scenarios.

## Future Improvements

- Introduce **adaptive thresholds** to handle concept drift.
- Experiment with more robust anomaly detection algorithms like **Isolation Forest** or **Autoencoders**.
- Implement a more advanced **data validation** process to handle different data types.