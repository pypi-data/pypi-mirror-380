import torch
import torch.nn as nn

import matplotlib.pyplot as plt
import numpy as np

from .mfs import GaussianMF, BellMF, SigmoidMF, TriangularMF
from .layers import Antecedents, Consequents, Inference, RecurrentInference
from .utils import _plot_var, _plot_rules, _print_rules, _rule_activations

class ANFIS(nn.Module):
    def __init__(
        self, 
        variables, 
        mf_shape, 
        and_operator=torch.prod, 
        output_activation=nn.Identity(), 
    ):
        '''Adaptative Neuro-Fuzzy Inference System with Takagi-Sugeno-Kang architecture. Can perform both regression and
           classification.

        Args:
            variables:            dict with two keys, 'inputs' and 'output'. The 'input' has a dict as its value,
                                  containing four keys: 'n_sets', 'uod', 'var_names' and 'mf_names'. They have lists as                                       
                                  their values, containing, respectively: int with number of fuzzy sets associated to the                                     
                                  variable, tuple/list with the universe of discourse of the variable, str with the name of                                   
                                  the variable and list of str with the name of the fuzzy sets. The lists need to be the                                       
                                  same length, and the index of them are all associated, that is, index 0 represents the                                       
                                  information of the same variable. Now, 'output' has only the keys 'var_names' and                                           
                                  'n_classes', with a str representing the name of the variable and an int with the number                                     
                                  of classes (if the model is a regressor, insert 1). 
            mf_shape:             str containing the shape of the fuzzy sets of the system. Supports 'triangular', 'bell'
                                  'sigmoid' and 'gaussian'.
            and_operator:         torch function to model the AND in the antecedents calculation.
            output_activation:    torch function for output activation function.
        '''

        super(ANFIS, self).__init__()

        self.input_n_sets = variables['inputs']['n_sets']
        self.input_uod = variables['inputs']['uod']
        self.input_var_names = variables['inputs']['var_names']
        self.input_mf_names = variables['inputs']['mf_names']
        
        self.output_var_names = variables['output']['var_names']
        self.output_n_classes = variables['output']['n_classes']
        
        self.mf_shape = mf_shape
        self.and_operator = and_operator
        
        if mf_shape == 'gaussian':
            self.memberships = nn.ModuleList(
                [GaussianMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        elif mf_shape == 'triangular':
            self.memberships = nn.ModuleList(
                [TriangularMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'bell':
            self.memberships = nn.ModuleList(
                [BellMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'sigmoid':
            self.memberships = nn.ModuleList(
                [SigmoidMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        self.antecedents = Antecedents(self.input_n_sets, and_operator)
        self.consequents = Consequents(self.input_n_sets, self.output_n_classes)
        self.inference = Inference(self.output_n_classes, output_activation)
        
    def forward(self, x):
        memberships = [mf(x[:, i]) for i, mf in enumerate(self.memberships)]
        antecedents = self.antecedents(memberships)
        consequents = self.consequents(x)
        Y = self.inference(antecedents, consequents)
        return Y

    def plot_var(self, var_name):
        '''Plots the membership functions for a certain variable of the model.

        Args:
            var_name:  str with the name of the variable, written in the same way as given in dict variables.
        '''

        return _plot_var(self, var_name)
    
    def rule_activations(self, x):
        '''Returns the normalized rule activation for a given input batch.

        Args:
            x:           tensor (N, n) with input data.

        Returns:
            activations: tensor (N, R) with normalized rule activations.
        '''

        return _rule_activations(self, x)

    def print_rules(self, precision=2):
        '''Returns a list with the rules of the model in str format.
        
        Args:
            precision: int for number of decimals to show for the rule parameters. 
            
        Returns:
            rules:     list of str representing the rules of the system.
        '''
        
        return _print_rules(self, precision)
    
    def plot_rules(
        self, 
        var_names, 
        n_points=1000, 
        thr=0.8, 
        levels=10, 
        cmap='viridis', 
        alpha=0.3,
        x_data=None,
        y_data=None,
    ):
        '''Plot the projection of the fuzzy rules in a two variable space.
        
        Args:
            var_names: list/tuple with the variables names.
            n_points:  int with 
            thr:       float between 0 and 1 with the threshold value of the fuzzy rules activation.
            levels:    same as matplotlib.pyplot.
            cmap:      same as matplotlib.pyplot.
            alpha:     same as matplotlib.pyplot.
            x_data:    data for scatter plot.
            y_data:    data for scatter plot.
        '''
        
        return _plot_rules(self, var_names, n_points, thr, levels, cmap, alpha, x_data, y_data)

class RANFIS(nn.Module):
    def __init__(
        self, 
        variables, 
        mf_shape, 
        seq_len,
        and_operator=torch.prod, 
        output_activation=nn.Identity(),
        bidirectional=False,
    ):
        '''Recurrent Neuro-Fuzzy Inference System with Takagi-Sugeno-Kang architecture. Can perform both regression and
           classification.

        Args:
            variables:            dict with two keys, 'inputs' and 'output'. The 'input' has a dict as its value,
                                  containing four keys: 'n_sets', 'uod', 'var_names' and 'mf_names'. They have lists as                                       
                                  their values, containing, respectively: int with number of fuzzy sets associated to the                                     
                                  variable, tuple/list with the universe of discourse of the variable, str with the name of                                   
                                  the variable and list of str with the name of the fuzzy sets. The lists need to be the                                       
                                  same length, and the index of them are all associated, that is, index 0 represents the                                       
                                  information of the same variable. Now, 'output' has only the keys 'var_names' and                                           
                                  'n_classes', with a str representing the name of the variable and an int with the number                                     
                                  of classes (if the model is a regressor, insert 1). 
            mf_shape:             str containing the shape of the fuzzy sets of the system. Supports 'triangular', 'bell'
                                  'sigmoid' and 'gaussian'.
            seq_len:              int with sequence lengths.
            and_operator:         torch function to model the AND in the antecedents calculation.
            output_activation:    torch function for output activation function.
            bidirectional:        bool to set bidirectional on RNN.
        '''

        super(RANFIS, self).__init__()

        self.input_n_sets = variables['inputs']['n_sets']
        self.input_uod = variables['inputs']['uod']
        self.input_var_names = variables['inputs']['var_names']
        self.input_mf_names = variables['inputs']['mf_names']
        
        self.output_var_names = variables['output']['var_names']
        self.output_n_classes = variables['output']['n_classes']
        
        self.mf_shape = mf_shape
        self.and_operator = and_operator
        self.seq_len = seq_len
        
        if mf_shape == 'gaussian':
            self.memberships = nn.ModuleList(
                [GaussianMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        elif mf_shape == 'triangular':
            self.memberships = nn.ModuleList(
                [TriangularMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'bell':
            self.memberships = nn.ModuleList(
                [BellMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'sigmoid':
            self.memberships = nn.ModuleList(
                [SigmoidMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        self.antecedents = Antecedents(self.input_n_sets, and_operator)
        self.consequents = Consequents(self.input_n_sets, self.output_n_classes)
        self.inference = RecurrentInference(
            self.output_n_classes, 
            self.seq_len, 
            bidirectional=bidirectional,
            output_activation=output_activation,
        )
        self.recurrent = nn.RNN(
            input_size=self.antecedents.n_rules * self.output_n_classes,
            hidden_size=self.antecedents.n_rules * self.output_n_classes,
            batch_first=True,
            bidirectional=bidirectional,
        )
    
    def forward(self, x, h=None):
        memberships = [mf(x[:, :, i]) for i, mf in enumerate(self.memberships)]
        antecedents = self.antecedents(memberships)
        consequents = self.consequents(x)
        h, h_n = self.recurrent(consequents)
        y_hat = self.inference(antecedents, consequents, h)
        return y_hat, h_n
    
    def plot_var(self, var_name):
        '''Plots the membership functions for a certain variable of the model.

        Args:
            var_name:  str with the name of the variable, written in the same way as given in dict variables.
        '''

        return _plot_var(self, var_name)
    
    def rule_activations(self, x):
        '''Returns the normalized rule activation for a given input batch.

        Args:
            x:           tensor (N, n) with input data.

        Returns:
            activations: tensor (N, R) with normalized rule activations.
        '''

        return _rule_activations(self, x)

    def print_rules(self, precision=2):
        '''Returns a list with the rules of the model in str format.
        
        Args:
            precision: int for number of decimals to show for the rule parameters. 
            
        Returns:
            rules:     list of str representing the rules of the system.
        '''
        
        return _print_rules(self, precision)
    
    def plot_rules(
        self, 
        var_names, 
        n_points=1000, 
        thr=0.8, 
        levels=10, 
        cmap='viridis', 
        alpha=0.3,
        x_data=None,
        y_data=None,
    ):
        '''Plot the projection of the fuzzy rules in a two variable space.
        
        Args:
            var_names: list/tuple with the variables names.
            n_points:  int with 
            thr:       float between 0 and 1 with the threshold value of the fuzzy rules activation.
            levels:    same as matplotlib.pyplot.
            cmap:      same as matplotlib.pyplot.
            alpha:     same as matplotlib.pyplot.
            x_data:    data for scatter plot.
            y_data:    data for scatter plot.
        '''
        
        return _plot_rules(self, var_names, n_points, thr, levels, cmap, alpha, x_data, y_data)
    
class LSTMANFIS(nn.Module):
    def __init__(
        self, 
        variables, 
        mf_shape, 
        seq_len,
        and_operator=torch.prod, 
        output_activation=nn.Identity(),
        bidirectional=False,
    ):
        '''Long-Short Term Memory Adaptative Neuro-Fuzzy Inference System with Takagi-Sugeno-Kang architecture. Can perform both regression and
           classification.

        Args:
            variables:            dict with two keys, 'inputs' and 'output'. The 'input' has a dict as its value,
                                  containing four keys: 'n_sets', 'uod', 'var_names' and 'mf_names'. They have lists as                                       
                                  their values, containing, respectively: int with number of fuzzy sets associated to the                                     
                                  variable, tuple/list with the universe of discourse of the variable, str with the name of                                   
                                  the variable and list of str with the name of the fuzzy sets. The lists need to be the                                       
                                  same length, and the index of them are all associated, that is, index 0 represents the                                       
                                  information of the same variable. Now, 'output' has only the keys 'var_names' and                                           
                                  'n_classes', with a str representing the name of the variable and an int with the number                                     
                                  of classes (if the model is a regressor, insert 1). 
            mf_shape:             str containing the shape of the fuzzy sets of the system. Supports 'triangular', 'bell'
                                  'sigmoid' and 'gaussian'.
            seq_len:              int with sequence lengths.
            and_operator:         torch function to model the AND in the antecedents calculation.
            output_activation:    torch function for output activation function.
            bidirectional:        bool to set bidirectional on LSTM.
        '''

        super(LSTMANFIS, self).__init__()

        self.input_n_sets = variables['inputs']['n_sets']
        self.input_uod = variables['inputs']['uod']
        self.input_var_names = variables['inputs']['var_names']
        self.input_mf_names = variables['inputs']['mf_names']
        
        self.output_var_names = variables['output']['var_names']
        self.output_n_classes = variables['output']['n_classes']
        
        self.mf_shape = mf_shape
        self.and_operator = and_operator
        self.seq_len = seq_len
        
        if mf_shape == 'gaussian':
            self.memberships = nn.ModuleList(
                [GaussianMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        elif mf_shape == 'triangular':
            self.memberships = nn.ModuleList(
                [TriangularMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'bell':
            self.memberships = nn.ModuleList(
                [BellMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'sigmoid':
            self.memberships = nn.ModuleList(
                [SigmoidMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        self.antecedents = Antecedents(self.input_n_sets, and_operator)
        self.consequents = Consequents(self.input_n_sets, self.output_n_classes)
        self.inference = RecurrentInference(
            self.output_n_classes, 
            self.seq_len, 
            bidirectional=bidirectional,
            output_activation=output_activation,
        )
        self.recurrent = nn.LSTM(
            input_size=self.antecedents.n_rules * self.output_n_classes,
            hidden_size=self.antecedents.n_rules * self.output_n_classes,
            batch_first=True,
            bidirectional=bidirectional,
        )
    
    def forward(self, x, hc=None):
        memberships = [mf(x[:, :, i]) for i, mf in enumerate(self.memberships)]
        antecedents = self.antecedents(memberships)
        consequents = self.consequents(x)
        h, (h_n, c_n) = self.recurrent(consequents)
        y_hat = self.inference(antecedents, consequents, h)
        return y_hat, (h_n, c_n)
    
    def plot_var(self, var_name):
        '''Plots the membership functions for a certain variable of the model.

        Args:
            var_name:  str with the name of the variable, written in the same way as given in dict variables.
        '''

        return _plot_var(self, var_name)
    
    def rule_activations(self, x):
        '''Returns the normalized rule activation for a given input batch.

        Args:
            x:           tensor (N, n) with input data.

        Returns:
            activations: tensor (N, R) with normalized rule activations.
        '''

        return _rule_activations(self, x)

    def print_rules(self, precision=2):
        '''Returns a list with the rules of the model in str format.
        
        Args:
            precision: int for number of decimals to show for the rule parameters. 
            
        Returns:
            rules:     list of str representing the rules of the system.
        '''
        
        return _print_rules(self, precision)
    
    def plot_rules(
        self, 
        var_names, 
        n_points=1000, 
        thr=0.8, 
        levels=10, 
        cmap='viridis', 
        alpha=0.3,
        x_data=None,
        y_data=None,
    ):
        '''Plot the projection of the fuzzy rules in a two variable space.
        
        Args:
            var_names: list/tuple with the variables names.
            n_points:  int with 
            thr:       float between 0 and 1 with the threshold value of the fuzzy rules activation.
            levels:    same as matplotlib.pyplot.
            cmap:      same as matplotlib.pyplot.
            alpha:     same as matplotlib.pyplot.
            x_data:    data for scatter plot.
            y_data:    data for scatter plot.
        '''
        
        return _plot_rules(self, var_names, n_points, thr, levels, cmap, alpha, x_data, y_data)
    
class GRUANFIS(nn.Module):
    def __init__(
        self, 
        variables, 
        mf_shape, 
        seq_len,
        and_operator=torch.prod, 
        output_activation=nn.Identity(),
        bidirectional=False,
    ):
        '''Gated Recurrent Unit Adaptative Neuro-Fuzzy Inference System with Takagi-Sugeno-Kang architecture. Can perform both regression and
           classification.

        Args:
            variables:            dict with two keys, 'inputs' and 'output'. The 'input' has a dict as its value,
                                  containing four keys: 'n_sets', 'uod', 'var_names' and 'mf_names'. They have lists as                                       
                                  their values, containing, respectively: int with number of fuzzy sets associated to the                                     
                                  variable, tuple/list with the universe of discourse of the variable, str with the name of                                   
                                  the variable and list of str with the name of the fuzzy sets. The lists need to be the                                       
                                  same length, and the index of them are all associated, that is, index 0 represents the                                       
                                  information of the same variable. Now, 'output' has only the keys 'var_names' and                                           
                                  'n_classes', with a str representing the name of the variable and an int with the number                                     
                                  of classes (if the model is a regressor, insert 1). 
            mf_shape:             str containing the shape of the fuzzy sets of the system. Supports 'triangular', 'bell'
                                  'sigmoid' and 'gaussian'.
            seq_len:              int with sequence lengths.
            and_operator:         torch function to model the AND in the antecedents calculation.
            output_activation:    torch function for output activation function.
            bidirectional:        bool to set bidirectional on GRU.
        '''

        super(GRUANFIS, self).__init__()

        self.input_n_sets = variables['inputs']['n_sets']
        self.input_uod = variables['inputs']['uod']
        self.input_var_names = variables['inputs']['var_names']
        self.input_mf_names = variables['inputs']['mf_names']
        
        self.output_var_names = variables['output']['var_names']
        self.output_n_classes = variables['output']['n_classes']
        
        self.mf_shape = mf_shape
        self.and_operator = and_operator
        self.seq_len = seq_len
        
        if mf_shape == 'gaussian':
            self.memberships = nn.ModuleList(
                [GaussianMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        elif mf_shape == 'triangular':
            self.memberships = nn.ModuleList(
                [TriangularMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'bell':
            self.memberships = nn.ModuleList(
                [BellMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        if mf_shape == 'sigmoid':
            self.memberships = nn.ModuleList(
                [SigmoidMF(n_sets_, uod_) for n_sets_, uod_ in zip(self.input_n_sets, self.input_uod)]
            )
            
        self.antecedents = Antecedents(self.input_n_sets, and_operator)
        self.consequents = Consequents(self.input_n_sets, self.output_n_classes)
        self.inference = RecurrentInference(
            self.output_n_classes, 
            self.seq_len, 
            bidirectional=bidirectional,
            output_activation=output_activation,
        )
        self.recurrent = nn.GRU(
            input_size=self.antecedents.n_rules * self.output_n_classes,
            hidden_size=self.antecedents.n_rules * self.output_n_classes,
            batch_first=True,
            bidirectional=bidirectional,
        )
    
    def forward(self, x, hc=None):
        memberships = [mf(x[:, :, i]) for i, mf in enumerate(self.memberships)]
        antecedents = self.antecedents(memberships)
        consequents = self.consequents(x)
        h, h_n = self.recurrent(consequents)
        y_hat = self.inference(antecedents, consequents, h)
        return y_hat, h_n
    
    def plot_var(self, var_name):
        '''Plots the membership functions for a certain variable of the model.

        Args:
            var_name:  str with the name of the variable, written in the same way as given in dict variables.
        '''

        return _plot_var(self, var_name)
    
    def rule_activations(self, x):
        '''Returns the normalized rule activation for a given input batch.

        Args:
            x:           tensor (N, n) with input data.

        Returns:
            activations: tensor (N, R) with normalized rule activations.
        '''

        return _rule_activations(self, x)

    def print_rules(self, precision=2):
        '''Returns a list with the rules of the model in str format.
        
        Args:
            precision: int for number of decimals to show for the rule parameters. 
            
        Returns:
            rules:     list of str representing the rules of the system.
        '''
        
        return _print_rules(self, precision)
    
    def plot_rules(
        self, 
        var_names, 
        n_points=1000, 
        thr=0.8, 
        levels=10, 
        cmap='viridis', 
        alpha=0.3,
        x_data=None,
        y_data=None,
    ):
        '''Plot the projection of the fuzzy rules in a two variable space.
        
        Args:
            var_names: list/tuple with the variables names.
            n_points:  int with 
            thr:       float between 0 and 1 with the threshold value of the fuzzy rules activation.
            levels:    same as matplotlib.pyplot.
            cmap:      same as matplotlib.pyplot.
            alpha:     same as matplotlib.pyplot.
            x_data:    data for scatter plot.
            y_data:    data for scatter plot.
        '''
        
        return _plot_rules(self, var_names, n_points, thr, levels, cmap, alpha, x_data, y_data)
