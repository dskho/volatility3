# This file is Copyright 2019 Volatility Foundation and licensed under the Volatility Software License 1.0
# which is available at https://www.volatilityfoundation.org/license/vsl-v1.0
#

from volatility.framework.symbols import intermed
from volatility.framework.symbols.mac import extensions


class MacKernelIntermedSymbols(intermed.IntermediateSymbolTable):
    provides = {"type": "interface"}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.set_type_class('proc', extensions.proc)
        self.set_type_class('fileglob', extensions.fileglob)
        self.set_type_class('vnode', extensions.vnode)
        self.set_type_class('vm_map_entry', extensions.vm_map_entry)
        self.set_type_class('vm_map_object', extensions.vm_map_object)
        self.set_type_class('socket', extensions.socket)
        self.set_type_class('inpcb', extensions.inpcb)
        self.set_type_class('queue_entry', extensions.queue_entry)
        self.set_type_class('ifnet', extensions.ifnet)
        self.set_type_class('sockaddr_dl', extensions.sockaddr_dl)
        self.set_type_class('sockaddr', extensions.sockaddr)
        self.set_type_class('sysctl_oid', extensions.sysctl_oid)
