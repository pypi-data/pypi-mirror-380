from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:OSCilloscope:DEModulation:PDEViation:CURRent \n
		Snippet: value: List[float] = driver.afRf.measurement.multiEval.oscilloscope.demodulation.pdeviation.current.fetch() \n
		Query the contents of the AF oscilloscope diagram for PM demodulation. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: dvt_time: Comma-separated list of 960 phase-deviation values (diagram from left to right) Unit: rad"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:OSCilloscope:DEModulation:PDEViation:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:OSCilloscope:DEModulation:PDEViation:CURRent \n
		Snippet: value: List[float] = driver.afRf.measurement.multiEval.oscilloscope.demodulation.pdeviation.current.read() \n
		Query the contents of the AF oscilloscope diagram for PM demodulation. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: dvt_time: Comma-separated list of 960 phase-deviation values (diagram from left to right) Unit: rad"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:AFRF:MEASurement<Instance>:MEValuation:OSCilloscope:DEModulation:PDEViation:CURRent?', suppressed)
		return response
