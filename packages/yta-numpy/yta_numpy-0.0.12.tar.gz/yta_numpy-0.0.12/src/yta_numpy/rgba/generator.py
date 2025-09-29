
from typing import Union

import numpy as np


class _RGBAColorFrameGenerator:
    """
    *For internal use only*

    Class to wrap functionality related to
    generating RGBA color frames.
    """

    @staticmethod
    def _get_numpy_array(
        color: Union[tuple[int, int, int], None],
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[int, None] = None
    ) -> np.ndarray:
        """
        *For internal use only*

        Get the numpy array with the provided
        color and all the attributes set.

        The size must be provided as (w, h), but
        the numpy array will be like (h, w). Be careful
        if you need to invert the size for your result 
        and pass it already inverted.

        The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        # 0 is transparent, 255 is opaque
        dimensions = (
            4
            if transparency is not None else
            3
        )

        # If 'color' is None, choose a random one
        color = (
            # TODO: Create random, not 'color'
            color
            if color is None else
            color
        )

        fill_value = (
            color + (transparency,)
            if transparency is not None else
            color
        )

        return np.full(
            shape = (size[1], size[0], dimensions),
            fill_value = fill_value,
            dtype = dtype
        )
    
    @staticmethod
    def white(
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[float, None] = None
    ) -> np.ndarray:
        """
        Get a numpy array that represents a full
        blue frame of the given 'size' and with
        the given 'dtype'.
        
        The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        return _RGBAColorFrameGenerator._get_numpy_array(
            color = (255, 255, 255),
            size = size,
            dtype = dtype,
            transparency = transparency
        )
    
    @staticmethod
    def black(
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[float, None] = None
    ) -> np.ndarray:
        """
        Get a numpy array that represents a full
        blue frame of the given 'size' and with
        the given 'dtype'.

        The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        return _RGBAColorFrameGenerator._get_numpy_array(
            color = (0, 0, 0),
            size = size,
            dtype = dtype,
            transparency = transparency
        )
    
    @staticmethod
    def red(
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[float, None] = None
    ) -> np.ndarray:
        """
        Get a numpy array that represents a full
        blue frame of the given 'size' and with
        the given 'dtype'.
        
       The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        return _RGBAColorFrameGenerator._get_numpy_array(
            color = (255, 0, 0),
            size = size,
            dtype = dtype,
            transparency = transparency
        )
    
    @staticmethod
    def green(
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[float, None] = None
    ) -> np.ndarray:
        """
        Get a numpy array that represents a full
        blue frame of the given 'size' and with
        the given 'dtype'.
        
       The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        return _RGBAColorFrameGenerator._get_numpy_array(
            color = (0, 255, 0),
            size = size,
            dtype = dtype,
            transparency = transparency
        )
    
    @staticmethod
    def blue(
        size: tuple[int, int] = (1920, 1080),
        dtype: np.dtype = np.uint8,
        transparency: Union[float, None] = None
    ) -> np.ndarray:
        """
        Get a numpy array that represents a full
        blue frame of the given 'size' and with
        the given 'dtype'.
        
        The 'transparency' must be an int in `[0, 255]`
        range:
        - `0` is opaque
        - `255` is transparent

        Providing 'transparency' as None will 
        result in a numpy with only 3 dimensions.
        """
        return _RGBAColorFrameGenerator._get_numpy_array(
            color = (0, 0, 255),
            size = size,
            dtype = dtype,
            transparency = transparency
        )

class RGBAFrameGenerator:
    """
    Class to wrap functionality related to
    generating RGBA frames.
    """

    color: _RGBAColorFrameGenerator = _RGBAColorFrameGenerator
    """
    Shortcut to rgba color generation.
    """