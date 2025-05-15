# 🌌 Live Sky Map

A fullscreen real-time **Sky map** built with Python, Tkinter, and [Skyfield](https://rhodesmill.org/skyfield/). This tool lets you visualize the current sky from your location — including the **Sun, Moon (with phase), planets, and over 30 deep-sky objects** like nebulae and galaxies.

Ideal for **Raspberry Pi setups**, astronomy enthusiasts, or as a live sky companion during telescope sessions.

---

## 🛰️ Features

- ✅ **Real-time astronomical tracking** (Sun, Moon, planets, DSOs)
- 🌙 **Moon phase** with dynamic brightness and percentage
- 🔭 Over 30 hand-picked **Messier and non-Messier objects** visualized
- 🪐 **Planets** shown with real positions from NASA JPL ephemeris
- 🧭 **Altitude/Azimuth grid** with labeled directions (N, S, E, W)
- 🕒 **Time Shift Slider** to explore past/future sky states
- 📅 **Live Clock and Date** display based on your location
- 🖼️ **Color-coded object types** (e.g., galaxies, nebulae, black holes)
- 🎯 Runs in **fullscreen**, perfect for touchscreens or planetarium setups

---

## 🧰 Prerequisites

This is a **Python 3** project. You will need the following Python libraries:

- `skyfield` – for ephemeris and astronomical calculations
- `pytz` – for accurate timezone support
- `tkinter` – for GUI rendering (included by default on most systems)

---

## 🔧 Installation

### 🖥️ On Windows/macOS/Linux:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhisekxp/-live-sky-map.git
   cd -live-sky-map
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the sky map:**
   ```bash
   python live_messier_sky.py
   ```

---

## 🍓 Running on Raspberry Pi (recommended for astronomy use)

1. Connect an HDMI display (5" or larger recommended).
2. Ensure Python 3 is installed (usually pre-installed).
3. Run:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install skyfield pytz
   python3 live_messier_sky.py
   ```
4. Use **touch input or mouse** to operate the “Now” button and close control.

---

## 🧭 Change Observer Location

Default location is **London**. To change it, edit the following line in `sky_map.py`:

```python
observer = earth + wgs84.latlon(51.5074, -0.1278)  # London
```

Replace it with your latitude and longitude.

---

## 📦 requirements.txt

Here's what your `requirements.txt` should contain:

```
skyfield
pytz
```

> `tkinter` is included with standard Python installations. On Linux, install via:
```bash
sudo apt install python3-tk
```

---

## ❓ FAQ

### Why is the Moon sometimes grey and sometimes bright?
The brightness of the Moon changes based on its **phase**. Full Moon appears brightest; New Moon is invisible.

### What are the small white dots?
They represent planets currently above the horizon.

### Can I add more objects?
Yes! You can add new deep-sky objects by editing the `objects` list and adding their Right Ascension and Declination coordinates.

---

## 📜 License

This project is released under the [MIT License](LICENSE). You are free to use, modify, and share it.

---

## ✨ Credits

- Astronomy calculations powered by [Skyfield](https://rhodesmill.org/skyfield/)
- Deep-sky object list curated manually
- Built with 💫 in Python by Abhisek Bhattacharya

---

## 🙌 Contributions Welcome!

Pull requests for features like:
- ISS tracking
- Constellation lines
- Observer location dropdown
- GUI enhancements

...are welcome!
