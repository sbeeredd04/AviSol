
import tkinter as tk
import pandas as pd

def save_input():
    landing_zone = landing_zone_entry.get()
    takeoff_zone = takeoff_zone_entry.get()
    efficiency = efficiency_entry.get()
    speed_scale = speed_scale_entry.get()
    preferred_time = preferred_time_entry.get()

    data = {
        'Landing Zone': [landing_zone],
        'Takeoff Zone': [takeoff_zone],
        'Efficiency': [efficiency],
        'Speed Scale': [speed_scale],
        'Preferred Time': [preferred_time]
    }

    df = pd.DataFrame(data)

    df.to_excel('output.clv', index=False)

    root.destroy()

root = tk.Tk()

landing_zone_label = tk.Label(root, text="Landing Zone:")
landing_zone_label.pack()
landing_zone_entry = tk.Entry(root)
landing_zone_entry.pack()

takeoff_zone_label = tk.Label(root, text="Takeoff Zone:")
takeoff_zone_label.pack()
takeoff_zone_entry = tk.Entry(root)
takeoff_zone_entry.pack()

efficiency_label = tk.Label(root, text="Efficiency:")
efficiency_label.pack()
efficiency_entry = tk.Entry(root)
efficiency_entry.pack()

speed_scale_label = tk.Label(root, text="Speed Scale:")
speed_scale_label.pack()
speed_scale_entry = tk.Entry(root)
speed_scale_entry.pack()

preferred_time_label = tk.Label(root, text="Preferred Time:")
preferred_time_label.pack()
preferred_time_entry = tk.Entry(root)
preferred_time_entry.pack()

save_button = tk.Button(root, text="Calculate", command=save_input)
save_button.pack()

root.mainloop()
