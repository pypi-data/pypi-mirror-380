"""
Module to resize numpy arrays.
"""
from typing import Union

import numpy as np


class NumpyResizer:
    """
    Class to wrap functionality related to 
    resizing numpy arrays.
    """

    @staticmethod
    def resize_distort(
        frame: np.ndarray,
        size: tuple[int, int]
    ) -> np.ndarray:
        """
        *Needs `opencv-python` installed*

        Resize the provided numpy 'frame' array to the
        given 'size', distorting the image (respecting
        not the aspect ratio).

        The `size` must be (w, h).
        """
        import cv2

        return cv2.resize(frame, size, interpolation = cv2.INTER_LINEAR)
    
    @staticmethod
    def resize_letterbox(
        frame: np.ndarray,
        size: tuple[int, int],
        do_keep_image_alpha: bool = True,
        background_color: Union[tuple[int, int, int], tuple[int, int, int, int], None] = None,
    ) -> np.ndarray:
        """
        Resize the provided numpy 'frame' array to the
        given 'size', keeping the alpha channel if the
        'do_keep_image_alpha' is set as True, and using
        the given 'background_color'.

        Providing 'background_color' as None will generate
        a full transparent background.

        The `size` must be (w, h).
        """
        import cv2

        # TODO: Parse 'background_color' as RGB or RGBA
        background_color = (
            [0, 0, 0, 0]
            if background_color is None else
            background_color
        )
        target_w, target_h = size
        h, w = frame.shape[:2]

        # Scale, maintaining the ratio
        scale = min(target_w / w, target_h / h)
        new_w, new_h = int(w * scale), int(h * scale)
        resized = cv2.resize(frame, (new_w, new_h), interpolation = cv2.INTER_LINEAR)

        if do_keep_image_alpha:
            # Force the alpha channel
            if resized.shape[2] == 3:
                alpha = np.full((new_h, new_w, 1), 255, dtype = resized.dtype)
                resized = np.concatenate([resized, alpha], axis = 2)

        # Black (opaque) canvas to place the image in
        # TODO: What if image non alpha and parameter
        # is False (?)
        bg = np.full((target_h, target_w, 4), background_color, dtype = resized.dtype)

        # Offsets to center the image
        y_off = (target_h - new_h) // 2
        x_off = (target_w - new_w) // 2

        # Paste resized image with its original alpha
        bg[y_off:y_off+new_h, x_off:x_off+new_w] = resized

        return bg
    
    @staticmethod
    def pad_with_color(
        frame: np.ndarray,
        size: tuple[int, int],
        background_color: Union[tuple[int, int, int], tuple[int, int, int, int], None] = None
    ) -> np.ndarray:
        """
        Make the provided numpy 'frame' array fit
        the given 'size' by applying a background
        color defined by the 'background_color'
        parameter.

        Providing 'background_color' as None will generate
        a full transparent background.

        The `size` must be (w, h).
        """
        # TODO: Parse 'background_color' as RGB or RGBA
        background_color = (
            [0, 0, 0, 0]
            if background_color is None else
            background_color
        )
        target_w, target_h = size
        h, w = frame.shape[:2]

        number_of_channels = len(background_color)

        if (
            number_of_channels == 4 and
            frame.shape[2] == 3
        ):
            # Frame to RGBA if color has alpha
            alpha = np.full((h, w, 1), 255, dtype = frame.dtype)
            frame = np.concatenate([frame, alpha], axis = 2)
            number_of_channels = 4

        # Canvas with background color
        bg = np.full((target_h, target_w, number_of_channels), background_color, dtype = frame.dtype)

        # Frame to canvas
        bg[:min(h, target_h), :min(w, target_w)] = frame[:target_h, :target_w]

        return bg