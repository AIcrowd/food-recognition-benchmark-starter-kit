
import mmcv
import numpy as np
import torch
from mmcv.ops import RoIPool
from mmcv.parallel import collate, scatter
from mmcv.runner import load_checkpoint

from mmdet.core import get_classes
from mmdet.datasets import replace_ImageToTensor
from mmdet.datasets.pipelines import Compose
from mmdet.models import build_detector
# import time


def inference(model, imgs):

    # start = time.process_time()
    imgs = [imgs]
    cfg = model.cfg
    device = 'cuda:0'
    if isinstance(imgs[0], np.ndarray):
        cfg = cfg.copy()
        # set loading pipeline type
        cfg.data.test.pipeline[0].type = 'LoadImageFromWebcam'

    cfg.data.test.pipeline = replace_ImageToTensor(cfg.data.test.pipeline)
    test_pipeline = Compose(cfg.data.test.pipeline)

    datas = []
    data = dict(img_info=dict(filename=imgs[0]), img_prefix=None)
    # build the data pipeline
    data = test_pipeline(data)
    datas.append(data)

    data = collate(datas, samples_per_gpu=len(imgs))
    # just get the actual data from DataContainer
    data['img_metas'] = [img_metas.data[0] for img_metas in data['img_metas']]
    data['img'] = [img.data[0] for img in data['img']]
    # scatter to specified GPU
    data = scatter(data, [device])[0]
    
    # forward the model
    with torch.no_grad():
        results = model(return_loss=False, rescale=True, **data)
    # your code here    
    # print(time.process_time() - start)
    return results[0]
