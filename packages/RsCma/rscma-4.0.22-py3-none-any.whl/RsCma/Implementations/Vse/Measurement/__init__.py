from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 87 total commands, 19 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def dmr(self):
		"""dmr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmr'):
			from .Dmr import DmrCls
			self._dmr = DmrCls(self._core, self._cmd_group)
		return self._dmr

	@property
	def nxdn(self):
		"""nxdn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nxdn'):
			from .Nxdn import NxdnCls
			self._nxdn = NxdnCls(self._core, self._cmd_group)
		return self._nxdn

	@property
	def tetra(self):
		"""tetra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tetra'):
			from .Tetra import TetraCls
			self._tetra = TetraCls(self._core, self._cmd_group)
		return self._tetra

	@property
	def dpmr(self):
		"""dpmr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpmr'):
			from .Dpmr import DpmrCls
			self._dpmr = DpmrCls(self._core, self._cmd_group)
		return self._dpmr

	@property
	def lte(self):
		"""lte commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def cons(self):
		"""cons commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cons'):
			from .Cons import ConsCls
			self._cons = ConsCls(self._core, self._cmd_group)
		return self._cons

	@property
	def ediagram(self):
		"""ediagram commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ediagram'):
			from .Ediagram import EdiagramCls
			self._ediagram = EdiagramCls(self._core, self._cmd_group)
		return self._ediagram

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def perror(self):
		"""perror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def evm(self):
		"""evm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	@property
	def ffError(self):
		"""ffError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ffError'):
			from .FfError import FfErrorCls
			self._ffError = FfErrorCls(self._core, self._cmd_group)
		return self._ffError

	@property
	def fdeviation(self):
		"""fdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def fdError(self):
		"""fdError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdError'):
			from .FdError import FdErrorCls
			self._fdError = FdErrorCls(self._core, self._cmd_group)
		return self._fdError

	@property
	def merror(self):
		"""merror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def ptFive(self):
		"""ptFive commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptFive'):
			from .PtFive import PtFiveCls
			self._ptFive = PtFiveCls(self._core, self._cmd_group)
		return self._ptFive

	@property
	def rfCarrier(self):
		"""rfCarrier commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfCarrier'):
			from .RfCarrier import RfCarrierCls
			self._rfCarrier = RfCarrierCls(self._core, self._cmd_group)
		return self._rfCarrier

	@property
	def sdistribute(self):
		"""sdistribute commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdistribute'):
			from .Sdistribute import SdistributeCls
			self._sdistribute = SdistributeCls(self._core, self._cmd_group)
		return self._sdistribute

	@property
	def spectrum(self):
		"""spectrum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	def stop(self) -> None:
		"""STOP:VSE:MEASurement<Instance> \n
		Snippet: driver.vse.measurement.stop() \n
		Pauses the measurement. \n
		"""
		self._core.io.write(f'STOP:VSE:MEASurement<Instance>')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:VSE:MEASurement<Instance> \n
		Snippet: driver.vse.measurement.stop_with_opc() \n
		Pauses the measurement. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:VSE:MEASurement<Instance>', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:VSE:MEASurement<Instance> \n
		Snippet: driver.vse.measurement.abort() \n
		Stops the measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:VSE:MEASurement<Instance>', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
