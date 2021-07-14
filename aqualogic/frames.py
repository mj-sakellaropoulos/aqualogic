from enum import Enum, unique


class Frames(Enum):
    FRAME_DLE = 0x10
    FRAME_STX = 0x02
    FRAME_ETX = 0x03

    # Local wired panel (black face with service button)
    FRAME_TYPE_LOCAL_WIRED_KEY_EVENT = b'\x00\x02'
    # Remote wired panel (white face)
    FRAME_TYPE_REMOTE_WIRED_KEY_EVENT = b'\x00\x03'
    # Wireless remote
    FRAME_TYPE_WIRELESS_KEY_EVENT = b'\x00\x83'
    FRAME_TYPE_ON_OFF_EVENT = b'\x00\x05'   # Seems to only work for some keys

    FRAME_TYPE_KEEP_ALIVE = b'\x01\x01'
    FRAME_TYPE_LEDS = b'\x01\x02'
    FRAME_TYPE_DISPLAY_UPDATE = b'\x01\x03'
    FRAME_TYPE_LONG_DISPLAY_UPDATE = b'\x04\x0a'
    FRAME_TYPE_PUMP_SPEED_REQUEST = b'\x0c\x01'
    FRAME_TYPE_PUMP_STATUS = b'\x00\x0c'

    #AquaPod mystery
    FRAME_TYPE_AQUAPOD_KEY_EVENT = b'\x00\x8c'
