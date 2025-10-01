"""
Vendored from smb-mm/models/ecg_fm/ecgfounder/net1d.py
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, data, label):
        self.data = data
        self.label = label

    def __getitem__(self, index):
        return (torch.tensor(self.data[index], dtype=torch.float), torch.tensor(self.label[index], dtype=torch.long))

    def __len__(self):
        return len(self.data)


class MyConv1dPadSame(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, groups=1):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.groups = groups
        self.conv = torch.nn.Conv1d(
            in_channels=self.in_channels,
            out_channels=self.out_channels,
            kernel_size=self.kernel_size,
            stride=self.stride,
            groups=self.groups,
        )

    def forward(self, x):
        net = x
        in_dim = net.shape[-1]
        out_dim = (in_dim + self.stride - 1) // self.stride
        p = max(0, (out_dim - 1) * self.stride + self.kernel_size - in_dim)
        pad_left = p // 2
        pad_right = p - pad_left
        net = F.pad(net, (pad_left, pad_right), "constant", 0)
        net = self.conv(net)
        return net


class MyMaxPool1dPadSame(nn.Module):
    def __init__(self, kernel_size):
        super().__init__()
        self.kernel_size = kernel_size
        self.max_pool = torch.nn.MaxPool1d(kernel_size=self.kernel_size)

    def forward(self, x):
        net = x
        p = max(0, self.kernel_size - 1)
        pad_left = p // 2
        pad_right = p - pad_left
        net = F.pad(net, (pad_left, pad_right), "constant", 0)
        net = self.max_pool(net)
        return net


class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)


class BasicBlock(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        ratio,
        kernel_size,
        stride,
        groups,
        downsample,
        is_first_block=False,
        use_bn=True,
        use_do=True,
    ):
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.ratio = ratio
        self.kernel_size = kernel_size
        self.groups = groups
        self.downsample = downsample
        self.stride = stride if self.downsample else 1
        self.is_first_block = is_first_block
        self.use_bn = use_bn
        self.use_do = use_do

        self.middle_channels = int(self.out_channels * self.ratio)

        self.bn1 = nn.BatchNorm1d(in_channels)
        self.activation1 = Swish()
        self.do1 = nn.Dropout(p=0.5)
        self.conv1 = MyConv1dPadSame(
            in_channels=self.in_channels, out_channels=self.middle_channels, kernel_size=1, stride=1, groups=1
        )

        self.bn2 = nn.BatchNorm1d(self.middle_channels)
        self.activation2 = Swish()
        self.do2 = nn.Dropout(p=0.5)
        self.conv2 = MyConv1dPadSame(
            in_channels=self.middle_channels,
            out_channels=self.middle_channels,
            kernel_size=self.kernel_size,
            stride=self.stride,
            groups=self.groups,
        )

        self.bn3 = nn.BatchNorm1d(self.middle_channels)
        self.activation3 = Swish()
        self.do3 = nn.Dropout(p=0.5)
        self.conv3 = MyConv1dPadSame(
            in_channels=self.middle_channels, out_channels=self.out_channels, kernel_size=1, stride=1, groups=1
        )

        r = 2
        self.se_fc1 = nn.Linear(self.out_channels, self.out_channels // r)
        self.se_fc2 = nn.Linear(self.out_channels // r, self.out_channels)
        self.se_activation = Swish()

        if self.downsample:
            self.max_pool = MyMaxPool1dPadSame(kernel_size=self.stride)

    def forward(self, x):
        identity = x
        out = x
        if not self.is_first_block:
            if self.use_bn:
                out = self.bn1(out)
            out = self.activation1(out)
            if self.use_do:
                out = self.do1(out)
        out = self.conv1(out)
        if self.use_bn:
            out = self.bn2(out)
        out = self.activation2(out)
        if self.use_do:
            out = self.do2(out)
        out = self.conv2(out)
        if self.use_bn:
            out = self.bn3(out)
        out = self.activation3(out)
        if self.use_do:
            out = self.do3(out)
        out = self.conv3(out)

        se = out.mean(-1)
        se = self.se_fc1(se)
        se = self.se_activation(se)
        se = self.se_fc2(se)
        se = torch.sigmoid(se)
        out = torch.einsum("abc,ab->abc", out, se)

        if self.downsample:
            identity = self.max_pool(identity)
        if self.out_channels != self.in_channels:
            identity = identity.transpose(-1, -2)
            ch1 = (self.out_channels - self.in_channels) // 2
            ch2 = self.out_channels - self.in_channels - ch1
            identity = F.pad(identity, (ch1, ch2), "constant", 0)
            identity = identity.transpose(-1, -2)
        out += identity
        return out


class BasicStage(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        ratio,
        kernel_size,
        stride,
        groups,
        i_stage,
        m_blocks,
        use_bn=True,
        use_do=True,
        verbose=False,
    ):
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.ratio = ratio
        self.kernel_size = kernel_size
        self.groups = groups
        self.i_stage = i_stage
        self.m_blocks = m_blocks
        self.use_bn = use_bn
        self.use_do = use_do
        self.verbose = verbose

        self.block_list = nn.ModuleList()
        for i_block in range(self.m_blocks):
            if self.i_stage == 0 and i_block == 0:
                self.is_first_block = True
            else:
                self.is_first_block = False
            if i_block == 0:
                self.downsample = True
                self.stride = stride
                self.tmp_in_channels = self.in_channels
            else:
                self.downsample = False
                self.stride = 1
                self.tmp_in_channels = self.out_channels
            tmp_block = BasicBlock(
                in_channels=self.tmp_in_channels,
                out_channels=self.out_channels,
                ratio=self.ratio,
                kernel_size=self.kernel_size,
                stride=self.stride,
                groups=self.groups,
                downsample=self.downsample,
                is_first_block=self.is_first_block,
                use_bn=self.use_bn,
                use_do=self.use_do,
            )
            self.block_list.append(tmp_block)

    def forward(self, x):
        out = x
        for i_block in range(self.m_blocks):
            net = self.block_list[i_block]
            out = net(out)
        return out


class Net1D(nn.Module):
    def __init__(
        self,
        in_channels,
        base_filters,
        ratio,
        filter_list,
        m_blocks_list,
        kernel_size,
        stride,
        groups_width,
        n_classes,
        use_bn=True,
        use_do=True,
        return_features=False,
        verbose=False,
    ):
        super().__init__()

        self.in_channels = in_channels
        self.base_filters = base_filters
        self.ratio = ratio
        self.filter_list = filter_list
        self.m_blocks_list = m_blocks_list
        self.kernel_size = kernel_size
        self.stride = stride
        self.groups_width = groups_width
        self.n_stages = len(filter_list)
        self.n_classes = n_classes
        self.use_bn = use_bn
        self.use_do = use_do
        self.return_features = return_features
        self.verbose = verbose

        self.first_conv = MyConv1dPadSame(
            in_channels=in_channels, out_channels=self.base_filters, kernel_size=self.kernel_size, stride=2
        )
        self.first_bn = nn.BatchNorm1d(base_filters)
        self.first_activation = Swish()

        self.stage_list = nn.ModuleList()
        in_channels = self.base_filters
        for i_stage in range(self.n_stages):
            out_channels = self.filter_list[i_stage]
            m_blocks = self.m_blocks_list[i_stage]
            tmp_stage = BasicStage(
                in_channels=in_channels,
                out_channels=out_channels,
                ratio=self.ratio,
                kernel_size=self.kernel_size,
                stride=self.stride,
                groups=out_channels // self.groups_width,
                i_stage=i_stage,
                m_blocks=m_blocks,
                use_bn=self.use_bn,
                use_do=self.use_do,
                verbose=self.verbose,
            )
            self.stage_list.append(tmp_stage)
            in_channels = out_channels

        self.dense = nn.Linear(in_channels, n_classes)

    def forward(self, x):
        out = x
        out = self.first_conv(out)
        if self.use_bn:
            out = self.first_bn(out)
        out = self.first_activation(out)
        for i_stage in range(self.n_stages):
            net = self.stage_list[i_stage]
            out = net(out)
        deep_features = out.mean(-1)
        output = self.dense(deep_features)
        if self.return_features:
            return output, out.transpose(2, 1)
        else:
            return output


