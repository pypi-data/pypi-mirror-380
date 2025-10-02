import torch
from position_encoding import get_relative_position_encoding_matrix


def test_positional_encoding():
    maxlen = 16

    code = get_relative_position_encoding_matrix(maxlen, 32)

    assert torch.all(code[0, 0] == code[5, 5])
    assert torch.all(code[0, 1] == code[5, 6])
    assert torch.all(code[1, 0] == code[6, 5])
    assert torch.any(code[5, 0] != code[0, 5])

    assert torch.any(code[0, 10] != code[2, 5])
