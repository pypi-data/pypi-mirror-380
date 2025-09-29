from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 3 total commands, 1 Subgroups, 2 group commands
	Repeated Capability: FrequencyLobe, default value after init: FrequencyLobe.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_frequencyLobe_get', 'repcap_frequencyLobe_set', repcap.FrequencyLobe.Nr1)

	def repcap_frequencyLobe_set(self, frequencyLobe: repcap.FrequencyLobe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FrequencyLobe.Default.
		Default value after init: FrequencyLobe.Nr1"""
		self._cmd_group.set_repcap_enum_value(frequencyLobe)

	def repcap_frequencyLobe_get(self) -> repcap.FrequencyLobe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dtone(self):
		"""dtone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import DtoneCls
			self._dtone = DtoneCls(self._core, self._cmd_group)
		return self._dtone

	def get_stone(self) -> List[float]:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:STONe \n
		Snippet: value: List[float] = driver.configure.afRf.measurement.multiEval.tones.fdialing.frequency.get_stone() \n
		Assigns single-tone frequencies to digits, for analysis of free-dialing tone sequences. \n
			:return: tones_frequency: Comma-separated list of 16 frequencies, assigned to the digits 0, 1, ..., 9, A, ..., F Specifying fewer frequencies leaves the remaining digits unchanged. Range: 60 Hz to 4000 Hz, Unit: Hz
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:STONe?')
		return response

	def set_stone(self, tones_frequency: List[float]) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:STONe \n
		Snippet: driver.configure.afRf.measurement.multiEval.tones.fdialing.frequency.set_stone(tones_frequency = [1.1, 2.2, 3.3]) \n
		Assigns single-tone frequencies to digits, for analysis of free-dialing tone sequences. \n
			:param tones_frequency: Comma-separated list of 16 frequencies, assigned to the digits 0, 1, ..., 9, A, ..., F Specifying fewer frequencies leaves the remaining digits unchanged. Range: 60 Hz to 4000 Hz, Unit: Hz
		"""
		param = Conversions.list_to_csv_str(tones_frequency)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:STONe {param}')

	# noinspection PyTypeChecker
	def get_range(self) -> enums.Bandwidth:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:RANGe \n
		Snippet: value: enums.Bandwidth = driver.configure.afRf.measurement.multiEval.tones.fdialing.frequency.get_range() \n
		Sets the frequency range of the lowpass filter and bandpass filter for a free dialing dual-tone measurement as in table
		Table 'Frequency range and measurement filters'. \n
			:return: bandwidth: FR1K | FR1K1 | FR1K2 | FR1K3 | FR1K4 FR1K Frequency range 1.0 kHz FR1K1 | FR1K2 | FR1K3 | FR1K4 Frequency ranges 1.1 kHz to 1.4 kHz
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:RANGe?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)

	def set_range(self, bandwidth: enums.Bandwidth) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:RANGe \n
		Snippet: driver.configure.afRf.measurement.multiEval.tones.fdialing.frequency.set_range(bandwidth = enums.Bandwidth.FR1K) \n
		Sets the frequency range of the lowpass filter and bandpass filter for a free dialing dual-tone measurement as in table
		Table 'Frequency range and measurement filters'. \n
			:param bandwidth: FR1K | FR1K1 | FR1K2 | FR1K3 | FR1K4 FR1K Frequency range 1.0 kHz FR1K1 | FR1K2 | FR1K3 | FR1K4 Frequency ranges 1.1 kHz to 1.4 kHz
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.Bandwidth)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:FDIaling:FREQuency:RANGe {param}')

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
