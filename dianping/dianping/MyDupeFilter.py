# -*- coding: utf-8 -*-
from scrapy.dupefilters import RFPDupeFilter

class MyRFPDupeFilter(RFPDupeFilter):
    def request_seen(self, request):
        fp = self.request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        #self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)