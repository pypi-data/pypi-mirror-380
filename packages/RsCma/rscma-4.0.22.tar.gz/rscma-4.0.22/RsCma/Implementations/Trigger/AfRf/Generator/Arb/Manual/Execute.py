from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExecuteCls:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""TRIGger:AFRF:GENerator<Instance>:ARB:MANual:EXECute \n
		Snippet: driver.trigger.afRf.generator.arb.manual.execute.set() \n
		Generates a trigger event for the trigger source 'Manual'. \n
		"""
		self._core.io.write(f'TRIGger:AFRF:GENerator<Instance>:ARB:MANual:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""TRIGger:AFRF:GENerator<Instance>:ARB:MANual:EXECute \n
		Snippet: driver.trigger.afRf.generator.arb.manual.execute.set_with_opc() \n
		Generates a trigger event for the trigger source 'Manual'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TRIGger:AFRF:GENerator<Instance>:ARB:MANual:EXECute', opc_timeout_ms)
