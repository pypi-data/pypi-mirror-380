from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def fetch(self) -> List[float]:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:FFT:DEModulation:PDEViation:MINimum \n
		Snippet: value: List[float] = driver.afRf.measurement.multiEval.fft.demodulation.pdeviation.minimum.fetch() \n
		Query the contents of the spectrum diagram for PM demodulation. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1793 phase-deviation values (diagram from left to right) Unit: dBrad"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:FFT:DEModulation:PDEViation:MINimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:FFT:DEModulation:PDEViation:MINimum \n
		Snippet: value: List[float] = driver.afRf.measurement.multiEval.fft.demodulation.pdeviation.minimum.read() \n
		Query the contents of the spectrum diagram for PM demodulation. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: power: Comma-separated list of 1793 phase-deviation values (diagram from left to right) Unit: dBrad"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:AFRF:MEASurement<Instance>:MEValuation:FFT:DEModulation:PDEViation:MINimum?', suppressed)
		return response
