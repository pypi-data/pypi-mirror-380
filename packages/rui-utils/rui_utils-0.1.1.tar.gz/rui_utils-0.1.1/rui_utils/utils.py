import pickle
import time
from pathlib import Path

import numpy as np
import yaml
from addict import Dict
from loguru import logger


def save_dict(dic: dict | Dict, path: str) -> None:
    r"""
    Save the dict to as pkl/yaml format
    """
    if isinstance(dic, Dict):
        dic = dic.to_dict()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if ".pkl" in str(path):
        with open(path, "wb") as f:
            pickle.dump(dic, f)
    elif ".yaml" in str(path) or ".yml" in str(path):
        with open(path, "w") as f:
            yaml.dump(dic, f, default_flow_style=False)


def GetRunTime(func):
    r"""
    Decorator to get the run time of a function
    """

    def call_func(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        Run_time = end_time - begin_time
        logger.debug(f"{func.__name__} run time: {Run_time:.2f}s")
        return ret

    return call_func


def l2norm(mat: np.ndarray) -> np.ndarray:
    r"""
    L2 norm of numpy array
    """
    stats = np.sqrt(np.sum(mat**2, axis=1, keepdims=True)) + 1e-9
    mat = mat / stats
    return mat
