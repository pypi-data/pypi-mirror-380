# Yet Another Framework Interface

YAFI is another GUI for the Framework Laptop Embedded Controller.
It is written in Python with a GTK4 Adwaita theme, and uses the [`CrOS_EC_Python`](https://github.com/Steve-Tech/CrOS_EC_Python) library to communicate with the EC.

It has support for fan control, temperature monitoring, LED control, and battery limiting.

## Installation

You can download the latest release from the [Releases page](https://github.com/Steve-Tech/YAFI/releases).

There are builds for Flatpak, and PyInstaller for portable execution on Linux or Windows.

### Linux

To allow YAFI to communicate with the EC, you need to copy the [`60-cros_ec_python.rules`](60-cros_ec_python.rules) file to `/etc/udev/rules.d/` and reload the rules with `sudo udevadm control --reload-rules && sudo udevadm trigger`.

### Windows

If your Laptop's BIOS supports Framework's EC driver, there is no need to install any third-party drivers. YAFI should also work without administrator privileges.

Otherwise, YAFI supports the [PawnIO](https://pawnio.eu/) driver, and will be automatically used if installed and there is no Framework driver available. YAFI will need to be run as administrator to communicate with the driver.

## Building

### Flatpak

Build and install the Flatpak package with `flatpak-builder --install --user build au.stevetech.yafi.json`.

You can also create a flatpak bundle with `flatpak-builder --repo=repo build au.stevetech.yafi.json` and install it with `flatpak install --user repo au.stevetech.yafi.flatpak`.

### Pip

#### System Dependencies

This project requires PyGObject, and the introspection data for GTK4 and Adwaita.
On Debian/Ubuntu, you can install these with:

```bash
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1
```

#### Install

Install the package with `pip install yafi`.

Pipx is also supported.

### Windows

It is possible to run YAFI on Windows using [gvsbuild](https://github.com/wingtk/gvsbuild/) and installing YAFI via pip, but it can be complicated and is therefore not recommended.

## Screenshots

### Fan Control and Temperature Monitoring

![Thermals Page](docs/1-thermals.png)

### LED Control

![LEDs Page](docs/2-leds.png)

### Battery Statistics

![Battery Page](docs/3-battery.png)

### Battery Limiting

![Battery Limiter Page](docs/4-battery-limit.png)

#### Battery Extender

![Battery Extender](docs/4a-battery-ext.png)

### Hardware Info

![Hardware Page](docs/5-hardware.png)

## Troubleshooting

### `[Errno 13] Permission denied: '/dev/cros_ec'`

This error occurs when the udev rules are not installed or not working. Make sure you have copied the `60-cros_ec_python.rules` file to `/etc/udev/rules.d/` and reloaded the rules with `sudo udevadm control --reload-rules && sudo udevadm trigger`.

### `Could not auto detect device, check you have the required permissions, or specify manually.`

This error occurs when `/dev/cros_ec` is not found, and the `CrOS_EC_Python` library also cannot talk over LPC.
You can either update your kernel to have a working `cros_ec_dev` driver, or run YAFI as root.

It can also occur if you do not have a CrOS EC, like on non Framework laptops.
