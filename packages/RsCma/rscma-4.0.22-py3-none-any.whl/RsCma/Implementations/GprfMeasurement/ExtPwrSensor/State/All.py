from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.ResourceState]:
		"""FETCh:GPRF:MEASurement<Instance>:EPSensor:STATe:ALL \n
		Snippet: value: List[enums.ResourceState] = driver.gprfMeasurement.extPwrSensor.state.all.fetch() \n
		Queries the main EPS measurement state and all substates. The substates provide additional information for the main state
		RUN. \n
			:return: meas_state: No help available"""
		response = self._core.io.query_str(f'FETCh:GPRF:MEASurement<Instance>:EPSensor:STATe:ALL?')
		return Conversions.str_to_list_enum(response, enums.ResourceState)
