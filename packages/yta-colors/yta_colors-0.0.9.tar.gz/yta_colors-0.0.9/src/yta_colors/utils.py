from yta_constants.color import ColorString
from yta_constants.regex import ColorRegularExpression
from yta_validation import PythonValidator
from colorsys import rgb_to_hsv as _rgb_to_hsv, hsv_to_rgb as _hsv_to_rgb
from typing import Union


def is_hexadecimal_color(
    color: str
) -> bool:
    """
    Check that the 'color' parameter is an hexadecimal
    color.
    """
    return ColorRegularExpression.HEXADECIMAL.parse(color)

def is_string_color(
    color: str
) -> bool:
    """
    Check that the 'color' parameter is an string 
    color accepted by our system, whose value is an
    hexadecimal value.
    """
    return ColorString.is_valid(color)

def is_array_or_tuple_without_alpha_normalized(
    color: Union[tuple, list]
):
    """
    Check that the 'color' parameter is an array or a
    tuple of 3 elements that are float values between
    0 and 1 (normalized value).
    """
    return (
        is_array_or_tuple_without_alpha and
        all(
            PythonValidator.is_instance_of(c, float) and
            0 <= c <= 1
            for c in color
        )
    )

def is_array_or_tuple_with_alpha_normalized(
    color: Union[tuple, list]
):
    """
    Check that the 'color' parameter is an array or a
    tuple of 4 elements that are float values between
    0 and 1 (normalized value).
    """
    return (
        is_array_or_tuple_with_alpha and
        all(
            PythonValidator.is_instance_of(c, float) and 
            0 <= c <= 1
            for c in color
        )
    )

def is_array_or_tuple_without_alpha(
    color: Union[tuple, list]
):
    """
    Check that the 'color' parameter is an array or a
    tuple of 3 elements that are int values between 0
    and 255.
    """
    return (
        PythonValidator.is_instance_of(color, [tuple, list]) and
        len(color) == 3 and
        all(
            PythonValidator.is_instance_of(c, int) and
            0 <= c <= 255
            for c in color
        )
    )

def is_array_or_tuple_with_alpha(
    color: Union[list, tuple]
) -> bool:
    """
    Check that the 'color' parameter is an array or a
    tuple of 4 elements that are int values between 0
    and 255.
    """
    return (
        PythonValidator.is_instance_of(color, [tuple, list]) and
        len(color) == 4 and
        all(
            PythonValidator.is_instance_of(c, int) and
            0 <= c <= 255
            for c in color
        )
    )

def parse_rgb_color(
    color: Union[tuple, list]
) -> list:
    """
    Parse the provided 'color' as RGB and returns it as
    r,g,b values.
    """
    if is_array_or_tuple_without_alpha_normalized(color):
        return color[0] * 255, color[1] * 255, color[2] * 255
    elif is_array_or_tuple_without_alpha(color):
        return color[0], color[1], color[2]
    else:
        raise Exception(f'The provided "color" parameter is not an RGB color.')

def parse_rgba_color(
    color: Union[tuple, list]
) -> list:
    """
    Parse the provided 'color' as RGBA and returns it as
    r,g,b,a values.
    """
    if is_array_or_tuple_with_alpha_normalized(color):
        return color[0] * 255, color[1] * 255, color[2] * 255, color[3] * 255
    elif is_array_or_tuple_with_alpha(color):
        return color[0], color[1], color[2], color[3]
    else:
        raise Exception(f'The provided "color" parameter is not an RGBA color.')
    
def parse_color(
    color: Union[str, list, tuple],
    do_force_alpha: bool = False
) -> Union[list, None]:
    """
    Tries to parse the provided 'color' and returns it
    as an RGBA if parseable, or None if not.

    The color can be:
    - String, representing a color, like `black`
    - Hex color string: `#FF00FF`, `0xFF00FF00`
    - RGBA color tuple: `[255, 255, 255, 255]`
    - RGB color tuple: `[255, 0, 255]`

    This is what we do:

    1. We try to parse the color as color name
    string.

    2. We check if the value is an hexadecimal
    value, accepting any kind of variation.

    3. We try to parse it as a RGBA tuple or
    array that includes the alpha channel.

    4. We try to parse it as a RGB tuple or
    array that includes the alpha channel.
    """
    string_color = None
    if PythonValidator.is_string(color):
        try:
            string_color = ColorString.to_enum(color.upper())
        except:
            pass

    color_array = None
    if string_color is not None:
        # String color name
        color_array = hex_to_rgba(string_color.value)
    elif (
        PythonValidator.is_string(color)
        and is_hexadecimal_color(color)
    ):
        # Any hexa decimal variation ('#ffffff')
        color_array = hex_to_rgba(color)
    else:
        # RGBA color array or tuple, such
        # as: [255, 255, 255, 255]
        try:
            color_array = parse_rgba_color(color)
        except:
            pass

        # RGB color array or tuple, such as:
        # (255, 255, 255)
        try:
            #color_array = *parse_rgb_color(color), 0
            alpha_value = (
                0
                if do_force_alpha else
                None
            )

            color_array = *parse_rgb_color(color), alpha_value
        except:
            pass

    # TODO: What about HSL, CYMK, etc. (?)

    return color_array
    
# These methods below are just actioners, they don't
# check anything as they will be used by a class that
# validates everything before using these methods.
def hex_to_rgba(
    hex_color: str,
    do_force_alpha: bool = False
) -> list:
    """
    Return a tuple containing the color in RGBA order.
    """
    # Hex can start with '0x', '0X' or '#'
    hex_color = hex_color.removeprefix('#').removeprefix('0x').removeprefix('0X')

    # Hex can have 1 character to represent each
    # value, instead of 2 ('123' instead of '112233'
    # or '123F' instead of '112233FF')
    hex_color = (
        ''.join(char * 2 for char in hex_color)
        if len(hex_color) in [3, 4] else
        hex_color
    )

    if len(hex_color) not in [6, 8]:
        raise Exception(f'The provided "{hex_color}" string is not a valid hex color.')
    
    # There is a difference between getting alpha 
    # as 0 or as None. None means there was no 
    # alpha channel provided
    alpha_value = (
        0
        if do_force_alpha else
        None
    )
    
    return (
        tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
        if len(hex_color) == 8 else
        tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (alpha_value,)
    )

def hex_to_rgb(
    hex_color: str
) -> list:
    """
    Return a tuple containing the color in RGB order.
    """
    r, g, b, _ = hex_to_rgba(hex_color)

    return r, g, b

def rgb_to_hex(
    rgb_color: list,
    do_include_alpha: bool = False
) -> list:
    """
    Return a tuple containing the color in RGB or RGBA
    order (according to the given 'do_include_alpha'
    parameter value).
    """
    r, g, b = parse_rgb_color(rgb_color)

    return rgba_to_hex([r, g, b, 255], do_include_alpha)

def rgba_to_hex(
    rgba_color: list,
    do_include_alpha: bool = False
) -> list:
    """
    Return a tuple containing the color in HEX mode
    (including the alpha value if the given
    'do_include_alpha' parameter is True).
    """
    r, g, b, a = parse_rgba_color(rgba_color)

    return (
        "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, a)
        if do_include_alpha else
        "#{:02x}{:02x}{:02x}".format(r, g, b)
    )

def rgba_to_hsl(
    rgba_color: list
) -> list:
    r, g, b, _ = parse_rgba_color(rgba_color)

    return rgb_to_hsl([r, g, b])

def rgb_to_hsl(
    rgb_color: list
) -> list:
    r, g, b = parse_rgb_color(rgb_color)

    # Values normalization
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    # Max and minimum values for RGB
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    # Tone (H)
    h = (
        0 # No difference => undefined (gray) tone
        if delta == 0 else
        (60 * ((g - b) / delta) + 360) % 360
        if cmax == r else
        (60 * ((b - r) / delta) + 120) % 360
        if cmax == g else
        (60 * ((r - g) / delta) + 240) % 360 # cmax == b
    )
    
    # Luminosity (L)
    l = (cmax + cmin) / 2
    
    # Saturation (S)
    s = (
        0 # No difference => saturation is 0
        if delta == 0 else
        delta / (1 - abs(2 * l - 1)) if l != 0 and l != 1 else delta / (2 - (cmax + cmin))
    )

    # TODO: I saw in some online solutions that they offer
    # the results without decimal figures
    return round(h, 2), round(s * 100, 2), round(l * 100, 2)

# TODO: Add 'hsl_to_rgb'
# TODO: Add 'hsl_to_rgba'

def rgb_to_cymk(
    rgb_color: list
) -> list:
    r, g, b = parse_rgb_color(rgb_color)

    r, g, b = r / 255.0, g / 255.0, b / 255.0

    k = 1 - max(r, g, b)

    if k == 1:
        c = m = y = 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

    # TODO: I saw in some online solutions that they offer
    # the results without decimal figures
    return round(c * 100, 2), round(m * 100, 2), round(y * 100, 2), round(k * 100, 2)

def rgb_to_hsv(
    rgb_color
) -> list:
    r, g, b = parse_rgb_color(rgb_color)

    # TODO: Assume this is not normalized
    return _rgb_to_hsv(r, g, b)

def rgba_to_hsv(
    rgba_color
) -> list:
    r, g, b, _ = parse_rgba_color(rgba_color)
    
    # TODO: Assume this is not normalized
    return _rgb_to_hsv(r, g, b)

def hsv_to_rgb(
    h,
    s,
    v
):
    # TODO: Assume this is not normalized
    return _hsv_to_rgb(h, s, v)

def hsv_to_rgba(
    h,
    s,
    v
):
    # TODO: Assume this is not normalized
    return *hsv_to_rgb(h, s, v), 255