from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DigitalCls:
	"""Digital commands group definition. 51 total commands, 5 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("digital", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def ttl(self):
		"""ttl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ttl'):
			from .Ttl import TtlCls
			self._ttl = TtlCls(self._core, self._cmd_group)
		return self._ttl

	@property
	def dmr(self):
		"""dmr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmr'):
			from .Dmr import DmrCls
			self._dmr = DmrCls(self._core, self._cmd_group)
		return self._dmr

	@property
	def tetra(self):
		"""tetra commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tetra'):
			from .Tetra import TetraCls
			self._tetra = TetraCls(self._core, self._cmd_group)
		return self._tetra

	@property
	def ptFive(self):
		"""ptFive commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptFive'):
			from .PtFive import PtFiveCls
			self._ptFive = PtFiveCls(self._core, self._cmd_group)
		return self._ptFive

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:AFRF:MEASurement<Instance>:DIGital \n
		Snippet: driver.afRf.measurement.digital.initiate() \n
		Starts or continues the measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:AFRF:MEASurement<Instance>:DIGital', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self) -> None:
		"""STOP:AFRF:MEASurement<Instance>:DIGital \n
		Snippet: driver.afRf.measurement.digital.stop() \n
		Pauses the measurement. \n
		"""
		self._core.io.write(f'STOP:AFRF:MEASurement<Instance>:DIGital')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:AFRF:MEASurement<Instance>:DIGital \n
		Snippet: driver.afRf.measurement.digital.stop_with_opc() \n
		Pauses the measurement. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:AFRF:MEASurement<Instance>:DIGital', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:AFRF:MEASurement<Instance>:DIGital \n
		Snippet: driver.afRf.measurement.digital.abort() \n
		Stops the measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:AFRF:MEASurement<Instance>:DIGital', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'DigitalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DigitalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
