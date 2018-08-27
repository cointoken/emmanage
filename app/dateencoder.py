from datetime import datetime
import json
 
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)
