from math import log
import torch


def get_absolute_position_encoding(max_length: int, encoding_depth: int) -> torch.Tensor:
    """Creates an absolute position encoding for the requested dimensions. (not masked).

    Args:
        max_length: maximum length of the encoded sequence
        encoding_depth: length of the positional encoding vectors per element of the sequence
    Returns:
        absolute position encoding [max_length, encoding_depth]
    """
    # [max_length, encoding_depth]
    pe = torch.zeros(max_length, encoding_depth)

    # [max_length, 1]
    position = torch.arange(0, max_length, dtype=torch.float).unsqueeze(1)

    # [encoding_depth]
    div_term = torch.exp(
        torch.arange(0, encoding_depth, 2).float() * (-log(10000.0) / encoding_depth)
    )

    # [max_length, encoding_depth]
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)

    return pe
