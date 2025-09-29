from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ElapsedStatsCls:
	"""ElapsedStats commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elapsedStats", core, parent)

	def fetch(self) -> int:
		"""FETCh:GPRF:MEASurement<Instance>:POWer:ESTatistics \n
		Snippet: value: int = driver.gprfMeasurement.power.elapsedStats.fetch() \n
		Returns the reliability indicator and the number of elapsed measurement intervals. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: stat_count: Number of elapsed measurement intervals. Range: 0 to configured statistic count"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:ESTatistics?', suppressed)
		return Conversions.str_to_int(response)
