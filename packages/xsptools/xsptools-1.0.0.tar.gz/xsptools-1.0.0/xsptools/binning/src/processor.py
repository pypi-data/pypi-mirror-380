import numpy as np
from . import helpers


class Processor:

    """Class to perform 3x3 binning of a frame.

    This class may only be used with an X-Spectrum Lambda CdTe 750k detector.

    Parameters
    ----------
    frame_height : int
                   Frame height in pixels.
    frame_width : int
                  Frame width in pixels.

    Attributes
    ----------
    bin_size : int
        Bin size in pixels (read-only).
    binned_frame_height : int
        Binned frame height in pixels (read-only).
    binned_frame_width : int
        Binned frame width in pixels (read-only).
    """


    def __init__(self, frame_height: int, frame_width: int):

        if frame_height != 516 or frame_width != 1554:
            raise ValueError("Invalid frame dimensions: shape must be ({},{})".format(516,1554))

        self._bin_size = 3
        self._frame_height = frame_height
        self._frame_width = frame_width
        self._pixel_mask_widened = []
        self._pixel_mask_nn_interpolation_indices = (None, None)
        self._interpolate = False


    @property
    def bin_size(self) -> int:
        return self._bin_size

    @property
    def binned_frame_height(self) -> int:
        return int(self._frame_height / self.bin_size)

    @property
    def binned_frame_width(self) -> int:
        return int(self._frame_width / self.bin_size)


    def add_pixel_mask(self, pixel_mask: np.ndarray):
        """Add a pixel mask to the binning Processor.

        A valid pixel mask will turn on an interpolation during binning. Bad pixels
        are set to the average of their 8 neighbors.

        Parameters
        ----------
        pixel_mask : np.ndarray
            Pixel mask, normally obtained via pyxsp. Must be reshaped to
            (frame_height, frame_width) before passing it.
        """
        if not isinstance(pixel_mask, np.ndarray):
            raise ValueError("Invalid pixel mask: pixel mask must be a numpy array")
        if pixel_mask.shape != (self._frame_height, self._frame_width):
            raise ValueError("Invalid pixel mask: pixel mask must have shape ({},{})".format(self._frame_height, self._frame_width))
        if pixel_mask.dtype != np.uint32:
            raise ValueError("Invalid pixel mask: data type must be 32-bit unsigned integer")

        decoded_mask = helpers.decode_mask(pixel_mask)
        self._pixel_mask_widened = helpers.pixel_mask_widened_strip(decoded_mask)
        self._pixel_mask_nn_interpolation_indices = helpers.pixel_mask_nn_interpolation_indices(decoded_mask)
        self._interpolate = True


    def bin_frame(self, frame: np.ndarray) -> np.ndarray:

        """3x3 binning of frames.

        Frames are binned and, if a pixel masx is found, bad pixels are set to the average of
        their neighbors before binning. Saturation is not affected, the original bit-depth
        range of `frame` is maintained.

        Parameters
        ----------
        frame : np.ndarray
            Frame to bin. Must be reshaped to (frame_height, frame_width)
            before passing it.

        Returns
        -------
        np.ndarray
            3x3 binned frame.
        """

        if not isinstance(frame, np.ndarray):
            raise ValueError("Invalid frame: frame must be a numpy array")
        if frame.shape != (self._frame_height,self._frame_width):
            raise ValueError("Invalid frame: frame must have shape ({},{})".format(self._frame_height,self._frame_width))

        new_frame = np.array(frame, copy=True)
        dtype = frame.dtype
        info = np.iinfo(dtype)

        new_frame[self._pixel_mask_widened] = 0
        if self._interpolate:
            new_frame = helpers.nn_interpolation(new_frame, self._pixel_mask_nn_interpolation_indices)

        new_frame = new_frame.reshape(new_frame.shape[0] // self._bin_size, self._bin_size, new_frame.shape[1] // self._bin_size, self.bin_size)
        new_frame = new_frame.sum(-1, dtype=np.uint32).sum(1, dtype=np.uint32)

        new_frame = np.clip(new_frame, info.min, info.max).astype(dtype)


        return new_frame
