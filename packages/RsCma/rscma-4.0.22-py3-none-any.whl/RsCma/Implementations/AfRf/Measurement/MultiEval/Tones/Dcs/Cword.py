from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CwordCls:
	"""Cword commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cword", core, parent)

	def fetch(self) -> List[str]:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:TONes:DCS:CWORd \n
		Snippet: value: List[str] = driver.afRf.measurement.multiEval.tones.dcs.cword.fetch() \n
		Query the code number of the five last detected code words. Code word results are separated by commas. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: codeword: Detected DCS code number as octal number Range: 16 to 511"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:TONes:DCS:CWORd?', suppressed)
		return Conversions.str_to_str_list(response)

	def read(self) -> List[str]:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:TONes:DCS:CWORd \n
		Snippet: value: List[str] = driver.afRf.measurement.multiEval.tones.dcs.cword.read() \n
		Query the code number of the five last detected code words. Code word results are separated by commas. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: codeword: Detected DCS code number as octal number Range: 16 to 511"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:MEValuation:TONes:DCS:CWORd?', suppressed)
		return Conversions.str_to_str_list(response)
