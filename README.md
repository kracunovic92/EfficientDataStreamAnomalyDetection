# Explanation

## Algorithm Selection

I choose to use z-scores combined with a dynamic threshold. Z-score is effective for detecting anomalies in continuous data streams because they mesure how far point deviates from the mean, accounting for variability.
Additionaly, I decided to use dynamic threshold  which helps addapting to new patterns, making it capable of handling concept drift and seasonal variations.

## Data Stream Simulation

For simulation I decided using Brownian motion that simulates volatility, with added periodic sinusoidal function which add seasonality to my data. This makes my stream highly versatile, allowing the detection algorithm to work on varied data patterns. The simulated anomalies based on a probability model further enhance the realism.

## Real-Time Anomaly Detection

The real-time detection method is efficient, continuously updating the reference window and calculating z-scores for each new data point. It ensures that anomalies are flagged as soon as they occur, maintaining a balance between detection speed and accuracy. By adjusting the threshold dynamically, the detector avoids false positives that might occur due to temporary spikes, ensuring more reliable anomaly detection.

## Optimization

The algorithm only requires basic statistics (mean and standard deviation), making it computationally lightweight and scalable for large streams.

## Visualization
The RealTimeVisualizer provides a clear, interactive plot that highlights both the data stream and detected anomalies. This fulfills the project’s requirement for straightforward visualization. Using real-time plotting gives immediate feedback on the algorithm's performance, making it easy to evaluate how well it adapts to concept drift and seasonal changes.
