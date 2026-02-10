# Traffic Sign Classification – Experimentation Process

This project uses a convolutional neural network (CNN) to classify traffic signs from the GTSRB dataset. The goal was not only to achieve good accuracy, but also to experiment with different model configurations and understand how architectural changes affect performance.

## Initial Model

I started with a basic convolutional neural network composed of two convolutional blocks (Conv2D + MaxPooling), followed by a single fully connected layer with 128 units. The model was trained for 10 epochs.

This initial version already achieved good results, with test accuracy around 94%. However, the training accuracy was higher than the test accuracy, indicating some degree of overfitting. This suggested that the model could benefit from additional regularization and further experimentation.

## Increasing Training Epochs and Model Capacity

In the second experiment, I increased the number of training epochs from 10 to 20 and added a Dropout layer before the output layer to reduce overfitting. Dropout helps prevent the model from relying too heavily on specific neurons during training.

With these changes, the model achieved a significant improvement, reaching approximately 98% accuracy on the test set. This showed that the model benefited from additional training time and better regularization.

I also experimented with increasing the size of the fully connected layer from 128 to 256 units. While this slightly improved accuracy in some runs, the improvement was minimal and the test loss increased slightly, indicating diminishing returns and a higher risk of overfitting.

## Increasing Network Depth

In the final experiment, I increased the depth of the network by adding a third convolutional block with 128 filters. This allowed the model to learn more complex visual features from the images.

After combining this deeper architecture with a fully connected layer of 128 units, Dropout, and 20 training epochs, the model achieved consistent and stable results across multiple runs. Test accuracy reached approximately 98.1%, with low test loss and minimal variation between executions.

## Final Model Choice

The final model consists of three convolutional blocks (with 32, 64, and 128 filters), followed by a fully connected layer with 128 units and a Dropout layer. This configuration provided the best balance between model complexity, performance, and stability.

Overall, this experimentation process demonstrated that increasing model complexity can improve performance, but only up to a certain point. Beyond that, simpler and more stable configurations often generalize better.