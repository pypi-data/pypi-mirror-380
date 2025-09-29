from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 248 total commands, 24 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import ReliabilityCls
			self._reliability = ReliabilityCls(self._core, self._cmd_group)
		return self._reliability

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def digital(self):
		"""digital commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_digital'):
			from .Digital import DigitalCls
			self._digital = DigitalCls(self._core, self._cmd_group)
		return self._digital

	@property
	def dmr(self):
		"""dmr commands group. 0 Sub-classes, 10 commands."""
		if not hasattr(self, '_dmr'):
			from .Dmr import DmrCls
			self._dmr = DmrCls(self._core, self._cmd_group)
		return self._dmr

	@property
	def nxdn(self):
		"""nxdn commands group. 0 Sub-classes, 11 commands."""
		if not hasattr(self, '_nxdn'):
			from .Nxdn import NxdnCls
			self._nxdn = NxdnCls(self._core, self._cmd_group)
		return self._nxdn

	@property
	def pocsag(self):
		"""pocsag commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_pocsag'):
			from .Pocsag import PocsagCls
			self._pocsag = PocsagCls(self._core, self._cmd_group)
		return self._pocsag

	@property
	def ptFive(self):
		"""ptFive commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_ptFive'):
			from .PtFive import PtFiveCls
			self._ptFive = PtFiveCls(self._core, self._cmd_group)
		return self._ptFive

	@property
	def userDefined(self):
		"""userDefined commands group. 0 Sub-classes, 14 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def zigbee(self):
		"""zigbee commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_zigbee'):
			from .Zigbee import ZigbeeCls
			self._zigbee = ZigbeeCls(self._core, self._cmd_group)
		return self._zigbee

	@property
	def dpmr(self):
		"""dpmr commands group. 1 Sub-classes, 11 commands."""
		if not hasattr(self, '_dpmr'):
			from .Dpmr import DpmrCls
			self._dpmr = DpmrCls(self._core, self._cmd_group)
		return self._dpmr

	@property
	def voip(self):
		"""voip commands group. 4 Sub-classes, 7 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def adelay(self):
		"""adelay commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adelay'):
			from .Adelay import AdelayCls
			self._adelay = AdelayCls(self._core, self._cmd_group)
		return self._adelay

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 9 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def modulator(self):
		"""modulator commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_modulator'):
			from .Modulator import ModulatorCls
			self._modulator = ModulatorCls(self._core, self._cmd_group)
		return self._modulator

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def internalGenerator(self):
		"""internalGenerator commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_internalGenerator'):
			from .InternalGenerator import InternalGeneratorCls
			self._internalGenerator = InternalGeneratorCls(self._core, self._cmd_group)
		return self._internalGenerator

	@property
	def dialing(self):
		"""dialing commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dialing'):
			from .Dialing import DialingCls
			self._dialing = DialingCls(self._core, self._cmd_group)
		return self._dialing

	@property
	def audioInput(self):
		"""audioInput commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def audioOutput(self):
		"""audioOutput commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_audioOutput'):
			from .AudioOutput import AudioOutputCls
			self._audioOutput = AudioOutputCls(self._core, self._cmd_group)
		return self._audioOutput

	@property
	def sout(self):
		"""sout commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sout'):
			from .Sout import SoutCls
			self._sout = SoutCls(self._core, self._cmd_group)
		return self._sout

	@property
	def tones(self):
		"""tones commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_tones'):
			from .Tones import TonesCls
			self._tones = TonesCls(self._core, self._cmd_group)
		return self._tones

	@property
	def cdefinition(self):
		"""cdefinition commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_cdefinition'):
			from .Cdefinition import CdefinitionCls
			self._cdefinition = CdefinitionCls(self._core, self._cmd_group)
		return self._cdefinition

	@property
	def arb(self):
		"""arb commands group. 3 Sub-classes, 6 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import ArbCls
			self._arb = ArbCls(self._core, self._cmd_group)
		return self._arb

	@property
	def interferer(self):
		"""interferer commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_interferer'):
			from .Interferer import InterfererCls
			self._interferer = InterfererCls(self._core, self._cmd_group)
		return self._interferer

	# noinspection PyTypeChecker
	def get_dsource(self) -> enums.DigitalSource:
		"""SOURce:AFRF:GENerator<Instance>:DSOurce \n
		Snippet: value: enums.DigitalSource = driver.source.afRf.generator.get_dsource() \n
		Selects the data source for digital scenarios. \n
			:return: dsource: DMR | ARB | NXDN | POCSag | P25 | UDEFined | ZIGBee | DPMR
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.DigitalSource)

	def set_dsource(self, dsource: enums.DigitalSource) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DSOurce \n
		Snippet: driver.source.afRf.generator.set_dsource(dsource = enums.DigitalSource.ARB) \n
		Selects the data source for digital scenarios. \n
			:param dsource: DMR | ARB | NXDN | POCSag | P25 | UDEFined | ZIGBee | DPMR
		"""
		param = Conversions.enum_scalar_to_str(dsource, enums.DigitalSource)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DSOurce {param}')

	# noinspection PyTypeChecker
	def get_mscheme(self) -> enums.ModulationScheme:
		"""SOURce:AFRF:GENerator<Instance>:MSCHeme \n
		Snippet: value: enums.ModulationScheme = driver.source.afRf.generator.get_mscheme() \n
		Selects the RF signal mode (modulation scheme) for analog scenarios. \n
			:return: mod_scheme: FMSTereo | FM | AM | USB | LSB | PM | CW | ARB FMSTereo FM stereo multiplex signal FM, PM, AM Frequency / phase / amplitude modulation USB, LSB Single sideband modulation, upper / lower sideband CW Constant wave signal (unmodulated RF carrier) ARB Waveform file (ARB file)
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:MSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationScheme)

	def set_mscheme(self, mod_scheme: enums.ModulationScheme) -> None:
		"""SOURce:AFRF:GENerator<Instance>:MSCHeme \n
		Snippet: driver.source.afRf.generator.set_mscheme(mod_scheme = enums.ModulationScheme.AM) \n
		Selects the RF signal mode (modulation scheme) for analog scenarios. \n
			:param mod_scheme: FMSTereo | FM | AM | USB | LSB | PM | CW | ARB FMSTereo FM stereo multiplex signal FM, PM, AM Frequency / phase / amplitude modulation USB, LSB Single sideband modulation, upper / lower sideband CW Constant wave signal (unmodulated RF carrier) ARB Waveform file (ARB file)
		"""
		param = Conversions.enum_scalar_to_str(mod_scheme, enums.ModulationScheme)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:MSCHeme {param}')

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
