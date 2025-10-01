import os
from typing import Generator, Optional, TypeAlias
from PIL import Image as PILImage


PathLike: TypeAlias = str | os.PathLike[str]


# Constants that represent the first (X) and second (Y) tuple in a location
# coordinate (X, Y)
X = 0
Y = 1

# Constants that represent the red (R), green (G), and blue (B) portions of
# a pixel color
R = 0
G = 1
B = 2


class ImageInitializationError(Exception):
    """ Exception used when initializing an image without a required filename """
    def __init__(self, message="Must supply a filename"):
        self.message = message
        super().__init__(self.message)


class Pixel:
    """ The Pixel class is used to represent a single pixel in an image. It
        has a location (X,Y) coordinate and references the image in which
        it is located. Users can get or set the RGB values of a pixel.
    """
    def __init__(self, location: tuple[int, int], image_data):
        """ Initialize a pixel with location (X,Y) coordinate and an image """
        self.location = location
        self.image_data = image_data

    @property
    def red(self) -> int:
        """ gets the red portion of the pixel value """
        return self.image_data[self.location][R]

    @red.setter
    def red(self, value: int | float) -> None:
        """ sets the red portion of the pixel value """
        _, g, b = self.image_data[self.location]
        self.image_data[self.location] = (int(value), g, b)

    @property
    def green(self) -> int:
        """ gets the green portion of the pixel value """
        return self.image_data[self.location][G]

    @green.setter
    def green(self, value: int | float) -> None:
        """ sets the green portion of the pixel value """
        r, _, b = self.image_data[self.location]
        self.image_data[self.location] = (r, int(value), b)

    @property
    def blue(self) -> int:
        """ gets the blue portion of the pixel value """
        return self.image_data[self.location][B]

    @blue.setter
    def blue(self, value: int | float) -> None:
        """ sets the blue portion of the pixel value """
        r, g, _ = self.image_data[self.location]
        self.image_data[self.location] = (r, g, int(value))

    @property
    def color(self) -> tuple[int, int, int]:
        """ gets the full rgb color of the pixel """
        return self.image_data[self.location]

    @color.setter
    def color(self, value: tuple[int | float, int | float, int | float]) -> None:
        """ sets the full rgb color of a pixel at once """
        self.image_data[self.location] = (int(value[R]), int(value[G]), int(value[B]))


class Image:
    """ The Image class provides a simplified interface to interact with
        images. Users can iterate over the pixels in the image, get the pixel at
        a particular (X, Y) coordinate, and get image properties such as height
        and width. Users interact with the Pixel class to get or change the RGB
        values of individual pixels.
    """
    def __init__(self, filename: Optional[PathLike] = None, image: Optional[PILImage.Image] = None):
        """ Initialize an image with either a filename or an image. If given a
            filename, the image is initialized from the file. If given an image,
            the image is initialized as a copy of this image. If neither a
            filename or an image is supplied, an exception is raised.

            image - a reference to a pillow image
            pixels - the pixels in the image
            location - the (X, Y) coordinate of the current pixel, used when
                iterating over all pixels; initialized to (0, 0)
        """
        if filename:
            self.image = PILImage.open(filename).convert('RGB')
        elif image:
            self.image = image
        else:
            raise ImageInitializationError
        self.pixels = self.image.load()
        self.location = (0, 0)
        self.generator = self.pixel_generator()

    @property
    def height(self) -> int:
        """ Get the height of the image in pixels """
        return self.image.height

    @property
    def width(self) -> int:
        """ Get the width of the image in pixels """
        return self.image.width

    def pixel_generator(self) -> Generator[Pixel, None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield Pixel((x, y), self.pixels)

    def __iter__(self) -> Generator[Pixel, None, None]:
        """ Return an iterator """
        return self.pixel_generator()

    def show(self) -> None:
        """ Shows the image in a window. """
        self.image.show()

    def save(self, filename: PathLike) -> None:
        self.image.save(filename, quality=100)

    def get_pixel(self, x: int, y: int) -> Pixel:
        """ Returns the pixel at the given (X, Y) coordinate """
        return Pixel((x, y), self.pixels)

    @staticmethod
    def blank(width: int, height: int) -> 'Image':
        """ Creates a blank (white) image of a given width and height. Can
            be passed an optional color to make an image of the desired color.
        """
        image = PILImage.new(mode="RGB", size=(width, height), color="white")
        i = Image(filename=None, image=image)
        return i
