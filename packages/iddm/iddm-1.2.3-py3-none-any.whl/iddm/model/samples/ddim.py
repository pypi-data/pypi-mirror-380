#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2023/7/7 9:55
    @Author : chairc
    @Site   : https://github.com/chairc
"""
from typing import Optional, List, Union

import torch
import logging
import coloredlogs
from torch import nn

from tqdm import tqdm

from iddm.model.samples.base import BaseDiffusion

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


class DDIMDiffusion(BaseDiffusion):
    """
    DDIM class
    """

    def __init__(
            self,
            noise_steps: int = 1000,
            sample_steps: int = 100,
            beta_start: float = 1e-4,
            beta_end: float = 2e-2,
            img_size: Optional[List[int]] = None,
            device: Union[str, torch.device] = "cpu",
            schedule_name: str = "linear",
            latent: bool = False,
            latent_channel: int = 8,
            autoencoder: Optional[nn.Module] = None
    ):
        """
        The implement of DDIM
        Paper: Denoising Diffusion Implicit Models
        URL: https://arxiv.org/abs/2010.02502
        :param noise_steps: Noise steps
        :param sample_steps: Sample steps
        :param beta_start: β start
        :param beta_end: β end
        :param img_size: Image size
        :param device: Device type
        :param schedule_name: Prepare the noise schedule name
        :param latent: Whether to use latent diffusion
        :param latent_channel: Latent channel size, default is 8
        :param autoencoder: Autoencoder model, if provided, will be used for latent diffusion
        """
        super().__init__(noise_steps=noise_steps, beta_start=beta_start, beta_end=beta_end, img_size=img_size,
                         device=device, schedule_name=schedule_name, latent=latent, latent_channel=latent_channel,
                         autoencoder=autoencoder)
        # Sample steps, it skips some steps
        self.sample_steps = sample_steps

        self.eta = 0

        # Calculate time step size, it skips some steps
        self._init_time_step()

    def _init_time_step(self):
        """
        Initialize the time step for DDIM sampling
        :return: List of tuples (current step, previous step)
        """
        self.time_step = torch.arange(0, self.noise_steps, (self.noise_steps // self.sample_steps)).long() + 1
        self.time_step = reversed(torch.cat((torch.tensor([0], dtype=torch.long), self.time_step)))
        self.time_step = list(zip(self.time_step[:-1], self.time_step[1:]))

    def _sample_loop(
            self,
            model: nn.Module,
            x: Optional[torch.Tensor] = None,
            n: int = 1,
            labels: Optional[torch.Tensor] = None,
            cfg_scale: Optional[float] = None
    ) -> torch.Tensor:
        """
        DDPM sample loop method
        :param model: Model
        :param x: Input image tensor, if provided, will be used as the starting point for sampling
        :param n: Number of sample images, x priority is greater than n
        :param labels: Labels
        :param cfg_scale: classifier-free guidance interpolation weight, users can better generate model effect.
        Avoiding the posterior collapse problem, Reference paper: 'Classifier-Free Diffusion Guidance'
        :return: Sample images
        """
        # The list of current time and previous time
        for i, p_i in tqdm(self.time_step):
            # Time step, creating a tensor of size n
            t = (torch.ones(n) * i).long().to(self.device)
            # Previous time step, creating a tensor of size n
            p_t = (torch.ones(n) * p_i).long().to(self.device)
            # Expand to a 4-dimensional tensor, and get the value according to the time step t
            alpha_t = self.alpha_hat[t][:, None, None, None]
            alpha_prev = self.alpha_hat[p_t][:, None, None, None]
            noise = torch.randn_like(x) if i > 1 else torch.zeros_like(x)

            # Predict noise
            predicted_noise = self._get_predicted_noise(model, x, t, labels, cfg_scale)

            # Calculation formula
            # Division would cause the value to be too large or too small, and it needs to be constrained
            # https://github.com/ermongroup/ddim/blob/main/functions/denoising.py#L54C12-L54C54
            x0_t = torch.clamp((x - (predicted_noise * torch.sqrt((1 - alpha_t)))) / torch.sqrt(alpha_t), -1, 1)
            # Sigma
            c1 = self.eta * torch.sqrt((1 - alpha_t / alpha_prev) * (1 - alpha_prev) / (1 - alpha_t))
            c2 = torch.sqrt((1 - alpha_prev) - c1 ** 2)
            # Predicted x0 + direction pointing to xt + sigma * predicted noise
            x = torch.sqrt(alpha_prev) * x0_t + c2 * predicted_noise + c1 * noise

        return x
