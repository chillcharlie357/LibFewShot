# -*- coding: utf-8 -*-
import sys

sys.dont_write_bytecode = True

import os
import torch
from core.config import Config
from core import Test



# 5-1 
# PATH = "./results/DeepEMD-miniImageNet--ravi-resnet12_emd-5-1-Jan-04-2024-17-31-25"
# 5-5 
PATH = "./results/DeepEMD-miniImageNet--ravi-resnet12_emd-5-5-Jan-04-2024-17-41-06"
VAR_DICT = {
    "test_epoch": 5,
    "device_ids": "0",
    "n_gpu": 1,
    "test_episode": 20,
    "episode_size": 2,
}


def main(rank, config):
    test = Test(rank, config, PATH)
    test.test_loop()


if __name__ == "__main__":
    config = Config(os.path.join(PATH, "config.yaml"), VAR_DICT).get_config_dict()

    if config["n_gpu"] > 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = config["device_ids"]
        torch.multiprocessing.spawn(main, nprocs=config["n_gpu"], args=(config,))
    else:
        main(0, config)
