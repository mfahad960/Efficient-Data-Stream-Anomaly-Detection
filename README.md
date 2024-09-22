
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
Z= (X−μ)/σ
​
Where:
- "X" is the data point,
- "μ" is the mean of the sliding window,
- "σ" is the standard deviation of the sliding window.

## How It Works

1. **Data Stream Generation**: The system generates a noisy sine wave using the `generate_data_stream()` function, where 3% of the values are randomly chosen to be anomalies (amplified by a factor of 2).
   
2. **Sliding Window**: The system uses a rolling window of recent data points to compute the mean and standard deviation for anomaly detection.

3. **Anomaly Detection**: The **Z-Score** is calculated for each new data point. If the Z-Score exceeds the threshold (default is 4), the data point is flagged as an anomaly.

4. **Real-Time Plot**: The data points are plotted in real-time using **Matplotlib**, with anomalies highlighted in red.

## Code Breakdown

### Key Functions

- `generate_data_stream()`: Simulates a continuous, oscillating data stream represented by a sine wave and noise. Occasional anomalies are injected.
- `z_score_algorithm()`: Calculates the Z-Score for a data point and determines if it is an anomaly.
- `detect_anomalies()`: Applies the Z-score algorithm to the data stream and stores the indices of detected anomalies.
- `real_time_plot()`: Plots the data stream in real-time, marking anomalies as red points.

### Error Handling and Edge Cases

- **Division by Zero**: In case the standard deviation of the window is zero (when all data points are the same), the Z-Score is set to zero, and no anomaly is flagged.
- **Real-Time Simulation**: Data is streamed with a 0.01-second delay to mimic real-time behavior, handled by `time.sleep()`.

## Optimizations

- **Sliding window**: Sliding window implemented with deque for efficient and more performant rolling window management, when using larger window sizes. This is due to deque being O(1) while lists are O(n) when appending or deleting data from the left.

- **Window Size**: The optimal size for the window was determined by trail and error. I found 18-24 units to be optimal for this case, and since the data stream is represented by a since wave, it works well in determining shifts apart from seasonal variations in the curve. Unless the the datapoints representing the anomalies are too close. This can be further improved using Exponentially Weighted Moving Average (EWMA) but I found it overkill for the problem at hand and given the choice of data stream simulation.

- **Threshold**: The Z-Score threshold for flagging anomalies is set to 4 units, since the anomalies are amplified by a factor of 2. This threshold works for both crests and trough values of the sine curve. I found smaller values to increase false positives, due to random noise and variation of the curve, which is also less efficient, while larger values increased false negetives, overlooking key data values.

## Future Improvements

- Experiment with more robust anomaly detection algorithms like **Isolation Forest**,  **Autoencoders** or **Exponentially Weighted Moving Average (EWMA)**.