from models.db import OfferStructure
import json


class Pixels(OfferStructure):
    def __init__(self, db, account_id):
        OfferStructure.__init__(self, db,  'pixels', account_id)
        self.set_constraint('pixels_pk', ['provider', 'offer_id'])

    def get_pixel(self, offer_id, provider):
        pix = self.get(['pixels'], where=f" where offer_id={offer_id} and provider='{provider}'")
        return json.loads(pix.iloc[0].pixels) if len(pix) else []