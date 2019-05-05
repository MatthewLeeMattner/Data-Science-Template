import tensorflow as tf


def define_model():
    pass

def load_model(model_location, model_define_func):
    model = model_define_func()
    model.load_weights(model_location)
