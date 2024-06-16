class Person:
    """
    Keep track of all data associated with a single participant.

    Stores `DataType` objects associated with `Player`.
    """
    def __init__(self, id, listofDataType1=[]):
        """
        The constructor for `Person` class.

        :param id: number
        :param listofDataType1: list of `DataType1` objects to initialize `Person` with
        """
        self.id = id
        self.data1 = listofDataType1

    def __lt__(self, other):
        return self.id < other.id

    def getID(self):
        """
        Returns identifier for `Person`

        :return: number
        """
        return self.id

    def doesDataExist(self, data_id):
        """
        Checks to see if certain data exists for this participant

        :param data_id: number
        :return: True or False
        """
        for d in self.data1:
            if d.getId() == data_id:
                return True
        return False

    def addData(self, data):
        """
        Add data to `Person` object's list of data

        :param data: `DataType` object
        :return: nothing
        """
        self.data1.append(data)

    def clearAllData(self):
        self.data1 = []

    def getDate(self):
        for data in self.data1:
            if data.date != None:
                return data.date
        raise('Date not found')

    def getExperiment(self):
        for data in self.data1:
            if data.experiment != None:
                return data.date
        raise('ExpName not found')

    def sortData(self):
        """
        Use python's sort funtion on the data associated with the `Person`
        """
        self.data1.sort()
        # n = len(self.data1)
        #
        # # Traverse through all array elements
        # for i in range(n):
        #
        #     # Last i elements are already in place
        #     for j in range(0, n - i - 1):
        #
        #         # traverse the array from 0 to n-i-1
        #         # Swap if the element found is greater
        #         # than the next element
        #         if self.data1[j] > self.data1[j + 1]:
        #             self.data1[j], self.data1[j + 1] = self.data1[j + 1], self.data1[j]