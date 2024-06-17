class DataType1:
    """
    Keep data about individual image attributes specific to a `Person`.

    This data has the following 5 columns grouped together:
        prt_#_vas.response_raw_i####
        prt_#_vas.rt_raw_i####
        prt_image_intens_resp.keys_raw_i####
        prt_image_intens_resp.rt_raw_i####
        prt_order_i####
    It also keeps track of which participant id it is associated with.
    """

    # amount of unique identifiers that have been initialized and list of unique identifiers
    unique_id_count = 0
    unique_id_list = []

    # amount of columns DataType1 takes up
    col_space = 5

    @staticmethod
    def reset():
        """
        Resets the static data stored
        """
        DataType1.unique_id_list = []
        DataType1.unique_id_count = 0


    def __init__(self, vas_response_raw = None, vas_rt_raw = None, image_intens_resp_keys_raw = None,
                 image_intens_resp_rt_raw=None, order= None,date=None, image_id=None, person_id=None, experiment=None):
        """
        Constructor for `DataType1` class.

        :param vas_response_raw: number
        :param vas_rt_raw: number
        :param image_intens_resp_keys_raw: number
        :param image_intens_resp_rt_raw: number
        :param order: number
        :param date: string
        :param data_id: number
        :param experiment: string, although default value is None
        """
        self.vas_response_raw = vas_response_raw
        self.vas_rt_raw = vas_rt_raw
        self.intense_resp_keys_raw = image_intens_resp_keys_raw
        self.intense_resp_rt_raw = image_intens_resp_rt_raw
        self.order = order
        self.date = date
        self.data_id = image_id
        self.person_id = person_id
        self.experiment = experiment
        if image_id is not None and image_id not in DataType1.unique_id_list:
            DataType1.unique_id_list.append(image_id)
            DataType1.unique_id_count += 1


    def __str__(self):
        return """\
DataType1 with id == {} associated with Person {} dated {}:
    vas_response == {}
    vas_rt == {}
    resp_keys == {}
    resp_rt == {}
    order == {}
    experiment == {}\
        """.format(self.data_id, self.person_id, self.date, self.vas_response_raw, self.vas_rt_raw, self.intense_resp_keys_raw,
                   self.intense_resp_rt_raw, self.order, self.experiment)


    def __lt__(self, other):
        return self.data_id < other.data_id


    def getAssociatedParticipantID(self):
        """
        Returns participant ID associated with this data

        :returns: integer
        """
        return self.person_id


    def getAllFields(self, exclude=False):
        """
        Returns tuple of all fields for spreadsheet

        :return: tuple of string and number objects
        """
        if self.date is not None:
            return (int(self.vas_response_raw), float(self.vas_rt_raw), int(self.intense_resp_keys_raw[-1]),
                float(self.intense_resp_rt_raw), int(self.order))
        else:
            return ('','','','','')


    def getId(self):
        """
        Returns object's identifier

        :return: number
        """
        return self.data_id