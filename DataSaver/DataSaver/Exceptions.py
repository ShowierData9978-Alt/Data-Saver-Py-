class error(Exception):
    pass


class NotJsonFile(error):
    pass

class NotJsonFormat(error):
    pass

class FileDoesNotExist(NotJsonFile):
    pass


class NotEnoughtStructure(NotJsonFile):
    pass