"""Dataclasses for Litter."""

from datetime import datetime
from typing import Any, ClassVar

from pydantic import BaseModel, Field

from pypetkitapi.const import (
    DEVICE_DATA,
    DEVICE_RECORDS,
    DEVICE_STATS,
    LITTER_NO_CAMERA,
    LITTER_WITH_CAMERA,
    T3,
    T4,
    T5,
    T6,
    T7,
    PetkitEndpoint,
)
from pypetkitapi.containers import (
    CloudProduct,
    Device,
    FirmwareDetail,
    LiveFeed,
    UserDevice,
    Wifi,
)
from pypetkitapi.purifier_container import Purifier


class SettingsLitter(BaseModel):
    """Sub-dataclass for settings of Litter.
    Litter -> settings
    """

    auto_interval_min: int | None = Field(None, alias="autoIntervalMin")
    auto_interval_spray: int | None = Field(None, alias="autoIntervalSpray")
    auto_product: int | None = Field(None, alias="autoProduct")
    auto_spray: int | None = Field(None, alias="autoSpray")
    auto_work: int | None = Field(None, alias="autoWork")
    avoid_repeat: int | None = Field(None, alias="avoidRepeat")
    bury: int | None = None
    camera: int | None = None
    camera_config: int | None = Field(None, alias="cameraConfig")
    camera_inward: int | None = Field(None, alias="cameraInward")
    camera_light: int | None = Field(None, alias="cameraLight")
    camera_off: int | None = Field(None, alias="cameraOff")
    cleanning_notify: int | None = Field(None, alias="cleanningNotify")
    click_ok_enable: int | None = Field(None, alias="clickOkEnable")
    control_settings: int | None = Field(None, alias="controlSettings")
    deep_clean: int | None = Field(None, alias="deepClean")
    deep_refresh: int | None = Field(None, alias="deepRefresh")
    deep_spray: int | None = Field(None, alias="deepSpray")
    deodorant_notify: int | None = Field(None, alias="deodorantNotify")
    distrub_multi_range: list[list[int]] | None = Field(None, alias="distrubMultiRange")
    disturb_config: int | None = Field(None, alias="disturbConfig")
    disturb_mode: int | None = Field(None, alias="disturbMode")
    disturb_range: list[int] | None = Field(None, alias="disturbRange")
    downpos: int | None = None
    dump_switch: int | None = Field(None, alias="dumpSwitch")
    fixed_time_clear: int | None = Field(None, alias="fixedTimeClear")
    fixed_time_spray: int | None = Field(None, alias="fixedTimeSpray")
    garbage_notify: int | None = Field(None, alias="garbageNotify")
    highlight: int | None = Field(None, alias="highlight")
    home_mode: int | None = Field(None, alias="homeMode")
    kitten: int | None = None
    kitten_percent: float | None = Field(None, alias="kittenPercent")
    kitten_tips_time: int | None = Field(None, alias="kittenTipsTime")
    lack_liquid_notify: int | None = Field(None, alias="lackLiquidNotify")
    lack_sand_notify: int | None = Field(None, alias="lackSandNotify")
    language: str | None = None
    language_follow: int | None = Field(None, alias="languageFollow")
    languages: list[str] | None = None
    light_assist: int | None = Field(None, alias="lightAssist")
    light_assist_config: int | None = Field(None, alias="lightAssistConfig")
    light_config: int | None = Field(None, alias="lightConfig")
    light_mode: int | None = Field(None, alias="lightMode")
    light_multi_range: list[Any] | None = Field(None, alias="lightMultiRange")
    light_range: list[int] | None = Field(None, alias="lightRange")
    lightest: int | None = Field(None, alias="lightest")
    litter_full_notify: int | None = Field(None, alias="litterFullNotify")
    live_encrypt: int | None = Field(None, alias="liveEncrypt")
    manual_lock: int | None = Field(None, alias="manualLock")
    microphone: int | None = None
    microlight: int | None = None
    move_notify: int | None = Field(None, alias="moveNotify")
    night: int | None = None
    no_remind: int | None = Field(None, alias="noRemind")
    no_sound: int | None = Field(None, alias="noSound")
    package_standard: list[int] | None = Field(None, alias="packageStandard")
    pet_detection: int | None = Field(None, alias="petDetection")
    pet_in_notify: int | None = Field(None, alias="petInNotify")
    pet_notify: int | None = Field(None, alias="petNotify")
    ph_detection: int | None = Field(None, alias="phDetection")
    pre_live: int | None = Field(None, alias="preLive")
    relate_k3_switch: int | None = Field(None, alias="relateK3Switch")
    sand_saving: int | None = Field(None, alias="sandSaving")
    sand_type: int | None = Field(None, alias="sandType")
    sand_tray_notify: int | None = Field(None, alias="sandTrayNotify")
    soft_mode: int | None = Field(None, alias="softMode")
    soft_mode_clean: int | None = Field(None, alias="softModeClean")
    spray_notify: int | None = Field(None, alias="sprayNotify")
    still_time: int | None = Field(None, alias="stillTime")
    stop_time: int | None = Field(None, alias="stopTime")
    system_sound_enable: int | None = Field(None, alias="systemSoundEnable")
    time_display: int | None = Field(None, alias="timeDisplay")
    toilet_detection: int | None = Field(None, alias="toiletDetection")
    toilet_light: int | None = Field(None, alias="toiletLight")
    toilet_light_assist: int | None = Field(None, alias="toiletLightAssist")
    toilet_light_assist_config: int | None = Field(
        None, alias="toiletLightAssistConfig"
    )
    toilet_notify: int | None = Field(None, alias="toiletNotify")
    tone_config: int | None = Field(None, alias="toneConfig")
    tone_mode: int | None = Field(None, alias="toneMode")
    tone_multi_range: list[list[int]] | None = Field(None, alias="toneMultiRange")
    tumbling: int | None = None
    underweight: int | None = Field(None, alias="underweight")
    unit: int | None = None
    urine: int | None = None
    upload: int | None = None
    voice: int | None = None
    volume: int | None = None
    wander_detection: int | None = Field(None, alias="wanderDetection")
    weight_popup: int | None = Field(None, alias="weightPopup")
    wifi_light_assist: int | None = Field(None, alias="wifiLightAssist")
    wifi_light_assist_config: int | None = Field(None, alias="wifiLightAssistConfig")
    wifi_light_assist_multi_range: list[list[int]] | None = Field(
        None, alias="wifiLightAssistMultiRange"
    )
    work_notify: int | None = Field(None, alias="workNotify")


class WorkState(BaseModel):
    """Sub-Sub-dataclass for state of Litter.
    Litter -> state ->  [STATE] -> WorkState
    """

    safe_warn: int | None = Field(None, alias="safeWarn")
    stop_time: int | None = Field(None, alias="stopTime")
    work_mode: int | None = Field(None, alias="workMode")
    work_process: int | None = Field(None, alias="workProcess")
    work_reason: int | None = Field(None, alias="workReason")
    pet_in_time: int | None = Field(None, alias="petInTime")


class StateLitter(BaseModel):
    """Sub-dataclass for state of Litter.
    Litter -> state
    """

    bagging_state: int | None = Field(None, alias="baggingState")
    battery: int | None = None
    box: int | None = None
    box_full: bool | None = Field(None, alias="boxFull")
    box_state: int | None = Field(None, alias="boxState")
    box_store_state: int | None = Field(None, alias="boxStoreState")
    camera_status: int | None = Field(None, alias="cameraStatus")
    deodorant_left_days: int | None = Field(None, alias="deodorantLeftDays")
    dump_state: int | None = Field(None, alias="dumpState")
    error_code: str | None = Field(None, alias="errorCode")
    error_detail: str | None = Field(None, alias="errorDetail")
    error_level: int | None = Field(None, alias="errorLevel")
    error_msg: str | None = Field(None, alias="errorMsg")
    frequent_restroom: int | None = Field(None, alias="frequentRestroom")
    liquid: int | None = None
    liquid_empty: bool | None = Field(None, alias="liquidEmpty")
    liquid_lack: bool | None = Field(None, alias="liquidLack")
    liquid_reset: int | None = Field(None, alias="liquidReset")
    light_state: WorkState | None = Field(None, alias="lightState")
    low_power: bool | None = Field(None, alias="lowPower")
    offline_time: int | None = Field(None, alias="offlineTime")
    ota: int | None = None
    overall: int | None = None
    pack_state: int | None = Field(None, alias="packState")
    package_install: int | None = Field(None, alias="packageInstall")
    package_secret: str | None = Field(None, alias="packageSecret")
    package_sn: str | None = Field(None, alias="packageSn")
    package_state: int | None = Field(None, alias="packageState")
    pet_error: bool | None = Field(None, alias="petError")
    pet_in_time: int | None = Field(None, alias="petInTime")
    pim: int | None = None
    pi_ins: int | None = Field(None, alias="piIns")
    power: int | None = None
    purification_left_days: int | None = Field(None, alias="purificationLeftDays")
    refresh_state: WorkState | None = Field(None, alias="refreshState")
    sand_correct: int | None = Field(None, alias="sandCorrect")
    sand_lack: bool | None = Field(None, alias="sandLack")
    sand_percent: int | None = Field(None, alias="sandPercent")
    sand_status: int | None = Field(None, alias="sandStatus")
    sand_type: int | None = Field(None, alias="sandType")
    sand_weight: int | None = Field(None, alias="sandWeight")
    sand_tray_sn: str | None = Field(None, alias="sandTraySn")  # T7 only
    sand_tray_secret: str | None = Field(None, alias="sandTraySecret")  # T7 only
    sand_tray_use_count: int | None = Field(None, alias="sandTrayUseCount")  # T7 only
    sand_tray_standard_count: int | None = Field(
        None, alias="sandTrayStandardCount"
    )  # T7 only
    sand_tray_standard_day: int | None = Field(
        None, alias="sandTrayStandardDay"
    )  # T7 only
    sand_tray_install_time: int | None = Field(
        None, alias="sandTrayInstallTime"
    )  # T7 only
    sand_tray_left_day: int | None = Field(None, alias="sandTrayLeftDay")  # T7 only
    sand_tray_state: int | None = Field(None, alias="sandTrayState")  # T7 only
    seal_door_state: int | None = Field(None, alias="sealDoorState")
    spray_days: int | None = Field(None, alias="sprayDays")
    spray_left_days: int | None = Field(None, alias="sprayLeftDays")
    spray_reset_time: int | None = Field(None, alias="sprayResetTime")
    spray_state: int | None = Field(None, alias="sprayState")
    top_ins: int | None = Field(None, alias="topIns")
    trunk_state: int | None = Field(None, alias="trunkState")
    used_times: int | None = Field(None, alias="usedTimes")
    wander_time: int | None = Field(None, alias="wanderTime")
    weight_state: int | None = Field(None, alias="weightState")
    wifi: Wifi | None = None
    work_state: WorkState | None = Field(None, alias="workState")
    ph_sand: int | None = Field(None, alias="phSand")  # T7 only
    soft_state: int | None = Field(None, alias="softState")  # T7 only
    soft_time: int | None = Field(None, alias="softTime")  # T7 only
    camera_state: int | None = Field(None, alias="cameraState")  # T7 only
    rotate_angle: str | None = Field(None, alias="rotateAngle")  # T7 only
    sand_tray_tip: int | None = Field(None, alias="sandTrayTip")  # T7 only


class ContentSC(BaseModel):
    """Sub-Sub-class of LitterRecord.
    LitterRecord -> subContent -> content
    """

    box: int | None = None
    box_full: bool | None = Field(None, alias="boxFull")
    detection_info: list | None = Field(None, alias="detectionInfo")
    err: str | None = None
    litter_percent: int | None = Field(None, alias="litterPercent")
    mark: int | None = None
    media: int | None = None
    ph_reason: int | None = Field(None, alias="phReason")
    ph_state: int | None = Field(None, alias="phState")
    result: int | None = None
    start_reason: int | None = Field(None, alias="startReason")
    start_time: int | None = Field(None, alias="startTime")
    upload: int | None = None
    urine_bolus: int | None = Field(None, alias="urineBolus")
    soft_stools: int | None = Field(None, alias="softStools")
    hard_stools: int | None = Field(None, alias="hardStools")


class LRContent(BaseModel):
    """Dataclass for sub-content of LitterRecord.
    LitterRecord -> ShitPictures
    """

    area: int | None = None
    auto_clear: int | None = Field(None, alias="autoClear")
    clear_over_tips: int | None = Field(None, alias="clearOverTips")
    count: int | None = None
    interval: int | None = None
    mark: int | None = None
    media: int | None = None
    pet_out_tips: int | None = Field(None, alias="petOutTips")
    pet_weight: int | None = Field(None, alias="petWeight")
    pet_voice: int | None = Field(None, alias="petVoice")
    start_time: int | None = Field(None, alias="startTime")
    time_in: int | None = Field(None, alias="timeIn")
    time_out: int | None = Field(None, alias="timeOut")
    toilet_detection: int | None = Field(None, alias="toiletDetection")
    upload: int | None = None
    error: int | None = None
    voice_time: str | list | None = Field(
        None, alias="voiceTime"
    )  # Workaround bad implementation from Petkit API for empty list "[]"


class ShitPictures(BaseModel):
    """Dataclass for sub-content of LitterRecord.
    LitterRecord -> ShitPictures
    """

    created_at: str | int | None = Field(None, alias="createdAt")
    pic_id: str | None = Field(None, alias="picId")
    shit_aes_key: str | None = Field(None, alias="shitAesKey")
    shit_picture: str | None = Field(None, alias="shitPicture")
    ph_state: int | None = Field(None, alias="phState")


class LRSubContent(BaseModel):
    """Subclass of LitterRecord.
    LitterRecord -> List[subContent]
    """

    aes_key: str | None = Field(None, alias="aesKey")
    content: ContentSC | None = None
    device_id: int | None = Field(None, alias="deviceId")
    duration: int | None = None
    enum_event_type: str | None = Field(None, alias="enumEventType")
    event_id: str | None = Field(None, alias="eventId")
    event_type: int | None = Field(None, alias="eventType")
    expire: int | None = None
    mark: int | None = None
    media: int | None = None
    media_api: str | None = Field(None, alias="mediaApi")
    preview: str | None = None
    related_event: str | None = Field(None, alias="relatedEvent")
    shit_aes_key: str | None = Field(None, alias="shitAesKey")
    shit_pictures: list[ShitPictures] | None = Field(None, alias="shitPictures")
    storage_space: int | None = Field(None, alias="storageSpace")
    sub_content: list[Any] | None = Field(None, alias="subContent")
    timestamp: int | None = None
    upload: int | None = None
    user_id: str | None = Field(None, alias="userId")


class LitterRecord(BaseModel):
    """Dataclass for feeder record data.
    Litter records (Main class)
    """

    data_type: ClassVar[str] = DEVICE_RECORDS

    aes_key: str | None = Field(None, alias="aesKey")
    avatar: str | None = None
    content: LRContent | None = None
    device_id: int | None = Field(None, alias="deviceId")
    duration: int | None = None
    enum_event_type: str | None = Field(None, alias="enumEventType")
    event_id: str | None = Field(None, alias="eventId")
    event_type: int | None = Field(None, alias="eventType")
    expire: int | None = None
    is_need_upload_video: int | None = Field(None, alias="isNeedUploadVideo")
    mark: int | None = None
    media: int | None = None
    media_api: str | None = Field(None, alias="mediaApi")
    pet_id: int | None = Field(None, alias="petId")
    pet_name: str | None = Field(None, alias="petName")
    preview: str | None = None
    related_event: str | None = Field(None, alias="relatedEvent")
    shit_pictures: list[ShitPictures] | None = Field(None, alias="shitPictures")
    storage_space: int | None = Field(None, alias="storageSpace")
    sub_content: list[LRSubContent] | None = Field(None, alias="subContent")
    timestamp: int | None = None
    toilet_detection: int | None = Field(None, alias="toiletDetection")
    upload: int | None = None
    user_id: str | None = Field(None, alias="userId")

    @classmethod
    def get_endpoint(cls, device_type: str) -> str:
        """Get the endpoint URL for the given device type."""
        if device_type in [T3, T4, T7]:  # T7 is here
            return PetkitEndpoint.GET_DEVICE_RECORD
        if device_type in [T5, T6]:  # T7 does not support this endpoint
            return PetkitEndpoint.GET_DEVICE_RECORD_RELEASE
        raise ValueError(f"Invalid device type: {device_type}")

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
        request_date: str | None = None,
    ) -> dict:
        """Generate query parameters including request_date."""
        device_type = device.device_type
        if device_type in LITTER_NO_CAMERA:
            request_date = request_date or datetime.now().strftime("%Y%m%d")
            key = "day" if device_type == T3 else "date"
            return {key: int(request_date), "deviceId": device.device_id}
        if device_type in LITTER_WITH_CAMERA:
            return {
                "timestamp": int(datetime.now().timestamp()),
                "deviceId": device.device_id,
                "type": device.type_code,
            }
        raise ValueError(f"Invalid device type: {device_type}")


class StatisticInfo(BaseModel):
    """Dataclass for statistic information.
    Subclass of LitterStats.
    """

    pet_id: int | None = Field(None, alias="petId")
    pet_name: str | None = Field(None, alias="petName")
    pet_times: int | None = Field(None, alias="petTimes")
    pet_total_time: int | None = Field(None, alias="petTotalTime")
    pet_weight: int | None = Field(None, alias="petWeight")
    statistic_date: int | None = Field(None, alias="statisticDate")
    x_time: int | None = Field(None, alias="xTime")


class LitterStats(BaseModel):
    """Dataclass for result data.
    Supported devices = T4 only (T3 ?)
    """

    data_type: ClassVar[str] = DEVICE_STATS

    avg_time: int | None = Field(None, alias="avgTime")
    pet_ids: list[dict] | None = Field(None, alias="petIds")
    statistic_info: list[StatisticInfo] | None = Field(None, alias="statisticInfo")
    statistic_time: str | None = Field(None, alias="statisticTime")
    times: int | None = None
    total_time: int | None = Field(None, alias="totalTime")

    @classmethod
    def get_endpoint(cls, device_type: str) -> str:
        """Get the endpoint URL for the given device type."""
        return PetkitEndpoint.STATISTIC

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> dict:
        """Generate query parameters including request_date."""

        if start_date is None and end_date is None:
            start_date = datetime.now().strftime("%Y%m%d")
            end_date = datetime.now().strftime("%Y%m%d")

        return {
            "endDate": end_date,
            "deviceId": device.device_id,
            "type": device.type_code,
            "startDate": start_date,
        }


class PetGraphContent(BaseModel):
    """Dataclass for content data."""

    auto_clear: int | None = Field(None, alias="autoClear")
    img: str | None = None
    interval: int | None = None
    is_shit: int | None = Field(None, alias="isShit")
    mark: int | None = None
    media: int | None = None
    pet_weight: int | None = Field(None, alias="petWeight")
    shit_weight: int | None = Field(None, alias="shitWeight")
    time_in: int | None = Field(None, alias="timeIn")
    time_out: int | None = Field(None, alias="timeOut")


class PetOutGraph(BaseModel):
    """Dataclass for event data.
    Main Dataclass
    """

    data_type: ClassVar[str] = DEVICE_STATS

    aes_key: str | None = Field(None, alias="aesKey")
    content: PetGraphContent | None = None
    duration: int | None = None
    event_id: str | None = Field(None, alias="eventId")
    expire: int | None = None
    is_need_upload_video: int | None = Field(None, alias="isNeedUploadVideo")
    media_api: str | None = Field(None, alias="mediaApi")
    pet_id: int | None = Field(None, alias="petId")
    pet_name: str | None = Field(None, alias="petName")
    preview: str | None = None
    storage_space: int | None = Field(None, alias="storageSpace")
    time: int | None = None
    toilet_time: int | None = Field(None, alias="toiletTime")

    @classmethod
    def get_endpoint(cls, device_type: str) -> str:
        """Get the endpoint URL for the given device type."""
        return PetkitEndpoint.GET_PET_OUT_GRAPH

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> dict:
        """Generate query parameters including request_date."""

        return {
            "timestamp": int(datetime.now().timestamp()),
            "deviceId": device.device_id,
        }


class Litter(BaseModel):
    """Dataclass for Litter Data.
    Supported devices = T3, T4, T5, T6
    """

    data_type: ClassVar[str] = DEVICE_DATA

    auto_upgrade: int | None = Field(None, alias="autoUpgrade")
    bt_mac: str | None = Field(None, alias="btMac")
    cloud_product: CloudProduct | None = Field(None, alias="cloudProduct")  # For T5/T6
    created_at: str | None = Field(None, alias="createdAt")
    deodorant_tip: int | None = Field(None, alias="deodorantTip")
    device_nfo: Device | None = None
    device_pet_graph_out: list[PetOutGraph] | None = None
    device_records: list[LitterRecord] | None = None
    device_stats: LitterStats | None = None
    firmware: float | str | None = None
    firmware_details: list[FirmwareDetail] = Field(alias="firmwareDetails")
    hardware: int
    id: int
    in_times: int | None = Field(None, alias="inTimes")
    is_pet_out_tips: int | None = Field(None, alias="isPetOutTips")
    k3_device: Purifier | None = Field(None, alias="k3Device")
    last_out_time: int | None = Field(None, alias="lastOutTime")
    locale: str | None = None
    live_feed: LiveFeed | None = None
    mac: str | None = None
    maintenance_time: int | None = Field(None, alias="maintenanceTime")
    medias: list | None = None
    multi_config: bool | None = Field(None, alias="multiConfig")
    name: str | None = None
    p2p_type: int | None = Field(None, alias="p2pType")
    package_ignore_state: int | None = Field(None, alias="packageIgnoreState")
    package_total_count: int | None = Field(None, alias="packageTotalCount")
    package_used_count: int | None = Field(None, alias="packageUsedCount")
    pet_in_tip_limit: int | None = Field(None, alias="petInTipLimit")
    pet_out_records: list[list[int]] | None = Field(None, alias="petOutRecords")
    pet_out_tips: list[Any] | None = Field(None, alias="petOutTips")
    purification_tip: int | None = Field(None, alias="purificationTip")
    ph_error_popup: int | None = Field(None, alias="phErrorPopup")
    secret: str | None = None
    service_status: int | None = Field(None, alias="serviceStatus")
    settings: SettingsLitter | None = None
    share_open: int | None = Field(None, alias="shareOpen")
    signup_at: str | None = Field(None, alias="signupAt")
    sn: str
    state: StateLitter | None = None
    timezone: float | None = None
    total_time: int | None = Field(None, alias="totalTime")
    user: UserDevice | None = None
    with_k3: int | None = Field(None, alias="withK3")

    @classmethod
    def get_endpoint(cls, device_type: str) -> str:
        """Get the endpoint URL for the given device type."""
        return PetkitEndpoint.DEVICE_DETAIL

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
    ) -> dict:
        """Generate query parameters including request_date."""
        return {"id": device.device_id}
