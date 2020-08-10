import sys
import colorsys
from textwrap import indent

import tinycss2
import tinycss2.ast

# Source: https://w3schools.sinsixx.com/css/css_colornames.asp.htm
COLOR_MAP = {
    'AliceBlue': 0xF0F8FF,
    'AntiqueWhite': 0xFAEBD7,
    'Aqua': 0x00FFFF,
    'Aquamarine': 0x7FFFD4,
    'Azure': 0xF0FFFF,
    'Beige': 0xF5F5DC,
    'Bisque': 0xFFE4C4,
    'Black': 0x000000,
    'BlanchedAlmond': 0xFFEBCD,
    'Blue': 0x0000FF,
    'BlueViolet': 0x8A2BE2,
    'Brown': 0xA52A2A,
    'BurlyWood': 0xDEB887,
    'CadetBlue': 0x5F9EA0,
    'Chartreuse': 0x7FFF00,
    'Chocolate': 0xD2691E,
    'Coral': 0xFF7F50,
    'CornflowerBlue': 0x6495ED,
    'Cornsilk': 0xFFF8DC,
    'Crimson': 0xDC143C,
    'Cyan': 0x00FFFF,
    'DarkBlue': 0x00008B,
    'DarkCyan': 0x008B8B,
    'DarkGoldenRod': 0xB8860B,
    'DarkGray': 0xA9A9A9,
    'DarkGreen': 0x006400,
    'DarkKhaki': 0xBDB76B,
    'DarkMagenta': 0x8B008B,
    'DarkOliveGreen': 0x556B2F,
    'Darkorange': 0xFF8C00,
    'DarkOrchid': 0x9932CC,
    'DarkRed': 0x8B0000,
    'DarkSalmon': 0xE9967A,
    'DarkSeaGreen': 0x8FBC8F,
    'DarkSlateBlue': 0x483D8B,
    'DarkSlateGray': 0x2F4F4F,
    'DarkTurquoise': 0x00CED1,
    'DarkViolet': 0x9400D3,
    'DeepPink': 0xFF1493,
    'DeepSkyBlue': 0x00BFFF,
    'DimGray': 0x696969,
    'DodgerBlue': 0x1E90FF,
    'FireBrick': 0xB22222,
    'FloralWhite': 0xFFFAF0,
    'ForestGreen': 0x228B22,
    'Fuchsia': 0xFF00FF,
    'Gainsboro': 0xDCDCDC,
    'GhostWhite': 0xF8F8FF,
    'Gold': 0xFFD700,
    'GoldenRod': 0xDAA520,
    'Gray': 0x808080,
    'Green': 0x008000,
    'GreenYellow': 0xADFF2F,
    'HoneyDew': 0xF0FFF0,
    'HotPink': 0xFF69B4,
    'IndianRed': 0xCD5C5C,
    'Indigo': 0x4B0082,
    'Ivory': 0xFFFFF0,
    'Khaki': 0xF0E68C,
    'Lavender': 0xE6E6FA,
    'LavenderBlush': 0xFFF0F5,
    'LawnGreen': 0x7CFC00,
    'LemonChiffon': 0xFFFACD,
    'LightBlue': 0xADD8E6,
    'LightCoral': 0xF08080,
    'LightCyan': 0xE0FFFF,
    'LightGoldenRodYellow': 0xFAFAD2,
    'LightGrey': 0xD3D3D3,
    'LightGreen': 0x90EE90,
    'LightPink': 0xFFB6C1,
    'LightSalmon': 0xFFA07A,
    'LightSeaGreen': 0x20B2AA,
    'LightSkyBlue': 0x87CEFA,
    'LightSlateGray': 0x778899,
    'LightSteelBlue': 0xB0C4DE,
    'LightYellow': 0xFFFFE0,
    'Lime': 0x00FF00,
    'LimeGreen': 0x32CD32,
    'Linen': 0xFAF0E6,
    'Magenta': 0xFF00FF,
    'Maroon': 0x800000,
    'MediumAquaMarine': 0x66CDAA,
    'MediumBlue': 0x0000CD,
    'MediumOrchid': 0xBA55D3,
    'MediumPurple': 0x9370D8,
    'MediumSeaGreen': 0x3CB371,
    'MediumSlateBlue': 0x7B68EE,
    'MediumSpringGreen': 0x00FA9A,
    'MediumTurquoise': 0x48D1CC,
    'MediumVioletRed': 0xC71585,
    'MidnightBlue': 0x191970,
    'MintCream': 0xF5FFFA,
    'MistyRose': 0xFFE4E1,
    'Moccasin': 0xFFE4B5,
    'NavajoWhite': 0xFFDEAD,
    'Navy': 0x000080,
    'OldLace': 0xFDF5E6,
    'Olive': 0x808000,
    'OliveDrab': 0x6B8E23,
    'Orange': 0xFFA500,
    'OrangeRed': 0xFF4500,
    'Orchid': 0xDA70D6,
    'PaleGoldenRod': 0xEEE8AA,
    'PaleGreen': 0x98FB98,
    'PaleTurquoise': 0xAFEEEE,
    'PaleVioletRed': 0xD87093,
    'PapayaWhip': 0xFFEFD5,
    'PeachPuff': 0xFFDAB9,
    'Peru': 0xCD853F,
    'Pink': 0xFFC0CB,
    'Plum': 0xDDA0DD,
    'PowderBlue': 0xB0E0E6,
    'Purple': 0x800080,
    'Red': 0xFF0000,
    'RosyBrown': 0xBC8F8F,
    'RoyalBlue': 0x4169E1,
    'SaddleBrown': 0x8B4513,
    'Salmon': 0xFA8072,
    'SandyBrown': 0xF4A460,
    'SeaGreen': 0x2E8B57,
    'SeaShell': 0xFFF5EE,
    'Sienna': 0xA0522D,
    'Silver': 0xC0C0C0,
    'SkyBlue': 0x87CEEB,
    'SlateBlue': 0x6A5ACD,
    'SlateGray': 0x708090,
    'Snow': 0xFFFAFA,
    'SpringGreen': 0x00FF7F,
    'SteelBlue': 0x4682B4,
    'Tan': 0xD2B48C,
    'Teal': 0x008080,
    'Thistle': 0xD8BFD8,
    'Tomato': 0xFF6347,
    'Turquoise': 0x40E0D0,
    'Violet': 0xEE82EE,
    'Wheat': 0xF5DEB3,
    'White': 0xFFFFFF,
    'WhiteSmoke': 0xF5F5F5,
    'Yellow': 0xFFFF00,
    'YellowGreen': 0x9ACD32
}
COLORS = list(COLOR_MAP.keys())
COLOR_MAP = dict(zip(map(str.lower, COLORS), COLOR_MAP.values()))

SPACE = tinycss2.ast.WhitespaceToken(None, None, ' ')

COMMA = tinycss2.ast.LiteralToken(None, None, ',')
# Long values for these properties, maybe containing a color
# CSS_PROPS_LONG_COLOR__UNUSED = {
#     'background',
#     'border',
#     'border-bottom',
#     'border-left',
#     'border-right',
#     'border-top',
#     'border-block-start',
#     'border-block-end',
#     'border-inline-start',
#     'border-inline-end',
#     'box-shadow',
#     'column-rule',
#     'outline',
#     'text-decoration',
#     'text-emphasis',
#     'text-shadow',
# }
CSS_PROPS_LONG_COLOR = {
    'box-shadow',
    'text-shadow',
}
# Properties taking a color value
CSS_PROPS_COLOR = {
    'background-color',
    'color',
    'border-color',
    'border-bottom-color',
    'border-left-color',
    'border-right-color',
    'border-top-color',
    'border-block-start-color',
    'border-block-end-color',
    'border-inline-start-color',
    'border-inline-end-color',
    'caret-color',
    'column-rule-color',
    'outline-color',
    'text-decoration-color',
    'text-emphasis-color',
    # SVG
    'stroke',
    'fill',
    'stop-color',
    'flood-color',
    'lighting-color',
}


def parse_rules(rules):
    color_rules = []
    for rule in rules:
        if not rule.content:
            continue  # no declarations, either empty or @import
        color_sub_rules = None
        if rule.type == 'at-rule':
            at_keyword = rule.at_keyword
            sub_rules = []
            declarations = []
            at_rule_content = tinycss2.parse_stylesheet(
                rule.content, skip_comments=True, skip_whitespace=True)
            for token in at_rule_content:
                if token.type.endswith('-rule'):
                    sub_rules.append(token)
                else:
                    declarations.append(token)
            if sub_rules:
                color_sub_rules = parse_rules(sub_rules)
        else:
            declarations = rule.content
        # Grab color declarations
        color_declarations = parse_colors(declarations)

        if color_sub_rules:
            color_declarations.extend(color_sub_rules)

        if color_declarations:
            # color_rule = tinycss2.ast.QualifiedRule(
            #     line=rule.source_line, column=rule.source_column,
            #     prelude=selector, content=color_declarations
            # )
            rule.content = color_declarations
            color_rules.append(rule)
    # Return CSS string
    return color_rules


def print_warning(msg, to_serialize=None, token=None):
    print('WARNING::' + msg + ' [Line {}, Column {}]'.format(
        token.source_line, token.source_column), file=sys.stderr)
    if to_serialize is not None:
        print(indent(tinycss2.serialize(to_serialize), '  '), file=sys.stderr)


def parse_colors(declarations):
    """

    Resources:
      https://tinycss2.readthedocs.io/en/latest/
      https://www.quackit.com/css/color/properties/
      https://developer.mozilla.org/en-US/docs/Web/HTML/Applying_color
    """
    color_declarations = []
    col_dec = []
    is_color = False  # whether declaration has a color
    is_property = True  # whether declaration is property or values side of ':'
    is_single = False  # single or multiple values expected for property
    is_known = False  # whether the color property is known or not

    for i, token in enumerate(declarations, start=1):
        if token.type == 'whitespace' or token.type == 'comment':
            continue

        if is_property:
            if len(col_dec) > 1:  # prop + ':'
                print_warning('More than one property discovered in single '
                              'declaration #{}'.format(i), declarations, token)
            col_dec.append(token)
        else:
            if col_dec[-1] is not SPACE:
                col_dec.append(SPACE)
            if not is_single:
                col_dec.append(token)

        color_hex = color_rgb = None
        alpha = None
        if token.type == 'literal':
            if token.value == ';':
                # end of line
                # TODO: space logic is sloppy
                if is_single:
                    if col_dec[-1] is SPACE:
                        col_dec[-1] = token
                    else:
                        col_dec.append(token)
                elif col_dec[-2] is SPACE:
                    del col_dec[-2]
                if is_color:
                    if not is_known:
                        print_warning('Parsed color for declaration with '
                                      'unknown color property', col_dec, token)
                    color_declarations.extend(col_dec)
                # Reset
                col_dec = []
                is_property = True
                is_color = is_single = is_known = False
            elif token.value == ':':
                if not is_property:
                    print_warning('Multiple ":" tokens found in declaration '
                                  '#{}'.format(i), declarations, token)
                is_property = False
                col_dec.append(SPACE)
        elif token.type == 'function':  # TODO: linear gradients, etc...
            # Note that no argument validation is done here other than # of args
            if is_property:
                print_warning('Function token found in declaration '
                              '#{}'.format(i), declarations, token)
            else:
                # For some reason, looks like browsers will auto-infer alpha
                # channel if specified, so take into consideration here...
                if token.lower_name == 'rgb' or token.lower_name == 'rgba':
                    args = parse_color_func_args(token, 255)
                    if args is not None:
                        color_rgb = args[:3]
                        if len(args) == 4:
                            alpha = args[3]
                elif token.lower_name == 'hsl' or token.lower_name == 'hsla':
                    args = parse_color_func_args(token, 1)
                    if args is not None:
                        v_h, v_s, v_l = args[:3]
                        if len(args) == 4:
                            alpha = args[3]
                        color_rgb = colorsys.hls_to_rgb(v_h, v_l, v_s)
        elif token.type == 'ident':
            token_val = token.value.lower()
            if is_property:
                token_val_normalized = token_val
                if token_val.startswith('-webkit-'):
                    token_val_normalized = token_val[len('-webkit-'):]
                elif token_val.startswith('-moz-'):
                    token_val_normalized = token_val[len('-moz-'):]

                if token.value.startswith('--'):
                    is_single = is_known = False
                elif token_val_normalized in CSS_PROPS_COLOR:
                    # known property, expect 1 value, maybe color
                    is_single = is_known = True
                elif token_val_normalized + '-color' in CSS_PROPS_COLOR:
                    # known property, expect 1 value, maybe color
                    is_single = is_known = True
                    token.value = token_val + '-color'
                elif token_val_normalized in CSS_PROPS_LONG_COLOR:
                    # known property, expect 1+ values, maybe color
                    is_single = False
                    is_known = True
                else:
                    # non-color/custom property, maybe color?
                    is_single = is_known = False
            else:
                # Check if value is known CSS color
                color_hex = COLOR_MAP.get(token_val)
        elif token.type == 'hash':
            if is_property:
                print_warning('Hash token parsed as property in declaration '
                              '#{}'.format(i), declarations, token)
            else:
                # TODO: is this always a color here?
                tv = token.value
                if len(tv) == 3:
                    color_hex = int(tv[0] + tv[0] + tv[1] + tv[1] +
                                    tv[2] + tv[2], 16)
                elif len(tv) == 4:
                    color_hex = int(tv[0] + tv[0] + tv[1] + tv[1] +
                                    tv[2] + tv[2], 16)
                    alpha = int(tv[3], 16) / 0x10
                elif len(tv) == 6:
                    color_hex = int(tv, 16)
                elif len(tv) == 8:
                    color_hex = int(tv[:6], 16)
                    alpha = int(tv[6:], 16) / 0x100
                else:
                    print_warning('Malformed hash token (as color) in '
                                  'declaration #{}'.format(i), declarations,
                                  token)

        if not is_property and (color_hex is not None or color_rgb is not None):
            is_color = True
            if color_rgb is None:
                color_rgb = hex2rgb(color_hex)
            color_rgb = handle_color(color_rgb)
            # Create rgb[a] token
            arguments = [make_number_token(color_rgb[0]), COMMA,
                         make_number_token(color_rgb[1]), COMMA,
                         make_number_token(color_rgb[2])]
            if alpha is None:
                function = 'rgb'
            else:
                function = 'rgba'
                arguments.extend([COMMA, make_number_token(alpha)])

            color_token = tinycss2.ast.FunctionBlock(
                line=None, column=None, name=function, arguments=arguments
            )
            if is_single:
                col_dec.append(color_token)
            else:
                col_dec[-1] = color_token

        if i == len(declarations):  # last token
            if is_color:
                if not is_known:
                    print_warning('Parsed color for declaration with '
                                  'unknown color property', col_dec, token)
                color_declarations.extend(col_dec)
    return color_declarations


def make_number_token(value):
    value_as_int = int(value)
    return tinycss2.ast.NumberToken(
        None, None, value, value_as_int,
        str(value if value == value_as_int else round(value, 3))
    )


def parse_color_func_args(func_token, pct_of):
    values = []
    need_comma = False
    for arg in func_token.arguments:
        if need_comma:
            if arg.type == 'literal' and arg.value == ',':
                need_comma = False
            elif arg.type != 'whitespace':
                return None  # invalid arguments
        else:
            if arg.type == 'number':
                values.append(arg.value)
                need_comma = True
            elif arg.type == 'percentage':
                # 4th argument assumed to be alpha (% of 1)
                values.append(arg.value * 1. / 100 if len(values) == 3 else
                              arg.value * pct_of / 100)
                need_comma = True
            elif arg.type != 'whitespace':
                return None  # invalid arguments
    if not 3 <= len(values) <= 4:
        return None
    return values


def hex2rgb(h):
    b = h & 0xff
    g = (h >> 8) & 0xff
    r = (h >> 16) & 0xff
    return r, g, b


def handle_color(rgb):
    color_hsv = colorsys.rgb_to_hsv(*rgb)
    # Filter saturate + output
    if color_hsv[1] < 0.15:
        # Invert color
        rgb = tuple(255 - c for c in rgb)
    return rgb


with open('css/nytimes.css') as f:
    css = tinycss2.parse_stylesheet(f.read(), skip_comments=True,
                                    skip_whitespace=True)

parsed_color_rules = parse_rules(css)
# Output the parsed CSS - TODO: if css-purge exists use with temporary file
print(tinycss2.serialize(parsed_color_rules))

# === Code for taking all colors and visualizing things/showing unique ===
# standardized_colors = []
# for c in colors:
#     if c.startswith('#'):
#         c = c[1:]
#         if len(c) == 6:
#             standardized_colors.append(c)
#         elif len(c) == 3:
#             standardized_colors.append(c[0] * 2 + c[1] * 2 + c[2] * 2)
#         else:
#             raise RuntimeError('This was unexpected')
#     elif c.startswith('rgb'):
#         pass
#     else:
#         # TODO: map color to hex code
#         standardized_colors.append(format(COLOR_MAP[c.upper()], '06X'))
#
# c_hex = list(set(standardized_colors))
# c_rgb = [(int(c[:2], 16), int(c[2:4], 16), int(c[4:], 16))
#          for c in c_hex]
# c_hsv = [colorsys.rgb_to_hsv(*c) for c in c_rgb]
# c_hls = [colorsys.rgb_to_hls(*c) for c in c_rgb]

# 1 = saturation
# sorted(range(len(c_rgb)), key=lambda i: c_hsv[i][1])
# n_buckets = 10
# buckets = [[] for _ in range(n_buckets)]
# for h, s, v in c_hsv:
#     bucket = min(int(s * 100 / n_buckets), n_buckets - 1)
#     buckets[bucket].append((h, s, v))

# for k in range(3):
#     fig = plt.figure(figsize=(20, 2))
#     ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8])
#     idxs = sorted(range(len(c_rgb)), key=lambda i: c_hls[i][k])
#     to_vis = [c_rgb[i] for i in idxs]
#     print([c_hsv[i] for i in idxs])
#     ax.imshow_rgb(*map(np.asarray, zip(*to_vis)))
#     fig.suptitle(str(k))

# print(rule_out)
# print(sorted(set(standardized_colors)))


# TODO: ignore selectors with e.g. "dark" in name
# TODO: background --> background-color only
# TODO: border or border-* (e.g. bottom) --> border-color only
# TODO: on borders above, can colors be specified only per side??
# TODO: https://sass2css.herokuapp.com/
# TODO: use HTML in color-changing. For non-filtered items, e.g. header with
#  dark blue background, find all child items and do not alter colors.

"""Cleanup dupe rules, etc. (TODO formatting params...)
```
sudo npm install css-purge -g
css-purge -i scratch_dark.css -o scratch_dark_purged.css
```
"""
