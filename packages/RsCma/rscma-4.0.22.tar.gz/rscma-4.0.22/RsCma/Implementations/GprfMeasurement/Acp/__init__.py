from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcpCls:
	"""Acp commands group definition. 38 total commands, 4 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acp", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def aclr(self):
		"""aclr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import AclrCls
			self._aclr = AclrCls(self._core, self._cmd_group)
		return self._aclr

	@property
	def power(self):
		"""power commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def obw(self):
		"""obw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .Obw import ObwCls
			self._obw = ObwCls(self._core, self._cmd_group)
		return self._obw

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:GPRF:MEASurement<Instance>:ACP \n
		Snippet: driver.gprfMeasurement.acp.initiate() \n
		Starts or continues the ACP measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:ACP', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:GPRF:MEASurement<Instance>:ACP \n
		Snippet: driver.gprfMeasurement.acp.stop() \n
		Pauses the ACP measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:ACP', opc_timeout_ms)
		# OpcSyncAllowed = true

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:GPRF:MEASurement<Instance>:ACP \n
		Snippet: driver.gprfMeasurement.acp.abort() \n
		Stops the ACP measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:ACP', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'AcpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AcpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
