from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DwidthCls:
	"""Dwidth commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwidth", core, parent)

	@property
	def sfactor(self):
		"""sfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfactor'):
			from .Sfactor import SfactorCls
			self._sfactor = SfactorCls(self._core, self._cmd_group)
		return self._sfactor

	def set(self, dwidth: enums.PwrFilterType, relative: enums.Relative, audioInput=repcap.AudioInput.Default) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:FILTer:DWIDth \n
		Snippet: driver.configure.afRf.measurement.audioInput.filterPy.dwidth.set(dwidth = enums.PwrFilterType.NARRow, relative = enums.Relative.CONStant, audioInput = repcap.AudioInput.Default) \n
		Configures the bandwidth of the distortion filter in an AF input path. \n
			:param dwidth: WIDE | NARRow | UDEF Wide, narrow or user-defined bandwidth
			:param relative: RELative | CONStant Bandwidth proportional to reference frequency or constant
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dwidth', dwidth, DataType.Enum, enums.PwrFilterType), ArgSingle('relative', relative, DataType.Enum, enums.Relative))
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:FILTer:DWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	class DwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Dwidth: enums.PwrFilterType: WIDE | NARRow | UDEF Wide, narrow or user-defined bandwidth
			- 2 Relative: enums.Relative: RELative | CONStant Bandwidth proportional to reference frequency or constant"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Dwidth', enums.PwrFilterType),
			ArgStruct.scalar_enum('Relative', enums.Relative)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dwidth: enums.PwrFilterType = None
			self.Relative: enums.Relative = None

	def get(self, audioInput=repcap.AudioInput.Default) -> DwidthStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:FILTer:DWIDth \n
		Snippet: value: DwidthStruct = driver.configure.afRf.measurement.audioInput.filterPy.dwidth.get(audioInput = repcap.AudioInput.Default) \n
		Configures the bandwidth of the distortion filter in an AF input path. \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: structure: for return value, see the help for DwidthStruct structure arguments."""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:FILTer:DWIDth?', self.__class__.DwidthStruct())

	def clone(self) -> 'DwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
