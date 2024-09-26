
from DataStream import DataStream
from RealTimeDetector import RealTimeDetector
from RealTimeVisualizer import RealTimeVisualizer


if __name__ == "__main__":

    try:
        data_stream = DataStream(initial_value=100, volatility= 0.5,seasonality_period=20)
        ks_detector = RealTimeDetector(window_size=10)
        visualizer = RealTimeVisualizer(data_stream, ks_detector)

        visualizer.start()

    except Exception as e:
        print(f"Error in main: {e}")