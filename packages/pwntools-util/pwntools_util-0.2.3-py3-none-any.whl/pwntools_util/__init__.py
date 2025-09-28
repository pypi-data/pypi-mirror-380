# pwntools wrapper with bytes casting and common utils

# ----- pwn -----

# imports

from .util import string_getter, type_convert
from .util.text_colors import colorize, TextColorCodes

import pwn
import subprocess

# class

class PwnUtil:
    def __init__(self):
        self._conn = None
        self._header = f"[{colorize('PwnUtil', TextColorCodes.Yellow)}]"
        self._isRemote = None
        self._isLocal = None

    # connect

    def connectRemote(self, host: str, port: int,
                      fam = "any", typ = "tcp",
                      sock=None, ssl=False, ssl_context=None, ssl_args=None, sni=True,
                      *args, **kwargs):
        print(f"{self._header}: Connecting to {colorize('remote', TextColorCodes.Green)}!")
        self._conn = pwn.remote(host, port, fam, typ, sock, ssl, ssl_context, ssl_args, sni, *args, **kwargs)
        self._isRemote = True
        self._isLocal = False

    def connectLocal(self, argv = None, *args, **kwargs):
        print(f"{self._header}: Connecting to {colorize('local', TextColorCodes.Blue)}!")
        self._conn = pwn.process(argv, *args, **kwargs)
        self._isLocal = True
        self._isRemote = False

    def connectLocal_py(self, path_to_file: str, path_to_interpreter = "./.venv/bin/python", *args, **kwargs):
        self.connectLocal([path_to_interpreter, path_to_file], *args, **kwargs)

    # disconnect

    def disconnect(self):
        if self._conn:
            self._conn.close()
            self._isRemote = self._isLocal = False
            print(f"{self._header}: Disconnected!")

    # get & send

    def getline(self, timeout = 5):
        return self._conn.recvline(timeout=timeout)

    def getuntil(self, data: str | bytes | tuple[str] | tuple[bytes], timeout = 5):
        return self._conn.recvuntil(type_convert.dataToBytes(data), timeout=timeout)

    def getall(self, timeout = 5):
        return self._conn.recvall(timeout=timeout)

    def sendline(self, data: str | bytes):
        self._conn.sendline(type_convert.dataToBytes(data))

    def interactive(self):
        self._conn.interactive()

    # ----- utility -----

    # proof of work

    def solve_redpwn_pow(self, message_before_command = "proof of work:"):
        self.getuntil(message_before_command)
        proof_command = self.getline().strip()
        for _ in range(10):
            if proof_command != b'':
                break
            proof_command = self.getline().strip()
        print(f"{self._header}: <{colorize('pow call', TextColorCodes.Green)}>: {proof_command.decode()}")
        solution = subprocess.check_output(["sh", "-c", proof_command]).strip()
        print(f"{self._header}: <{colorize('solution', TextColorCodes.Green)}>: {solution.decode()}")
        self.sendline(solution)

    # integer

    def getFromLine_Int(self):
        return string_getter.getFromString_Int(self.getline().decode())

    def getAllFromLine_Int(self):
        return string_getter.getAllFromString_Int(self.getline().decode())

    def getListFromLine_Int(self):
        return string_getter.getListFromString_Int(self.getline().decode())

    # float

    def getFromLine_Float(self):
        return string_getter.getFromString_Float(self.getline().decode())

    def getAllFromLine_Float(self):
        return string_getter.getAllFromString_Float(self.getline().decode())

    def getListFromLine_Float(self):
        return string_getter.getListFromString_Float(self.getline().decode())
