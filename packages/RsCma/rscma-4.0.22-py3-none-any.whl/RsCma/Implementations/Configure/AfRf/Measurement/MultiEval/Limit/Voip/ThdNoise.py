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

	def set(self, enable: bool, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:THDNoise \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.voip.thdNoise.set(enable = False, upper = 1.0) \n
		Configures limits for the THD+N results, measured via the VoIP input path. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param upper: Upper THD+N limit Range: 0 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:THDNoise {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThdNoiseStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Upper: float: Upper THD+N limit Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None

	def get(self) -> ThdNoiseStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:THDNoise \n
		Snippet: value: ThdNoiseStruct = driver.configure.afRf.measurement.multiEval.limit.voip.thdNoise.get() \n
		Configures limits for the THD+N results, measured via the VoIP input path. \n
			:return: structure: for return value, see the help for ThdNoiseStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:THDNoise?', self.__class__.ThdNoiseStruct())
