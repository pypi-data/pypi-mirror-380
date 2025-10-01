import numpy as np
from baremetalml import BaseTransformer
class NormalScaler(BaseTransformer):
    def fit(self, X):
        X = self.check_x(X)
        self.min = X.min(axis=0)
        self.max = X.max(axis=0)
        
    def transform(self, X):
        X = self.check_x(X)
        range_ = self.max - self.min
        range_[range_ == 0] = 1           
        X_norm = (X - self.min) / range_  
        return X_norm
    

    



        
        
