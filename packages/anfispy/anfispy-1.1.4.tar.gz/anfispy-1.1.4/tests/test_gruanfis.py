import pytest
import torch
import numpy as np
from ANFISpy.anfis import GRUANFIS

n_vars = 3
n_classes = 2
mf_names = [['L', 'M', 'H']]

variables_reg = {
    'inputs': {
        'n_sets': [3, 3, 3],
        'uod': n_vars * [(0, 1)],
        'var_names': ['a', 'b', 'c'],
        'mf_names': n_vars * mf_names,
    },
    'output': {
        'var_names': 'd',
        'n_classes': 1,
    },
}

variables_cla = {
    'inputs': {
        'n_sets': [3, 3, 3],
        'uod': n_vars * [(0, 1)],
        'var_names': ['a', 'b', 'c'],
        'mf_names': n_vars * mf_names,
    },
    'output': {
        'var_names': 'd',
        'n_classes': n_classes,
    },
}

batch_size = 5
seq_len = 7

x = torch.randn(batch_size, seq_len, n_vars, dtype=torch.float32)
y_reg = torch.randn(batch_size, seq_len, 1, dtype=torch.float32)
y_cla = torch.ones(batch_size, seq_len, dtype=torch.long)

mf_type = ['gaussian', 'bell', 'sigmoid', 'triangular']
bidirectional = [False, True]

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_initialization_regression(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_reg, mf_type, seq_len, bidirectional=bidirectional)
    assert len(gruanfis.input_n_sets) == 3
    assert len(gruanfis.input_uod) == 3
    assert len(gruanfis.input_var_names) == 3
    assert gruanfis.output_var_names == 'd'
    assert gruanfis.output_n_classes == 1

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_initialization_classification(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_cla, mf_type, seq_len, bidirectional=bidirectional)
    assert len(gruanfis.input_n_sets) == 3
    assert len(gruanfis.input_uod) == 3
    assert len(gruanfis.input_var_names) == 3
    assert gruanfis.output_var_names == 'd'
    assert gruanfis.output_n_classes == n_classes

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_regression_forward(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_reg, mf_type, seq_len, bidirectional=bidirectional)
    y_pred = gruanfis(x)[0]
    assert y_pred.shape == (batch_size, seq_len, 1)

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_classification_forward(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_cla, mf_type, seq_len, bidirectional=bidirectional)
    y_pred = gruanfis(x)[0]
    assert y_pred.shape == (batch_size, seq_len, n_classes)

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_training_regression(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_reg, mf_type, seq_len, bidirectional=bidirectional)
    optimizer = torch.optim.Adam(gruanfis.parameters(), lr=0.01)
    criterion = torch.nn.MSELoss()

    for _ in range(5):  
        optimizer.zero_grad()
        y_pred = gruanfis(x)[0]
        loss = criterion(y_pred, y_reg)
        loss.backward()
        optimizer.step()

    for name, param in gruanfis.named_parameters():
        assert param.grad is not None
        assert not torch.all(param.grad == 0)

@pytest.mark.parametrize("mf_type,bidirectional", [(mf, bid) for mf in mf_type for bid in bidirectional])
def test_training_classification(mf_type, bidirectional):
    gruanfis = GRUANFIS(variables_cla, mf_type, seq_len, bidirectional=bidirectional)
    optimizer = torch.optim.Adam(gruanfis.parameters(), lr=0.01)
    criterion = torch.nn.CrossEntropyLoss()

    for _ in range(5):  
        optimizer.zero_grad()
        y_pred = gruanfis(x)[0].view(-1, n_classes)
        loss = criterion(y_pred, y_cla.view(-1))
        loss.backward()
        optimizer.step()

    for name, param in gruanfis.named_parameters():
        assert param.grad is not None
        assert not torch.all(param.grad == 0)