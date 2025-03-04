# ResNet-UNet for Crater Detection

## Overview

This project implements a **deep ResNet-UNet model** for crater detection using TensorFlow/Keras. The model is designed to segment craters in images, leveraging the **ResNet blocks** for feature extraction and **UNet architecture** for upsampling and segmentation.

## Model Architecture

The model consists of:

- **ResNet Blocks**: Residual learning helps in deep feature extraction while preventing vanishing gradients.
- **Downsampling Path (Encoder)**: Uses max-pooling and ResNet blocks to extract deep spatial features.
- **Bottleneck Layer**: Captures the most abstracted features with high receptive fields.
- **Upsampling Path (Decoder)**: Uses transposed convolutions and skip connections to recover spatial information and generate segmentation masks.

### ResNet Block

Each **ResNet block** contains:

- Two convolutional layers (3x3 kernel)
- Batch normalization for stability
- ReLU activation
- Residual connection to allow gradient flow

## Usage

 - Clone the repo
   ```sh
   git clone https://github.com/scifre/crater-detection.git
   cd crater-detection
    ```
 - Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

## Results


## Conclusion

This **ResNet-UNet model** effectively detects craters by combining deep residual learning with UNet-style segmentation. The use of **skip connections and residual blocks** improves performance, making it robust for complex image segmentation tasks.

---

Let me know if you need any modifications! 🚀

