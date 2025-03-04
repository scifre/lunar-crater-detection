ResNet-UNet for Crater Detection

Overview

This project implements a deep ResNet-UNet model for crater detection using TensorFlow/Keras. The model is designed to segment craters in images, leveraging the ResNet blocks for feature extraction and UNet architecture for upsampling and segmentation.

Model Architecture

The model consists of:

ResNet Blocks: Residual learning helps in deep feature extraction while preventing vanishing gradients.

Downsampling Path (Encoder): Uses max-pooling and ResNet blocks to extract deep spatial features.

Bottleneck Layer: Captures the most abstracted features with high receptive fields.

Upsampling Path (Decoder): Uses transposed convolutions and skip connections to recover spatial information and generate segmentation masks.

ResNet Block

Each ResNet block contains:

Two convolutional layers (3x3 kernel)

Batch normalization for stability

ReLU activation

Residual connection to allow gradient flow
