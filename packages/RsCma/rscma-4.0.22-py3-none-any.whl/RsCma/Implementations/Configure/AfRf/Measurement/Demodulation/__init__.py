from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodulationCls:
	"""Demodulation commands group definition. 36 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodulation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmStereo(self):
		"""fmStereo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmStereo'):
			from .FmStereo import FmStereoCls
			self._fmStereo = FmStereoCls(self._core, self._cmd_group)
		return self._fmStereo

	@property
	def modDepth(self):
		"""modDepth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modDepth'):
			from .ModDepth import ModDepthCls
			self._modDepth = ModDepthCls(self._core, self._cmd_group)
		return self._modDepth

	@property
	def fdeviation(self):
		"""fdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def gcoupling(self):
		"""gcoupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gcoupling'):
			from .Gcoupling import GcouplingCls
			self._gcoupling = GcouplingCls(self._core, self._cmd_group)
		return self._gcoupling

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmode'):
			from .Tmode import TmodeCls
			self._tmode = TmodeCls(self._core, self._cmd_group)
		return self._tmode

	@property
	def filterPy(self):
		"""filterPy commands group. 4 Sub-classes, 6 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Demodulation:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation \n
		Snippet: value: enums.Demodulation = driver.configure.afRf.measurement.demodulation.get_value() \n
		Selects the type of demodulation to be performed. \n
			:return: demodulation: FMSTereo | FM | AM | USB | LSB | PM FMSTereo FM stereo multiplex signal FM, PM, AM Frequency / phase / amplitude modulation USB, LSB Single sideband modulation, upper / lower sideband
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DEModulation?')
		return Conversions.str_to_scalar_enum(response, enums.Demodulation)

	def set_value(self, demodulation: enums.Demodulation) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation \n
		Snippet: driver.configure.afRf.measurement.demodulation.set_value(demodulation = enums.Demodulation.AM) \n
		Selects the type of demodulation to be performed. \n
			:param demodulation: FMSTereo | FM | AM | USB | LSB | PM FMSTereo FM stereo multiplex signal FM, PM, AM Frequency / phase / amplitude modulation USB, LSB Single sideband modulation, upper / lower sideband
		"""
		param = Conversions.enum_scalar_to_str(demodulation, enums.Demodulation)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DEModulation {param}')

	def clone(self) -> 'DemodulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
