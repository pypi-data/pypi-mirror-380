from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UpdateCls:
	"""Update commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	def set(self) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:LEVel:PEAK:DELTa:UPDate \n
		Snippet: driver.configure.afRf.measurement.voip.level.peak.delta.update.set() \n
		For level peak, triggers the update of the measurement value for VoIP. \n
		"""
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:VOIP:LEVel:PEAK:DELTa:UPDate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:LEVel:PEAK:DELTa:UPDate \n
		Snippet: driver.configure.afRf.measurement.voip.level.peak.delta.update.set_with_opc() \n
		For level peak, triggers the update of the measurement value for VoIP. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:AFRF:MEASurement<Instance>:VOIP:LEVel:PEAK:DELTa:UPDate', opc_timeout_ms)
