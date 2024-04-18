from elements.captcha.base64 import get_base64
from elements.captcha.captcha_id import get_captcha_id
from utils.break_captcha import break_captcha

id = get_captcha_id()
base64 = get_base64("3874376E753970323766457323EDD3E9B6B51324A27E3B3552B732220F7E8608A1DB2481EAA9B9348B02")
captcha = break_captcha(base64)
print(captcha)