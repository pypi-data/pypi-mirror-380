from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def fetch(self) -> float:
		"""FETCh:AFRF:MEASurement<Instance>:SROutines:RIFBandwidth:BANDwidth \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rifBandwidth.bandwidth.fetch() \n
		Query the bandwidth as difference between higher frequency and lower frequency, that is the 'RX Bandwidth'. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: bandwidth: 'RX Bandwidth' Range: 0 Hz to 1 MHz, Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:SROutines:RIFBandwidth:BANDwidth?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""READ:AFRF:MEASurement<Instance>:SROutines:RIFBandwidth:BANDwidth \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rifBandwidth.bandwidth.read() \n
		Query the bandwidth as difference between higher frequency and lower frequency, that is the 'RX Bandwidth'. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: bandwidth: 'RX Bandwidth' Range: 0 Hz to 1 MHz, Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:SROutines:RIFBandwidth:BANDwidth?', suppressed)
		return Conversions.str_to_float(response)
