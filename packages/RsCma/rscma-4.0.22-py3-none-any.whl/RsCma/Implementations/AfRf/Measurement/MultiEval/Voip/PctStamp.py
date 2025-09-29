from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PctStampCls:
	"""PctStamp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pctStamp", core, parent)

	def fetch(self) -> int:
		"""FETCh:AFRF:MEASurement<instance>:MEValuation:VOIP:PCTStamp \n
		Snippet: value: int = driver.afRf.measurement.multiEval.voip.pctStamp.fetch() \n
		No command help available \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: pct_stamp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:VOIP:PCTStamp?', suppressed)
		return Conversions.str_to_int(response)
