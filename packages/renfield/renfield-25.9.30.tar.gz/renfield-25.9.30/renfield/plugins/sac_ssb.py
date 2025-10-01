"""SAC SSB plugin"""

# pylint: disable=invalid-name, c-extension-no-member, unused-import


import datetime
from pathlib import Path

# Import path may change depending on if it's dev or production.
try:
    from lib.ham_utility import get_logged_band
    from lib.plugin_common import gen_adif, get_points, online_score_xml
    from lib.version import __version__
except (ImportError, ModuleNotFoundError):
    from renfield.lib.ham_utility import get_logged_band
    from renfield.lib.plugin_common import gen_adif, get_points, online_score_xml
    from renfield.lib.version import __version__

name = "SAC SSB"
cabrillo_name = "SAC-SSB"
mode = "SSB"  # CW SSB BOTH RTTY

# 1 once per contest, 2 work each band, 3 each band/mode, 4 no dupe checking
dupe_type = 2

scandinavian_prefixes = [
    "JW",
    "JX",
    "LA",
    "LB",
    "LC",
    "LG",
    "LI",
    "LJ",
    "LN",
    "OF",
    "OG",
    "OH",
    "OI",
    "OFØ",
    "OGØ",
    "OHØ",
    "OJØ",
    "OX",
    "XP",
    "OW",
    "OY",
    "5P",
    "5Q",
    "OU",
    "OV",
    "OZ",
    "7S",
    "8S",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SF",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "TF",
]


def points(self):
    """Calc point"""
    # 7.1 For Scandinavian stations:
    #   EUROPEAN stations, outside Scandinavia, are worth two (2) points for every complete QSO.
    #   NON-EUROPEAN stations are worth three (3) points for every complete QSO.
    # 7.2 For non-Scandinavian stations:
    #   EUROPEAN stations receive one (1) point for every complete Scandinavian QSO.
    #   NON-EUROPEAN stations receive one (1) point for every complete Scandinavian QSO on
    #       14, 21, and 28 MHz and three (3) points for every complete QSO on 3.5 and 7 MHz.

    if self.contact_is_dupe > 0:
        return 0

    myprimary_pfx = ""
    mycontinent = ""
    hisprimary_pfx = ""
    hiscontinent = ""

    result = self.cty_lookup(self.station.get("Call", ""))
    if result:
        for item in result.items():
            myprimary_pfx = item[1].get("primary_pfx", "")
            mycontinent = item[1].get("continent", "")

    result = self.cty_lookup(self.contact.get("Call", ""))
    if result:
        for item in result.items():
            hisprimary_pfx = item[1].get("primary_pfx", "")
            hiscontinent = item[1].get("continent", "")

    if (
        myprimary_pfx in scandinavian_prefixes
        and hisprimary_pfx not in scandinavian_prefixes
    ):
        if hiscontinent == "EU":
            return 2
        return 3
    if (
        myprimary_pfx not in scandinavian_prefixes
        and hisprimary_pfx in scandinavian_prefixes
    ):
        if mycontinent == "EU":
            return 1
        if self.contact.get("Band", 0) in ["3.5", "7"]:
            return 3
        if self.contact.get("Band", 0) in ["14", "21", "28"]:
            return 1

    # Something wrong
    return 0


def show_mults(self):
    """Return display string for mults"""
    myprimary_pfx = ""
    mult_count = 0

    result = self.cty_lookup(self.station.get("Call", ""))
    if result:
        for item in result.items():
            myprimary_pfx = item[1].get("primary_pfx", "")

    if myprimary_pfx in scandinavian_prefixes:
        result = self.database.fetch_country_band_count()
        mult_count = result.get("cb_count", 0)
    else:
        query = f"SELECT count(DISTINCT(CountryPrefix || ':' || substr(WPXPrefix,3,1) || ':' || Band)) as mults from DXLOG where ContestNR = {self.pref.get('contest', '1')} AND CountryPrefix IN ('JW', 'JX', 'LA', 'LB', 'LC', 'LG', 'LI', 'LJ' , 'LN', 'OF', 'OG', 'OH', 'OI', 'OFØ', 'OGØ', 'OHØ', 'OJØ', 'OX', 'XP', 'OW', 'OY', '5P', '5Q', 'OU', 'OV', 'OZ', '7S', '8S', 'SA', 'SB', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'TF');"
        result = self.database.exec_sql(query)
        mult_count = result.get("mults", 0)
    return mult_count


def show_qso(self):
    """Return qso count"""
    result = self.database.fetch_qso_count()
    if result:
        return int(result.get("qsos", 0))
    return 0


def calc_score(self):
    """Return calculated score"""
    result = self.database.fetch_points()
    if result is not None:
        score = result.get("Points", "0")
        if score is None:
            score = "0"
        contest_points = int(score)
        mults = show_mults(self)
        return contest_points * mults
    return 0


def adif(self):
    """Call the generate ADIF function"""
    gen_adif(self, cabrillo_name, "SAC-SSB")


def output_cabrillo_line(line_to_output, ending, file_descriptor, file_encoding):
    """"""
    print(
        line_to_output.encode(file_encoding, errors="ignore").decode(),
        end=ending,
        file=file_descriptor,
    )


def cabrillo(self, file_encoding):
    """Generates Cabrillo file. Maybe."""
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = (
        str(Path.home())
        + "/"
        + f"{self.station.get('Call', '').upper()}_{cabrillo_name}_{date_time}.log"
    )
    self.log_info(f"Saving log to:{filename}")
    log = self.database.fetch_all_contacts_asc()
    try:
        with open(filename, "w", encoding=file_encoding, newline="") as file_descriptor:
            output_cabrillo_line(
                "START-OF-LOG: 3.0",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CREATED-BY: Not1MM v{__version__}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CONTEST: {cabrillo_name}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            if self.station.get("Club", ""):
                output_cabrillo_line(
                    f"CLUB: {self.station.get('Club', '').upper()}",
                    "\r\n",
                    file_descriptor,
                    file_encoding,
                )
            output_cabrillo_line(
                f"CALLSIGN: {self.station.get('Call','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"LOCATION: {self.station.get('ARRLSection', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CATEGORY-OPERATOR: {self.contest_settings.get('OperatorCategory','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CATEGORY-ASSISTED: {self.contest_settings.get('AssistedCategory','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CATEGORY-BAND: {self.contest_settings.get('BandCategory','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            mode = self.contest_settings.get("ModeCategory", "")
            if mode in ["SSB+CW", "SSB+CW+DIGITAL"]:
                mode = "MIXED"
            output_cabrillo_line(
                f"CATEGORY-MODE: {mode}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CATEGORY-TRANSMITTER: {self.contest_settings.get('TransmitterCategory','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            if self.contest_settings.get("OverlayCategory", "") != "N/A":
                output_cabrillo_line(
                    f"CATEGORY-OVERLAY: {self.contest_settings.get('OverlayCategory','')}",
                    "\r\n",
                    file_descriptor,
                    file_encoding,
                )
            output_cabrillo_line(
                f"GRID-LOCATOR: {self.station.get('GridSquare','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"CATEGORY-POWER: {self.contest_settings.get('PowerCategory','')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )

            output_cabrillo_line(
                f"CLAIMED-SCORE: {calc_score(self)}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            ops = f"@{self.station.get('Call','')}"
            list_of_ops = self.database.get_ops()
            for op in list_of_ops:
                ops += f", {op.get('Operator', '')}"
            output_cabrillo_line(
                f"OPERATORS: {ops}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"NAME: {self.station.get('Name', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"ADDRESS: {self.station.get('Street1', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"ADDRESS-CITY: {self.station.get('City', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"ADDRESS-STATE-PROVINCE: {self.station.get('State', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"ADDRESS-POSTALCODE: {self.station.get('Zip', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"ADDRESS-COUNTRY: {self.station.get('Country', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            output_cabrillo_line(
                f"EMAIL: {self.station.get('Email', '')}",
                "\r\n",
                file_descriptor,
                file_encoding,
            )
            for contact in log:
                the_date_and_time = contact.get("TS", "")
                themode = contact.get("Mode", "")
                if themode in ("LSB", "USB", "FM"):
                    themode = "PH"
                frequency = str(int(contact.get("Freq", "0"))).rjust(5)

                loggeddate = the_date_and_time[:10]
                loggedtime = the_date_and_time[11:13] + the_date_and_time[14:16]
                output_cabrillo_line(
                    f"QSO: {frequency} {themode} {loggeddate} {loggedtime} "
                    f"{contact.get('StationPrefix', '').ljust(13)} "
                    f"{str(contact.get('SNT', '')).ljust(3)} "
                    f"{str(contact.get('SentNr', '')).ljust(6)} "
                    f"{contact.get('Call', '').ljust(13)} "
                    f"{str(contact.get('RCV', '')).ljust(3)} "
                    f"{str(contact.get('NR', '')).ljust(6)}",
                    "\r\n",
                    file_descriptor,
                    file_encoding,
                )
            output_cabrillo_line("END-OF-LOG:", "\r\n", file_descriptor, file_encoding)
    except IOError as ioerror:
        self.log_info(f"Error saving the log: {ioerror}")
        return


def recalculate_mults(self):
    """Recalculates multipliers after change in logged qso."""


def get_mults(self):
    """Get mults for RTC XML"""
    mults = {}
    mults["wpxprefix"] = show_mults(self)
    return mults


def just_points(self):
    """Get points for RTC XML"""
    return get_points(self)
