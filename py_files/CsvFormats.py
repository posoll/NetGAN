"""
This file contains a list of formats that the data file could be in.
"""
from py_files.DataType1 import DataType1
import os


def format0(filepath, experiment = None, prt = "1"):
    """
    Returns a list of `DataType1` if file is has format0 layout.

    :param filepath: string of complete filepath to .csv file
    :returns: list of `DataType` objects
    """
    ret = []
    headers = []
    order = 0   # in this format, images appear in order
    # get particpant id number
    person_id = int(filepath.split(os.path.sep)[-1].split("_")[0])
    with open(filepath, "r", encoding="utf-8-sig") as f:
        for line in f:
            if len(headers) == 0:
                # if headers list is empty, we need to discover headers and set indices for each relevant column
                headers = line.split(",")
                response_raw = headers.index("prt_{}_vas.response".format(prt))
                rt_raw = headers.index("prt_{}_vas.rt".format(prt))
                if "prt_image_intens_resp.keys" in headers:     # this part differs between "R1 P1" and "R1 P1 (1)"
                    keys_raw = headers.index("prt_image_intens_resp.keys")
                    keys_rt_raw = headers.index("prt_image_intens_resp.rt")
                else:
                    keys_raw = headers.index("prt_{}_image_intensity_resp.keys".format(prt))
                    keys_rt_raw = headers.index("prt_1_image_intensity_resp.rt")
                id_col = headers.index("PictureRatings_{}".format(prt))
                date_index = -5  # headers.index("date")
                expName_index = -4  # headers.index("expName")
            else:
                # if not headers, then parse as data
                line = line.split(",")
                if line != ['\n'] and len(line[id_col]) != 0:
                    id = line[id_col].split("/")[1].split(".")[0]
                else:
                    continue
                ret.append(DataType1(line[response_raw], line[rt_raw], line[keys_raw], line[keys_rt_raw],
                                     order, line[date_index], id, person_id, line[expName_index]))
                order += 1
    return ret

def format1():
    """
    This format is a slightly modified format0, so it will adjust to adhere to format0 and call it.

    :returns: list of `DataType` objects
    """
    pass