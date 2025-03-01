# PyStocky: a stock price prediction library based on PyTorch

PyStocky is a stock price prediction library implemented using the PyTorch framework, which utilizes deep learning
models such as LSTM to predict the future trends of the stock market. This library aims to provide financial analysts
and data scientists with a powerful and flexible tool to assist them in market analysis and investment decision-making.

## Characteristics

- **Based on PyTorch**: Utilizing PyTorch's powerful deep learning library for model construction and training.
- **LSTM model**: uses long short-term memory networks to capture long-term dependencies in time series data.
- **Easy to use**: Provides a concise API for quick stock price prediction.
- **Customizability**: allows users to customize model parameters to adapt to different datasets and prediction needs.

## Installation

PyStocky can be installed through pip:

```bash
pip install pystocky
```

## Quick Start

Here are the basic steps on how to use PyStocky for stock price prediction:

### Import the library
```python
import pystocky
```

### Configure
```python
config = pystocky.config.init_from_dict({
    'data': 'data/GOOG.csv',
    'output': 'model/'
})
```

### Train and show the results
```python
trainer = pystocky.trainer.Trainer(config)
trainer.train()
trainer.show()
```

**note: In example above, please make sure there is a line named 'close'**
