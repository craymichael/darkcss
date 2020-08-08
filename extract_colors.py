import re
import sys
import colorsys
from itertools import chain

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
COLOR_MAP = dict(zip(map(str.upper, COLORS), COLOR_MAP.values()))
COLORS_UPPER = list(COLOR_MAP.keys())
COLORS_LOWER = list(map(str.lower, COLORS))
COLORS_MISC = [
    r'rgb *\( *[0-9]{1,3} *, *[0-9]{1,3} *, *[0-9]{1,3} *\)',
    # TODO: alpha is 0-1
    r'rgba *\( *[0-9]{1,3} *, *[0-9]{1,3} *, *[0-9]{1,3} *, *[0-9]{1,3} *\)'
]
RE_C = re.compile(
    r'(#[a-fA-F0-9]{3}|'
    r'#[a-fA-F0-9]{6}|'
    r'(?<=[: \t\n])(?:' +
    '|'.join(chain(COLORS, COLORS_UPPER, COLORS_LOWER, COLORS_MISC)) +
    r'))'
    r'(?:[; \t\n!}]+|$)'
)
# CSS rules
RE_R = re.compile(
    r'([^{}]+{(?:([^{}]*{[^{}]*}[^{}]*)+|[^{}]*)})'
)

# if len(sys.argv) == 1:
#     css_orig = sys.stdin.read()
# elif len(sys.argv) == 2:
#     filename = sys.argv[1]
#     with open(filename, 'r') as f:
#         css_orig = f.read()
# else:
#     sys.exit('Usage: use it correctly')
#
# css_tmp = css_orig
# css_mod = ''
# while True:
#     # Remove comments
#     idx_a = css_tmp.find('/*')
#     if idx_a == -1:
#         css_mod += css_tmp
#         break
#     idx_b_adjust = idx_a + 2
#     idx_b = css_tmp[idx_b_adjust:].find('*/') + idx_b_adjust
#     if idx_b == -1:
#         raise ValueError('Invalid comment: "{}"'.format(
#             css_tmp[idx_a:idx_a + 80]))
#     css_mod += css_tmp[:idx_a]
#     css_tmp = css_tmp[idx_b + 2:]


def handle_color(line):
    # Color
    color_orig = color = color_match.groups()[0]
    alpha = None

    if color.startswith('#'):
        color = color[1:]
        if len(color) == 6:
            pass
        elif len(color) == 3:
            color = color[0] * 2 + color[1] * 2 + color[2] * 2
        else:
            raise RuntimeError('This was unexpected')
        color_rgb = (int(color[:2], 16),
                     int(color[2:4], 16),
                     int(color[4:], 16))
    elif color.startswith('rgb'):
        color_rgb = color[color.index('(') + 1:
                          color.index(')')].split(',')
        if color[3] == 'a':
            assert len(color_rgb) == 4
            alpha = color_rgb.pop(3)
        else:
            assert len(color_rgb) == 3
        color_rgb = list(map(int, color_rgb))
    else:
        color = format(COLOR_MAP[color.upper()], '06X')
        color_rgb = (int(color[:2], 16),
                     int(color[2:4], 16),
                     int(color[4:], 16))

    colors.append(color)

    color_hsv = colorsys.rgb_to_hsv(*color_rgb)

    # Filter saturate + output
    # if color_rgb == (48, 65, 84):  # TODO: ad hoc for propublica
    if color_hsv[1] < 0.15:
        # Invert color
        # color_rgb = [120, 147, 179]  # TODO: ad hoc for propublica
        color_rgb = [255 - c for c in color_rgb]
        if alpha is None:
            color = '#' + ''.join(map(lambda u: format(u, '02X'),
                                      color_rgb))
        else:
            color_rgb.append(alpha)
            color = 'rgba({}, {}, {}, {})'.format(*color_rgb)
        line = line.replace(color_orig, color)

        # Rule with colors
        color_content.append(
            ': '.join(line.strip().split(':', 1)) + ';'
        )
    # Rescale from min-max 000-FFF to 111-EEE
    # def scale_channel(ch):
    #     return round(ch / 0xFF * (0xEE - 0x11) + 0x11)
    #
    #
    # color_rgb = list(map(scale_channel, color_rgb))
    # if alpha is None:
    #     color = '#' + ''.join(map(lambda u: format(u, '02X'),
    #                               color_rgb))
    # else:
    #     color_rgb.append(alpha)
    #     color = 'rgba({}, {}, {}, {})'.format(*color_rgb)
    # line = line.replace(color_orig, color)
    # # Rule with colors
    # color_content.append(
    #     ': '.join(line.strip().split(':', 1)) + ';'
    # )


rule_out = ''
colors = []
# TODO: the following string breaks RE_R regex (catastrophic backtracking):
#  @supports (grid-auto-flow:dense){.sg-row.s-result-list{display:grid;align-items:stretch;justify-items:stretch}.sg-row.s-result-list.s-search-results{grid-auto-flow:dense}.s-result-list>.sg-col{float:none;min-width:0;width:auto}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col{min-width:0;width:auto}.s-result-list>.s-flex-geom.sg-col{display:block}.s-result-list>*{grid-column:1/-1}.s-result-list>.sg-col-1-of-16{grid-column:auto/span 1}.s-result-list>.sg-col-2-of-16{grid-column:auto/span 2}.s-result-list>.sg-col-3-of-16{grid-column:auto/span 3}.s-result-list>.sg-col-4-of-16{grid-column:auto/span 4}.s-result-list>.sg-col-5-of-16{grid-column:auto/span 5}.s-result-list>.sg-col-6-of-16{grid-column:auto/span 6}.s-result-list>.sg-col-7-of-16{grid-column:auto/span 7}.s-result-list>.sg-col-8-of-16{grid-column:auto/span 8}.s-result-list>.sg-col-9-of-16{grid-column:auto/span 9}.s-result-list>.sg-col-10-of-16{grid-column:auto/span 10}.s-result-list>.sg-col-11-of-16{grid-column:auto/span 11}.s-result-list>.sg-col-12-of-16{grid-column:auto/span 12}.s-result-list>.sg-col-13-of-16{grid-column:auto/span 13}.s-result-list>.sg-col-14-of-16{grid-column:auto/span 14}.s-result-list>.sg-col-15-of-16{grid-column:auto/span 15}.s-result-list>.sg-col-16-of-16{grid-column:auto/span 16}@media (min-width:1250px){.s-result-list>.sg-col-1-of-20{grid-column:auto/span 1}.s-result-list>.sg-col-2-of-20{grid-column:auto/span 2}.s-result-list>.sg-col-3-of-20{grid-column:auto/span 3}.s-result-list>.sg-col-4-of-20{grid-column:auto/span 4}.s-result-list>.sg-col-5-of-20{grid-column:auto/span 5}.s-result-list>.sg-col-6-of-20{grid-column:auto/span 6}.s-result-list>.sg-col-7-of-20{grid-column:auto/span 7}.s-result-list>.sg-col-8-of-20{grid-column:auto/span 8}.s-result-list>.sg-col-9-of-20{grid-column:auto/span 9}.s-result-list>.sg-col-10-of-20{grid-column:auto/span 10}.s-result-list>.sg-col-11-of-20{grid-column:auto/span 11}.s-result-list>.sg-col-12-of-20{grid-column:auto/span 12}.s-result-list>.sg-col-13-of-20{grid-column:auto/span 13}.s-result-list>.sg-col-14-of-20{grid-column:auto/span 14}.s-result-list>.sg-col-15-of-20{grid-column:auto/span 15}.s-result-list>.sg-col-16-of-20{grid-column:auto/span 16}.s-result-list>.sg-col-17-of-20{grid-column:auto/span 17}.s-result-list>.sg-col-18-of-20{grid-column:auto/span 18}.s-result-list>.sg-col-19-of-20{grid-column:auto/span 19}.s-result-list>.sg-col-20-of-20{grid-column:auto/span 20}}.sg-row.s-result-list{margin-right:-12px}.sg-row.s-result-list{grid-template-columns:repeat(12,1fr)}.s-result-list>.sg-col-13-of-16{grid-column:auto/span 12}.s-result-list>.sg-col-14-of-16{grid-column:auto/span 12}.s-result-list>.sg-col-15-of-16{grid-column:auto/span 12}.s-result-list>.sg-col-16-of-16{grid-column:auto/span 12}@media (min-width:1250px){.sg-row.s-result-list{grid-template-columns:repeat(16,1fr)}.s-result-list>.sg-col-17-of-20{grid-column:auto/span 16}.s-result-list>.sg-col-18-of-20{grid-column:auto/span 16}.s-result-list>.sg-col-19-of-20{grid-column:auto/span 16}.s-result-list>.sg-col-20-of-20{grid-column:auto/span 16}}@media (min-width:220px){.nav-ewc-persistent-hover.a-js .sg-row.s-result-list{grid-template-columns:repeat(12,1fr)}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-9-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-10-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-11-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-12-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-13-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-14-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-15-of-16{grid-column:auto/span 12}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-16-of-16{grid-column:auto/span 12}}@media (min-width:1470px){.nav-ewc-persistent-hover.a-js .sg-row.s-result-list{grid-template-columns:repeat(16,1fr)}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-13-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-14-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-15-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-16-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-17-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-18-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-19-of-20{grid-column:auto/span 16}.nav-ewc-persistent-hover.a-js .s-result-list>.sg-col-20-of-20{grid-column:auto/span 16}}}


import tinycss2
import tinycss2.ast


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


def parse_colors(declarations):
    # https://tinycss2.readthedocs.io/en/latest/
    color_declarations = []
    col_dec = []
    is_color = False
    for token in declarations:
        if ((token.type == 'whitespace' and not col_dec) or
                token.type == 'comment'):
            continue  # ignore these tokens
        # Otherwise
        col_dec.append(token)
        if token.type == 'literal' and token.value == ';':
            # end of line
            if is_color:
                color_declarations.extend(col_dec)
            # Reset
            col_dec = []
            is_color = False
        elif (token.type == 'function' and
              (token.lower_name == 'rgb' or token.lower_name == 'rgba')):
            is_color = True  # rgb/rgba
        elif token.type == 'ident':
            token_val = token.value.lower()
            if token_val.endswith('-color') or token_val == 'color':
                is_color = True  # token with color as value
        elif token.type == 'hash':
            # TODO: is this always true?
            is_color = True  # hash token, get value using `token.value`
    return color_declarations


with open('css/nytimes.css') as f:
    css = tinycss2.parse_stylesheet(f.read(), skip_comments=True,
                                    skip_whitespace=True)

color_rules = parse_rules(css)
print(tinycss2.serialize(color_rules))

# TODO
# tinycss2.ast.FunctionBlock -> x.arguments for rgb/rgba (x.name)
# <IdentToken color>, <LiteralToken :>, <IdentToken black>
# <IdentToken color>, <LiteralToken :>, <HashToken #fff>


for match in RE_R.finditer(css_mod):
    rule, nested = match.groups()
    # Check if nested, e.g. due to @media...{...{...}...}
    if nested:
        # print('I am too dumb to handle this properly so hopefully this works '
        #       'treating as non-nested color-replacement rule...')
        # TODO: this code is correct but just use code past continue in function
        #  etc.
        # sub_iter = RE_R.finditer(rule[0])
        print('FIXME::ignoring rule', rule, file=sys.stderr)

    # if RE_C.search(rule):
    #     print(rule)
    start = rule.index('{')
    rule_content = rule[start + 1:rule.rindex('}')]
    color_content = []
    for line in rule_content.split(';'):
        # TODO: multiple colors in same line/rule...
        color_match = RE_C.search(line)
        if color_match:
            handle_color(line)
    if color_content:
        sep = '\n    '
        rule_pretty = (
                ',\n'.join(
                    [s.strip() for s in rule[:start].split(',')]) + ' {' +
                sep + sep.join(color_content) + '\n}'
        )
        rule_out += rule_pretty + '\n'

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

print(rule_out)
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
