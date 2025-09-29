from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, gen_control: bool) -> None:
		"""SOURce:XRT:GENerator<Instance>:STATe \n
		Snippet: driver.source.xrt.generator.state.set(gen_control = False) \n
		Starts and stops the XRT100 generator. \n
			:param gen_control: ON | OFF ON Starts the generator. OFF Stops the generator.
		"""
		param = Conversions.bool_to_str(gen_control)
		self._core.io.write_with_opc(f'SOURce:XRT:GENerator<Instance>:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GeneratorState:
		"""SOURce:XRT:GENerator<Instance>:STATe \n
		Snippet: value: enums.GeneratorState = driver.source.xrt.generator.state.get() \n
		Starts and stops the XRT100 generator. \n
			:return: gen_state: OFF | ON | PENDing OFF Generator is off. ON Generator is running. PENDing Start or stop of the generator is ongoing."""
		response = self._core.io.query_str_with_opc(f'SOURce:XRT:GENerator<Instance>:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.GeneratorState)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.GeneratorState]:
		"""SOURce:XRT:GENerator<Instance>:STATe:ALL \n
		Snippet: value: List[enums.GeneratorState] = driver.source.xrt.generator.state.get_all() \n
		Queries all states of the XRT100 generator. \n
			:return: all_states: OFF | ON | PENDing
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:STATe:ALL?')
		return Conversions.str_to_list_enum(response, enums.GeneratorState)
