#!/usr/bin/env python

import io
import json
import re

HEIGHT_FACTOR = 20
MILLIPOINTS = 1000
PTS_PER_INCH = 72

PS_FONTS = [
    "AvantGarde-Book",
    "AvantGarde-BookOblique",
    "AvantGarde-Demi",
    "AvantGarde-DemiOblique",
    "Bookman",
    "Bookman-Light",
    "Bookman-LightItalic",
    "Bookman-Demi",
    "Bookman-DemiItalic",
    "Courier",
    "Courier-Oblique",
    "Courier-Bold",
    "Courier-BoldOblique",
    "Helvetica",
    "Helvetica-Oblique",
    "Helvetica-Bold",
    "Helvetica-BoldOblique",
    "Helvetica-Narrow",
    "Helvetica-Narrow-Oblique",
    "Helvetica-Narrow-Bold",
    "Helvetica-Narrow-BoldOblique",
    "NewCenturySchlbk-Roman",
    "NewCenturySchlbk-Italic",
    "NewCenturySchlbk-Bold",
    "NewCenturySchlbk-BoldItalic",
    "Palatino-Roman",
    "Palatino-Italic",
    "Palatino-Bold",
    "Palatino-BoldItalic",
    "Symbol",
    "Times-Roman",
    "Times-Italic",
    "Times-Bold",
    "Times-BoldItalic",
    "ZapfChancery-MediumItalic ",
    "ZapfDingbats",
]


def get_character_widths(fontfile):
    widths = {}
    font_name = None
    cap_height = None
    x_height = None
    font_dict = {}
    with open(fontfile, "rb") as fobj:
        byte_string = fobj.read()
        decoded_string = byte_string.decode("ascii", errors="ignore")
        in_metrics = False
        for tline in decoded_string.split("\n"):
            line = tline.encode("ascii", "ignore").decode("ascii")
            if "FontName" in line:
                font_name = re.split(r"\s+", line)[1]
                continue
            if "CapHeight" in line:
                cap_height = float(re.split(r"\s+", line)[1])
                continue
            if "XHeight" in line:
                x_height = float(re.split(r"\s+", line)[1])
                continue
            if "StartCharMetrics" in line:
                in_metrics = True
                continue
            if "EndCharMetrics" in line:
                break

            if in_metrics:
                parts = line.split(";")
                chr_idx = int(re.split(r"\s+", parts[0].strip())[1])

                if chr_idx > 126 or chr_idx < 32:
                    break

                ascii_chr = chr(chr_idx)
                width = float(re.split(r"\s+", parts[1].strip())[1])
                widths[ascii_chr] = width

    font_dict["cap_height"] = cap_height
    font_dict["x_height"] = x_height
    font_dict["widths"] = widths
    return (font_name, font_dict)


class FontCalculator:
    def __init__(self, fontfile_or_fileobj, limit_to_postscript=False):
        if not hasattr(fontfile_or_fileobj, "read"):
            with open(fontfile_or_fileobj, "rt") as fobj:
                self.font_data = json.load(fobj)
        else:
            self.font_data = json.load(fontfile_or_fileobj)
        self.limit_names(PS_FONTS)

    def save_database(self, filename):
        with open(filename, "wt") as fobj:
            json.dump(self.font_data, fobj)

    def limit_names(self, names):
        new_fonts = {}
        # make a new "database" with only the supplied font names
        for font_name, font_info in self.font_data.items():
            if font_name in names:
                new_fonts[font_name] = font_info
        self.font_data = new_fonts.copy()

    def get_string_size_points(self, instring, font, fontsize):
        if font not in self.font_data:
            raise KeyError(f"Font {font} not in database")
        font_dict = self.font_data[font]
        char_width = 0
        for chr in instring:
            char_width += font_dict["widths"][chr]
        width = (char_width * fontsize) / MILLIPOINTS
        return (width, font_dict["cap_height"] * HEIGHT_FACTOR / MILLIPOINTS)

    def get_string_size_inches(self, instring, font, fontsize):
        width, height = self.get_string_size_points(instring, font, fontsize)
        return (width / PTS_PER_INCH, height / PTS_PER_INCH)

    def get_font_names(self):
        return list(self.font_data.keys())

    def get_matching_fonts(self, pattern):
        font_names = self.get_font_names()
        matches = []
        for fname in font_names:
            if re.search(pattern, fname, flags=re.IGNORECASE) is not None:
                matches.append(fname)

        return matches

    @classmethod
    def from_directory(cls, font_folder):
        fonts = {}
        afm_files = font_folder.glob("**/*.afm")
        for afm_file in afm_files:
            font_name, font_dict = get_character_widths(afm_file)
            fonts[font_name] = font_dict
        fobj = io.StringIO(json.dumps(fonts))
        fobj.seek(0)
        return cls(fobj)
