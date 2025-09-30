"""Utility functions related to calculations"""
from typing import List
import numpy as np


def normalize_array(my_array: np.ndarray) -> np.ndarray:
    """ Normalize the values in an array to sum to 1"""
    motif_base_freq = my_array / sum(my_array)
    return motif_base_freq


def convert_pfm_to_ppm(pfm: np.ndarray) -> np.ndarray:
    """ Convert position frequency matrix to position \
        probability matrix

    Parameters
    ----------
    pfm: np.ndarray
        A single motif in position frequency matrix format \
        2-D numpy array

    Return
    ------
    ppm: np.ndarray
        A single motif in position probability matrix format
    """
    ppm = []
    for row in pfm:
        ppm.append(normalize_array(row))
    return np.array(ppm)


def sample_lengths(
        len_min: int,
        len_max: int,
        num_len: int,
        rng: np.random.Generator) -> List[int]:
    """
    Sample a list of lengths given min and max values (uniform)

    Parameters
    ----------
    len_seq_min: int
        Minimum length to be sampled
    len_seq_max: int
        Maximum length to be sampled (included in range)
    num_seq: int
        Number of lengths to generate
    rng: np.random.Generator
        Random generator for length

    Return
    ------
    _: List[int]
        A list of uniformly sampled lengths
    """
    return rng.integers(
        low=len_min,
        high=len_max,
        endpoint=True,
        size=num_len)
