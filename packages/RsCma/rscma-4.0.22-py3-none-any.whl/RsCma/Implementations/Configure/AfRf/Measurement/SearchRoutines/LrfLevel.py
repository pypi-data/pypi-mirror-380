from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrfLevelCls:
	"""LrfLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrfLevel", core, parent)

	def set(self, enabled: bool, min_level: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:LRFLevel \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.lrfLevel.set(enabled = False, min_level = 1.0) \n
		Configures the minimum RF level for the signal generator. \n
			:param enabled: OFF | ON
			:param min_level: Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enabled', enabled, DataType.Boolean), ArgSingle('min_level', min_level, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LRFLevel {param}'.rstrip())

	# noinspection PyTypeChecker
	class LrfLevelStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enabled: bool: OFF | ON
			- 2 Min_Level: float: Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enabled'),
			ArgStruct.scalar_float('Min_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enabled: bool = None
			self.Min_Level: float = None

	def get(self) -> LrfLevelStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:LRFLevel \n
		Snippet: value: LrfLevelStruct = driver.configure.afRf.measurement.searchRoutines.lrfLevel.get() \n
		Configures the minimum RF level for the signal generator. \n
			:return: structure: for return value, see the help for LrfLevelStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LRFLevel?', self.__class__.LrfLevelStruct())
