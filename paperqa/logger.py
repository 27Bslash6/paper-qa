import logging

formatter = logging.Formatter("%(asctime)s  %(name)-40s  %(levelname)s: %(message)s")

handler = logging.StreamHandler()
handler.setFormatter(formatter)

LOGGER = logging.getLogger()
LOGGER.propagate = False
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.getLevelName("INFO"))
