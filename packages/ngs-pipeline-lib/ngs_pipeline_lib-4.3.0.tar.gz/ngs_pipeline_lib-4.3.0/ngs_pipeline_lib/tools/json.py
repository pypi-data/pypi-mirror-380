import json
from datetime import datetime


# extend the json.JSONEncoder class
class NGSJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # datetime object are encoded as ISO 8601
        if isinstance(obj, datetime):
            return obj.isoformat(timespec="milliseconds").replace("+00:00", "Z")

        return json.JSONEncoder.default(self, obj)
