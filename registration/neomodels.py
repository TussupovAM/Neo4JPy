# registration/neomodels.py
from neomodel import StructuredNode, StringProperty

class NeoUser(StructuredNode):
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
