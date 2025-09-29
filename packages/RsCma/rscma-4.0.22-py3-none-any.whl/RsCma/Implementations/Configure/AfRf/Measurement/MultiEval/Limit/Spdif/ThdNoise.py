from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThdNoiseCls:
	"""ThdNoise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thdNoise", core, parent)

	def set(self, enable_left: bool, upper_left: float, enable_right: bool, upper_right: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:SIN:THDNoise \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.spdif.thdNoise.set(enable_left = False, upper_left = 1.0, enable_right = False, upper_right = 1.0) \n
		Configures limits for the THD+N results, measured via the SPDIF input path. \n
			:param enable_left: OFF | ON Enables or disables the limit check for the left SPDIF channel
			:param upper_left: Upper THD+N limit for the left SPDIF channel Range: 0.001 % to 100 %, Unit: %
			:param enable_right: OFF | ON Enables or disables the limit check for the right SPDIF channel
			:param upper_right: Upper THD+N limit for the right SPDIF channel Range: 0.001 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_left', enable_left, DataType.Boolean), ArgSingle('upper_left', upper_left, DataType.Float), ArgSingle('enable_right', enable_right, DataType.Boolean), ArgSingle('upper_right', upper_right, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:SIN:THDNoise {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThdNoiseStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable_Left: bool: OFF | ON Enables or disables the limit check for the left SPDIF channel
			- 2 Upper_Left: float: Upper THD+N limit for the left SPDIF channel Range: 0.001 % to 100 %, Unit: %
			- 3 Enable_Right: bool: OFF | ON Enables or disables the limit check for the right SPDIF channel
			- 4 Upper_Right: float: Upper THD+N limit for the right SPDIF channel Range: 0.001 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Left'),
			ArgStruct.scalar_float('Upper_Left'),
			ArgStruct.scalar_bool('Enable_Right'),
			ArgStruct.scalar_float('Upper_Right')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Left: bool = None
			self.Upper_Left: float = None
			self.Enable_Right: bool = None
			self.Upper_Right: float = None

	def get(self) -> ThdNoiseStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:SIN:THDNoise \n
		Snippet: value: ThdNoiseStruct = driver.configure.afRf.measurement.multiEval.limit.spdif.thdNoise.get() \n
		Configures limits for the THD+N results, measured via the SPDIF input path. \n
			:return: structure: for return value, see the help for ThdNoiseStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:SIN:THDNoise?', self.__class__.ThdNoiseStruct())
