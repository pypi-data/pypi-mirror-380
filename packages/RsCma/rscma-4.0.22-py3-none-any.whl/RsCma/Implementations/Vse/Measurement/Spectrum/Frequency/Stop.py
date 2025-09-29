from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StopCls:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def fetch(self) -> float:
		"""FETCh:VSE:MEASurement<Instance>:SPECtrum:FREQuency:STOP \n
		Snippet: value: float = driver.vse.measurement.spectrum.frequency.stop.fetch() \n
		Queries the stop frequency of the measured spectrum. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: stop_frequency: Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:VSE:MEASurement<Instance>:SPECtrum:FREQuency:STOP?', suppressed)
		return Conversions.str_to_float(response)
