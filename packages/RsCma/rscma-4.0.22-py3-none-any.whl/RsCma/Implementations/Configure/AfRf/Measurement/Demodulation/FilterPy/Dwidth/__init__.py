from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


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

	def set(self, dwidth_left: enums.PwrFilterType, relative_left: enums.Relative, dwidth_right: enums.PwrFilterType, relative_right: enums.Relative) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FILTer:DWIDth \n
		Snippet: driver.configure.afRf.measurement.demodulation.filterPy.dwidth.set(dwidth_left = enums.PwrFilterType.NARRow, relative_left = enums.Relative.CONStant, dwidth_right = enums.PwrFilterType.NARRow, relative_right = enums.Relative.CONStant) \n
		Configures the bandwidth of the distortion filter in the RF input path. For FM stereo, the settings configure the left
		and the right audio channel. For other modulation types, only the <...Left> settings are relevant. The <...
		Right> settings have no effect. \n
			:param dwidth_left: WIDE | NARRow | UDEF Wide or narrow bandwidth
			:param relative_left: RELative | CONStant Bandwidth proportional to reference frequency or constant
			:param dwidth_right: WIDE | NARRow | UDEF
			:param relative_right: RELative | CONStant
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dwidth_left', dwidth_left, DataType.Enum, enums.PwrFilterType), ArgSingle('relative_left', relative_left, DataType.Enum, enums.Relative), ArgSingle('dwidth_right', dwidth_right, DataType.Enum, enums.PwrFilterType), ArgSingle('relative_right', relative_right, DataType.Enum, enums.Relative))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DEModulation:FILTer:DWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	class DwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Dwidth_Left: enums.PwrFilterType: WIDE | NARRow | UDEF Wide or narrow bandwidth
			- 2 Relative_Left: enums.Relative: RELative | CONStant Bandwidth proportional to reference frequency or constant
			- 3 Dwidth_Right: enums.PwrFilterType: WIDE | NARRow | UDEF
			- 4 Relative_Right: enums.Relative: RELative | CONStant"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Dwidth_Left', enums.PwrFilterType),
			ArgStruct.scalar_enum('Relative_Left', enums.Relative),
			ArgStruct.scalar_enum('Dwidth_Right', enums.PwrFilterType),
			ArgStruct.scalar_enum('Relative_Right', enums.Relative)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dwidth_Left: enums.PwrFilterType = None
			self.Relative_Left: enums.Relative = None
			self.Dwidth_Right: enums.PwrFilterType = None
			self.Relative_Right: enums.Relative = None

	def get(self) -> DwidthStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FILTer:DWIDth \n
		Snippet: value: DwidthStruct = driver.configure.afRf.measurement.demodulation.filterPy.dwidth.get() \n
		Configures the bandwidth of the distortion filter in the RF input path. For FM stereo, the settings configure the left
		and the right audio channel. For other modulation types, only the <...Left> settings are relevant. The <...
		Right> settings have no effect. \n
			:return: structure: for return value, see the help for DwidthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:DEModulation:FILTer:DWIDth?', self.__class__.DwidthStruct())

	def clone(self) -> 'DwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
