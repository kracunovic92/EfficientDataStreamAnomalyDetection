import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class RealTimeVisualizer:

    def __init__(self, data_stream, detector):
        self.data_stream = data_stream
        self.detector = detector
        self.x_data = []
        self.y_data = []
        self.anomalies_x = []
        self.anomalies_y = []

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], label="Data Stream")
        self.anomaly_points, = self.ax.plot([], [], 'ro', label="Anomaly")  # Red dots for anomalies
        self.ax.set_title("Real-Time Data Stream with Anomalies")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.ax.legend()


    def update_plot(self, frame):

        try:

            new_value = self.data_stream.generate_data_point(frame)
            is_anomaly = self.detector.detect_new_anomaly(new_value)

            self.x_data.append(frame)
            self.y_data.append(new_value)

            if is_anomaly:
                self.anomalies_x.append(frame)
                self.anomalies_y.append(new_value)
                print(f"Anomaly detected at time {frame}, value: {new_value}")
            
            self.line.set_data(self.x_data, self.y_data)
            self.anomaly_points.set_data(self.anomalies_x,self.anomalies_y)


            self.ax.set_xlim(0, max(self.x_data) + 1)
            self.ax.set_ylim(min(self.y_data) - 1, max(self.y_data) + 1)

            return self.line, self.anomaly_points
        except Exception as e:
            print(f"Error during plot update: {e}")
    
    def start(self):

        animation = FuncAnimation(self.fig, self.update_plot, interval= 500)
        plt.show()

