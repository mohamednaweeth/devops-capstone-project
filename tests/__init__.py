from service import talisman

@classmethod
def setUpClass(cls):
    """Run once before all tests"""
    { other lines of code here ... }
    talisman.force_https = False
