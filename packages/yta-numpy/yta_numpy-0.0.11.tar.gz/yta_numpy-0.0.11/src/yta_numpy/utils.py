from yta_numpy.rgba.utils import RGBAFrameUtils
from PIL import Image


def save_numpy_frame_as_file(
    frame: 'np.ndarray',
    output_filename: str
):
    # TODO: Force 'IMAGE' output (?)
    # Example: np.zeros((480, 640, 3), dtype=np.uint8)
    Image.fromarray(frame).save(output_filename)

    return output_filename

