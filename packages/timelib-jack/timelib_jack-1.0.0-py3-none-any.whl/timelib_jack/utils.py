from __future__ import annotations
import datetime, hashlib, zoneinfo, logging
from typing import Optional
import re

logger = logging.getLogger("timelib-jack.utils")

class TimeUtils:
    """
    فئة مساعدة للتعامل مع الوقت والمناطق الزمنية
    - حساب الوقت القادم لمهام cron
    - حماية من تعديل الوقت
    - تحويل المناطق الزمنية
    """
    @staticmethod
    def compute_time_hash(tz: Optional[str]=None) -> str:
        """احسب hash للوقت الحالي لحماية البرنامج من تعديل ساعة النظام"""
        now = datetime.datetime.now(tz=zoneinfo.ZoneInfo(tz) if tz else None)
        return hashlib.sha256(str(now.timestamp()).encode()).hexdigest()

    @staticmethod
    def check_time_integrity(old_hash: str, tz: Optional[str]=None):
        """تحقق من سلامة الوقت، إذا تم التلاعب يخرج البرنامج"""
        new_hash = TimeUtils.compute_time_hash(tz)
        if new_hash != old_hash:
            logger.warning("Time tampering detected! Exiting...")
            import os
            os._exit(1)

    @staticmethod
    def convert_timezone(dt: datetime.datetime, tz_from: str, tz_to: str) -> datetime.datetime:
        """تحويل وقت من منطقة زمنية لأخرى"""
        from_zone = zoneinfo.ZoneInfo(tz_from)
        to_zone = zoneinfo.ZoneInfo(tz_to)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=from_zone)
        return dt.astimezone(to_zone)

    @staticmethod
    def next_cron(cron_str: str) -> datetime.datetime:
        """
        احسب التوقيت القادم لمهمة cron
        صيغة بسيطة: "* * * * *" (minute hour day month weekday)
        يدعم فقط * أو أرقام
        """
        now = datetime.datetime.now()
        fields = cron_str.strip().split()
        if len(fields) != 5:
            raise ValueError("Invalid cron string, expected 5 fields")
        minute, hour, day, month, weekday = fields
        next_dt = now.replace(second=0, microsecond=0)
        if minute != "*": next_dt = next_dt.replace(minute=int(minute))
        if hour != "*": next_dt = next_dt.replace(hour=int(hour))
        if next_dt <= now:
            next_dt += datetime.timedelta(minutes=1)
        return next_dt