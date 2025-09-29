from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApplicationCls:
	"""Application commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("application", core, parent)

	# noinspection PyTypeChecker
	def get_select(self) -> enums.SubTabDigitalMeas:
		"""DISPlay:AFRF:MEASurement<Instance>:DIGital:APPLication:SELect \n
		Snippet: value: enums.SubTabDigitalMeas = driver.display.afRf.measurement.digital.application.get_select() \n
		Selects the subtab to display in the 'Digital' tab. \n
			:return: sub_tab: OVERview | SINFo | BER OVERview 'Overview' subtab SINFo 'Signal Info' subtab BER 'BER' subtab
		"""
		response = self._core.io.query_str('DISPlay:AFRF:MEASurement<Instance>:DIGital:APPLication:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.SubTabDigitalMeas)

	def set_select(self, sub_tab: enums.SubTabDigitalMeas) -> None:
		"""DISPlay:AFRF:MEASurement<Instance>:DIGital:APPLication:SELect \n
		Snippet: driver.display.afRf.measurement.digital.application.set_select(sub_tab = enums.SubTabDigitalMeas.BER) \n
		Selects the subtab to display in the 'Digital' tab. \n
			:param sub_tab: OVERview | SINFo | BER OVERview 'Overview' subtab SINFo 'Signal Info' subtab BER 'BER' subtab
		"""
		param = Conversions.enum_scalar_to_str(sub_tab, enums.SubTabDigitalMeas)
		self._core.io.write(f'DISPlay:AFRF:MEASurement<Instance>:DIGital:APPLication:SELect {param}')
