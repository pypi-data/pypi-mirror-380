"""
Vendored ECGFounder wrappers to load checkpoints and return features.
"""

import torch
import torch.nn as nn
from .net1d import Net1D


def ft_12lead_ECGFounder(device, pth, n_classes, linear_prob=False):
    model = Net1D(
        in_channels=12,
        base_filters=64,
        ratio=1,
        filter_list=[64, 160, 160, 400, 400, 1024, 1024],
        m_blocks_list=[2, 2, 2, 3, 3, 4, 4],
        kernel_size=16,
        stride=2,
        groups_width=16,
        verbose=False,
        use_bn=False,
        use_do=False,
        n_classes=n_classes,
        return_features=True,
    )

    checkpoint = torch.load(pth, map_location=device, weights_only=False)
    state_dict = checkpoint["state_dict"]
    state_dict = {k: v for k, v in state_dict.items() if not k.startswith("dense.")}
    model.load_state_dict(state_dict, strict=False)

    model.dense = nn.Linear(model.dense.in_features, n_classes).to(device)
    if linear_prob:
        for name, param in model.named_parameters():
            if "dense" not in name:
                param.requires_grad = False
    model.to(device)
    return model


def ft_1lead_ECGFounder(device, pth, n_classes, linear_prob=False):
    model = Net1D(
        in_channels=1,
        base_filters=64,
        ratio=1,
        filter_list=[64, 160, 160, 400, 400, 1024, 1024],
        m_blocks_list=[2, 2, 2, 3, 3, 4, 4],
        kernel_size=16,
        stride=2,
        groups_width=16,
        verbose=False,
        use_bn=False,
        use_do=False,
        n_classes=n_classes,
        return_features=True,
    )

    checkpoint = torch.load(pth, map_location=device, weights_only=False)
    state_dict = checkpoint["state_dict"]
    state_dict = {k: v for k, v in state_dict.items() if not k.startswith("dense.")}
    model.load_state_dict(state_dict, strict=False)

    model.dense = nn.Linear(model.dense.in_features, n_classes).to(device)
    if linear_prob:
        for name, param in model.named_parameters():
            if "dense" not in name:
                param.requires_grad = False
    model.to(device)
    return model


