# FakeMCServer (object-oriented)

> This is a fork of [FakeMCServer](https://github.com/ZockerSK/FakeMCServer). I forked it because I wanted to make it object-oriented, so that it is easier to use in other projects.

This program creates a simple Minecraft protocol wrapper, which imitates a full Minecraft server. This can be used to respond to pings with some information provided without the need to **start** a (Java) server.

![Overview](https://raw.githubusercontent.com/ZockerSK/FakeMCServerImages/main/overview.png)

- [FakeMCServer (object-oriented)](#fakemcserver-object-oriented)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Other information](#other-information)
  - [Contribution](#contribution)

## Usage

You can start this program by using

1. Clone this repository in your project repository
2. Use the example code below

Example usage 1:

```python
from FakeMCServer import FakeMCServer

server = FakeMCServer()
server.start_server()
```

Example usage 2:

```python
from FakeMCServer import FakeMCServer

server = FakeMCServer(motd={"1": "§4Maintenance!", "2": "§aCheck example.com for more information!")
server.start_server()
```

## Parameters

| Parameter                    | Type | Default Value                                                             | Description                                            |
| ---------------------------- | ---- | ------------------------------------------------------------------------- | ------------------------------------------------------ |
| `ip`                         | str  | "0.0.0.0"                                                                 | The IP address the server should bind to.              |
| `port`                       | int  | 25565                                                                     | The port the server should listen on.                  |
| `motd`                       | dict | {"1": "§4Maintenance!", "2": "§aCheck example.com for more information!"} | The Message of the Day displayed to clients.           |
| `version_text`               | str  | "§4Maintenance"                                                           | The version text displayed to clients.                 |
| `kick_message`               | list | ["§bSorry", "", "§aThis server is offline!"]                              | The message displayed to clients when they are kicked. |
| `server_icon`                | str  | "server_icon.png"                                                         | The path to the server icon file.                      |
| `samples`                    | list | ["§bexample.com", "", "§4Maintenance"]                                    | The samples displayed to clients.                      |
| `show_hostname_if_available` | bool | True                                                                      | Whether to show the hostname if it's available.        |
| `player_max`                 | int  | 0                                                                         | The maximum number of players allowed on the server.   |
| `player_online`              | int  | 0                                                                         | The number of players currently online.                |
| `protocol`                   | int  | 2                                                                         | The protocol version used by the server.               |

## Other information

Please note, that the `server_icon` **must** be 64x64 and a png file.

In this configuration you can use typical Minecraft message formatting tags.

`show_..._if_available` enables/disables the resolution of the hostname of the ip/that the IP will be displayed, if the hostname is available

`protocol` is the server's game version ID (see [wiki.vg](https://wiki.vg/Protocol_version_numbers) for more details)

`samples` specifies the player displayed when hovering over the player count/version information.

![Samples](https://raw.githubusercontent.com/ZockerSK/FakeMCServerImages/main/samples.png)

## Contribution

If you find some issues or encounter problems, feel free to write an issue providing your problem and some information regarding your setup (like Minecraft version, python version, ...).
This goes for this fork as well as for the original repository.
