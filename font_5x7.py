# Dot matrix LCD font of 5 wide by 7 high.
# 0 : on, voxel should be drawn
# not 0: off, voxel should be cleared

# size of digits/letters
FONT_HEIGHT = 7
FONT_WIDTH = 5

font_design = {
    '0': [
        ' 000 ',
        '0   0',
        '0  00',
        '0 0 0',
        '00  0',
        '0   0',
        ' 000 ',
        ],
    '1': [
        '  0',
        ' 00',
        '  0',
        '  0',
        '  0',
        '  0',
        ' 000',
        ],
    '2': [
        ' 000',
        '0   0',
        '    0',
        '   0',
        '  0',
        ' 0',
        '00000',
        ],
    '3': [
        '00000',
        '   0',
        '  0',
        '   0',
        '    0',
        '0   0',
        ' 000',
        ],
    '4': [
        '   0',
        '  00',
        ' 0 0',
        '0  0',
        '00000',
        '   0',
        '   0',
        ],
    '5': [
        '00000',
        '0    ',
        '0000 ',
        '    0',
        '    0',
        '0   0',
        ' 000',
        ],
    '6': [
        '  00 ',
        ' 0   ',
        '0    ',
        '0000 ',
        '0   0',
        '0   0',
        ' 000 ',
        ],
    '7': [
        '00000',
        '    0',
        '   0 ',
        '  0  ',
        ' 0   ',
        ' 0   ',
        ' 0   ',
        ],
    '8': [
        ' 000 ',
        '0   0',
        '0   0',
        ' 000 ',
        '0   0',
        '0   0',
        ' 000',
        ],
    '9': [
        ' 000 ',
        '0   0',
        '0   0',
        ' 0000',
        '    0',
        '   0',
        ' 00',
        ],
    ':': [
        '     ',
        '  00 ',
        '  00 ',
        '     ',
        '  00 ',
        '  00 ',
        '     ',
        ],
    '-': [
        '',
        '     ',
        '     ',
        ' 000 ',
        '     ',
        '     ',
        '',
        ],
    ' ': [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ],
}
