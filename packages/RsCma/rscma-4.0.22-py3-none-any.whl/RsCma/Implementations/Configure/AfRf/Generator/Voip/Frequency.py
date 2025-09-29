from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_atm_frequency(self) -> bool:
		"""CONFigure:AFRF:GENerator<Instance>:VOIP:FREQuency:ATMFrequency \n
		Snippet: value: bool = driver.configure.afRf.generator.voip.frequency.get_atm_frequency() \n
		No command help available \n
			:return: atm_frequency: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:GENerator<Instance>:VOIP:FREQuency:ATMFrequency?')
		return Conversions.str_to_bool(response)

	def set_atm_frequency(self, atm_frequency: bool) -> None:
		"""CONFigure:AFRF:GENerator<Instance>:VOIP:FREQuency:ATMFrequency \n
		Snippet: driver.configure.afRf.generator.voip.frequency.set_atm_frequency(atm_frequency = False) \n
		No command help available \n
			:param atm_frequency: No help available
		"""
		param = Conversions.bool_to_str(atm_frequency)
		self._core.io.write(f'CONFigure:AFRF:GENerator<Instance>:VOIP:FREQuency:ATMFrequency {param}')
