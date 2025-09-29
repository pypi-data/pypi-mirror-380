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
			- 2 Frequency: float: Frequency of the measured AF signal Unit: Hz
			- 3 Level: float: Effective level of the AC component of the measured AF signal Unit: V
			- 4 Dc_Level: float: Level of the DC component of the measured AF signal (input coupling DC required) Unit: V"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Dc_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Frequency: float = None
			self.Level: float = None
			self.Dc_Level: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:AIN:FIRSt:AFSignal:MAXimum \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.audioInput.first.afSignal.maximum.fetch() \n
		Query the AF frequency and level results measured for an AF input path. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:AIN:FIRSt:AFSignal:MAXimum?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:AIN:FIRSt:AFSignal:MAXimum \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.audioInput.first.afSignal.maximum.read() \n
		Query the AF frequency and level results measured for an AF input path. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:MEValuation:AIN:FIRSt:AFSignal:MAXimum?', self.__class__.ResultData())
