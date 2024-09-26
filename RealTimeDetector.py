import numpy as np
from collections import deque

class RealTimeDetector:
    """
    Class which detects  anomlies in real-time using classical statistical method.

    """

    def __init__(self, window_size=50, threshold = 3, threshold_rate = 0.1, min_threshold = 2.8):
        if window_size <= 0:
            raise ValueError("window_size must be positive")
        if threshold <= 0:
            raise ValueError("threshold must be positive")
        
        self.window_size = window_size 
        self.reference_window = deque(maxlen=window_size)
        self.z_scores = deque(maxlen=window_size)
        self.dynamic_threshold = threshold
        self.threshold_rate = threshold_rate
        self.min_threshold = min_threshold
        

    def adjust_threshold(self):
        """
        Adjust the threshold based on recent scores in a controlled manner.
        """
        if len(self.z_scores) >= self.window_size:
            mean = np.mean(self.z_scores)
            std = np.std(self.z_scores)
            new_z = mean + std
            max_score = max(new_z, self.min_threshold)
            adjustment = (max_score - self.dynamic_threshold) * self.threshold_rate
            self.dynamic_threshold += adjustment


    def detect_new_anomaly(self, new_value):
        """
        Detect anomalies in incoming data
        """
        if len(self.reference_window) < self.window_size:
            self.reference_window.append(new_value)
            return False
        
        mean = np.mean(self.reference_window)
        std = np.std(self.reference_window)
        score = (new_value - mean) / std if std > 0 else 0

        self.z_scores.append(score)
        self.adjust_threshold()
        self.reference_window.append(new_value)

        if abs(score) >= self.dynamic_threshold:
            return True
        
        return False