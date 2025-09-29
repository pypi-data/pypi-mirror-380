from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchRoutinesCls:
	"""SearchRoutines commands group definition. 94 total commands, 7 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("searchRoutines", core, parent)

	@property
	def taDelay(self):
		"""taDelay commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_taDelay'):
			from .TaDelay import TaDelayCls
			self._taDelay = TaDelayCls(self._core, self._cmd_group)
		return self._taDelay

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def rsensitivity(self):
		"""rsensitivity commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_rsensitivity'):
			from .Rsensitivity import RsensitivityCls
			self._rsensitivity = RsensitivityCls(self._core, self._cmd_group)
		return self._rsensitivity

	@property
	def rifBandwidth(self):
		"""rifBandwidth commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rifBandwidth'):
			from .RifBandwidth import RifBandwidthCls
			self._rifBandwidth = RifBandwidthCls(self._core, self._cmd_group)
		return self._rifBandwidth

	@property
	def rsquelch(self):
		"""rsquelch commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsquelch'):
			from .Rsquelch import RsquelchCls
			self._rsquelch = RsquelchCls(self._core, self._cmd_group)
		return self._rsquelch

	@property
	def ssnr(self):
		"""ssnr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssnr'):
			from .Ssnr import SsnrCls
			self._ssnr = SsnrCls(self._core, self._cmd_group)
		return self._ssnr

	@property
	def tsensitivity(self):
		"""tsensitivity commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsensitivity'):
			from .Tsensitivity import TsensitivityCls
			self._tsensitivity = TsensitivityCls(self._core, self._cmd_group)
		return self._tsensitivity

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:AFRF:MEASurement<Instance>:SROutines \n
		Snippet: driver.afRf.measurement.searchRoutines.initiate() \n
		Starts or continues the search routine. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:AFRF:MEASurement<Instance>:SROutines', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self) -> None:
		"""STOP:AFRF:MEASurement<Instance>:SROutines \n
		Snippet: driver.afRf.measurement.searchRoutines.stop() \n
		Pauses the search routine. \n
		"""
		self._core.io.write(f'STOP:AFRF:MEASurement<Instance>:SROutines')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:AFRF:MEASurement<Instance>:SROutines \n
		Snippet: driver.afRf.measurement.searchRoutines.stop_with_opc() \n
		Pauses the search routine. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:AFRF:MEASurement<Instance>:SROutines', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:AFRF:MEASurement<Instance>:SROutines \n
		Snippet: driver.afRf.measurement.searchRoutines.abort() \n
		Stops the search routine. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:AFRF:MEASurement<Instance>:SROutines', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'SearchRoutinesCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SearchRoutinesCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
