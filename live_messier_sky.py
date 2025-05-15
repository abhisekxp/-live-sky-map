import tkinter as tk
import math
from skyfield.api import load, Star, wgs84

# Helper functions
def hms_to_hours(h, m, s):
    return h + m/60 + s/3600

def dms_to_degrees(d, m, s):
    sign = -1 if d < 0 else 1
    return sign * (abs(d) + m/60 + s/3600)

def get_color(dso_type):
    colors = {
        "globular_cluster": "#F4C430",       
        "bright_nebula": "#7FFFD4",           
        "dark_nebula": "#4B0082",           
        "planetary_nebula": "#FF6EB4",   
        "reflection_nebula": "#87CEEB",       
        "galaxy": "#DC143C",                   
        "supernova_remnant": "#9370DB",       
        "supermassive_black_hole": "#8B0000",  
        "planet": "#FFFFFF",                   
    }
    return colors.get(dso_type, "#FFFFFF")

# Load ephemeris
eph = load('de421.bsp')
earth, sun, moon = eph['earth'], eph['sun'], eph['moon']
ts = load.timescale()

# Your location
#New York - (40.7128, -74.0060)
#London - (51.5074, -0.1278)
#Paris - (48.8566, 2.3522)
#Tokyo - (35.6895, 139.6917)
#Sydney - (-33.8688, 151.2093)
#Moscow - (55.7558, 37.6173)
#Beijing - (39.9042, 116.4074)
#Dubai - (25.2769, 55.2962)
#São Paulo - (-23.5505, -46.6333)
#Johannesburg - (-26.2041, 28.0473)
#Los Angeles - (34.0522, -118.2437)
#Toronto - (43.6532, -79.3832)
#Berlin - (52.5200, 13.4050)
#Mumbai - (19.0760, 72.8777)
#Singapore - (1.3521, 103.8198)
#Seoul - (37.5665, 126.9780)
#Mexico City - (19.4326, -99.1332)
#Istanbul - (41.0082, 28.9784)
#Cairo - (30.0444, 31.2357)
#Bangkok - (13.7563, 100.5018)

observer = earth + wgs84.latlon(51.5074, -0.1278)  # London

static_messier_list = [
    ("M1", "- Crab Nebula"),
    ("M8", "- Lagoon Nebula"),
    ("M13", "- Great Hercules Cluster"),
    ("M15", "- Great Pegasus Cluster"),
    ("M16", "- Eagle Nebula"),
    ("M17", "- Swan Nebula"),
    ("M22", "- Great Sagittarius Cluster"),
    ("M27", "- Dumbbell Nebula"),
    ("M31", "- Andromeda Galaxy"),
    ("M33", "- Triangulum Galaxy"),
    ("M42", "- Orion Nebula"),
    ("M51", "- Whirlpool Galaxy"),
    ("M57", "- Ring Nebula"),
    ("M63", "- Sunflower Galaxy"),
    ("M64", "- Black Eye Galaxy"),
    ("M65", "- Leo Triplet (Galaxy)"),
    ("M76", "- Little Dumbbell Nebula"),
    ("M81", "- Bode's Galaxy"),
    ("M82", "- Cigar Galaxy"),
    ("M83", "- Southern Pinwheel Galaxy"),
    ("M87", "- Virgo A Galaxy"),
    ("M97", "- Owl Nebula"),
    ("M101", "- Pinwheel Galaxy"),
    ("M104", "- Sombrero Galaxy"),
    ("S279", "- Running Man Nebula"),
    ("B33", "- Horsehead Nebula"),
    ("C33", "- Eastern Veil Nebula"),
    ("C34", "- Western Veil Nebula"),
    ("NGC 7000", "- North America Nebula"),
    ("NGC 7635", "- Bubble Nebula"),
    ("NGC 2237", "- Rosette Nebula"),
    ("NGC 2359", "- Thor's Helmet"),
    ("NGC 6888", "- Crescent Nebula"),
    ("Monster", "- Sagittarius A* (Supermassive Black Hole)"),
]


objects = [
    {"name": "M1", "ra": (5, 34, 31.94), "dec": (22, 0, 52.2), "type": "supernova_remnant"},
    {"name": "M8", "ra": (18, 3, 37.0), "dec": (-24, 23, 12), "type": "bright_nebula"},
    {"name": "M13", "ra": (16, 41, 41.24), "dec": (36, 27, 35.5), "type": "globular_cluster"},
    {"name": "M15", "ra": (21, 29, 58.0), "dec": (12, 10, 1), "type": "globular_cluster"},
    {"name": "M16", "ra": (18, 18, 48.0), "dec": (-13, 47, 0), "type": "bright_nebula"},
    {"name": "M17", "ra": (18, 20, 48.0), "dec": (-16, 10, 0), "type": "bright_nebula"},
    {"name": "M22", "ra": (18, 36, 24.0), "dec": (-23, 54, 12), "type": "globular_cluster"},
    {"name": "M27", "ra": (19, 59, 36.34), "dec": (22, 43, 16.09), "type": "planetary_nebula"},
    {"name": "M31", "ra": (0, 42, 44.3), "dec": (41, 16, 9), "type": "galaxy"},
    {"name": "M33", "ra": (1, 33, 50.9), "dec": (30, 39, 36), "type": "galaxy"},
    {"name": "M42", "ra": (5, 35, 17.3), "dec": (-5, 23, 28), "type": "bright_nebula"},
    {"name": "M51", "ra": (13, 29, 52.7), "dec": (47, 11, 43), "type": "galaxy"},
    {"name": "M57", "ra": (18, 53, 35.0), "dec": (33, 1, 45), "type": "planetary_nebula"},
    {"name": "M63", "ra": (13, 15, 49.3), "dec": (42, 1, 45), "type": "galaxy"},
    {"name": "M64", "ra": (12, 56, 43.6), "dec": (21, 41, 0), "type": "galaxy"},
    {"name": "M65", "ra": (11, 18, 55.7), "dec": (13, 5, 32), "type": "galaxy"},
    {"name": "M76", "ra": (1, 42, 19.5), "dec": (51, 34, 31), "type": "planetary_nebula"},
    {"name": "M81", "ra": (9, 55, 33.2), "dec": (69, 3, 55), "type": "galaxy"},
    {"name": "M82", "ra": (9, 55, 52.2), "dec": (69, 40, 47), "type": "galaxy"},
    {"name": "M83", "ra": (13, 37, 0.9), "dec": (-29, 51, 57), "type": "galaxy"},
    {"name": "M87", "ra": (12, 30, 49.4), "dec": (12, 23, 28), "type": "galaxy"},
    {"name": "M97", "ra": (11, 14, 48.0), "dec": (55, 1, 9), "type": "planetary_nebula"},
    {"name": "M101", "ra": (14, 3, 12.6), "dec": (54, 20, 57), "type": "galaxy"},
    {"name": "M104", "ra": (12, 39, 59.4), "dec": (-11, 37, 23), "type": "galaxy"},
    {"name": "B33", "ra": (5, 40, 59.0), "dec": (-2, 27, 30), "type": "dark_nebula"},
    {"name": "S279", "ra": (5, 35, 16.0), "dec": (-4, 52, 0), "type": "reflection_nebula"},
    {"name": "C33", "ra": (20, 56, 18.0), "dec": (31, 43, 0), "type": "supernova_remnant"},
    {"name": "C34", "ra": (20, 45, 38.0), "dec": (30, 43, 0), "type": "supernova_remnant"},
    {"name": "NGC 7000", "ra": (20, 58, 54.0), "dec": (44, 19, 0), "type": "bright_nebula"},
    {"name": "NGC 7635", "ra": (23, 20, 48.0), "dec": (61, 12, 6), "type": "bright_nebula"},
    {"name": "NGC 2237", "ra": (6, 33, 45.0), "dec": (4, 59, 54), "type": "bright_nebula"},
    {"name": "NGC 2359", "ra": (7, 18, 30.0), "dec": (-13, 13, 0), "type": "bright_nebula"},
    {"name": "NGC 6888", "ra": (20, 12, 6.0), "dec": (38, 21, 18), "type": "bright_nebula"},
    {"name": "Monster", "ra": (17, 45, 40.0), "dec": (-29, 0, 28), "type": "supermassive_black_hole"},
]


# Tkinter window
root = tk.Tk()
root.title("Live Messier Sky Map")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='black')
canvas.pack(fill="both", expand=True)

center_x = screen_width // 2
center_y = screen_height // 2
sky_radius = min(screen_width, screen_height) // 2 - 60  # margin

def close_dashboard():
    root.destroy()

# === Time Shift Slider and Now Button ===

# Update when slider moves
def on_slider_change(val):
    update()

# Horizontal time shift slider (-5h to +5h)
time_shift_slider = tk.Scale(
    root,
    from_=-8,
    to=8,
    orient='horizontal',
    label='Time Shift (Hours)',
    length=400,
    resolution=0.1,
    fg='#90EE90',
    bg='black',
    highlightbackground='black',
    troughcolor='#333',
    font=('Arial', 20, 'bold'),
    command=on_slider_change
)
time_shift_slider.set(0)
time_shift_slider.place(x=screen_width - 450, y=screen_height - 150)

# "Now" button to reset time shift to 0
def reset_to_now():
    time_shift_slider.set(0)
    update()

now_button = tk.Button(
    root,
    text="Now",
    command=reset_to_now,
    bg="#222",
    fg="#90EE90",
    font=('Arial', 16, 'bold'),
    relief=tk.RAISED
)
now_button.place(x=screen_width - 130, y=screen_height - 150)


def get_moon_phase(t):
    observer_pos = earth.at(t)
    sun_pos = observer_pos.observe(sun).apparent()
    moon_pos = observer_pos.observe(moon).apparent()
    elongation = sun_pos.separation_from(moon_pos).degrees
    return elongation

def draw_moon(x, y, radius, elongation_deg):
    # Phase from 0 (new) to 1 (full)
    phase = (1 - math.cos(math.radians(elongation_deg))) / 2
    brightness = int(phase * 255)
    brightness_hex = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=brightness_hex, outline=brightness_hex)


def update():
    canvas.delete("all")

    # Draw color index (legend) on right side
    legend_items = [
        ("Globular Cluster", "#F4C430"),         # Goldenrod - denser, older clusters
        ("Bright Nebula", "#7FFFD4"),            # Aquamarine - glowing, energetic
        ("Planetary Nebula", "#FF6EB4"),         # Hot Pink - eye-catching and structured
        ("Dark Nebula", "#4B0082"),              # Midnight Blue - mysterious and obscuring
        ("Reflection Nebula", "#87CEEB"),        # Sky Blue - light scattered by dust
        ("Galaxy", "#DC143C"),                   # Crimson - majestic and powerful
        ("Supernova Remnant", "#9370DB"),        # Medium Purple - chaotic and rich in energy
        ("Planet", "#FFFFFF"),                   # White - classical simplicity
        ("Black Hole", "#8B0000"),               # Dark Red - danger and intensity
    ]


    for idx, (label, color) in enumerate(legend_items):
        legend_x = screen_width - 250  # Near right edge
        legend_y = 50 + idx * 30       # 30 pixels gap between entries
        # Draw color box
        canvas.create_oval(legend_x, legend_y, legend_x + 10, legend_y + 10, fill=color, outline=color)
        # Draw text
        canvas.create_text(legend_x + 20, legend_y + 5, text=label, anchor='w', fill='#90EE90', font=('Arial', 12, 'bold'))


    #Draw static list
    for idx, (messier_number, popular_name) in enumerate(static_messier_list):
        list_x = 50   # Fixed x position (left side)
        list_y = 50 + idx * 25   # 25 pixel gap between rows
        canvas.create_text(list_x, list_y, text=f"{messier_number} {popular_name}", fill='#90EE90', anchor='w', font=('Arial', 12, 'bold'))

    # Draw altitude circles
    for alt in range(0, 90, 5):
        r = (90 - alt) / 90 * sky_radius
        if alt in [30, 60]:
            line_width = 1
            altcolor = '#90EE90'
        elif alt == 0:
            line_width = 2
            altcolor = '#90EE90'
        else:
            line_width = 1
            altcolor = 'gray'
        canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, outline=altcolor, width=line_width)
        canvas.create_text(center_x - 12, center_y - r, text=f"{alt}°", fill='#90EE90', font=('Arial', 12, 'bold'))

    # Draw azimuth lines
    for az in range(0, 360, 5):
        angle_rad = math.radians(az)
        x_outer = center_x + sky_radius * math.sin(angle_rad)
        y_outer = center_y - sky_radius * math.cos(angle_rad)
        if az in [0, 90, 180, 270]:
            azcolor = '#90EE90'
        else:
            azcolor = 'gray'
        canvas.create_line(center_x, center_y, x_outer, y_outer, fill=azcolor, width=1)

        if az % 90 == 0:
            label = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}[az]
            lx = center_x + (sky_radius + 30) * math.sin(angle_rad)
            ly = center_y - (sky_radius + 30) * math.cos(angle_rad)
            canvas.create_text(lx, ly, text=label, fill='#90EE90', font=('Arial', 26, 'bold'))
        else:
            lx = center_x + (sky_radius + 20) * math.sin(angle_rad)
            ly = center_y - (sky_radius + 20) * math.cos(angle_rad)
            canvas.create_text(lx, ly, text=str(az), fill='#90EE90', font=('Arial', 12, 'bold'))

    from datetime import timedelta
    shift_hours = time_shift_slider.get()
    t = ts.now() + timedelta(hours=shift_hours)


    placed_labels = []

    for obj in objects:
        ra_hours = hms_to_hours(*obj['ra'])
        dec_degrees = dms_to_degrees(*obj['dec'])

        star = Star(ra_hours=ra_hours, dec_degrees=dec_degrees)
        astrometric = observer.at(t).observe(star).apparent()
        alt, az, _ = astrometric.altaz()

        if alt.degrees >= 0:
            radius = (90 - alt.degrees) / 90 * sky_radius
            az_rad = math.radians(az.degrees)
            x = center_x + radius * math.sin(az_rad)
            y = center_y - radius * math.cos(az_rad)

            # Draw dot
            dot_color = get_color(obj['type'])

            if obj['type'] == "planet":
                canvas.create_oval(x-2, y-2, x+2, y+2, fill=dot_color, outline=dot_color)
            else:
                canvas.create_oval(x-3, y-3, x+3, y+3, fill=dot_color, outline=dot_color)


            # Default label offset
            offset_x = 15 if x < center_x else -15
            offset_y = -15 if y < center_y else 15

            # Conflict detection and adjustment
            conflict = False
            for (lx, ly) in placed_labels:
                if math.hypot((x + offset_x) - lx, (y + offset_y) - ly) < 30:
                    conflict = True
                    break

            if conflict:
                offset_x += 20
                offset_y += 20

            label_x = x + offset_x
            label_y = y + offset_y
            canvas.create_text(label_x, label_y, text=obj['name'], fill=dot_color, font=('Arial', 14, 'bold'))

            placed_labels.append((label_x, label_y))

    # Compute Sun's position
    astrometric_sun = observer.at(t).observe(sun).apparent()
    sun_alt, sun_az, _ = astrometric_sun.altaz()

    if sun_alt.degrees >= 0:
        sun_r = (90 - sun_alt.degrees) / 90 * sky_radius
        sun_az_rad = math.radians(sun_az.degrees)
        sun_x = center_x + sun_r * math.sin(sun_az_rad)
        sun_y = center_y - sun_r * math.cos(sun_az_rad)

        canvas.create_oval(sun_x - 10, sun_y - 10, sun_x + 10, sun_y + 10, fill='yellow', outline='yellow')
        canvas.create_text(sun_x, sun_y + 20, text="Sun", fill='yellow', font=('Arial', 14, 'bold'))
    else:
        sun_x = center_x
        sun_y = center_y

    # Compute Moon position
    astrometric_moon = observer.at(t).observe(moon).apparent()
    moon_alt, moon_az, _ = astrometric_moon.altaz()

    if moon_alt.degrees >= 0:
        moon_r = (90 - moon_alt.degrees) / 90 * sky_radius
        moon_az_rad = math.radians(moon_az.degrees)
        moon_x = center_x + moon_r * math.sin(moon_az_rad)
        moon_y = center_y - moon_r * math.cos(moon_az_rad)

        elongation = get_moon_phase(t)
        phase = (1 - math.cos(math.radians(elongation))) / 2
        moon_percent = int(phase * 100)

        draw_moon(moon_x, moon_y, 10, elongation)
        canvas.create_text(moon_x, moon_y + 20, text=f"Moon ({moon_percent}%)", fill='white', font=('Arial', 14, 'bold'))



    planets = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter']

    for name in planets:
        planet = eph[name]
        astrometric = observer.at(t).observe(planet).apparent()
        alt, az, _ = astrometric.altaz()

        if alt.degrees >= 0:
            radius = (90 - alt.degrees) / 90 * sky_radius
            az_rad = math.radians(az.degrees)
            x = center_x + radius * math.sin(az_rad)
            y = center_y - radius * math.cos(az_rad)

            # Draw white dot
            canvas.create_oval(x-4, y-4, x+4, y+4, fill='white', outline='white')

            # Add label
            label_name = name.capitalize().split()[0]  # To show 'Jupiter' not 'Jupiter barycenter'
            canvas.create_text(x, y + 12, text=label_name, fill='white', font=('Arial', 12, 'bold'))

   
    from datetime import datetime
    import pytz
    london = pytz.timezone("Europe/London")

    # Get time and date
    now = datetime.now(london)
    local_now = now.strftime("%I:%M %p")  # clock with AM/PM
    local_date = now.strftime("%d %b %Y")    # date like 29 Apr 2025

    # Draw date, clock, and location
    date_y = screen_height // 2 - 40
    time_y = screen_height // 2
    location_y = screen_height // 2 + 40

    canvas.create_text(screen_width - 175, date_y, text=local_date, fill='#90EE90', font=('Courier', 25, 'bold'))
    canvas.create_text(screen_width - 175, time_y, text=local_now, fill='#90EE90', font=('Courier', 35, 'bold'))
    canvas.create_text(screen_width - 175, location_y, text="London", fill='#90EE90', font=('Arial', 30, 'bold'))


    # Draw close button (small rectangle with "X")
    button_x1 = screen_width - 60
    button_y1 = 10
    button_x2 = screen_width - 10
    button_y2 = 40

    canvas.create_rectangle(button_x1, button_y1, button_x2, button_y2, fill="red", outline="white")
    canvas.create_text((button_x1 + button_x2) / 2, (button_y1 + button_y2) / 2, text="X", fill="white", font=('Arial', 14, 'bold'))

    # Bind mouse click event
    def on_click(event):
         if button_x1 <= event.x <= button_x2 and button_y1 <= event.y <= button_y2:
             close_dashboard()

    canvas.bind("<Button-1>", on_click)


    root.after(60000, update)  # run update every minute

update()  # start the first update
root.attributes('-fullscreen', True)
root.mainloop()