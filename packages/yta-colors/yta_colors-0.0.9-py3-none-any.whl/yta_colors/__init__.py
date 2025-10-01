"""
Library to make very easy working with colors.

---

Some information for developers:

About the `force_alpha` parameter:
- `False` => Do not force it, return it as it
was stored in the color. Can be None or a
value between [0, 255].
- `None` => Force it to None.
- `[0, 255]` => Force it to this value. Float
values will be parsed as int.
"""
from yta_colors.converter import ColorConverter
from yta_colors.utils import parse_color
from yta_programming.metaclasses import _GetAttrReturnsNoneMetaClass
from yta_validation import PythonValidator
from yta_validation.parameter import ParameterValidator
from typing import Union


class Color:
    """
    Class to represent a color, stored as RGBA, simplifying
    the way we interact with color and provide them as
    parameters and the way we make color conversion. The
    color is stored as a not-normalized color, but values
    can be normalized through the methods that allow it
    (those including the 'normalized' bool parameter).

    The alpha channel is special and can be or can be not
    present in the color. The absence of the alpha channel
    is different from having it but being transparent. That
    is why we stored also accept alpha value as None. You
    can force an alpha value when working with the color,
    but you will know that originally that color was defined
    without that alpha channel (very important for image or
    video edition).

    The color attributes must be initialized with a value
    in the `[0, 255]` range (`alpha` can be `None`).

    About the special alpha channel:
    - `alpha=0` means full transparent
    - `alpha=255` means full opaque
    - `alpha=None` means no alpha channel
    """

    @property
    def has_alpha(
        self
    ) -> bool:
        """
        Flag to indicate if the color was defined
        originally with an alpha value.
        """
        return self.a is not None

    def __init__(
        self,
        red: int,
        green: int,
        blue: int,
        alpha: Union[int, None] = 255
    ):
        # TODO: Maybe we could accept floats and parse
        # them in between 0.0 and 1.0
        ParameterValidator.validate_mandatory_number_between('red', red, 0, 255)
        ParameterValidator.validate_mandatory_number_between('green', green, 0, 255)
        ParameterValidator.validate_mandatory_number_between('blue', blue, 0, 255)
        ParameterValidator.validate_number_between('alpha', alpha, 0, 255)

        alpha = (
            int(alpha)
            if alpha is not None else
            None
        )

        self.r: int = int(red)
        """
        Red color, from 0 to 255, where 0 is no value and 255
        is everything.
        """
        self.g: int = int(green)
        """
        Green color, from 0 to 255, where 0 is no value and 255
        is everything.
        """
        self.b: int = int(blue)
        """
        Blue color, from 0 to 255, where 0 is no value and 255
        is everything.
        """
        self.a: Union[int, None] = alpha
        """
        Alpha (transparency), from 0 to 255, where 0 is no
        value (transparent) and 255 is everything (opaque).
        """

    @property
    def rgb_not_normalized(
        self
    ) -> tuple[int, int, int]:
        """
        Get the color as a tuple of the 3 RGB values that
        are, in order: red, green, blue. These values are
        not normalized, so each value is in the interval
        [0, 255].

        Example here:
        - `Red opaque color => [255, 0, 0, 0]`
        """
        return self._to_rgb_or_rgba(
            do_include_alpha = False,
            do_normalize = False
        )
    
    @property
    def rgb_normalized(
        self
    ) -> tuple[float, float, float]:
        """
        Get the color as a tuple of the 3 RGB values that
        are, in order: red, green, blue. These values are
        normalized, so each value is in the interval [0, 1].

        Example here:
        - `Red opaque color => [1.0, 0.0, 0.0]`
        """
        return self._to_rgb_or_rgba(
            do_include_alpha = False,
            do_normalize = True
        )
    
    @property
    def rgba_not_normalized(
        self
    ) -> tuple[int, int, int, Union[int, None]]:
        """
        Get the color as a tuple of the 3 RGB values and
        a 4th value representing the transparency, that
        are, in order: red, green, blue, alpha. These
        values are not normalized, so each value is in
        the interval [0, 255].

        The alpha value could be None, use 'to_rgba' to
        force an alpha value.

        Example here:
        - `Red opaque color => [255, 0, 0, 255]`
        """
        return self._to_rgb_or_rgba(
            do_include_alpha = True,
            do_normalize = False
        )

    @property
    def rgba_normalized(
        self
    ) -> tuple[float, float, float, Union[float, None]]:
        """
        Get the color as a tuple of the 3 RGB values and
        a 4th value representing the transparency, that
        are, in order: red, green, blue, alpha. These
        values are normalized, so each value is in the
        interval [0, 1].

        The alpha value could be None, use 'to_rgba' to
        force an alpha value.

        Example here:
        - `Red opaque color => [1.0, 0.0, 0.0, 1.0]`
        """
        return self._to_rgb_or_rgba(
            do_include_alpha = True,
            do_normalize = True
        )
    
    # TODO: What do we do if alpha is None (?)
    @property
    def hex_with_alpha(
        self
    ):
        """
        Get the color as a string representing it in
        hexadecimal value. The result will be #RRGGBBAA
        because it includes the alpha value in the last
        position.

        The alpha value could be None, use it carefully.
        """
        return ColorConverter.rgba_to_hex(
            color = self.rgba_not_normalized,
            do_include_alpha = True
        )

    @property
    def hex_without_alpha(
        self
    ):
        """
        Get the color as a string representing it in
        hexadecimal value. The result will be #RRGGBB
        because it doesn't include the alpha value.

        The alpha value could be None, use it carefully.
        """
        return ColorConverter.rgba_to_hex(
            color = self.rgba_not_normalized,
            do_include_alpha = False
        )
    
    # TODO: What do we do if alpha is None (?)
    @property
    def hsl(
        self
    ):
        """
        Get the color as an HSL color.

        The alpha value could be None, use it carefully.
        """
        return ColorConverter.rgba_to_hsl(color = self.rgba_not_normalized)
    
    # TODO: What do we do if alpha is None (?)
    @property
    def cymk(
        self
    ):
        """
        Get the color as an CYMK color.

        The alpha value could be None, use it carefully.
        """
        return ColorConverter.rgba_to_cymk(color = self.rgba_not_normalized)

    # TODO: What do we do if alpha is None (?)
    @property
    def hsv(
        self
    ):
        """
        Get the color as a HSV color.

        The alpha value could be None, use it carefully.
        """
        return ColorConverter.rgba_to_hsv(color = self.rgba_not_normalized)

    # Directly related to libraries below
    # TODO: Add more, not only for OpenCV,
    # even if the format is the same
    @property
    def for_opencv(
        self
    ) -> tuple[int, int, int]:
        """
        Get the color in a BGR format, which is the 
        format that the OpenCV library handles.
        """
        return (self.b, self.g, self.r)
    
    def to_rgba(
        self,
        force_alpha: Union[bool, None, int] = False,
        do_normalize: bool = False
    ) -> Union[tuple[float, float, float, Union[float, None]], tuple[int, int, int, Union[int, None]]]:
        """
        Get a tuple representing the color as an
        RGBA color.

        About the `force_alpha` parameter:
        - `False` => Do not force it, return it as it
        was stored in the color. Can be None or a
        value between [0, 255].
        - `None` => Force it to None.
        - `[0, 255]` => Force it to this value.

        Examples below:
        - White transparent: `(255, 255, 255, 0)`
        - Green with no alpha: `(0, 255, 0, None)`
        - Red opaque: `(255, 0, 0, 255)`
        """
        return self._to_rgb_or_rgba(
            do_include_alpha = True,
            force_alpha = force_alpha,
            do_normalize = do_normalize
        )
    
    def _to_rgb_or_rgba(
        self,
        do_include_alpha: bool = False,
        force_alpha: Union[bool, None, int] = False,
        do_normalize: bool = False
    ):
        """
        *For internal use only*

        Turn the color instant into a representation
        of it, normalized or not, as a tuple.

        About the `force_alpha` parameter:
        - `False` => Do not force it, return it as it
        was stored in the color. Can be None or a
        value between [0, 255].
        - `None` => Force it to None.
        - `[0, 255]` => Force it to this value. Float
        values will be parsed as int.
        """
        if do_include_alpha:
            if force_alpha not in [False, None]:
                ParameterValidator.validate_mandatory_number_between('force_alpha', force_alpha, 0, 255)

            alpha = (
                self.a
                if force_alpha is False else
                None
                if force_alpha is None else
                # float values parsed as int
                int(force_alpha)
            )

            values = (self.r, self.g, self.b, alpha)
        else:
            values = (self.r, self.g, self.b)

        return (
            tuple(
                (
                    value / 255.0
                    if value is not None else
                    value
                )
                for value in values
            )
            if do_normalize else
            values
        )
    
    # TODO: Use the cv2 library to make other changes
    @staticmethod
    def parse(
        color: Union[list, tuple, str, 'ColorString', 'Color']
    ) -> 'Color':
        """
        Parse the provided 'color' parameter and return the
        color as r,g,b,a values or raises an Exception if it
        is not a valid and parseable color.

        This method accepts string colors (if names are
        registered in our system), hexadecimal colors (than
        can also include alpha value), RGB array or tuples
        (that can be normalized, with float values between
        0.0 and 1.0, or not normalized, with int values
        between 0 and 255), or RGBA array or tuples, similar
        to RGB but including a 4h alpha value.

        Check 'yta_constants.color.ColorString' variables
        to know the color strings we accept.
        """
        if PythonValidator.is_instance_of(color, Color):
            return color

        color = parse_color(color)

        if color is None:
            raise Exception(f'The provided "color" parameter is not parseable.')
        
        return Color(*color)
    
    @staticmethod
    def transparent(
    ) -> 'Color':
        """
        Get a full transparent Color instance.
        """
        return Color(0, 0, 0, 0)

class Colors(metaclass = _GetAttrReturnsNoneMetaClass):
    """
    *This class is dynamically built.*
    *This class returns None if no attribute.*

    Class to hold color constants to simplify
    the way we use them. These colors are built
    with RGB values so they don't include any
    transparency.

    If you need a black color for your OpenCV
    library, just do this:
    - `Colors.BLACK.for_opencv`

    This class is dynamically built with the
    values we have in our own library
    `yta_constants.color.ColorString`.
    """

    @staticmethod
    def from_str(
        color: str
    ) -> Union[Color, None]:
        """
        Transform a color name string into a Color instance
        if the value provided is registered in our list.

        Check `yta_constants.color.ColorString`.
        """
        return getattr(Colors, color.upper(), None)
        
"""
This below is generating our list dynamically
according to the constants we have in the 
'yta_constants.color.ColorString' list. We 
won't need to repeat the values but we will
not see the values in the pydoc
"""
from yta_constants.color import ColorString
for color_string in ColorString.get_all():
    # The value comes without alpha, but we
    # want to the alpha to be 255
    setattr(Colors, color_string.name, Color.parse(f'{color_string.value}FF'))