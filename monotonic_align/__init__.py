import numpy as np
from monotonic_align.core import maximum_path_c
import torch


def maximum_path(neg_cent, mask):
  """ Cython optimized version.
  neg_cent: [b, t_y, t_x]
  mask: [b, t_y, t_x]
  """
  device = neg_cent.device
  dtype = neg_cent.dtype
  neg_cent = neg_cent.contiguous().data.cpu().numpy().astype(np.float32)
  path = np.zeros(neg_cent.shape, dtype=np.int32)

  t_y_max = mask.sum(1)[:, 0].data.cpu().numpy().astype(np.int32)
  t_x_max = mask.sum(2)[:, 0].data.cpu().numpy().astype(np.int32)
  maximum_path_c(path, neg_cent, t_y_max, t_x_max)
  return torch.from_numpy(path).to(device=device, dtype=dtype)