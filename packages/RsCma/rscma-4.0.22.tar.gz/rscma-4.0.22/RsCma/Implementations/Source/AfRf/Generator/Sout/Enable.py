from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, left: bool, right: bool) -> None:
		"""SOURce:AFRF:GENerator<Instance>:SOUT:ENABle \n
		Snippet: driver.source.afRf.generator.sout.enable.set(left = False, right = False) \n
		Enables or disables the left and right channel of the SPDIF OUT connector. \n
			:param left: OFF | ON
			:param right: OFF | ON
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('left', left, DataType.Boolean), ArgSingle('right', right, DataType.Boolean))
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:SOUT:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Left: bool: OFF | ON
			- 2 Right: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Left'),
			ArgStruct.scalar_bool('Right')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Left: bool = None
			self.Right: bool = None

	def get(self) -> EnableStruct:
		"""SOURce:AFRF:GENerator<Instance>:SOUT:ENABle \n
		Snippet: value: EnableStruct = driver.source.afRf.generator.sout.enable.get() \n
		Enables or disables the left and right channel of the SPDIF OUT connector. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:AFRF:GENerator<Instance>:SOUT:ENABle?', self.__class__.EnableStruct())
