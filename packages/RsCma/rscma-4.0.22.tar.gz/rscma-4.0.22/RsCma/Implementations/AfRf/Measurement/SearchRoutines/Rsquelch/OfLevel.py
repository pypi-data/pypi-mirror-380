from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OfLevelCls:
	"""OfLevel commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofLevel", core, parent)

	def fetch(self) -> float:
		"""FETCh:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rsquelch.ofLevel.fetch() \n
		Query the RF level at which the DUT closes the squelch so that the audio signal is not muted anymore. CALCulate commands
		return error indicators instead of measurement values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: off_level: RF level at squelch switch-off level Range: -158 dBm to 16 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel?', suppressed)
		return Conversions.str_to_float(response)

	def calculate(self) -> float or bool:
		"""CALCulate:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel \n
		Snippet: value: float or bool = driver.afRf.measurement.searchRoutines.rsquelch.ofLevel.calculate() \n
		Query the RF level at which the DUT closes the squelch so that the audio signal is not muted anymore. CALCulate commands
		return error indicators instead of measurement values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: off_level: (float or boolean) RF level at squelch switch-off level Range: -158 dBm to 16 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel?', suppressed)
		return Conversions.str_to_float_or_bool(response)

	def read(self) -> float:
		"""READ:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rsquelch.ofLevel.read() \n
		Query the RF level at which the DUT closes the squelch so that the audio signal is not muted anymore. CALCulate commands
		return error indicators instead of measurement values. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: off_level: RF level at squelch switch-off level Range: -158 dBm to 16 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:SROutines:RSQuelch:OFLevel?', suppressed)
		return Conversions.str_to_float(response)
