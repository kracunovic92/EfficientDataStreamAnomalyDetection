import numpy as np

    
class DataStream:
    def __init__(self, initial_value=0, drift=0.01, volatility=0.5, seasonality_period = 30, seasonality_amplitude = 1):
        """
        Initialize the DataStream with parameters for simulation, including seasonality.
        
        Arguments:
            initial_value: Initial value for the Brownian motion.
            drift: Mean change per step for the simulation.
            volatility: Standard deviation of the noise for the simulation.
        """
        self.initial_value = initial_value
        self.drift = drift 
        self.volatility = volatility 
        self.current_value = initial_value 
        self.seasonality_period = seasonality_period 
        self.seasonality_amplitude = seasonality_amplitude
        self.anomaly_probability = 0.1

    def generate_data_point(self,step):
        '''
        Generate data point with Brownian Motion with drift
        '''
        anomaly = 0
        if np.random.rand() < self.anomaly_probability:
            anomaly = self.current_value* 0.05 * np.random.choice([-1,1])

        brownian_step = np.random.normal(0, self.volatility)
        seasonal_effect = self.seasonality_amplitude * np.sin(2 * np.pi * step / self.seasonality_period)
        self.current_value += brownian_step + self.drift + seasonal_effect + anomaly
        
        return self.current_value



