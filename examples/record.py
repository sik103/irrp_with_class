#!/usr/bin/env python3

from irrp_with_class import IRRP


irrp = IRRP(gpio=18, filename="codes", post=130, no_confirm=True)
irrp.record("light:on")
