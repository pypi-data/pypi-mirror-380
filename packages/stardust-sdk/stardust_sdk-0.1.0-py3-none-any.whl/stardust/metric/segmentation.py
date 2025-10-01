import numpy as np


class Segmentation:
    def __repr__(self) -> str:
        description = 'Calculate segmentation metric'
        return description

    def __init__(self, gts: np.array, preds: np.array, num_classes: int) -> None:
        self.num_classes = num_classes
        assert np.max(gts) < self.num_classes
        assert np.max(preds) < self.num_classes
        assert len(preds.size()) == 2 and len(gts.size()) == 2
        self.gts = gts
        self.preds = preds
        self.h, self.w = self.gts.shape
        self.confuse_matrix = self.confusion_matrix()

    def confusion_matrix(self) -> np.array:
        """
        compute confusion matrix

        Returns:
            confusion_matrix(ndarray):
        """
        results = np.zeros((self.num_classes, self.num_classes), dtype=np.uint8)
        for i, j in zip(self.gts.flatten(), self.preds.flatten()):
            results[i, j] += 1
        return results

    def global_pixel_accuracy(self):
        """
        compute global pixel accuracy

        Returns:
            global pixel accuracy(float):
        """
        return len(np.where(self.gts == self.preds)[0]) / (self.h * self.w)

    def class_accuracy(self, class_id: int):
        """
        compute accuracy of the ith class

        Args:
            class_id: int

        Returns:
            class accuracy: float
        """
        assert class_id >= self.num_classes
        return self.confuse_matrix[class_id, class_id] / np.sum(self.confuse_matrix[class_id, :])

    def mean_pixel_accuracy(self):
        """
        compute accuracy of all classes

        Returns:
            mean pixel accuracy: float
        """
        result = 0
        for class_id in range(self.num_classes):
            result += (self.confuse_matrix[class_id, class_id] / np.sum(self.confuse_matrix[class_id, :]))
        return result / self.num_classes

    def IOU(self, class_id: int):
        """
        compute IOU of the ith class

        Args:
            class_id: int

        Returns:
            IOU: float
        """
        assert class_id >= self.num_classes
        return self.confuse_matrix[class_id, class_id] / (np.sum(self.confuse_matrix[class_id, :]) + np.sum(self.confuse_matrix[:, class_id]) - self.confuse_matrix[class_id, class_id])

    def mean_IOU(self):
        """
        compute mean IOU of all classes

        Returns:
            mean IOU: float
        """
        result = 0
        for class_id in range(self.num_classes):
            result += self.confuse_matrix[class_id, class_id] / (np.sum(self.confuse_matrix[class_id, :]) + np.sum(self.confuse_matrix[:, class_id]) - self.confuse_matrix[class_id, class_id])
        return result / self.num_classes
