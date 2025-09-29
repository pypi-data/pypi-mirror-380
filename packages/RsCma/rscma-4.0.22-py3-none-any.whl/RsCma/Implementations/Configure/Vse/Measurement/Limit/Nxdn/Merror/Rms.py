from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmsCls:
	"""Rms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def set(self, enable: bool, limit: float) -> None:
		"""CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:MERRor:RMS \n
		Snippet: driver.configure.vse.measurement.limit.nxdn.merror.rms.set(enable = False, limit = 1.0) \n
		Configures an upper limit for the measured 'RMS' value of the magnitude error for the digital standard 'NXDN'. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param limit: Upper magnitude error limit for 'RMS' value Range: 0 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('limit', limit, DataType.Float))
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:MERRor:RMS {param}'.rstrip())

	# noinspection PyTypeChecker
	class RmsStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Limit: float: Upper magnitude error limit for 'RMS' value Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get(self) -> RmsStruct:
		"""CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:MERRor:RMS \n
		Snippet: value: RmsStruct = driver.configure.vse.measurement.limit.nxdn.merror.rms.get() \n
		Configures an upper limit for the measured 'RMS' value of the magnitude error for the digital standard 'NXDN'. \n
			:return: structure: for return value, see the help for RmsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:MERRor:RMS?', self.__class__.RmsStruct())
