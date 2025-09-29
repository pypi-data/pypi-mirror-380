from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Level_Peak: float: Unit: %
			- 3 Level_Rms: float: Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Level_Peak'),
			ArgStruct.scalar_float('Level_Rms')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Level_Peak: float = None
			self.Level_Rms: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:SINRight:LEVel:DELTa:MAXimum \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.spdifRight.level.delta.maximum.fetch() \n
		Query delta results for AF frequency of SPDIF path. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:SINRight:LEVel:DELTa:MAXimum?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:SINRight:LEVel:DELTa:MAXimum \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.spdifRight.level.delta.maximum.read() \n
		Query delta results for AF frequency of SPDIF path. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:MEValuation:SINRight:LEVel:DELTa:MAXimum?', self.__class__.ResultData())
