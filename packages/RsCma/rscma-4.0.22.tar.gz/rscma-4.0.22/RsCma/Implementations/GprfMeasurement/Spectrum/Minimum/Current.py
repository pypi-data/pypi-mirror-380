from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""FETCh:GPRF:MEASurement<Instance>:SPECtrum:MINimum:CURRent \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.minimum.current.fetch() \n
		Query the result traces calculated with the 'MinPeak' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:SPECtrum:MINimum:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:GPRF:MEASurement<Instance>:SPECtrum:MINimum:CURRent \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.minimum.current.read() \n
		Query the result traces calculated with the 'MinPeak' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:SPECtrum:MINimum:CURRent?', suppressed)
		return response
