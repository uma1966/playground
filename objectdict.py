
class Config1:
    ONE = 'one'
    TWO = 2
    THREE = 3.0

class Config2:
    ONE = 'eins'
    TWO = 2.0
    THREE = 3


config = Config1
print(config.ONE, config.TWO, config.THREE)
config = Config2
print(config.ONE, config.TWO, config.THREE)