
from controller import Robot

# Khoi tao robot
robot = Robot()

# Lay timestep
timestep = int(robot.getBasicTimeStep())

print("CONTROLLER STARTED!")

FL = robot.getDevice("FL")
FR = robot.getDevice("FR")
BL = robot.getDevice("BL")
BR = robot.getDevice("BR")
motors = [
    FL,FR,BL,BR
]

for motor in motors:

    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)


def set_speed(left_speed, right_speed):

    # Hai bánh trái
    FL.setVelocity(left_speed)
    BL.setVelocity(left_speed)

    # Hai bánh phải
    FR.setVelocity(right_speed)
    BR.setVelocity(right_speed)
# Vong lap mo phong
while robot.step(timestep) != -1:
    set_speed(1.0, 1.0)
    
    
    pass
