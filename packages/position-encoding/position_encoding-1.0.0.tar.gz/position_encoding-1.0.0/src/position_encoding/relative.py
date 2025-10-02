import torch


def get_relative_position_encoding_matrix(max_length: int, encoding_depth: int = 0) -> torch.Tensor:
    """Get a one-hot encoded relative position matrix (not masked).

    It distinguishes between left side (.., -2, -1, 0) and right side (0, 1, 2, ..) relative positions.

    Args:
        max_length: max length of the encoded sequence
        encoding_depth: dimensionality for relative position one hot encoding,
                        by default it makes the encoding as large as necessary to fit all relative positions.

    Returns:
        one hot encoded relative positions: [max_length, max_length, encoding_depth]
    """
    if encoding_depth == 0:
        encoding_depth = 2 * max_length - 1

    # Direct computation without intermediate large tensors
    i_coords = torch.arange(max_length).unsqueeze(1)  # [max_length, 1]
    j_coords = torch.arange(max_length).unsqueeze(0)  # [1, max_length]

    # Compute relative positions and map to indices
    rel_pos = i_coords - j_coords  # [max_length, max_length]
    bin_indices = rel_pos + (max_length - 1)  # Shift to [0, 2*max_length-2]

    # Clamp if encoding_depth is smaller
    bin_indices = torch.clamp(bin_indices, 0, encoding_depth - 1)

    return torch.nn.functional.one_hot(bin_indices, num_classes=encoding_depth)
