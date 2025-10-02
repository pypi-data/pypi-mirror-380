<div align="center">
    <h1 style="font-size: large; font-weight: bold;">Robust-ai</h1>
</div><div align="center">
	<a href="#">
        <img src="https://img.shields.io/badge/Python-3.9%20--%203.10-blue">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/GPU-Required-red">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Requires-CUDA-blue">
    </a>
    </a>
	<a href="_static/pylint/pylint.txt">
        <img src="_static/pylint/pylint.svg" alt="Pylint Score">
    </a>
    <a href="_static/flake8/index.html">
        <img src="_static/flake8/flake8.svg" alt="Flake8 Report">
    </a>
	<a href="_static/coverage/index.html">
        <img src="_static/coverage/coverage.svg" alt="Coverage report">
    </a>
</div>

<br>
<div align="center">
    <a href="https://github.com/IRT-SystemX/robust-ai">
        <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github" alt="GitHub">
    </a>
    <a href="https://irt-systemx.github.io/robust-ai/">
        <img src="https://img.shields.io/badge/Online%20Documentation-available-0A66C2?logo=readthedocs&logoColor=white" alt="Docs">
    </a>
    <a href="https://pypi.org/project/robust-ai/">
        <img src="https://img.shields.io/pypi/v/robust-ai?color=blue&label=PyPI&logo=pypi&logoColor=white" alt="PyPI">
    </a>
</div>

<br>

Robust-ai is a library of training methods designed to improve the robustness of computer vision models.
Warning : This library requires to have a GPU, CPU-only mode is not supported.
## Getting started

To install and use the library, it is recommended to create a Python virtual environment. You can do that with virtualenv, as follows:

### Setting environement
```bash
pip install virtualenv
virtualenv -p <path/to/python3.10> myenv
source myenv/bin/activate
```
### Installation
Once your virtual environment is activated, you can install the robust-ai library directly from Pypi by typing :

```bash
pip install robust-ai
```

This command will install the robust-ai package and all required dependencies.

## Input/Output

### Input

Advertrain takes a torch dataloader as input.

### Ouput

As output, the library returns a model saved as a local .pth file.

## Usage pattern

You have to generate a dataloader in pytorch.

```
trainer = AdversarialTraining(model=your_architecture, optimizer=your_optimizer, loss_func=your_criterion, device=your_device, epsilon=your_epsilon)
trainer.fit(epochs=2, train_dataloader=your_train_dataloader, val_dataloader=your_val_dataloader, patience=2, checkpoint=your_path)
```

For more informations, you can follow the notebook example here :
[Notebook](examples/training.ipynb)

### How to run the provided example

- Download the example dataset [here](http://minio-storage.apps.confianceai-public.irtsysx.fr/ml-models/robust-ai-dataset.zip)
and unzip it in the ```examples/``` folder. Once done, you should have subfolder named ```/examples/dataset/c00``` 

- Launch the jupyter notebook ```examples/training.ipynb```

## Architectures

The library provides four neural network architectures. More specifically, two main architectures are implemented, as well as two derived architectures for each of them :

- ConvNet
- ConvNet with DropBlock regularization
- ResNet
- ResNet with DropBlock regularization

### ConvNet

A Convolutional Neural Network (ConvNet or CNN) is a type of deep learning algorithm primarily used for processing data with a grid-like topology, such as images, using convolutional layers to automatically and adaptively learn spatial hierarchies of features.

### ResNet

ResNet, short for Residual Network, is a type of convolutional neural network (CNN) that introduces residual connections or "shortcuts" to jump over some layers, helping to solve the vanishing gradient problem and enabling the training of much deeper networks.

### DropBlock

DropBlock is a structured form of dropout directed at regularizing convolutional networks. In DropBlock, units in a contiguous region of a feature map are dropped together. As DropBlock discards features in a correlated area, the networks must look elsewhere for evidence to fit the data.

The implementation for this part is based on this [Paper](https://arxiv.org/abs/1810.12890v1) and use a copy of this 
[Code](https://github.com/miguelvr/dropblock/blob/7fb8fbfcb197a4bb57dc9193bcd6f375ff683f85/dropblock/dropblock.py#L6)

## Training methods

Acutally five training methods are available. They take the form of five classes :

- ClassicalTraining
- AdversarialTraining
- AutoAttackTraining
- FireTraining
- TradesTraining

### ClassicalTraining

This is the class to train a model without considering improved robustness.

All other training methods inherit from this class.

### AdversarialTraining

This is the class to train model against adversarial attack. This method is based on an external :
[cleverhans](https://github.com/cleverhans-lab/cleverhans)

### AutoAttackTraining

"Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks"
Francesco Croce, Matthias Hein
ICML 2020
[AutoAttack](https://github.com/fra31/auto-attack)

### FireTraining

"Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks"
Francesco Croce, Matthias Hein
ICML 2020
[Fire](https://github.com/MarinePICOT/Adversarial-Robustness-via-Fisher-Rao-Regularization/blob/main/src/losses.py)

### TradesTraining

TRADES minimizes a regularized surrogate loss L(.,.) (e.g., the cross-entropy loss) for adversarial training
[Trades](https://github.com/yaodongyu/TRADES)

## Contributors and Support

<p align="center">
  Robust-ai is developed by  
  <a href="https://www.irt-systemx.fr/en/" title="IRT SystemX">
   <img src="https://www.irt-systemx.fr/wp-content/uploads/2013/03/system-x-logo.jpeg"  height="70">
  </a>and supported by the 
<a href="https://www.trustworthy-ai-foundation.eu/" title="European Trustworthy AI association">
<img src="https://media.licdn.com/dms/image/v2/D4E0BAQGzfvLxz3sS8Q/company-logo_200_200/B4EZfkq1KLHwAI-/0/1751888122857/european_trustworthy_ai_foundation_logo?e=1759968000&v=beta&t=L2BNgzJNtZeWxHyrU_8Ap3VhrJ_9MdZmh-75IDQIMDc"  height="90">
</a>
</p>
