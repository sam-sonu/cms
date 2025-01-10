class SRIClient(object):
    def __init__(self, app_id="76668"):
        self.host = getattr(settings, "SRI_API_HOST", "")
        self.access_key = getattr(settings, "SRI_ACCESS_KEY", "")
        self.secret_key = getattr(settings, "SRI_SECRET_KEY", "")
        self.password = getattr(settings, "SRI_API_PASS", "")
        self.app_id = app_id
        
        
