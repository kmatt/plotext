from plotext._utility import join, memorize, transpose
from plotext._utility.platform import platform

##############################################
##########    Default Markers      ###########
##############################################

space = ' ' # the default null character that appears as background to all plots

plot_marker = "hd" if platform == 'unix' else 'dot'

marker_codes = {'sd'         :'█',
                'dot'        :'•',
                'dollar'     :'$',
                'euro'       :'€',
                'bitcoin'    :'฿',
                'at'         :'@',
                'heart'      :'♥',
                'smile'      :'☺',
                'gclef'      :'𝄞',
                'note'       :'𝅘𝅥',
                'shamrock'   :'☘',
                'atom'       :'⚛',
                'snowflake'  :'❄',
                'star'       : '❋',
                'flower'     : '❁',
                'lightning'  :'🌩',
                'queen'      :'♕',
                'king'       :'♔',
                'cross'      :'♰',
                'yinyang'    :'☯',
                'om'         :'ॐ',
                'osiris'     :'𓂀',
                'zero'       :'🯰',
                'one'        :'🯱',
                'two'        :'🯲',
                'three'      :'🯳',
                'four'       :'🯴',
                'five'       :'🯵',
                'six'        :'🯶',
                'seven'      :'🯷',
                'eight'      :'🯸',
                'nine'       :'🯹'}

hd_symbols = {'hd'  : '▞',
              'fhd' : '🬗',
              'braille' : '⢕'} # the markers that represents the higher definition characters

hd_codes = {(0,0,0,0): ' ', (1,0,0,0): '▘', (0,0,1,0): '▖', (0,0,0,1): '▗', (0,1,0,0): '▝', (1,0,1,0): '▌', (0,1,0,1): '▐', (0,0,1,1): '▄', (1,1,0,0):    '▀', (1,0,0,1): '▚',  (0,1,1,0): '▞', (1,1,1,0): '▛', (1,0,1,1): '▙', (0,1,1,1): '▟', (1,1,0,1): '▜', (1,1,1,1): '█'} # codes for high definition markers used to easily sum them; eg: '▘' + '▗' = '▚'
hd_markers = {hd_codes[el] : el for el in hd_codes}

fhd_codes = {(0,0,0,0,0,0): ' ', (1,0,1,0,1,0):'▌', (0,1,0,1,0,1): '▐', (1,1,1,1,1,1): '█', (1,0,0,0,0,0):'🬀', (0,1,0,0,0,0):'🬁', (1,1,0,0,0,0):'🬂', (0,0,1,0,0,0):'🬃', (1,0,1,0,0,0):'🬄', (0,1,1,0,0,0):'🬅', (1,1,1,0,0,0):'🬆', (0,0,0,1,0,0):'🬇', (1,0,0,1,0,0):'🬈', (0,1,0,1,0,0):'🬉', (1,1,0,1,0,0):'🬊', (0,0,1,1,0,0):'🬋', (1,0,1,1,0,0):'🬌', (0,1,1,1,0,0):'🬍', (1,1,1,1,0,0):'🬎', (0,0,0,0,1,0):'🬏', (1,0,0,0,1,0):'🬐', (0,1,0,0,1,0):'🬑', (1,1,0,0,1,0):'🬒', (0,0,1,0,1,0):'🬓', (0,1,1,0,1,0):'🬔', (1,1,1,0,1,0):'🬕', (0,0,0,1,1,0):'🬖', (1,0,0,1,1,0):'🬗', (0,1,0,1,1,0):'🬘', (1,1,0,1,1,0):'🬙', (0,0,1,1,1,0):'🬚', (1,0,1,1,1,0):'🬛', (0,1,1,1,1,0):'🬜', (1,1,1,1,1,0):'🬝', (0,0,0,0,0,1):'🬞', (1,0,0,0,0,1):'🬟', (0,1,0,0,0,1):'🬠', (1,1,0,0,0,1):'🬡', (0,0,1,0,0,1):'🬢', (1,0,1,0,0,1):'🬣', (0,1,1,0,0,1):'🬤', (1,1,1,0,0,1):'🬥', (0,0,0,1,0,1):'🬦', (1,0,0,1,0,1):'🬧', (1,1,0,1,0,1):'🬨', (0,0,1,1,0,1):'🬩', (1,0,1,1,0,1):'🬪', (0,1,1,1,0,1):'🬫', (1,1,1,1,0,1):'🬬', (0,0,0,0,1,1):'🬭', (1,0,0,0,1,1):'🬮', (0,1,0,0,1,1):'🬯', (1,1,0,0,1,1):'🬰', (0,0,1,0,1,1):'🬱', (1,0,1,0,1,1):'🬲', (0,1,1,0,1,1):'🬳', (1,1,1,0,1,1):'🬴', (0,0,0,1,1,1):'🬵', (1,0,0,1,1,1):'🬶', (0,1,0,1,1,1):'🬷', (1,1,0,1,1,1):'🬸', (0,0,1,1,1,1):'🬹', (1,0,1,1,1,1):'🬺', (0,1,1,1,1,1):'🬻'} # codes for full high definition markers used to easily sum them; eg: '🬐' + '🬇' = '🬗'
fhd_markers = {fhd_codes[el] : el for el in fhd_codes}

braille_codes = {(0,0,0,0,0,0,0,0):' ', (1,0,0,0,0,0,0,0):'⠁', (0,0,1,0,0,0,0,0):'⠂', (1,0,1,0,0,0,0,0):'⠃', (0,0,0,0,1,0,0,0):'⠄', (1,0,0,0,1,0,0,0):'⠅', (0,0,1,0,1,0,0,0):'⠆', (1,0,1,0,1,0,0,0):'⠇', (0,1,0,0,0,0,0,0):'⠈', (1,1,0,0,0,0,0,0):'⠉', (0,1,1,0,0,0,0,0):'⠊', (1,1,1,0,0,0,0,0):'⠋', (0,1,0,0,1,0,0,0):'⠌', (1,1,0,0,1,0,0,0):'⠍', (0,1,1,0,1,0,0,0):'⠎', (1,1,1,0,1,0,0,0):'⠏', (0,0,0,1,0,0,0,0):'⠐', (1,0,0,1,0,0,0,0):'⠑', (0,0,1,1,0,0,0,0):'⠒', (1,0,1,1,0,0,0,0):'⠓', (0,0,0,1,1,0,0,0):'⠔', (1,0,0,1,1,0,0,0):'⠕', (0,0,1,1,1,0,0,0):'⠖', (1,0,1,1,1,0,0,0):'⠗', (0,1,0,1,0,0,0,0):'⠘', (1,1,0,1,0,0,0,0):'⠙', (0,1,1,1,0,0,0,0):'⠚', (1,1,1,1,0,0,0,0):'⠛', (0,1,0,1,1,0,0,0):'⠜', (1,1,0,1,1,0,0,0):'⠝', (0,1,1,1,1,0,0,0):'⠞', (1,1,1,1,1,0,0,0):'⠟', (0,0,0,0,0,1,0,0):'⠠', (1,0,0,0,0,1,0,0):'⠡', (0,0,1,0,0,1,0,0):'⠢', (0,0,0,0,1,1,0,0):'⠤', (1,0,0,0,1,1,0,0):'⠥', (0,0,1,0,1,1,0,0):'⠦', (1,0,1,0,1,1,0,0):'⠧', (0,1,0,0,0,1,0,0):'⠨', (1,1,0,0,0,1,0,0):'⠩', (0,1,1,0,0,1,0,0):'⠪', (1,1,1,0,0,1,0,0):'⠫', (0,1,0,0,1,1,0,0):'⠬', (1,1,0,0,1,1,0,0):'⠭', (0,1,1,0,1,1,0,0):'⠮', (1,1,1,0,1,1,0,0):'⠯', (0,0,0,1,0,1,0,0):'⠰', (1,0,0,1,0,1,0,0):'⠱', (0,0,1,1,0,1,0,0):'⠲', (1,0,1,1,0,1,0,0):'⠳', (0,0,0,1,1,1,0,0):'⠴', (1,0,0,1,1,1,0,0):'⠵', (0,0,1,1,1,1,0,0):'⠶', (1,0,1,1,1,1,0,0):'⠷', (0,1,0,1,0,1,0,0):'⠸', (1,1,0,1,0,1,0,0):'⠹', (0,1,1,1,0,1,0,0):'⠺', (1,1,1,1,0,1,0,0):'⠻', (0,1,0,1,1,1,0,0):'⠼', (1,1,0,1,1,1,0,0):'⠽', (0,1,1,1,1,1,0,0):'⠾', (1,1,1,1,1,1,0,0):'⠿', (0,0,0,0,0,0,1,0):'⡀', (1,0,0,0,0,0,1,0):'⡁', (0,0,1,0,0,0,1,0):'⡂', (1,0,1,0,0,0,1,0):'⡃', (0,0,0,0,1,0,1,0):'⡄', (1,0,0,0,1,0,1,0):'⡅', (0,0,1,0,1,0,1,0):'⡆', (1,0,1,0,1,0,1,0):'⡇', (0,1,0,0,0,0,1,0):'⡈', (1,1,0,0,0,0,1,0):'⡉', (0,1,1,0,0,0,1,0):'⡊', (1,1,1,0,0,0,1,0):'⡋', (0,1,0,0,1,0,1,0):'⡌', (1,1,0,0,1,0,1,0):'⡍', (0,1,1,0,1,0,1,0):'⡎', (1,1,1,0,1,0,1,0):'⡏', (0,0,0,1,0,0,1,0):'⡐', (1,0,0,1,0,0,1,0):'⡑', (0,0,1,1,0,0,1,0):'⡒', (1,0,1,1,0,0,1,0):'⡓', (0,0,0,1,1,1,1,0):'⡔', (1,0,0,1,1,1,1,0):'⡕', (0,0,1,1,1,0,1,0):'⡖', (1,0,1,1,1,0,1,0):'⡗', (0,1,0,1,0,0,1,0):'⡘', (1,1,0,1,0,0,1,0):'⡙', (0,1,1,1,0,0,1,0):'⡚', (1,1,1,1,0,0,1,0):'⡛', (0,1,0,1,1,0,1,0):'⡜', (1,1,0,1,1,0,1,0):'⡝', (0,1,1,1,1,0,1,0):'⡞', (1,1,1,1,1,0,1,0):'⡟', (0,0,0,0,0,1,1,0):'⡠', (1,0,0,0,0,1,1,0):'⡡', (0,0,1,0,0,1,1,0):'⡢', (1,0,1,0,0,1,1,0):'⡣', (0,0,0,0,1,1,1,0):'⡤', (1,0,0,0,1,1,1,0):'⡥', (0,0,1,0,1,1,1,0):'⡦', (1,0,1,0,1,1,1,0):'⡧', (0,1,0,0,0,1,1,0):'⡨', (1,1,0,0,0,1,1,0):'⡩', (0,1,1,0,0,1,1,0):'⡪', (0,1,0,0,1,1,1,0):'⡬', (1,1,0,0,1,1,1,0):'⡭', (0,1,1,0,1,1,1,0):'⡮', (1,1,1,0,1,1,1,0):'⡯', (0,0,0,1,0,1,1,0):'⡰', (1,0,0,1,0,1,1,0):'⡱', (0,0,1,1,0,1,1,0):'⡲', (1,0,1,1,0,1,1,0):'⡳', (0,0,0,1,1,1,1,0):'⡴', (1,0,0,1,1,1,1,0):'⡵', (0,0,1,1,1,1,1,0):'⡶', (1,0,1,1,1,1,1,0):'⡷', (0,1,0,1,0,1,1,0):'⡸', (1,1,0,1,0,1,1,0):'⡹', (0,1,1,1,0,1,1,0):'⡺', (1,1,1,1,0,1,1,0):'⡻', (0,1,0,1,1,1,1,0):'⡼', (1,1,0,1,1,1,1,0):'⡽', (0,1,1,1,1,1,1,0):'⡾', (1,1,1,1,1,1,1,0):'⡿', (0,0,0,0,0,0,0,1):'⢀', (1,0,0,0,0,0,0,1):'⢁', (0,0,1,0,0,0,0,1):'⢂', (1,0,1,0,0,0,0,1):'⢃', (0,0,0,0,1,0,0,1):'⢄', (1,0,0,0,1,0,0,1):'⢅', (0,0,1,0,1,0,0,1):'⢆', (1,0,1,0,1,0,0,1):'⢇', (0,1,0,0,0,0,0,1):'⢈', (1,1,0,0,0,0,0,1):'⢉', (0,1,1,0,0,0,0,1):'⢊', (1,1,1,0,0,0,0,1):'⢋', (0,1,0,0,1,0,0,1):'⢌', (1,1,0,0,1,0,0,1):'⢍', (0,1,1,0,1,0,0,1):'⢎', (1,1,1,0,1,0,0,1):'⢏', (0,0,0,1,0,0,0,1):'⢐', (1,0,0,1,0,0,0,1):'⢑', (0,0,1,1,0,0,0,1):'⢒', (1,0,1,1,0,0,0,1):'⢓', (0,0,0,1,1,0,0,1):'⢔', (1,0,0,1,1,0,0,1):'⢕', (0,0,1,1,1,0,0,1):'⢖', (1,0,1,1,1,0,0,1):'⢗', (0,1,0,1,0,0,0,1):'⢘', (1,1,0,1,0,0,0,1):'⢙', (0,1,1,1,0,0,0,1):'⢚', (1,1,1,1,0,0,0,1):'⢛', (0,1,0,1,1,0,0,1):'⢜', (1,1,0,1,1,0,0,1):'⢝', (0,1,1,1,1,0,0,1):'⢞', (1,1,1,1,1,0,0,1):'⢟', (0,0,0,0,0,1,0,1):'⢠', (1,0,0,0,0,1,0,1):'⢡', (0,0,1,0,0,1,0,1):'⢢', (1,0,1,0,0,1,0,1):'⢣', (0,0,0,0,1,1,0,1):'⢤', (1,0,0,0,1,1,0,1):'⢥', (0,0,1,0,1,1,0,1):'⢦', (1,0,1,0,1,1,0,1):'⢧', (0,1,0,0,0,1,0,1):'⢨', (1,1,0,0,0,1,0,1):'⢩', (0,1,1,0,0,1,0,1):'⢪', (1,1,1,0,0,1,0,1):'⢫', (0,1,0,0,1,1,0,1):'⢬', (1,1,0,0,1,1,0,1):'⢭', (0,1,1,0,1,1,0,1):'⢮', (1,1,1,0,1,1,0,1):'⢯', (0,0,0,1,0,1,0,1):'⢰', (1,0,0,1,0,1,0,1):'⢱', (0,0,1,1,0,1,0,1):'⢲', (1,0,1,1,0,1,0,1):'⢳', (0,0,0,1,1,1,0,1):'⢴', (1,0,0,1,1,1,0,1):'⢵', (0,0,1,1,1,1,0,1):'⢶', (1,0,1,1,1,1,0,1):'⢷', (0,1,0,1,0,1,0,1):'⢸', (1,1,0,1,0,1,0,1):'⢹', (0,1,1,1,0,1,0,1):'⢺', (1,1,1,1,0,1,0,1):'⢻', (0,1,0,1,1,1,0,1):'⢼', (1,1,0,1,1,1,0,1):'⢽', (0,1,1,1,1,1,0,1):'⢾', (1,1,1,1,1,1,0,1):'⢿', (0,0,0,0,0,0,1,1):'⣀', (1,0,0,0,0,0,1,1):'⣁', (0,0,1,0,0,0,1,1):'⣂', (1,0,1,0,0,0,1,1):'⣃', (0,0,0,0,1,0,1,1):'⣄', (1,0,0,0,1,0,1,1):'⣅', (0,0,1,0,1,0,1,1):'⣆', (1,0,1,0,1,0,1,1):'⣇', (0,1,0,0,0,0,1,1):'⣈', (1,1,0,0,0,0,1,1):'⣉', (0,1,1,0,0,0,1,1):'⣊', (1,1,1,0,0,0,1,1):'⣋', (0,1,0,0,1,0,1,1):'⣌', (1,1,0,0,1,0,1,1):'⣍', (0,1,1,0,1,0,1,1):'⣎', (1,1,1,0,1,0,1,1):'⣏', (0,0,0,1,0,0,1,1):'⣐', (1,0,0,1,0,0,1,1):'⣑', (0,0,1,1,0,0,1,1):'⣒', (1,0,1,1,0,0,1,1):'⣓', (0,0,0,1,1,0,1,1):'⣔', (1,0,0,1,1,0,1,1):'⣕', (0,0,1,1,1,0,1,1):'⣖', (1,0,1,1,1,0,1,1):'⣗', (0,1,0,1,0,0,1,1):'⣘', (1,1,0,1,0,0,1,1):'⣙', (0,1,1,1,0,0,1,1):'⣚', (1,1,1,1,0,0,1,1):'⣛', (0,1,0,1,1,0,1,1):'⣜', (1,1,0,1,1,0,1,1):'⣝', (0,1,1,1,1,0,1,1):'⣞', (1,1,1,1,1,0,1,1):'⣟', (0,0,0,0,0,1,1,1):'⣠', (1,0,0,0,0,1,1,1):'⣡', (0,0,1,0,0,1,1,1):'⣢', (1,0,1,0,0,1,1,1):'⣣', (0,0,0,0,1,1,1,1):'⣤', (1,0,0,0,1,1,1,1):'⣥', (0,0,1,0,1,1,1,1):'⣦', (1,0,1,0,1,1,1,1):'⣧', (0,1,0,0,0,1,1,1):'⣨', (1,1,0,0,0,1,1,1):'⣩', (0,1,1,0,0,1,1,1):'⣪', (1,1,1,0,0,1,1,1):'⣫', (0,1,0,0,1,1,1,1):'⣬', (1,1,0,0,1,1,1,1):'⣭', (0,1,1,0,1,1,1,1):'⣮', (1,1,1,0,1,1,1,1):'⣯', (0,0,0,1,0,1,1,1):'⣰', (1,0,0,1,0,1,1,1):'⣱', (0,0,1,1,0,1,1,1):'⣲', (1,0,1,1,0,1,1,1):'⣳', (0,0,0,1,1,1,1,1):'⣴', (1,0,0,1,1,1,1,1):'⣵', (0,0,1,1,1,1,1,1):'⣶', (1,0,1,1,1,1,1,1):'⣷', (0,1,0,1,0,1,1,1):'⣸', (1,1,0,1,0,1,1,1):'⣹', (0,1,1,1,0,1,1,1):'⣺', (1,1,1,1,0,1,1,1):'⣻', (0,1,0,1,1,1,1,1):'⣼', (1,1,0,1,1,1,1,1):'⣽', (0,1,1,1,1,1,1,1):'⣾', (1,1,1,1,1,1,1,1):'⣿', (0,0,0,1,1,0,1,0):'⡔', (1,0,0,1,1,0,1,0):'⡕', (1,0,1,0,0,1,0,0):'⠣', (1,1,1,0,0,1,1,0):'⡫'}
braille_markers = {braille_codes[el] : el for el in braille_codes}

@memorize
def get_hd_marker(code):
   return hd_codes[code] if len(code) == 4 else fhd_codes[code] if len(code) == 6 else braille_codes[code]

def marker_factor(marker, hd, fhd, braille): # usefull to improve the resolution of the canvas for higher resolution markers
   return hd if marker == 'hd' else fhd if marker == 'fhd' else braille if marker == 'braille' else 1
