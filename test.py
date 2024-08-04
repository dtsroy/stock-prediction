import pystocky

config = pystocky.config.init_from_dict({
    'data': 'data/GOOG.csv',
    'output': 'model/'
})

trainer = pystocky.trainer.Trainer(config)
trainer.train()
trainer.show()