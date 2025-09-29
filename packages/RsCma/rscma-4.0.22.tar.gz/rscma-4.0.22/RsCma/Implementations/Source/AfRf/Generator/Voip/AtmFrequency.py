from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtmFrequencyCls:
	"""AtmFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atmFrequency", core, parent)

	def get_enable(self) -> bool:
		"""SOURce:AFRF:GENerator<Instance>:VOIP:ATMFrequency:ENABle \n
		Snippet: value: bool = driver.source.afRf.generator.voip.atmFrequency.get_enable() \n
		Copies the current value of the carrier center frequency of AFRF generator to the RF measurements Also, copies the
		frequency value when changing the carrier frequency value via the FID. \n
			:return: atm_frequency: OFF | ON
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:VOIP:ATMFrequency:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, atm_frequency: bool) -> None:
		"""SOURce:AFRF:GENerator<Instance>:VOIP:ATMFrequency:ENABle \n
		Snippet: driver.source.afRf.generator.voip.atmFrequency.set_enable(atm_frequency = False) \n
		Copies the current value of the carrier center frequency of AFRF generator to the RF measurements Also, copies the
		frequency value when changing the carrier frequency value via the FID. \n
			:param atm_frequency: OFF | ON
		"""
		param = Conversions.bool_to_str(atm_frequency)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:VOIP:ATMFrequency:ENABle {param}')
