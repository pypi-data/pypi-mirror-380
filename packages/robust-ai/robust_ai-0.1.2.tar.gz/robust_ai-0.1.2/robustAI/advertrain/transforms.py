from torchvision import transforms
from torchvision.transforms import Compose


class DataTransformations:
    """
    Class to create and return training and test data transformations.

    This class encapsulates the creation of data transformations used in training and testing.
    It provides methods to get composed series of transformations for both scenarios.
    """

    def __init__(self, train_prob: float = 0.5):
        """
        Initializes the DataTransformations class.

        Args:
            train_prob (float): The probability of applying transformations in training. Default is 0.5.
        """
        self.train_prob = train_prob

    def get_train_transforms(self) -> Compose:
        """
        Creates and returns a series of training data transformations.

        Returns:
            Compose: A composed series of transformations for training data.
        """
        return transforms.Compose(
            [
                transforms.Pad((0, 120)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip(),
                transforms.RandomApply(
                    [
                        transforms.RandomAffine(5),
                        transforms.RandomAffine(0, translate=(0.02, 0.02)),
                        transforms.ColorJitter(
                            brightness=0.5, contrast=0.2, saturation=0.2, hue=0
                        ),
                    ],
                    p=self.train_prob,
                ),
                transforms.Resize(size=(64, 128)),
                transforms.ToTensor(),
            ]
        )

    def get_test_transforms(self) -> Compose:
        """
        Creates and returns a series of test data transformations.

        Returns:
            Compose: A composed series of transformations for test data.
        """
        return transforms.Compose(
            [
                transforms.Pad((0, 120)),
                transforms.Resize((64, 128)),
                transforms.ToTensor(),
            ]
        )
