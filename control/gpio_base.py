import pigpio

# Initialize pigpio
pi = pigpio.pi()

# Helper for RPi.GPIO-style event detection
class EventDetector:
    def __init__(self, pi):
        self.pi = pi
        self.events = {}
        self.callbacks = {}

    def add_event_detect(self, gpio, edge, callback=None, bouncetime=200):
        # bouncetime is in ms, pigpio debounce is in microseconds
        self.pi.set_glitch_filter(gpio, bouncetime * 1000)
        
        if edge == 31: # RISING
            pigpio_edge = pigpio.RISING_EDGE
        elif edge == 32: # FALLING
            pigpio_edge = pigpio.FALLING_EDGE
        else: # BOTH
            pigpio_edge = pigpio.EITHER_EDGE
            
        self.events[gpio] = False
        def internal_callback(g, level, tick):
            self.events[g] = True
            if callback:
                callback(g)
            
        self.callbacks[gpio] = self.pi.callback(gpio, pigpio_edge, internal_callback)

    def remove_event_detect(self, gpio):
        if gpio in self.callbacks:
            self.callbacks[gpio].cancel()
            del self.callbacks[gpio]
        if gpio in self.events:
            del self.events[gpio]

    def event_detected(self, gpio):
        if gpio in self.events:
            detected = self.events[gpio]
            self.events[gpio] = False
            return detected
        return False

event_detector = EventDetector(pi)
