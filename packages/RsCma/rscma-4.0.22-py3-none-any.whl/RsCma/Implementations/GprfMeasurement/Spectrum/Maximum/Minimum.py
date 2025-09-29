from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def fetch(self) -> List[float]:
		"""FETCh:GPRF:MEASurement<Instance>:SPECtrum:MAXimum:MINimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.maximum.minimum.fetch() \n
		Query the result traces calculated with the 'MaxPeak' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:SPECtrum:MAXimum:MINimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:GPRF:MEASurement<Instance>:SPECtrum:MAXimum:MINimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.maximum.minimum.read() \n
		Query the result traces calculated with the 'MaxPeak' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:SPECtrum:MAXimum:MINimum?', suppressed)
		return response
