from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakCls:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, enable: bool, limit: float) -> None:
		"""CONFigure:VSE:MEASurement<Instance>:LIMit:DPMR:FFERor:PEAK \n
		Snippet: driver.configure.vse.measurement.limit.dpmr.ffError.peak.set(enable = False, limit = 1.0) \n
		Configures an upper limit for the measured peak value of the FSK frequency error for the digital standard 'DPMR'. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param limit: Upper FSK frequency error limit for peak value Range: 0 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('limit', limit, DataType.Float))
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:LIMit:DPMR:FFERor:PEAK {param}'.rstrip())

	# noinspection PyTypeChecker
	class PeakStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Limit: float: Upper FSK frequency error limit for peak value Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get(self) -> PeakStruct:
		"""CONFigure:VSE:MEASurement<Instance>:LIMit:DPMR:FFERor:PEAK \n
		Snippet: value: PeakStruct = driver.configure.vse.measurement.limit.dpmr.ffError.peak.get() \n
		Configures an upper limit for the measured peak value of the FSK frequency error for the digital standard 'DPMR'. \n
			:return: structure: for return value, see the help for PeakStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:VSE:MEASurement<Instance>:LIMit:DPMR:FFERor:PEAK?', self.__class__.PeakStruct())
