"""
Internal module
Custom dataset for training and prediction
"""

from torch.utils.data import Dataset


class TimeSeriesDatasetForLSTM(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, i):
        return self.x[i], self.y[i]

    def get(self):
        return self.x, self.y
