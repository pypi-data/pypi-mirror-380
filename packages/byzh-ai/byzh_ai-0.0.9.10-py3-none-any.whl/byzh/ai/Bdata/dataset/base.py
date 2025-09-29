import os
import numpy as np
import torch
from torchvision import datasets
from typing import Literal
from pathlib import Path
from byzh.core import B_os

from ..standard import b_data_standard2d

class Download_Base:
    def __init__(self, save_dir=..., mean=None, std=None):
        self.save_dir = save_dir
        self.name = Path(save_dir).name
        self.mean = mean
        self.std = std

        self.num_classes = self._get_num_classes()
        self.shape = self._get_shape()

        self.save_paths = [
            os.path.join(self.save_dir, f'{self.name}_X_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_train.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test.pt'),
            os.path.join(self.save_dir, f'{self.name}_y_test.pt'),
        ]
        self.save_paths_standard = [
            os.path.join(self.save_dir, f'{self.name}_X_train_standard.pt'),
            os.path.join(self.save_dir, f'{self.name}_X_test_standard.pt'),
        ]

    def _get_num_classes(self):
        raise NotImplementedError
    def _get_shape(self):
        raise NotImplementedError
    def download(self):
        raise NotImplementedError

    def standardization(self):
        if self._check(self.save_paths_standard):
            X_train_standard = torch.load(self.save_paths_standard[0])
            X_test_standard = torch.load(self.save_paths_standard[1])
            return X_train_standard, X_test_standard
        elif self._check(self.save_paths):
            X_train = torch.load(self.save_paths[0])
            X_test = torch.load(self.save_paths[2])
            # 转换
            X_train_standard, X_test_standard = b_data_standard2d([X_train, X_test], template_data=X_train, mean=self.mean, std=self.std)
            # 保存
            os.makedirs(self.save_dir, exist_ok=True)
            torch.save(X_train_standard, self.save_paths_standard[0])
            torch.save(X_test_standard, self.save_paths_standard[1])
            return X_train_standard, X_test_standard
        else:
            raise ValueError(f"{self.name} 不存在, 请先下载~")
    def get_data(self):
        '''
        keys: 'num_classes', 'X_train', 'y_train', 'X_test', 'y_test', 'X_train_standard', 'X_test_standard'
        :return:
        '''
        result = dict()
        result['num_classes'] = self.num_classes

        X_train, y_train, X_test, y_test = self.download()
        result['X_train'] = X_train
        result['y_train'] = y_train
        result['X_test'] = X_test
        result['y_test'] = y_test

        X_train_standard, X_test_standard = self.standardization()
        result['X_train_standard'] = X_train_standard
        result['X_test_standard'] = X_test_standard

        return result

    def _check(self, filepaths:list):
        flag = True
        for filepath in filepaths:
            flag = flag and os.path.exists(filepath)
        return flag
