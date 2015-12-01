# 'Line Follower' program
# Robot

import pi2go, time

pi2go.init()

# Defining speed
speed = 60

try:
  while True:
  # Defining sensors
  left = pi2go.irLeftLine()
  right = pi2go.irRightLine()
    if left == right: # if both sensors are the same (either on or off)
      pi2go.forward(speed)
    elif left == True: # if left sensor is on
      pi2go.spinRight(speed)
    elif right == True #if right sensor is on
      pi2go.spinLeft(speed)
      
finally: # cleanup
  pi2go.cleanup()
