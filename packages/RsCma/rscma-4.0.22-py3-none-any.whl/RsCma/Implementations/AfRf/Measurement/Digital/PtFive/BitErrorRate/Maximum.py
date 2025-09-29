from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self) -> float:
		"""FETCh:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum \n
		Snippet: value: float = driver.afRf.measurement.digital.ptFive.bitErrorRate.maximum.fetch() \n
		Queries BER measurement results for the P25 standard. CALCulate commands return error indicators instead of measurement
		values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: ber: Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus:
		"""CALCulate:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum \n
		Snippet: value: enums.ResultStatus = driver.afRf.measurement.digital.ptFive.bitErrorRate.maximum.calculate() \n
		Queries BER measurement results for the P25 standard. CALCulate commands return error indicators instead of measurement
		values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: ber: Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus)

	def read(self) -> float:
		"""READ:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum \n
		Snippet: value: float = driver.afRf.measurement.digital.ptFive.bitErrorRate.maximum.read() \n
		Queries BER measurement results for the P25 standard. CALCulate commands return error indicators instead of measurement
		values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: ber: Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:DIGital:PTFive:BERate:MAXimum?', suppressed)
		return Conversions.str_to_float(response)
