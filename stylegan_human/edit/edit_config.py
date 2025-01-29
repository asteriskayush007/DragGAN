# Copyright (c) SenseTime Research. All rights reserved.

attr_dict = {
    'interface_gan': {
        'upper_length': [-1],  # strength: negative for shorter, positive for longer
        'bottom_length': [1]
    },
    'stylespace': {
        'upper_length': [5, -5, 0.0028],  # layer, strength, threshold
        'bottom_length': [3, 5, 0.003]
    },
    'sefa': {
        'upper_length': [[4, 5, 6, 7], 5],  # layer, strength
        'bottom_length': [[4, 5, 6, 7], 5]
    }
}
