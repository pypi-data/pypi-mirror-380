import os
import sys
import traceback
from wowool.package.lib.wowool_plugin import match_info
import warnings
import re
from functools import lru_cache


ISO_DATE_PATTERN = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?:T(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)?$"
)


@lru_cache(maxsize=128)
def dateparser_parse_cached(date_str: str, date_order=None, time_zone=None, relative_base=None):
    from dateparser import parse

    settings = {}
    if date_order:
        settings["DATE_ORDER"] = date_order
    if time_zone:
        settings["TIME_ZONE"] = time_zone
    if relative_base:
        settings["RELATIVE_BASE"] = relative_base
    return parse(date_str, settings=settings)


def dateparser_parse(
    *args,
    date_order=None,
    time_zone=None,
    relative_base=None,
):

    if ISO_DATE_PATTERN.match(args[0]):
        # if the date is in ISO format, we can use the built-in datetime parsing
        from datetime import datetime

        try:
            return datetime.fromisoformat(args[0])
        except ValueError:
            return None
    try:

        # warnings.simplefilter(action="ignore", category=Warning)
        retval = dateparser_parse_cached(args[0], date_order=date_order, time_zone=time_zone, relative_base=relative_base)
        # if retval is None:
        #     print(f"result: {args[0]}, {retval}")
        return retval
    finally:
        pass
        # warnings.simplefilter(action="default", category=Warning)


def _set_document_date_literal(ud, literal):
    try:
        update_initial_date = True
        if "__initial_date" in ud and ud["__initial_date"] is True:
            update_initial_date = False

        date_order = None
        if "date_order" in ud:
            date_order = ud["date_order"]
        elif "WOWOOL_DOCUMENT_DATE_ORDER" in os.environ:
            date_order = os.environ["WOWOOL_DOCUMENT_DATE_ORDER"]
        else:
            date_order = "YMD"

        document_date = dateparser_parse(literal, date_order=date_order)
        if update_initial_date:
            ud["document_date"] = document_date.isoformat()
        if "initial_date" in ud and ud["initial_date"] == "True":
            ud["__initial_date"] = True

    except Exception:
        if "WOWOOL_LOG_LEVEL" in os.environ and os.environ["WOWOOL_LOG_LEVEL"] == "trace":
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)


def make_date_attribute(date) -> str:
    return date.isoformat()[:10]


def set_document_date(ud):
    try:
        match = match_info()
        capture = match.capture()

        update_initial_date = True
        if "__initial_date" in ud and ud["__initial_date"] is True:
            update_initial_date = False

        date_order = None
        time_zone = None
        if capture.timezone:
            time_zone = capture.timezone
        if "date_order" in ud:
            date_order = ud["date_order"]
        elif capture.date_order:
            date_order = capture.date_order
        elif "WOWOOL_DOCUMENT_DATE_ORDER" in os.environ:
            date_order = os.environ["WOWOOL_DOCUMENT_DATE_ORDER"]

        document_date = dateparser_parse(capture.literal(), date_order=date_order, time_zone=time_zone)
        if update_initial_date:
            ud["document_date"] = document_date.isoformat()
        if "initial_date" in ud and ud["initial_date"] == "True":
            ud["__initial_date"] = True
        _date = capture.Date
        if not _date:
            _date = capture.add_concept("Date")
        if not _date:
            if "WOWOOL_LOG_LEVEL" in os.environ and os.environ["WOWOOL_LOG_LEVEL"] == "trace":
                # DEBUG
                # ---------------------------------------------------
                print("EOT: Could not set initial date.")
            return False
        # let transform it and calculate the absolute date.
        str_iso_date = document_date.isoformat()
        if not _date.has("abs_date"):
            _date.add_attribute("abs_date", make_date_attribute(document_date))
            # abs_date.add_attribute("iso", document_date.isoformat())

        capture.remove()
        return str_iso_date

    except Exception:
        if "WOWOOL_LOG_LEVEL" in os.environ and os.environ["WOWOOL_LOG_LEVEL"] == "trace":
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)


def round_date(date_str):
    return date_str.split(".")[0]


def get_document_date(ud: dict):
    if document_date := ud.get("document_date"):
        return document_date
    elif document_date := ud.get("initial_date"):
        return document_date


def resolve_date(ud):
    try:
        match = match_info()
        capture = match.capture()
        date_str = capture.literal()
        date_str = capture.canonical()
        document_date_str = document_date = None

        time_phrase = capture.find_one("TimePhrase")
        if time_phrase and time_phrase.has("_resolve") and time_phrase.attribute("_resolve") == "false":
            return

        date_concept = capture.find_one("Date")
        if date_concept:
            date_str = date_concept.literal()
            values = date_concept.find("/Number|Month/")
            if len(values) == 3 and values[1].uri == "Month":
                date_str = f"{round_date(values[2].canonical())}-{round_date(values[1].canonical())}-{round_date(values[0].canonical())}"

        if document_date_str := get_document_date(ud):
            _set_document_date_literal(ud, document_date_str)

        if "date_order" in ud:
            date_order = ud["date_order"]
        elif capture.date_order:
            date_order = capture.date_order
        elif "WOWOOL_DOCUMENT_DATE_ORDER" in os.environ:
            date_order = os.environ["WOWOOL_DOCUMENT_DATE_ORDER"]
        else:
            if date_str.find("-") == 4:
                date_order = "YMD"
            else:
                date_order = "DMY"

        if document_date_str:
            document_date = dateparser_parse(document_date_str)
        relative_base = document_date if document_date else None
        date = dateparser_parse(date_str, relative_base=relative_base, date_order=date_order)
        if not date:
            date = dateparser_parse(date_str, date_order="YMD")
            if not date:
                return False

        if not date:
            return

        abs_date = capture.Date
        # if we already have a Date in the collection we will use this one
        if not abs_date:
            # as we did not have one let add a new Concept
            abs_date = capture.add_concept("Date")
        if not abs_date:
            # that failed for some strange thing, then let's remove the capture
            # group the triggered it.
            # print("debug:do not have a date")
            capture.remove()
            return False

        if abs_date.has("abs_date"):
            # resolve_date_ = abs_date.attribute("abs_date")
            # ud["last_seen_date"] = resolve_date_
            return

        # let transform it and calculate the absolute date.
        abs_date.add_attribute("abs_date", make_date_attribute(date))
        capture.remove()
        # ud["last_seen_date"] = resolve_date
    except KeyboardInterrupt as kbex:
        raise kbex
    except Exception:
        traceback.print_exc(file=sys.stdout)
        if "WOWOOL_LOG_LEVEL" in os.environ and os.environ["WOWOOL_LOG_LEVEL"] == "trace":
            # DEBUG
            # ---------------------------------------------------
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)
