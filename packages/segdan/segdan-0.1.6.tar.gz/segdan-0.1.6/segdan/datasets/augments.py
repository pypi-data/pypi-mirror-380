import albumentations as A
import cv2

def get_training_augmentation(resize_height = 512, resize_width=512, background=None):
    if background == None:
        background = 0
        
    train_transform = [
        A.Resize(height=resize_height, width=resize_width),
        A.HorizontalFlip(p=0.5),
        A.Affine(
            scale=(0.8, 1.2),  
            translate_percent={"x": 0.1, "y": 0.1}, 
            rotate=10, 
            fill=background, 
            fill_mask=background,  
            border_mode=cv2.BORDER_CONSTANT, 
            p=1
        ),
        A.PadIfNeeded(min_height=None, min_width=None, pad_height_divisor=32, pad_width_divisor=32, fill=background, fill_mask=background),
        A.OneOf(
            [
                A.GaussNoise(std_range=(0.1,0.2), p=1),
                A.CLAHE(p=1),
                A.RandomBrightnessContrast(p=1),
                A.RandomGamma(p=1),
            ],
            p=0.9,
        ),
        A.OneOf(
            [
                A.Sharpen(p=1),
                A.Blur(blur_limit=3, p=1),
                A.MotionBlur(blur_limit=3, p=1),
            ],
            p=0.9,
        ),
        A.OneOf(
            [
                A.RandomBrightnessContrast(p=1),
                A.HueSaturationValue(p=1),
            ],
            p=0.9,
        ),
        A.CoarseDropout(num_holes_range=(1,8), hole_height_range=(8,32), hole_width_range=(8,32), fill=background, fill_mask=background, p=0.3),
        A.GridDistortion(p=0.2),
    ]
    return A.Compose(train_transform)


def get_validation_augmentation(resize_height = 512, resize_width=512, background=None):
    if background == None:
        background = 0

    test_transform = [
       A.Resize(height=resize_height, width=resize_width),
       A.PadIfNeeded(min_height=None, min_width=None, pad_height_divisor=32, pad_width_divisor=32, fill=background, fill_mask=background)
    ]
    return A.Compose(test_transform)