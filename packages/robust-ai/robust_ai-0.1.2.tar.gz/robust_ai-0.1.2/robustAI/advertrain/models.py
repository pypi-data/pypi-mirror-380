import torch
from torch import Tensor, nn
from torch.nn import functional as F

from robustAI.advertrain.dependencies.dropblock import DropBlock2d


class Normalize(nn.Module):
    def __init__(self, mean: Tensor, std: Tensor, device: torch.device) -> None:
        """
        Initialize the Normalize module.

        This module is used to normalize image data by subtracting the mean and
        dividing by the standard deviation.

        Args:
            mean (Tensor): A tensor containing the mean values for each channel.
            std (Tensor): A tensor containing the standard deviation for each channel.
            device (torch.device): The device (CPU or GPU) to which the tensors should be moved.
        """
        super().__init__()

        self.mean = mean.unsqueeze(-1).unsqueeze(-1).to(device)
        self.std = std.unsqueeze(-1).unsqueeze(-1).to(device)

    def forward(self, x: Tensor) -> Tensor:
        """
        Normalize the input tensor.

        Applies the normalization operation on the input tensor using the mean and
        standard deviation provided during initialization.

        Args:
            x (Tensor): The input tensor to be normalized.

        Returns:
            Tensor: The normalized tensor.
        """
        return (x - self.mean) / self.std


class ConvNet(nn.Module):
    """
    Convolutional Neural Network with dropout layers, designed for processing images of size 64x128.

    This network includes a normalization layer, several convolutional layers with
    ReLU activation and max pooling, followed by fully connected layers with dropout
    for regularization. It is suited for tasks like image classification where dropout
    can help reduce overfitting.

    Attributes:
        norm (Normalize): Normalization layer to preprocess the input images.
        conv1, conv2_1, conv3_1, conv4_1 (nn.Conv2d): Convolutional layers for feature extraction.
        pooling (nn.MaxPool2d): Max pooling layer to reduce spatial dimensions.
        activation (nn.ReLU): Activation function.
        dropout (nn.Dropout): Dropout layer for regularization.
        linear1, linear2, linear3 (nn.Linear): Fully connected layers for classification.
    """

    def __init__(self, device: torch.device, p: float = 0.2) -> None:
        """
        Initializes the ConvNetDropout model with dropout layers.

        Args:
            device (torch.device): The device to which the model and tensors should be moved.
            p (float): Dropout probability. Default is 0.2.
        """
        super().__init__()

        self.norm = Normalize(
            torch.Tensor([0.4632, 0.4532, 0.4485]),
            torch.Tensor([0.1646, 0.1759, 0.1739]),
            device,
        )

        self.conv1 = nn.Conv2d(3, 32, 7, padding=3)
        self.conv2_1 = nn.Conv2d(32, 64, 5, padding=2)
        self.conv3_1 = nn.Conv2d(64, 128, 5, padding=2)
        self.conv4_1 = nn.Conv2d(128, 256, 5, padding=2)

        self.pooling = nn.MaxPool2d(2)
        self.activation = nn.ReLU()
        self.dropout = nn.Dropout(p=p)

        self.linear1 = nn.Linear(4 * 8 * 256, 2048)
        self.linear2 = nn.Linear(2048, 1024)
        self.linear3 = nn.Linear(1024, 2)

        self.to(device)

    def forward(self, x: Tensor) -> Tensor:
        """
        Defines the forward pass of the ConvNetDropout.

        The input tensor is processed through normalization, convolutional layers,
        pooling layers, dropout layers, and fully connected layers sequentially to
        produce the output tensor.

        Args:
            x (Tensor): Input tensor of shape (batch_size, 3, 64, 128).

        Returns:
            Tensor: Output tensor after processing through the network.
        """
        x = self.norm(x)

        y = self.activation(self.conv1(x))
        y = self.pooling(y)

        y = self.activation(self.conv2_1(y))
        y = self.pooling(y)

        y = self.activation(self.conv3_1(y))
        y = self.pooling(y)

        y = self.activation(self.conv4_1(y))
        y = self.pooling(y)

        y = self.activation(self.linear1(torch.reshape(y, (-1, 4 * 8 * 256))))
        y = self.dropout(y)
        y = self.activation(self.linear2(y))
        y = self.dropout(y)
        y = self.linear3(y)

        return y


class ConvNetDropblock(nn.Module):
    """
    Convolutional Neural Network with DropBlock regularization, designed for processing images of size 64x128.

    This network includes a normalization layer, several convolutional layers with
    ReLU activation and max pooling, followed by fully connected layers with dropout
    and DropBlock for regularization. It is suited for tasks like image classification
    where advanced regularization techniques can help reduce overfitting.

    Attributes:
        norm (Normalize): Normalization layer to preprocess the input images.
        conv1, conv2_1, conv3_1, conv4_1 (nn.Conv2d): Convolutional layers for feature extraction.
        pooling (nn.MaxPool2d): Max pooling layer to reduce spatial dimensions.
        activation (nn.ReLU): Activation function.
        dropout (nn.Dropout): Dropout layer for regularization.
        dropblock (DropBlock2d): DropBlock layer for structured dropout.
        linear1, linear2, linear3 (nn.Linear): Fully connected layers for classification.
    """

    def __init__(self, device: torch.device, p: float = 0.2, drop_prob: float = 0.0, n_steps: int = 10) -> None:
        """
        Initializes the ConvNetDropblock model with DropBlock layers.

        Args:
            device (torch.device): The device (CPU or GPU) to which the model and tensors should be moved.
            p (float): Dropout probability for the standard dropout layers. Default is 0.2.
            drop_prob (float): Initial probability for DropBlock. Default is 0.1.
            n_steps (int): Number of steps over which DropBlock probability should reach its maximum. Default is 10.
        """
        super().__init__()

        self.norm = Normalize(
            torch.Tensor([0.4632, 0.4532, 0.4485]),
            torch.Tensor([0.1646, 0.1759, 0.1739]),
            device,
        )

        self.conv1 = nn.Conv2d(3, 32, 7, padding=3)
        self.conv2_1 = nn.Conv2d(32, 64, 5, padding=2)
        self.conv3_1 = nn.Conv2d(64, 128, 5, padding=2)
        self.conv4_1 = nn.Conv2d(128, 256, 5, padding=2)

        self.pooling = nn.MaxPool2d(2)
        self.activation = nn.ReLU()
        self.dropout = nn.Dropout(p=p)

        self.dropblock = DropBlock2d(drop_prob=drop_prob)
        self.drop_prob = drop_prob
        self.n_epochs = n_steps
        self.epochs = 0

        self.linear1 = nn.Linear(4 * 8 * 256, 2048)
        self.linear2 = nn.Linear(2048, 1024)
        self.linear3 = nn.Linear(1024, 2)

        self.to(device)

    def forward(self, x: Tensor) -> Tensor:
        """
        Defines the forward pass of the ConvNetDropblock.

        The input tensor is processed through normalization, convolutional layers,
        pooling layers, DropBlock layers, dropout layers, and fully connected layers
        sequentially to produce the output tensor.

        Args:
            x (Tensor): Input tensor of shape.

        Returns:
            Tensor: Output tensor after processing through the network.
        """
        x = self.norm(x)

        y = self.activation(self.conv1(x))
        y = self.pooling(y)
        y = self.dropblock(y)

        y = self.activation(self.conv2_1(y))
        y = self.pooling(y)
        y = self.dropblock(y)

        y = self.activation(self.conv3_1(y))
        y = self.pooling(y)
        y = self.dropblock(y)

        y = self.activation(self.conv4_1(y))
        y = self.pooling(y)

        y = self.activation(self.linear1(torch.reshape(y, (-1, 4 * 8 * 256))))
        y = self.dropout(y)
        y = self.activation(self.linear2(y))
        y = self.dropout(y)
        y = self.linear3(y)

        return y


class ResNet(nn.Module):
    """
    A custom implementation of a Residual Network (ResNet) for processing images.

    This network consists of multiple convolutional layers, each followed by batch normalization,
    and some layers include dropout for regularization. The network uses skip connections
    similar to a ResNet architecture, adding the output of one layer to another layer.
    """

    def __init__(self, device: torch.device, p: float = 0.2) -> None:
        """
        Initializes the ResNet model.

        Args:
            device (torch.device): The device to which the model and tensors should be moved.
        """
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv1_bn = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv2_bn = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv3_drop = nn.Dropout2d(p=0.2)
        self.conv3_bn = nn.BatchNorm2d(32)

        self.conv4 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv4_bn = nn.BatchNorm2d(64)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv5_bn = nn.BatchNorm2d(64)
        self.conv6 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv6_drop = nn.Dropout2d(p=0.2)
        self.conv6_bn = nn.BatchNorm2d(64)

        self.conv7 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv7_bn = nn.BatchNorm2d(128)
        self.conv8 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.conv8_bn = nn.BatchNorm2d(128)
        self.conv9 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.conv9_drop = nn.Dropout2d(p=p)
        self.conv9_bn = nn.BatchNorm2d(128)

        self.conv10 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.conv10_bn = nn.BatchNorm2d(256)
        self.conv11 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv11_bn = nn.BatchNorm2d(256)
        self.conv12 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv12_drop = nn.Dropout2d(p=p)
        self.conv12_bn = nn.BatchNorm2d(256)

        self.fc1 = nn.Linear(256 * 8 * 16, 2048)
        self.fc1_bn = nn.BatchNorm1d(2048)
        self.fc2 = nn.Linear(2048, 2)

        self.to(device)

    def forward(self, inp: Tensor) -> Tensor:
        """
        Defines the forward pass of the ResNet.

        The input tensor is processed through a series of convolutional layers with skip connections,
        batch normalization, and dropout, followed by fully connected layers to produce the output tensor.

        Args:
            inp (Tensor): Input tensor of appropriate shape, typically matching the input size of the first
            convolutional layer.

        Returns:
            Tensor: Output tensor after processing through the network.
        """
        res = F.relu(self.conv1_bn(self.conv1(inp)))
        x = F.relu(self.conv2_bn(self.conv2(res)))
        x = self.conv3_drop(self.conv3(x))
        block1_out = F.relu(self.conv3_bn(F.max_pool2d(x + res, 2)))  # 32x64

        res = F.relu(self.conv4_bn(self.conv4(block1_out)))
        x = F.relu(self.conv5_bn(self.conv5(res)))
        x = self.conv6_drop(self.conv6(x))
        block2_out = F.relu(self.conv6_bn(F.max_pool2d(x + res, 2)))  # 16x32

        res = F.relu(self.conv7_bn(self.conv7(block2_out)))
        x = F.relu(self.conv8_bn(self.conv8(res)))
        x = self.conv9_drop(self.conv9(x))
        block3_out = F.relu(self.conv9_bn(F.max_pool2d(x + res, 2)))  # 8x16

        res = F.relu(self.conv10_bn(self.conv10(block3_out)))
        x = F.relu(self.conv11_bn(self.conv11(res)))
        x = F.relu(self.conv12_bn(self.conv12_drop(self.conv12(x + res))))

        x = x.view(-1, 256 * 8 * 16)
        x = F.relu(self.fc1_bn(self.fc1(x)))
        x = F.dropout(x, training=self.training, p=0.2)
        x = self.fc2(x)
        return x


class ResNetDropblock(nn.Module):
    """
    A custom implementation of a Residual Network (ResNet) for processing images.

    This network consists of multiple convolutional layers, each followed by batch normalization,
    and some layers include dropout for regularization. The network uses skip connections
    similar to a ResNet architecture, adding the output of one layer to another layer.
    """

    def __init__(self, device: torch.device, p: float = 0.2, drop_prob: float = 0.0) -> None:
        """
        Initializes the ResNet model.

        Args:
            device (torch.device): The device to which the model and tensors should be moved.
        """
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv1_bn = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv2_bn = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv3_drop = nn.Dropout2d(p=0.2)
        self.conv3_bn = nn.BatchNorm2d(32)

        self.conv4 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv4_bn = nn.BatchNorm2d(64)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv5_bn = nn.BatchNorm2d(64)
        self.conv6 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv6_drop = nn.Dropout2d(p=0.2)
        self.conv6_bn = nn.BatchNorm2d(64)

        self.conv7 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv7_bn = nn.BatchNorm2d(128)
        self.conv8 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.conv8_bn = nn.BatchNorm2d(128)
        self.conv9 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.conv9_drop = nn.Dropout2d(p=p)
        self.conv9_bn = nn.BatchNorm2d(128)

        self.conv10 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.conv10_bn = nn.BatchNorm2d(256)
        self.conv11 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv11_bn = nn.BatchNorm2d(256)
        self.conv12 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv12_drop = nn.Dropout2d(p=p)
        self.conv12_bn = nn.BatchNorm2d(256)

        self.dropblock = DropBlock2d(drop_prob=drop_prob)
        self.drop_prob = drop_prob

        self.fc1 = nn.Linear(256 * 8 * 16, 2048)
        self.fc1_bn = nn.BatchNorm1d(2048)
        self.fc2 = nn.Linear(2048, 2)

        self.to(device)

    def forward(self, inp: Tensor) -> Tensor:
        """
        Defines the forward pass of the ResNet.

        The input tensor is processed through a series of convolutional layers with skip connections,
        batch normalization, and dropout, followed by fully connected layers to produce the output tensor.

        Args:
            inp (Tensor): Input tensor of appropriate shape, typically matching the input size of the first
            convolutional layer.

        Returns:
            Tensor: Output tensor after processing through the network.
        """
        res = F.relu(self.conv1_bn(self.conv1(inp)))
        x = F.relu(self.conv2_bn(self.conv2(res)))
        x = self.conv3_drop(self.conv3(x))
        x = self.dropblock(x)
        block1_out = F.relu(self.conv3_bn(F.max_pool2d(x + res, 2)))  # 32x64

        res = F.relu(self.conv4_bn(self.conv4(block1_out)))
        x = F.relu(self.conv5_bn(self.conv5(res)))
        x = self.conv6_drop(self.conv6(x))
        x = self.dropblock(x)
        block2_out = F.relu(self.conv6_bn(F.max_pool2d(x + res, 2)))  # 16x32

        res = F.relu(self.conv7_bn(self.conv7(block2_out)))
        x = F.relu(self.conv8_bn(self.conv8(res)))
        x = self.conv9_drop(self.conv9(x))
        x = self.dropblock(x)
        block3_out = F.relu(self.conv9_bn(F.max_pool2d(x + res, 2)))  # 8x16

        res = F.relu(self.conv10_bn(self.conv10(block3_out)))
        x = F.relu(self.conv11_bn(self.conv11(res)))
        x = F.relu(self.conv12_bn(self.conv12_drop(self.conv12(x + res))))
        x = self.dropblock(x)

        x = x.view(-1, 256 * 8 * 16)
        x = F.relu(self.fc1_bn(self.fc1(x)))
        x = F.dropout(x, training=self.training, p=0.2)
        x = self.fc2(x)
        return x
