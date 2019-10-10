# System libs
import os
import random
import time

# Numerical libs
import torch
import torch.nn.functional as F
import numpy as np
import scipy.io.wavfile as wavfile
from scipy.misc import imsave
from mir_eval.separation import bss_eval_sources

# Our libs
from arguments import ArgParser
from dataset import MUSICMixDataset
from models import ModelBuilder, activate
from utils import AverageMeter, \
    recover_rgb, magnitude2heatmap, \
    istft_reconstruction, warpgrid, \
    combine_video_audio, save_video, makedirs
from viz import plot_loss_metrics, HTMLVisualizer
import imageio

if __name__ == "__main__":
    dataset_train = MUSICMixDataset(
            args.list_train, args, split='train')
        
    loader_train = torch.utils.data.DataLoader(
        dataset_train,
        batch_size=20,
        shuffle=True,
        num_workers=0,
        drop_last=True)

    load_data=iter(loader_train)
    print(next(load_data))