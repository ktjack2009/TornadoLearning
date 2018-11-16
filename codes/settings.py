# 参数

from collections import namedtuple

key_string = [
    'port',
]
Options = namedtuple('Options', key_string)
options = Options(
    port=8000
)
