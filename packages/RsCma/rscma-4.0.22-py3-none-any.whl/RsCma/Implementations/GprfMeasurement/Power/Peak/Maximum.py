from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def calculate(self) -> List[float or bool]:
		"""CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum \n
		Snippet: value: List[float or bool] = driver.gprfMeasurement.power.peak.maximum.calculate() \n
		Query the 'Power Maximum' result. CALCulate commands return an error indicator instead of a power value. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power_maximum_max: (float or boolean items) 'Power Maximum' result Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)

	def fetch(self) -> List[float]:
		"""FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.power.peak.maximum.fetch() \n
		Query the 'Power Maximum' result. CALCulate commands return an error indicator instead of a power value. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power_maximum_max: 'Power Maximum' result Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum \n
		Snippet: value: List[float] = driver.gprfMeasurement.power.peak.maximum.read() \n
		Query the 'Power Maximum' result. CALCulate commands return an error indicator instead of a power value. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power_maximum_max: 'Power Maximum' result Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:PEAK:MAXimum?', suppressed)
		return response
