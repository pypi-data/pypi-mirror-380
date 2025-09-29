from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtFiveCls:
	"""PtFive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptFive", core, parent)

	# noinspection PyTypeChecker
	def get_ptype(self) -> enums.PayloadType:
		"""CONFigure:AFRF:MEASurement<Instance>:DIGital:PTFive:PTYPe \n
		Snippet: value: enums.PayloadType = driver.configure.afRf.measurement.digital.ptFive.get_ptype() \n
		Defines the payload type for P25 digital standard. \n
			:return: payload_type: P1011 | SILence 1011 Audio tone with a frequency of 1011 Hz. SILence The payload contains silence.
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DIGital:PTFive:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadType)
