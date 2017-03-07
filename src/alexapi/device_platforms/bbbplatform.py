import Adafruit_BBIO.GPIO as GPIO

from .rpilikeplatform import RPiLikePlatform


class BbbPlatform(RPiLikePlatform):

	def __init__(self, config):
		super(BbbPlatform, self).__init__(config, 'bbb', GPIO)

	def setup(self):
		GPIO.setwarnings(False)
		GPIO.cleanup()

		super(BbbPlatform, self).setup()
