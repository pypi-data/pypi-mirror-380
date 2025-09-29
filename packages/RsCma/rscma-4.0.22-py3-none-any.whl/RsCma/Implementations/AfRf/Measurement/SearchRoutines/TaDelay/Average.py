from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self) -> float:
		"""FETCh:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.taDelay.average.fetch() \n
		No command help available \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: delay: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""READ:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.taDelay.average.read() \n
		No command help available \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: delay: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus:
		"""CALCulate:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage \n
		Snippet: value: enums.ResultStatus = driver.afRf.measurement.searchRoutines.taDelay.average.calculate() \n
		No command help available \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: delay: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:AFRF:MEASurement<Instance>:SROutines:TADelay:AVERage?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus)
