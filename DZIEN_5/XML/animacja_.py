import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
import matplotlib.animation as animation
import shutil
import sys

# --- wymagany do MP4: ffmpeg ---
if shutil.which("ffmpeg") is None:
    sys.exit(
        "Brak ffmpeg w PATH.\n"
        "Zainstaluj ffmpeg i uruchom ponownie.\n"
        "Windows (choco): choco install ffmpeg\n"
        "macOS (brew):   brew install ffmpeg\n"
        "Linux (apt):    sudo apt-get install ffmpeg"
    )

G = 9.8   # m/s^2
L1 = 1.0  # m
L2 = 1.0  # m
L  = L1 + L2
M1 = 1.0  # kg
M2 = 1.0  # kg
t_stop = 2.5
history_len = 500  # (tu nieużywane, ale zostawiam jeśli chcesz dodać "ogon")

def derivs(t, state):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1]**2 * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3]**2 * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3]**2 * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1]**2 * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)
    return dydx

# --- czas ---
dt = 0.01
t = np.arange(0, t_stop, dt)

# --- warunki początkowe (stopnie -> radiany) ---
th1, w1 = 120.0, 0.0
th2, w2 = -10.0, 0.0
state = np.radians([th1, w1, th2, w2])

# --- integracja Eulera ---
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt

# --- współrzędne ---
x1 = L1*np.sin(y[:, 0]);  y1 = -L1*np.cos(y[:, 0])
x2 = L2*np.sin(y[:, 2]) + x1;  y2 = -L2*np.cos(y[:, 2]) + y1

# --- rysunek ---
fig = plt.figure(figsize=(5, 4), dpi=120)
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.0))
ax.set_aspect('equal')
ax.grid()

line,  = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'time = %.2fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    trace.set_data([], [])
    time_text.set_text('')
    return line, trace, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    trace.set_data(x2[:i], y2[:i])  # ślad końcówki wahadła 2
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text

frames = len(y)
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=frames, interval=dt*1000, blit=True
)

# --- zapis do MP4 ---
writer = animation.FFMpegWriter(fps=int(1/dt), bitrate=2000, metadata={"artist": "DoublePendulum"})
output_path = "double_pendulum.mp4"
ani.save(output_path, writer=writer)

print(f"Zapisano: {output_path}")
# plt.show()  # opcjonalnie: podgląd po nagraniu
