from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IndividualCls:
	"""Individual commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("individual", core, parent)

	def get_dtime(self) -> List[float]:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DTIMe \n
		Snippet: value: List[float] = driver.source.afRf.generator.dialing.fdialing.individual.get_dtime() \n
		Sets individual digit times for digits of the free dialing sequence. \n
			:return: digit_time_array: Comma-separated list of individual digit times of the digits of the dialing sequence Unit: s
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DTIMe?')
		return response

	def set_dtime(self, digit_time_array: List[float]) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DTIMe \n
		Snippet: driver.source.afRf.generator.dialing.fdialing.individual.set_dtime(digit_time_array = [1.1, 2.2, 3.3]) \n
		Sets individual digit times for digits of the free dialing sequence. \n
			:param digit_time_array: Comma-separated list of individual digit times of the digits of the dialing sequence Unit: s
		"""
		param = Conversions.list_to_csv_str(digit_time_array)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DTIMe {param}')

	def get_dpause(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DPAuse \n
		Snippet: value: float = driver.source.afRf.generator.dialing.fdialing.individual.get_dpause() \n
		Common length of the pause between two individual digits of a free dialing sequence. \n
			:return: digit_pause: Range: 0 to 3, Unit: s
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DPAuse?')
		return Conversions.str_to_float(response)

	def set_dpause(self, digit_pause: float) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DPAuse \n
		Snippet: driver.source.afRf.generator.dialing.fdialing.individual.set_dpause(digit_pause = 1.0) \n
		Common length of the pause between two individual digits of a free dialing sequence. \n
			:param digit_pause: Range: 0 to 3, Unit: s
		"""
		param = Conversions.decimal_value_to_str(digit_pause)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:FDIaling:INDividual:DPAuse {param}')
