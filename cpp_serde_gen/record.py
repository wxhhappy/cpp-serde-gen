import clang.cindex as cl


class RecordField(object):
    """
    """

    def __init__(self, name, t="void", access="PUBLIC"):
        self.name = name
        self.type = t
        self.access = access

    def __str__(self):
        return "{0}, {1}, {2}".format(self.name, self.type, self.access)

    def __eq__(self, other):
        return self.name == other.name and \
            self.type == other.type and \
            self.access == other.access


class Record(object):

    def __init__(self, name, fields=[], serdes=[]):
        self.name = name
        self.fields = fields
        self.serdes = serdes

    def append_field(self, field):
        self.fields.append(field)

    # A serde is the string key of a serializer/deserializer class.
    def append_serde(self, serde):
        self.serdes.append(serde)

    def __str__(self):
        return "name: {0}\nfields: {1}".format(self.name,
                                               [str(field) for field in
                                                self.fields])
