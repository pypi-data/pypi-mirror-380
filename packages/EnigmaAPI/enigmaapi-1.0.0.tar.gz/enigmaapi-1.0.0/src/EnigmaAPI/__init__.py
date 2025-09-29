import ctypes
import sys
import platform
from ctypes import c_bool, c_int, c_char_p, c_wchar_p, POINTER, Structure, c_ulong


def is_executable_64bit(executable_path=None):
    if executable_path is None:
        executable_path = sys.executable
    arch, _ = platform.architecture(executable_path)
    return arch == "64bit"

# 自动选择 DLL
if is_executable_64bit():
    dll_name = "enigma_ide64.dll"
else:
    dll_name = "enigma_ide.dll"

try:
    enigma = ctypes.WinDLL(dll_name)
    print(f"已加载 {dll_name}")
except OSError as e:
    raise RuntimeError(f"无法加载 DLL: {dll_name}") from e


# --------------------
# 常量
# --------------------
NUMBER_OF_CRYPTED_SECTIONS = 16  # 按官方定义

# --------------------
# 结构体
# --------------------
class TKeyInformation(Structure):
    _fields_ = [
        ("Stolen", c_bool),
        ("CreationYear", c_ulong),
        ("CreationMonth", c_ulong),
        ("CreationDay", c_ulong),
        ("UseKeyExpiration", c_bool),
        ("ExpirationYear", c_ulong),
        ("ExpirationMonth", c_ulong),
        ("ExpirationDay", c_ulong),
        ("UseHardwareLocking", c_bool),
        ("UseExecutionsLimit", c_bool),
        ("ExecutionsCount", c_ulong),
        ("UseDaysLimit", c_bool),
        ("DaysCount", c_ulong),
        ("UseRunTimeLimit", c_bool),
        ("RunTimeMinutes", c_ulong),
        ("UseGlobalTimeLimit", c_bool),
        ("GlobalTimeMinutes", c_ulong),
        ("UseCountyLimit", c_bool),
        ("CountryCode", c_ulong),
        ("UseRegisterAfter", c_bool),
        ("RegisterAfterYear", c_ulong),
        ("RegisterAfterMonth", c_ulong),
        ("RegisterAfterDay", c_ulong),
        ("UseRegisterBefore", c_bool),
        ("RegisterBeforeYear", c_ulong),
        ("RegisterBeforeMonth", c_ulong),
        ("RegisterBeforeDay", c_ulong),
        ("EncryptedSections", c_bool * NUMBER_OF_CRYPTED_SECTIONS)
    ]

PKeyInformation = POINTER(TKeyInformation)

# --------------------
# 注册 API 包装
# --------------------

# 基本注册检查/保存
enigma.EP_RegCheckKey.argtypes = [c_char_p, c_char_p]
enigma.EP_RegCheckKey.restype = c_bool
enigma.EP_RegCheckKeyA.argtypes = [c_char_p, c_char_p]
enigma.EP_RegCheckKeyA.restype = c_bool
enigma.EP_RegCheckKeyW.argtypes = [c_wchar_p, c_wchar_p]
enigma.EP_RegCheckKeyW.restype = c_bool

enigma.EP_RegCheckAndSaveKey.argtypes = [c_char_p, c_char_p]
enigma.EP_RegCheckAndSaveKey.restype = c_bool
enigma.EP_RegCheckAndSaveKeyA.argtypes = [c_char_p, c_char_p]
enigma.EP_RegCheckAndSaveKeyA.restype = c_bool
enigma.EP_RegCheckAndSaveKeyW.argtypes = [c_wchar_p, c_wchar_p]
enigma.EP_RegCheckAndSaveKeyW.restype = c_bool

enigma.EP_RegDeleteKey.argtypes = []
enigma.EP_RegDeleteKey.restype = c_bool

enigma.EP_RegHardwareID.argtypes = []
enigma.EP_RegHardwareID.restype = c_char_p
enigma.EP_RegHardwareIDA.argtypes = []
enigma.EP_RegHardwareIDA.restype = c_char_p
enigma.EP_RegHardwareIDW.argtypes = []
enigma.EP_RegHardwareIDW.restype = c_wchar_p

enigma.EP_RegSaveKey.argtypes = [c_char_p, c_char_p]
enigma.EP_RegSaveKey.restype = c_bool
enigma.EP_RegSaveKeyA.argtypes = [c_char_p, c_char_p]
enigma.EP_RegSaveKeyA.restype = c_bool
enigma.EP_RegSaveKeyW.argtypes = [c_wchar_p, c_wchar_p]
enigma.EP_RegSaveKeyW.restype = c_bool

enigma.EP_RegLoadAndCheckKey.argtypes = []
enigma.EP_RegLoadAndCheckKey.restype = c_bool

enigma.EP_RegShowDialog.argtypes = []
enigma.EP_RegShowDialog.restype = None

# --------------------
# 注册日期/执行/天数/时间 API
# --------------------
enigma.EP_RegKeyCreationDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyCreationDate.restype = c_bool
enigma.EP_RegKeyCreationDateEx.argtypes = []
enigma.EP_RegKeyCreationDateEx.restype = c_int

enigma.EP_RegKeyExpirationDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyExpirationDate.restype = c_bool
enigma.EP_RegKeyExpirationDateEx.argtypes = []
enigma.EP_RegKeyExpirationDateEx.restype = c_int

enigma.EP_RegKeyExecutions.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyExecutions.restype = c_bool
enigma.EP_RegKeyExecutionsLeft.argtypes = []
enigma.EP_RegKeyExecutionsLeft.restype = c_int
enigma.EP_RegKeyExecutionsTotal.argtypes = []
enigma.EP_RegKeyExecutionsTotal.restype = c_int

enigma.EP_RegKeyDays.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyDays.restype = c_bool
enigma.EP_RegKeyDaysLeft.argtypes = []
enigma.EP_RegKeyDaysLeft.restype = c_int
enigma.EP_RegKeyDaysTotal.argtypes = []
enigma.EP_RegKeyDaysTotal.restype = c_int

enigma.EP_RegKeyRuntime.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyRuntime.restype = c_bool
enigma.EP_RegKeyRuntimeLeft.argtypes = []
enigma.EP_RegKeyRuntimeLeft.restype = c_int
enigma.EP_RegKeyRuntimeTotal.argtypes = []
enigma.EP_RegKeyRuntimeTotal.restype = c_int

enigma.EP_RegKeyGlobalTime.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyGlobalTime.restype = c_bool
enigma.EP_RegKeyGlobalTimeLeft.argtypes = []
enigma.EP_RegKeyGlobalTimeLeft.restype = c_int
enigma.EP_RegKeyGlobalTimeTotal.argtypes = []
enigma.EP_RegKeyGlobalTimeTotal.restype = c_int

enigma.EP_RegKeyRegisterAfterDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyRegisterAfterDate.restype = c_bool
enigma.EP_RegKeyRegisterAfterDateEx.argtypes = []
enigma.EP_RegKeyRegisterAfterDateEx.restype = c_int

enigma.EP_RegKeyRegisterBeforeDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_RegKeyRegisterBeforeDate.restype = c_bool
enigma.EP_RegKeyRegisterBeforeDateEx.argtypes = []
enigma.EP_RegKeyRegisterBeforeDateEx.restype = c_int

enigma.EP_RegKeyStatus.argtypes = []
enigma.EP_RegKeyStatus.restype = c_int

# --------------------
# EP_RegKeyInformation 系列
# --------------------
enigma.EP_RegKeyInformation.argtypes = [c_char_p, c_char_p, PKeyInformation]
enigma.EP_RegKeyInformation.restype = c_bool
enigma.EP_RegKeyInformationA.argtypes = [c_char_p, c_char_p, PKeyInformation]
enigma.EP_RegKeyInformationA.restype = c_bool
enigma.EP_RegKeyInformationW.argtypes = [c_wchar_p, c_wchar_p, PKeyInformation]
enigma.EP_RegKeyInformationW.restype = c_bool

# --------------------
# EP_RegKeySection 系列
# --------------------
for i in range(1, 17):
    fn_name = f"EP_RegKeySection{i}" if i > 1 else "EP_RegKeySection"
    fn = getattr(enigma, fn_name)
    fn.argtypes = []
    fn.restype = c_bool

enigma.EP_RegKeySections.argtypes = []
enigma.EP_RegKeySections.restype = c_int

# Trial / demo functions
enigma.EP_TrialExecutions.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_TrialExecutions.restype = c_bool
enigma.EP_TrialExecutionsLeft.argtypes = []
enigma.EP_TrialExecutionsLeft.restype = c_int
enigma.EP_TrialExecutionsTotal.argtypes = []
enigma.EP_TrialExecutionsTotal.restype = c_int

enigma.EP_TrialDays.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_TrialDays.restype = c_bool
enigma.EP_TrialDaysLeft.argtypes = []
enigma.EP_TrialDaysLeft.restype = c_int
enigma.EP_TrialDaysTotal.argtypes = []
enigma.EP_TrialDaysTotal.restype = c_int

enigma.EP_TrialExpirationDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_TrialExpirationDate.restype = c_bool
enigma.EP_TrialExpirationDateEx.argtypes = []
enigma.EP_TrialExpirationDateEx.restype = c_int

enigma.EP_TrialDateTillDate.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
enigma.EP_TrialDateTillDate.restype = c_bool
enigma.EP_TrialDateTillDateStartEx.argtypes = []
enigma.EP_TrialDateTillDateStartEx.restype = c_int
enigma.EP_TrialDateTillDateEndEx.argtypes = []
enigma.EP_TrialDateTillDateEndEx.restype = c_int

enigma.EP_TrialExecutionTime.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_TrialExecutionTime.restype = c_bool
enigma.EP_TrialExecutionTimeLeft.argtypes = []
enigma.EP_TrialExecutionTimeLeft.restype = c_int
enigma.EP_TrialExecutionTimeTotal.argtypes = []
enigma.EP_TrialExecutionTimeTotal.restype = c_int

# Crypt functions
enigma.EP_CryptDecryptBuffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte), c_int, c_char_p]
enigma.EP_CryptDecryptBuffer.restype = None
enigma.EP_CryptDecryptBufferEx.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), c_int, ctypes.POINTER(ctypes.c_ubyte), c_int]
enigma.EP_CryptDecryptBufferEx.restype = None
enigma.EP_CryptEncryptBuffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte), c_int, c_char_p]
enigma.EP_CryptEncryptBuffer.restype = None
enigma.EP_CryptEncryptBufferEx.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), c_int, ctypes.POINTER(ctypes.c_ubyte), c_int]
enigma.EP_CryptEncryptBufferEx.restype = None
enigma.EP_CryptHashBuffer.argtypes = [c_int, ctypes.POINTER(ctypes.c_ubyte), c_int, ctypes.POINTER(ctypes.c_ubyte)]
enigma.EP_CryptHashBuffer.restype = c_int
enigma.EP_CryptHashFileA.argtypes = [c_int, c_char_p, ctypes.POINTER(ctypes.c_ubyte)]
enigma.EP_CryptHashFileA.restype = c_int
enigma.EP_CryptHashFileW.argtypes = [c_int, c_wchar_p, ctypes.POINTER(ctypes.c_ubyte)]
enigma.EP_CryptHashFileW.restype = c_int
enigma.EP_CryptHashStringA.argtypes = [c_int, c_char_p, ctypes.POINTER(ctypes.c_ubyte)]
enigma.EP_CryptHashStringA.restype = c_int
enigma.EP_CryptHashStringW.argtypes = [c_int, c_wchar_p, ctypes.POINTER(ctypes.c_ubyte)]
enigma.EP_CryptHashStringW.restype = c_int

# Checkup / protection functions
enigma.EP_CheckupCopies.argtypes = [POINTER(c_int), POINTER(c_int)]
enigma.EP_CheckupCopies.restype = c_bool
enigma.EP_CheckupCopiesCurrent.argtypes = []
enigma.EP_CheckupCopiesCurrent.restype = c_int
enigma.EP_CheckupCopiesTotal.argtypes = []
enigma.EP_CheckupCopiesTotal.restype = c_int
enigma.EP_CheckupIsEnigmaOk.argtypes = []
enigma.EP_CheckupIsEnigmaOk.restype = c_bool
enigma.EP_CheckupIsProtected.argtypes = []
enigma.EP_CheckupIsProtected.restype = c_bool
enigma.EP_EnigmaVersion.argtypes = []
enigma.EP_EnigmaVersion.restype = c_int
enigma.EP_MiscCountryCode.argtypes = []
enigma.EP_MiscCountryCode.restype = c_int
enigma.EP_MiscGetWatermark.argtypes = [c_int, ctypes.c_void_p]  # PWMContent 视情况替换为 ctypes 结构
enigma.EP_MiscGetWatermark.restype = c_int

# Protected string
enigma.EP_ProtectedStringByID.argtypes = [c_int, c_char_p, c_int]
enigma.EP_ProtectedStringByID.restype = c_int
enigma.EP_ProtectedStringByKey.argtypes = [c_char_p, c_char_p, c_int]
enigma.EP_ProtectedStringByKey.restype = c_int

# Splash screen
enigma.EP_SplashScreenShow.argtypes = []
enigma.EP_SplashScreenShow.restype = c_int
enigma.EP_SplashScreenHide.argtypes = []
enigma.EP_SplashScreenHide.restype = None

# Virtualization check
enigma.EP_CheckupVirtualizationTools.argtypes = []
enigma.EP_CheckupVirtualizationTools.restype = c_bool

# Load configuration
enigma.EP_LoadConfiguration.argtypes = [c_char_p]
enigma.EP_LoadConfiguration.restype = c_bool
enigma.EP_LoadConfigurationA.argtypes = [c_char_p]
enigma.EP_LoadConfigurationA.restype = c_bool
