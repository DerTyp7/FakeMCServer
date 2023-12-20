#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import base64
import os.path

from FakeMCServer.socket_server import SocketServer


class FakeMCServer:
    def __init__(self, ip: str = "0.0.0.0",
                 port: int = 25565, motd: dict = {"1": "§4Maintenance!", "2": "§aCheck example.com for more information!"},
                 version_text: str = "§4Maintenance", kick_message: list = ["§bSorry", "", "§aThis server is offline!"],
                 server_icon: str = "server_icon.png", samples: list = ["§bexample.com", "", "§4Maintenance"], show_hostname_if_available: bool = True,
                 player_max: int = 0, player_online: int = 0, protocol: int = 2):
        self.logger = logging.getLogger("FakeMCServer")
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        file_handler = logging.FileHandler("logs/access.log")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        self.ip = ip
        self.port = port
        self.motd = motd["1"] + "\n" + motd["2"]
        self.version_text = version_text
        self.kick_message = ""
        self.samples = samples
        self.show_hostname = show_hostname_if_available
        self.player_max = player_max
        self.player_online = player_online
        self.protocol = protocol
        self.server_icon = None

        for message in kick_message:
            self.kick_message += message + "\n"

        if not os.path.exists(server_icon):
            self.logger.warning(
                "Server icon doesn't exist - submitting none...")
        else:
            with open(server_icon, 'rb') as image:
                self.server_icon = "data:image/png;base64," + \
                    base64.b64encode(image.read()).decode()

    def start_server(self):
        try:
            self.logger.info("Setting up server...")
            self.server = SocketServer(self.ip, self.port, self.motd, self.version_text, self.kick_message, self.samples,
                                       self.server_icon, self.logger, self.show_hostname, self.player_max, self.player_online, self.protocol)
            self.server.start()
        except KeyboardInterrupt:
            self.logger.info("Shutting down server...")
            self.server.close()
            self.logger.info("Done. Thanks for using FakeMCServer!")
            exit(0)
        except Exception as e:
            self.logger.exception(e)


# * Example usage:
# if __name__ == '__main__':
#     server = FakeMCServer(
#         motd={"1": "§4Testing!", "2": "§aCheck example.com for more information!"},)
#     server.start_server()
