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

	def read(self) -> List[float]:
		"""READ:VSE:MEASurement<Instance>:SDIStribute:CURRent \n
		Snippet: value: List[float] = driver.vse.measurement.sdistribute.current.read() \n
		Query the symbol distribution that is the distribution of the measured frequency deviations. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: symbols: The list of frequency deviations."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:VSE:MEASurement<Instance>:SDIStribute:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""FETCh:VSE:MEASurement<Instance>:SDIStribute:CURRent \n
		Snippet: value: List[float] = driver.vse.measurement.sdistribute.current.fetch() \n
		Query the symbol distribution that is the distribution of the measured frequency deviations. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: symbols: The list of frequency deviations."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:VSE:MEASurement<Instance>:SDIStribute:CURRent?', suppressed)
		return response
