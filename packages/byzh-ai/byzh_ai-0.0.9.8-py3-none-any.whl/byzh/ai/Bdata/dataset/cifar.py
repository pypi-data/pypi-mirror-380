import os
import numpy as np
import torch
from torchvision import datasets
from typing import Literal
from pathlib import Path
from byzh.core import B_os

from ..standard import b_data_standard2d

class B_Download_CIFAR10:
    def __init__(self, save_dir='./CIFAR10', mean=None, std=None):
        self.save_dir = save_dir
        self.name = Path(save_dir).name
        self.mean = mean
        self.std = std

        self.num_classes = 10

    def __check(self, filepaths: list):
        flag = True
        for filepath in filepaths:
            flag = flag and os.path.exists(filepath)
        return flag

    def b_get_CIFAR10_TV(self):
        '''
        采用 torchvision 下载数据集\n

        :param save_dir:
        :return: X_train, y_train, X_test, y_test
        '''
        downloading_dir = os.path.join(self.save_dir, f'{self.name}_download_dir')
        save_paths = [
            os.path.join(self.save_dir, f'{self.name}_X_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_test.pt'),
        ]

        if self.__check(save_paths):
            X_train = torch.load(save_paths[0])
            y_train = torch.load(save_paths[1])
            X_test = torch.load(save_paths[2])
            y_test = torch.load(save_paths[3])
            return X_train, y_train, X_test, y_test

        # 未标准化
        train_data = datasets.CIFAR10(root=downloading_dir, train=True, download=True)
        test_data = datasets.CIFAR10(root=downloading_dir, train=False, download=True)

        # 拆分
        X_train = torch.tensor(train_data.data).permute(0, 3, 1, 2) / 255.0  # shape [50000, 3, 32, 32]
        y_train = torch.tensor(train_data.targets)  # shape [50000]
        X_test = torch.tensor(test_data.data).permute(0, 3, 1, 2) / 255.0  # shape [10000, 3, 32, 32]
        y_test = torch.tensor(test_data.targets)  # shape [10000]
        print(f"X_train.shape: {X_train.shape}")
        print(f"y_train.shape: {y_train.shape}")
        print(f"X_test.shape: {X_test.shape}")
        print(f"y_test.shape: {y_test.shape}")
        B, C, H, W = X_train.shape
        print(f"X_train[{B // 2}, {C // 2}, {H // 2}]=\n{X_train[B // 2, C // 2, H // 2]}")

        # 标准化
        X_train, X_test = b_data_standard2d([X_train, X_test], template_data=X_train, mean=self.mean, std=self.std)

        # 保存
        os.makedirs(self.save_dir, exist_ok=True)
        torch.save(X_train, save_paths[0])
        torch.save(y_train, save_paths[1])
        torch.save(X_test, save_paths[2])
        torch.save(y_test, save_paths[3])

        B_os.rm(downloading_dir)

        return X_train, y_train, X_test, y_test

    def b_get_CIFAR10_HF(self):
        """
        使用 Hugging Face datasets 下载 MNIST

        :param save_dir: 保存路径
        :param mean, std: 标准化用
        :return: X_train, y_train, X_test, y_test (torch.Tensor)
        """
        save_paths = [
            os.path.join(self.save_dir, f'{self.name}_X_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_test.pt'),
        ]

        if self.__check(save_paths):
            X_train = torch.load(save_paths[0])
            y_train = torch.load(save_paths[1])
            X_test = torch.load(save_paths[2])
            y_test = torch.load(save_paths[3])
            return X_train, y_train, X_test, y_test

        # HF 数据集
        from datasets import load_dataset
        train_ds = load_dataset("uoft-cs/cifar10", split="train")
        test_ds = load_dataset("uoft-cs/cifar10", split="test")

        # 转 torch.Tensor
        X_train = torch.tensor(np.stack([np.array(img) for img in train_ds['img']])).permute(0, 3, 1, 2) / 255.0
        y_train = torch.tensor(train_ds['label'])
        X_test = torch.tensor(np.stack([np.array(img) for img in test_ds['img']])).permute(0, 3, 1, 2) / 255.0
        y_test = torch.tensor(test_ds['label'])
        print(f"X_train.shape: {X_train.shape}")
        print(f"y_train.shape: {y_train.shape}")
        print(f"X_test.shape: {X_test.shape}")
        print(f"y_test.shape: {y_test.shape}")
        B, C, H, W = X_train.shape
        print(f"X_train[{B // 2}, {C // 2}, {H // 2}]=\n{X_train[B // 2, C // 2, H // 2]}")

        # 标准化
        X_train, X_test = b_data_standard2d([X_train, X_test], template_data=X_train, mean=self.mean, std=self.std)

        # 保存
        os.makedirs(self.save_dir, exist_ok=True)
        torch.save(X_train, save_paths[0])
        torch.save(y_train, save_paths[1])
        torch.save(X_test, save_paths[2])
        torch.save(y_test, save_paths[3])

        return X_train, y_train, X_test, y_test


class B_Download_CIFAR100:
    def __init__(self, save_dir='./CIFAR100', mean=None, std=None):
        self.save_dir = save_dir
        self.name = Path(save_dir).name
        self.mean = mean
        self.std = std

        self.num_classes = 100

    def __check(self, filepaths: list):
        flag = True
        for filepath in filepaths:
            flag = flag and os.path.exists(filepath)
        return flag

    def download_TV(self):
        '''
        采用 torchvision 下载数据集\n

        :param save_dir:
        :return: X_train, y_train, X_test, y_test
        '''
        downloading_dir = os.path.join(self.save_dir, f'{self.name}_download_dir')
        save_paths = [
            os.path.join(self.save_dir, f'{self.name}_X_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_test.pt'),
        ]

        if self.__check(save_paths):
            X_train = torch.load(save_paths[0])
            y_train = torch.load(save_paths[1])
            X_test = torch.load(save_paths[2])
            y_test = torch.load(save_paths[3])
            return X_train, y_train, X_test, y_test

        # 未标准化
        train_data = datasets.CIFAR100(root=downloading_dir, train=True, download=True)
        test_data = datasets.CIFAR100(root=downloading_dir, train=False, download=True)

        # 拆分
        X_train = torch.tensor(train_data.data).permute(0, 3, 1, 2) / 255.0  # shape [50000, 3, 32, 32]
        y_train = torch.tensor(train_data.targets)  # shape [50000]
        X_test = torch.tensor(test_data.data).permute(0, 3, 1, 2) / 255.0  # shape [10000, 3, 32, 32]
        y_test = torch.tensor(test_data.targets)  # shape [10000]
        print(f"X_train.shape: {X_train.shape}")
        print(f"y_train.shape: {y_train.shape}")
        print(f"X_test.shape: {X_test.shape}")
        print(f"y_test.shape: {y_test.shape}")
        B, C, H, W = X_train.shape
        print(f"X_train[{B // 2}, {C // 2}, {H // 2}]=\n{X_train[B // 2, C // 2, H // 2]}")

        # 标准化
        X_train, X_test = b_data_standard2d([X_train, X_test], template_data=X_train, mean=self.mean, std=self.std)

        # 保存
        os.makedirs(self.save_dir, exist_ok=True)
        torch.save(X_train, save_paths[0])
        torch.save(y_train, save_paths[1])
        torch.save(X_test, save_paths[2])
        torch.save(y_test, save_paths[3])

        B_os.rm(downloading_dir)

        return X_train, y_train, X_test, y_test

    def download_HF(self, label_type: Literal['fine_label', 'coarse_label'] = 'fine_label'):
        """
        使用 Hugging Face datasets 下载 MNIST

        :param save_dir: 保存路径
        :param mean, std: 标准化用
        :return: X_train, y_train, X_test, y_test (torch.Tensor)
        """
        save_paths = [
            os.path.join(self.save_dir, f'{self.name}_X_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_test.pt'),
        ]

        if self.__check(save_paths):
            X_train = torch.load(save_paths[0])
            y_train = torch.load(save_paths[1])
            X_test = torch.load(save_paths[2])
            y_test = torch.load(save_paths[3])
            return X_train, y_train, X_test, y_test

        # HF 数据集
        from datasets import load_dataset
        train_ds = load_dataset("uoft-cs/cifar100", split="train")
        test_ds = load_dataset("uoft-cs/cifar100", split="test")

        # 转 torch.Tensor
        X_train = torch.tensor(np.stack([np.array(img) for img in train_ds['img']])).permute(0, 3, 1, 2) / 255.0
        y_train = torch.tensor(train_ds[label_type])  # fine_label是100类, coarse_label是20类
        X_test = torch.tensor(np.stack([np.array(img) for img in test_ds['img']])).permute(0, 3, 1, 2) / 255.0
        y_test = torch.tensor(test_ds[label_type])  # fine_label是100类, coarse_label是20类
        print(f"X_train.shape: {X_train.shape}")
        print(f"y_train.shape: {y_train.shape}")
        print(f"X_test.shape: {X_test.shape}")
        print(f"y_test.shape: {y_test.shape}")
        B, C, H, W = X_train.shape
        print(f"X_train[{B // 2}, {C // 2}, {H // 2}]=\n{X_train[B // 2, C // 2, H // 2]}")

        # 标准化
        X_train, X_test = b_data_standard2d([X_train, X_test], template_data=X_train, mean=self.mean, std=self.std)

        # 保存
        os.makedirs(self.save_dir, exist_ok=True)
        torch.save(X_train, save_paths[0])
        torch.save(y_train, save_paths[1])
        torch.save(X_test, save_paths[2])
        torch.save(y_test, save_paths[3])

        return X_train, y_train, X_test, y_test