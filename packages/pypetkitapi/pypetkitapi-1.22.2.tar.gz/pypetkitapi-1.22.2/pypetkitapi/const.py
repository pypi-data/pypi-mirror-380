"""Constants for the pypetkitapi library."""

from enum import StrEnum

DEFAULT_COUNTRY = "DE"
DEFAULT_TZ = "Europe/Berlin"
PTK_DBG = "enable_dbg"

RES_KEY = "result"
ERR_KEY = "error"
SUCCESS_KEY = "success"

DEVICE_RECORDS = "deviceRecords"
DEVICE_DATA = "deviceData"
DEVICE_STATS = "deviceStats"
PET_DATA = "petData"
LIVE_DATA = "liveData"

# Bluetooth
BLE_CONNECT_ATTEMPT = 32
BLE_START_TRAME = [250, 252, 253]
BLE_END_TRAME = [251]

# PetKit Models
FEEDER = "feeder"
FEEDER_MINI = "feedermini"
D3 = "d3"
D4 = "d4"
D4S = "d4s"
D4H = "d4h"
D4SH = "d4sh"
T3 = "t3"
T4 = "t4"
T5 = "t5"
T6 = "t6"
T7 = "t7"
W4 = "w4"
W5 = "w5"
CTW2 = "ctw2"
CTW3 = "ctw3"
K2 = "k2"
K3 = "k3"
PET = "pet"

# Litter
DEVICES_LITTER_BOX = [T3, T4, T5, T6, T7]
LITTER_WITH_CAMERA = [T5, T6, T7]
LITTER_NO_CAMERA = [T3, T4]
# Feeder
FEEDER_WITH_CAMERA = [D4H, D4SH]
DEVICES_FEEDER = [FEEDER, FEEDER_MINI, D3, D4, D4S, D4H, D4SH]
# Water Fountain
DEVICES_WATER_FOUNTAIN = [W4, W5, CTW2, CTW3]
# Purifier
DEVICES_PURIFIER = [K2, K3]
# All devices
ALL_DEVICES = [
    *DEVICES_LITTER_BOX,
    *DEVICES_FEEDER,
    *DEVICES_WATER_FOUNTAIN,
    *DEVICES_PURIFIER,
]


class PetkitDomain(StrEnum):
    """Petkit URL constants"""

    PASSPORT_PETKIT = "https://passport.petkt.com/"
    CHINA_SRV = "https://api.petkit.cn/6/"


class Client(StrEnum):
    """Platform constants"""

    PLATFORM_TYPE = "android"
    OS_VERSION = "15.1"
    MODEL_NAME = "23127PN0CG"
    SOURCE = "app.petkit-android"
    PHONE_BRAND = "Xiaomi"


class Header(StrEnum):
    """Header constants"""

    ACCEPT = "*/*"
    ACCEPT_LANG = "en-US;q=1, it-US;q=0.9"
    ENCODING = "gzip, deflate"
    API_VERSION = "12.4.9"
    CONTENT_TYPE = "application/x-www-form-urlencoded"
    AGENT = "okhttp/3.14.19"
    CLIENT = f"{Client.PLATFORM_TYPE}({Client.OS_VERSION};{Client.MODEL_NAME})"
    LOCALE = "en-US"
    IMG_VERSION = "1"
    HOUR = "24"


CLIENT_NFO = {
    "locale": Header.LOCALE.value,
    "name": Client.MODEL_NAME.value,
    "osVersion": Client.OS_VERSION.value,
    "phoneBrand": Client.PHONE_BRAND.value,
    "platform": Client.PLATFORM_TYPE.value,
    "source": Client.SOURCE.value,
    "version": Header.API_VERSION.value,
}

LOGIN_DATA = {
    "oldVersion": Header.API_VERSION.value,
}


class MediaType(StrEnum):
    """Record Type constants"""

    VIDEO = "mp4"
    IMAGE = "jpg"


class VideoType(StrEnum):
    """Record Type constants"""

    HIGHLIGHT = "highlight"
    PLAYBACK = "playback"


class RecordType(StrEnum):
    """Record Type constants"""

    EAT = "eat"
    FEED = "feed"
    MOVE = "move"
    PET = "pet"
    TOILETING = "toileting"
    WASTE_CHECK = "waste_check"
    DISH_BEFORE = "dish_before"
    DISH_AFTER = "dish_after"


RecordTypeLST = [
    RecordType.EAT,
    RecordType.FEED,
    RecordType.MOVE,
    RecordType.PET,
    RecordType.TOILETING,
    RecordType.WASTE_CHECK,
    RecordType.DISH_BEFORE,
    RecordType.DISH_AFTER,
]


class PetkitEndpoint(StrEnum):
    """Petkit Endpoint constants"""

    REGION_SERVERS = "v1/regionservers"
    LOGIN = "user/login"
    GET_LOGIN_CODE = "user/sendcodeforquicklogin"
    REFRESH_SESSION = "user/refreshsession"
    DETAILS = "user/details2"
    UNREAD_STATUS = "user/unreadStatus"
    FAMILY_LIST = "group/family/list"
    REFRESH_HOME_V2 = "refreshHomeV2"

    # Common to many device
    DEVICE_DETAIL = "device_detail"
    DEVICE_DATA = "deviceData"
    GET_DEVICE_RECORD = "getDeviceRecord"
    GET_DEVICE_RECORD_RELEASE = "getDeviceRecordRelease"
    UPDATE_SETTING = "updateSettings"
    UPDATE_SETTING_OLD = "update"

    # Bluetooth
    BLE_AS_RELAY = "ble/ownSupportBleDevices"
    BLE_CONNECT = "ble/connect"
    BLE_POLL = "ble/poll"
    BLE_CANCEL = "ble/cancel"
    BLE_CONTROL_DEVICE = "ble/controlDevice"

    # Fountain & Litter Box
    CONTROL_DEVICE = "controlDevice"
    GET_WORK_RECORD = "getWorkRecord"

    # Litter Box
    DEODORANT_RESET = "deodorantReset"  # For N50 only
    STATISTIC = "statistic"
    STATISTIC_RELEASE = "statisticRelease"
    GET_PET_OUT_GRAPH = "getPetOutGraph"

    # Video features
    LIVE = "start/live"
    GET_M3U8 = "getM3u8"
    CLOUD_VIDEO = "cloud/video"
    GET_DOWNLOAD_M3U8 = "getDownloadM3u8"

    # Feeders
    REPLENISHED_FOOD = "added"
    FRESH_ELEMENT_CALIBRATION = "food_reset"
    FRESH_ELEMENT_CANCEL_FEED = "cancel_realtime_feed"
    DESICCANT_RESET_OLD = "desiccant_reset"
    DESICCANT_RESET_NEW = "desiccantReset"
    CALL_PET = "callPet"
    CANCEL_FEED = "cancelRealtimeFeed"
    MANUAL_FEED_OLD = "save_dailyfeed"  # For Feeder/FeederMini
    MANUAL_FEED_NEW = "saveDailyFeed"  # For all other feeders
    DAILY_FEED_AND_EAT = "dailyFeedAndEat"  # D3
    FEED_STATISTIC = "feedStatistic"  # D4
    DAILY_FEED = "dailyFeeds"  # D4S
    REMOVE_DAILY_FEED = "removeDailyFeed"
    RESTORE_DAILY_FEED = "restoreDailyFeed"
    SAVE_FEED = "saveFeed"  # For Feeding plan

    # Schedule
    SCHEDULE = "schedule/schedules"
    SCHEDULE_SAVE = "schedule/save"
    SCHEDULE_REMOVE = "schedule/remove"
    SCHEDULE_COMPLETE = "schedule/complete"
    SCHEDULE_HISTORY = "schedule/userHistorySchedules"

    # Pet
    PET_UPDATE_SETTING = "updatepetprops"
