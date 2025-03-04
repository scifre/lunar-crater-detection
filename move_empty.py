import os
import shutil

def move_empty_labels_and_images(image_folder, label_folder, dest_folder):
    # Create destination folders if they don't exist
    empty_image_folder = os.path.join(dest_folder, 'empty_images')
    empty_label_folder = os.path.join(dest_folder, 'empty_labels')
    
    os.makedirs(empty_image_folder, exist_ok=True)
    os.makedirs(empty_label_folder, exist_ok=True)

    # Get list of images and labels
    images = sorted(os.listdir(image_folder))
    labels = sorted(os.listdir(label_folder))
    
    for img, label in zip(images, labels):
        label_path = os.path.join(label_folder, label)
        
        # Check if the label file is empty
        if os.stat(label_path).st_size == 0:
            print(f"Moving image {img} and empty label {label} to {dest_folder}")
            
            # Move the image to the empty_images folder
            img_path = os.path.join(image_folder, img)
            shutil.move(img_path, os.path.join(empty_image_folder, img))
            
            # Move the empty label to the empty_labels folder
            shutil.move(label_path, os.path.join(empty_label_folder, label))

    print("All empty label files and their corresponding images have been moved.")

# Define your paths here
image_folder = 'LU3M6TGT_yolo_format/valid/images'
label_folder = 'LU3M6TGT_yolo_format/valid/labels'
dest_folder = 'LU3M6TGT_yolo_format/empty'

# Call the function to move empty labels and their images
move_empty_labels_and_images(image_folder, label_folder, dest_folder)
