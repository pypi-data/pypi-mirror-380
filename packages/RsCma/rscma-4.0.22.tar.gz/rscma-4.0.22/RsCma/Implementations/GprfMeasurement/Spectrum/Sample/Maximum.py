from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""FETCh:GPRF:MEASurement<Instance>:SPECtrum:SAMPle:MAXimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.sample.maximum.fetch() \n
		Query the result traces calculated with the 'Sample' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:SPECtrum:SAMPle:MAXimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:GPRF:MEASurement<Instance>:SPECtrum:SAMPle:MAXimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.spectrum.sample.maximum.read() \n
		Query the result traces calculated with the 'Sample' detector. The current, average, minimum and maximum traces can be
		retrieved. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1001 power values Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:SPECtrum:SAMPle:MAXimum?', suppressed)
		return response
