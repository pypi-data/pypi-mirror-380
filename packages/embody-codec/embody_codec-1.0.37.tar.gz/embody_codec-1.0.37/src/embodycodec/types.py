"""Complex types for the EmBody device"""

import enum
import struct
from abc import ABC
from dataclasses import astuple
from dataclasses import dataclass
from typing import TypeVar


class ExecuteCommandType(enum.Enum):
    RESET_DEVICE = 0x01
    REBOOT_DEVICE = 0x02
    PRESS_BUTTON = 0x03
    FORCE_ON_BODY = 0x04
    FORCE_USB_CONNECTION = 0x05
    FORCE_BLE_CONNECTION = 0x06
    FORCE_BATTERY_LEVEL = 0x07
    REINIT_SERVICE = 0x08
    AFE_READ_ALL_REGISTERS = 0xA1
    AFE_WRITE_REGISTER = 0xA2
    AFE_CALIBRATION_COMMAND = 0xA3
    AFE_GAIN_SETTING = 0xA4


class SystemStatusType(enum.Enum):
    NONE = 0x00
    INIT = 0x01
    OK = 0x02
    WARNING = 0x03
    INIT_FAILED = 0x04
    FAILED = 0x05


T = TypeVar("T", bound="ComplexType")


@dataclass
class ComplexType(ABC):
    """Abstract base class for complex types"""

    struct_format = ""
    """pack/unpack format to be overridden by sub-classes"""

    @classmethod
    def default_length(cls) -> int:
        return struct.calcsize(cls.struct_format)

    @classmethod
    def decode(cls: type[T], data: bytes) -> T:
        if len(data) < cls.default_length():
            raise BufferError(
                f"Buffer too short for {cls.__name__} message. Received "
                f"{len(data)} bytes, expected {cls.default_length()} bytes"
            )
        msg = cls(*(struct.unpack(cls.struct_format, data[0 : cls.default_length()])))
        return msg

    def length(self) -> int:
        return struct.calcsize(self.struct_format)

    def encode(self) -> bytes:
        return struct.pack(self.struct_format, *astuple(self))


@dataclass
class BloodPressure(ComplexType):
    struct_format = ">HHHIH"
    sys: int
    dia: int
    bp_map: int
    pat: int
    pulse: int


@dataclass
class Reporting(ComplexType):
    struct_format = ">HB"
    interval: int
    on_change: int


@dataclass
class PulseRaw(ComplexType):
    struct_format = ">ii"
    ecg: int
    ppg: int


@dataclass
class PulseRawAll(ComplexType):
    struct_format = ">iiii"
    ecg: int
    ppg_green: int
    ppg_red: int
    ppg_ir: int


@dataclass
class PulseRawList(ComplexType):
    tick: int
    format: int
    no_of_ecgs: int
    no_of_ppgs: int
    ecgs: list[int]
    ppgs: list[int]
    len = 0

    def length(self) -> int:
        return self.len

    @classmethod
    def decode(cls, data: bytes) -> "PulseRawList":
        if len(data) < 10:
            raise BufferError(f"Buffer too short for message. Received {len(data)} bytes, expected at least 10 bytes")
        (tick,) = struct.unpack("<H", data[0:2])
        (format_and_sizes,) = struct.unpack("<B", data[2:3])
        fmt, no_of_ecgs, no_of_ppgs = PulseRawList.to_format_and_lengths(format_and_sizes)
        ecgs = []
        ppgs = []
        bytes_per_ecg_and_ppg = 1 if fmt == 0 else 2 if fmt == 1 else 3 if fmt == 2 else 4
        pos = 3
        for _ in range(no_of_ecgs):
            ecg = int.from_bytes(data[pos : pos + bytes_per_ecg_and_ppg], byteorder="little", signed=True)
            ecgs.append(ecg)
            pos += bytes_per_ecg_and_ppg
        for _ in range(no_of_ppgs):
            ppg = int.from_bytes(data[pos : pos + bytes_per_ecg_and_ppg], byteorder="little", signed=True)
            ppgs.append(ppg)
            pos += bytes_per_ecg_and_ppg
        msg = PulseRawList(
            tick=tick,
            format=fmt,
            no_of_ecgs=no_of_ecgs,
            no_of_ppgs=no_of_ppgs,
            ecgs=ecgs,
            ppgs=ppgs,
        )
        msg.len = 1 + (no_of_ecgs * bytes_per_ecg_and_ppg) + (no_of_ppgs * bytes_per_ecg_and_ppg)
        return msg

    def encode(self) -> bytes:
        format_and_length = PulseRawList.from_format_and_lengths(self.format, self.no_of_ecgs, self.no_of_ppgs)
        bytes_per_ecg_and_ppg = 1 if self.format == 0 else 2 if self.format == 1 else 3 if self.format == 2 else 4
        payload = struct.pack("<H", self.tick)
        payload += struct.pack("<B", format_and_length)
        for element in range(self.no_of_ecgs):
            payload += int.to_bytes(
                self.ecgs[element],
                length=bytes_per_ecg_and_ppg,
                byteorder="little",
                signed=True,
            )
        for element in range(self.no_of_ppgs):
            payload += int.to_bytes(
                self.ppgs[element],
                length=bytes_per_ecg_and_ppg,
                byteorder="little",
                signed=True,
            )
        return payload

    @staticmethod
    def to_format_and_lengths(format_and_sizes: int) -> tuple:
        fmt = format_and_sizes & 0x3
        no_of_ecgs = (format_and_sizes & 0x0F) >> 2
        no_of_ppgs = (format_and_sizes & 0xF0) >> 4
        return fmt, no_of_ecgs, no_of_ppgs

    @staticmethod
    def from_format_and_lengths(fmt: int, no_of_ecgs: int, no_of_ppgs: int) -> int:
        format_and_sizes = no_of_ppgs & 0xF
        format_and_sizes <<= 2
        format_and_sizes += no_of_ecgs & 0x3
        format_and_sizes <<= 2
        format_and_sizes += fmt & 0x3
        return format_and_sizes & 0xFF


@dataclass
class SystemStatus(ComplexType):
    status: list[SystemStatusType]
    worst: list[SystemStatusType]

    @classmethod
    def decode(cls, data: bytes) -> "SystemStatus":
        if len(data) < 1:
            raise BufferError(f"Buffer too short for message. Received {len(data)} bytes, expected at least 1 bytes")
        (format_and_sizes,) = struct.unpack("<B", data[2:3])
        status = []
        worst = []
        for n in range(len(data)):
            status.append(SystemStatusType(data[n] & 0x0F))
            worst.append(SystemStatusType(data[n] >> 4 & 0x0F))
        return SystemStatus(
            status=status,
            worst=worst,
        )

    def encode(self) -> bytes:
        payload = b""
        for n in range(len(self.status)):
            payload += bytes([self.status[n].value & 0x0F | ((self.worst[n].value << 4) & 0xF0)])
        return payload


@dataclass
class Imu(ComplexType):
    struct_format = ">B"
    orientation_and_activity: int


@dataclass
class ImuRaw(ComplexType):
    struct_format = ">hhhhhh"
    acc_x: int = 0
    acc_y: int = 0
    acc_z: int = 0
    gyr_x: int = 0
    gyr_y: int = 0
    gyr_z: int = 0


@dataclass
class AccRaw(ComplexType):
    struct_format = ">hhh"
    acc_x: int = 0
    acc_y: int = 0
    acc_z: int = 0


@dataclass
class GyroRaw(ComplexType):
    struct_format = ">hhh"
    gyr_x: int = 0
    gyr_y: int = 0
    gyr_z: int = 0


@dataclass
class FlashInfo(ComplexType):
    struct_format = "<BHH"
    files: int = 0
    used: int = 0
    free: int = 0


@dataclass
class Recording(ComplexType):
    struct_format = ">BBBBBB"
    day_start: int
    day_end: int
    day_interval: int
    night_interval: int
    recording_start: int
    recording_stop: int


@dataclass
class Diagnostics(ComplexType):
    struct_format = ">HhHHIIII"
    rep_soc: int
    avg_current: int
    rep_cap: int
    full_cap: int
    tte: int
    ttf: int
    voltage: int
    avg_voltage: int


@dataclass
class BatteryDiagnostics(ComplexType):
    struct_format = "<IIHHhhHHHH"
    ttf: int  # s Time To Full
    tte: int  # s Time To Empty
    voltage: int  # mV *10 (0-6553.5 mV) Battery Voltage
    avg_voltage: int  # mV *10 (0-6553.5 mV) Average Battery Voltage
    current: int  # mA *100 (-327.68 - +327.67 mA) Battery Current
    avg_current: int  # mA *100 (-327.68 - +327.67 mA) Average Battery Current
    full_cap: int
    # mAh *100 (0-655.35 mAh) Total battery capacity calculated after each cycle
    rep_cap: int  # mAh *100 (0-655.35 mAh) Remaining capacity
    repsoc: int  # % *100  (0-100.00 %) Reported State Of Charge (Combined and final result)
    vfsoc: int  # % *100  (0-100.00 %) Voltage based fuelgauge State Of Charge

    def to_str(self):
        return (
            f"ttf: {self.ttf}, tte: {self.tte}, voltage: {self.voltage} ({self.voltage / 10}mV), "
            f"avg_voltage: {self.avg_voltage} ({self.avg_voltage / 10}mV), current: {self.current} "
            f"({self.current / 100}mA), avg_current: {self.avg_current} ({self.avg_current / 100}mA), "
            f"full_cap: {self.full_cap} ({self.full_cap / 100}mAh), rep_cap: {self.rep_cap} "
            f"({self.rep_cap / 100}mAh), repsoc: {self.repsoc} ({self.repsoc / 100}%), "
            f"vfsoc: {self.vfsoc} ({self.vfsoc / 100}%)"
        )


@dataclass
class AfeSettings(ComplexType):
    struct_format = ">BBBBIIif"
    rf_gain: int
    cf_value: int
    ecg_gain: int
    ioffdac_range: int
    led1: int
    led4: int
    off_dac: int
    relative_gain: float


@dataclass
class AfeSettingsAll(ComplexType):
    struct_format = ">BBBBIIIIiiif"
    rf_gain: int | None
    cf_value: int | None
    ecg_gain: int | None
    ioffdac_range: int | None
    led1: int | None
    led2: int | None
    led3: int | None
    led4: int | None
    off_dac1: int | None
    off_dac2: int | None
    off_dac3: int | None
    relative_gain: float | None


F = TypeVar("F", bound="File")


@dataclass
class File(ComplexType):
    struct_format = ">26s"
    file_name: str | bytes

    @classmethod
    def decode(cls: type[F], data: bytes) -> F:
        msg = cls(*(struct.unpack(cls.struct_format, data[0 : cls.default_length()])))
        if msg.file_name is not None and isinstance(msg.file_name, bytes):
            msg.file_name = msg.file_name.split(b"\x00", maxsplit=1)[0].decode("utf-8")
        return msg

    def encode(self) -> bytes:
        return struct.pack(self.struct_format, str(self.file_name).encode("utf-8"))


@dataclass
class FileWithLength(File):
    struct_format = File.struct_format + "I"
    file_size: int

    def encode(self) -> bytes:
        return struct.pack(self.struct_format, str(self.file_name).encode("utf-8"), self.file_size)
