from pynetbox.core.response import Record, JsonField

class ObjectChanges(Record):
    object_data = JsonField
    postchange_data = JsonField
    prechange_data = JsonField

    def __str__(self):
        return self.request_id

class ConfigContextAssignments(Record):
    pass

class ConfigContexts(Record):
    pass

class ExportTemplates(Record):
    pass

class IxApi(Record):
    pass

class Tags(Record):
    pass

class Webhooks(Record):
    pass