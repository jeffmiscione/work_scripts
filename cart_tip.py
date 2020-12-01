import math

pivot_to_COM_vertical = .90775 # m
pivot_to_COM_horizontal = .33645 # m
theta = math.atan(pivot_to_COM_vertical / pivot_to_COM_horizontal)
radius = math.sqrt(pow(pivot_to_COM_vertical, 2) + pow(pivot_to_COM_horizontal, 2))
mass = 545.5 # kg
g = -9.81 # m/s^2
I = 690 # moment of inertia (kg * m^2)

lin_velocity_init = 0.5 # m/s
ang_velocity_prev = lin_velocity_init / pivot_to_COM_vertical # rads
angle_prev = 0      # initial angle (radians)
t_now = 0           # current simulation time (s)
t_stop = 10         # time at which simulation will stop (s)
t_step = 0.001      # time step for simulation (s)

while t_now < t_stop:
    t_now = t_now + t_step      # increment time
    torque = mass * g * pivot_to_COM_horizontal # Nm
    alpha = torque / I

    ang_velocity = (alpha * t_step) + ang_velocity_prev
    angle = (ang_velocity * t_step) + angle_prev

    # at end of loop
    pivot_to_COM_horizontal = radius * math.cos(angle + theta)

    print("%s, %s" % (t_now, angle))

    if pivot_to_COM_horizontal <= 0:
        print('failure')
        break

    if angle < 0:
        print('success')
        break

    ang_velocity_prev = ang_velocity
    angle_prev = angle