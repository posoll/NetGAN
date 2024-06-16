class Experiment:
    """
    This is a class to hold all `Person`s in an experiment.

    Maintains a list of `people` in the experiment.
    """
    def __init__(self, name = "Unnamed", listofPersons = []):
        """
        The constructor for `Experiment` class.

        :param name: string
        :param listofPersons: list of `Person` objects to initialize the experiment with
        """
        self.name = name
        self.people = listofPersons

