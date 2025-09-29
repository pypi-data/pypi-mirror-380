from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmsCls:
	"""Rms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def set(self, enable: bool, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:FDEViation:RMS \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.demodulation.fdeviation.rms.set(enable = False, upper = 1.0) \n
		Configures a limit for the 'RMS' frequency deviation results, measured for FM. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param upper: Upper frequency deviation limit Range: 0 Hz to 100 kHz, Unit: Hz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:FDEViation:RMS {param}'.rstrip())

	# noinspection PyTypeChecker
	class RmsStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Upper: float: Upper frequency deviation limit Range: 0 Hz to 100 kHz, Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None

	def get(self) -> RmsStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:FDEViation:RMS \n
		Snippet: value: RmsStruct = driver.configure.afRf.measurement.multiEval.limit.demodulation.fdeviation.rms.get() \n
		Configures a limit for the 'RMS' frequency deviation results, measured for FM. \n
			:return: structure: for return value, see the help for RmsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:FDEViation:RMS?', self.__class__.RmsStruct())
