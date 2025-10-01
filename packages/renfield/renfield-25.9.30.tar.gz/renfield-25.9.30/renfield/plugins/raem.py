"""Ernst Krenkel Memorial"""

# pylint: disable=invalid-name, c-extension-no-member, unused-import


# RAEM Contest
#  	Status:	Active
#  	Geographic Focus:	Worldwide
#  	Participation:	Worldwide
#  	Mode:	    CW
#  	Bands:	    80, 40, 20, 15, 10m
#  	Classes:	Single Op All Band (Low/High)
#               Single Op Single Band
#               Multi-Single
#  	Max power:	HP: >100 watts
#               LP: 100 watts
#  	Exchange:	Serial No. + latitude (degs only) + hemisphere + longitude (degs only) + hemisphere (see rules)
#               N=North, S=South, W=West, O=East (e.g. 57N 85O)
#  	Work stations:	Once per band
#  	QSO Points:	50 points + 1 point for every degree difference in geo location, both latitude and longitude
#               QSO with Polar station: 100 points additional
#               QSO with RAEM Memorial Station: 300 points additional
#  	Multipliers:	Polar stations multiply total QSO points by 1.1
#  	Score Calculation:	Total score = total QSO points
#  	E-mail logs to:	raem[at]srr[dot]ru
#  	Upload log at:	http://ua9qcq.com/
#  	Mail logs to:	(none)
#  	Find rules at:	https://raem.srr.ru/rules/
#  	Cabrillo name:	RAEM

# Label and field names
# callsign_label, callsign
# snt_label, sent
# rcv_label, receive
# other_label, other_1
# exch_label, other_2

# command button names
# esc_stop
# log_it
# mark
# spot_it
# wipe


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

name = "RAEM"
cabrillo_name = "RAEM"
mode = "CW"  # CW SSB BOTH RTTY

# 1 once per contest, 2 work each band, 3 each band/mode, 4 no dupe checking
dupe_type = 2


def latlondif(self, exchange1: str):
    """"""
    ourexchange = self.contest_settings.get("SentExchange", None)
    if ourexchange is None:
        return 0, False
    ourexchange = ourexchange.upper()
    if len(exchange1) < 4:
        return 0, False
    exchange1 = exchange1.upper()

    latindex = None
    ourlat = None
    ourlon = None
    if "N" in ourexchange:
        latindex = ourexchange.index("N")
        lat = ourexchange[:latindex]
        if lat.isnumeric():
            ourlat = int(lat)
    if "S" in ourexchange:
        latindex = ourexchange.index("S")
        lat = ourexchange[:latindex]
        if lat.isnumeric():
            ourlat = int(lat)
    if "W" in ourexchange:
        lon = ourexchange[latindex + 1 : ourexchange.index("W")]
        if lon.isnumeric():
            ourlon = int(lon)
    if "O" in ourexchange:
        lon = ourexchange[latindex + 1 : ourexchange.index("O")]
        if lon.isnumeric():
            ourlon = int(lon)
    if ourlat is None or ourlon is None:
        return 0, False

    hislat = None
    hislon = None
    if "N" in exchange1:
        latindex = exchange1.index("N")
        lat = exchange1[:latindex]
        if lat.isnumeric():
            hislat = int(lat)
    if "S" in exchange1:
        latindex = exchange1.index("S")
        lat = exchange1[:latindex]
        if lat.isnumeric():
            hislat = int(lat)
    if "W" in exchange1:
        lon = exchange1[latindex + 1 : exchange1.index("W")]
        if lon.isnumeric():
            hislon = int(lon)
    if "O" in exchange1:
        lon = exchange1[latindex + 1 : exchange1.index("O")]
        if lon.isnumeric():
            hislon = int(lon)
    if hislat is None or hislon is None:
        return 0, False

    return abs(ourlat - hislat) + abs(ourlon - hislon), hislat >= 66


def points(self):
    """Calc point"""
    # 50 points + 1 point for every degree difference in geo location, both latitude and longitude
    # QSO with Polar station: 100 points additional
    # QSO with RAEM Memorial Station: 300 points additional

    if self.contact_is_dupe > 0:
        return 0
    points = 50
    morepoints, ispolar = latlondif(self, self.other_2.text())
    points += morepoints
    if ispolar is not False:
        points += 100
    if self.callsign.text() == "RAEM":
        points += 300

    return points


def show_mults(self):
    """Return display string for mults"""
    ourexchange = self.contest_settings.get("SentExchange", None)
    if ourexchange is None:
        return 0, False
    ourexchange = ourexchange.upper()

    latindex = None
    ourlat = None
    if "N" in ourexchange:
        latindex = ourexchange.index("N")
        lat = ourexchange[:latindex]
        if lat.isnumeric():
            ourlat = int(lat)
    if "S" in ourexchange:
        latindex = ourexchange.index("S")
        lat = ourexchange[:latindex]
        if lat.isnumeric():
            ourlat = int(lat)

    if ourlat is not None:
        if ourlat >= 66:
            return 1.1

    return 1


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
    gen_adif(self, cabrillo_name, "RAEM")


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
                    f"{str(contact.get('SentNr', '')).ljust(6)} "
                    f"{self.contest_settings.get('SentExchange', '').ljust(14).upper()}"
                    f"{contact.get('Call', '').ljust(13)} "
                    f"{str(contact.get('NR', '')).ljust(6)}"
                    f"{str(contact.get('Exchange1', '')).ljust(14)} ",
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
    # all_contacts = self.database.fetch_all_contacts_asc()
    # for contact in all_contacts:
    #     time_stamp = contact.get("TS", "")
    #     wpx = contact.get("WPXPrefix", "")
    #     result = self.database.fetch_wpx_exists_before_me(wpx, time_stamp)
    #     wpx_count = result.get("wpx_count", 1)
    #     if wpx_count == 0:
    #         contact["IsMultiplier1"] = 1
    #     else:
    #         contact["IsMultiplier1"] = 0
    #     self.database.change_contact(contact)


def get_mults(self):
    """Get mults for RTC XML"""
    mults = {}
    return mults


def just_points(self):
    """Get points for RTC XML"""
    return get_points(self)
