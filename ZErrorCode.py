from enum import Enum

#�v���B�z�u��C
class ZVision_Tool(Enum):
    #eVision �C
    eVision,
	#Open CV �C
    OpenCV,
	#�ۦ�}�o�C
    Customer

#�v����m���O�C
class ZImageByteType(Enum):
    #�C�@�ӹ����� 8 Bit �Ӫ�ܡC
    Image8,
	#�C�@�ӹ����� 24 Bit �Ӫ�ܡC
    Image24,
	#�C�@�ӹ����� 1 Bit �Ӫ�ܡC
    Image1,
	#�����C
    NA

#�v���ɮ׮榡�C
class ZImageFileType(Enum):
    #Windows Bitmap�A����ɦW�� *.bmp �C
    BMP,
	#Jpeg�A����ɦW�� *.jpg �� *.jpeg �C
    Jpeg,
	#Jpeg2000�A����ɦW�� *.j2k �C
    Jpeg2000,
	#PNG�A����ɦW�� *.png �C
    PNG,
	#TIFF�A����ɦW�� *.titf �C
    TIFF,

#IO���A�C
class ZIOState(Enum): 
	#�}�C
	On, 
	#���C
	Off, 
	#�����C
	Unknow,

#���~���A�X�C
class ZErrorCode(Enum)
	#�w�]���A�A���\�C
	ST_SUCCESS = 0,
	#System Error
	#�t�ο��~�C
	ER_SYSTEM = -100,
	#�t�ο��~�A�ϥΪ̤������~�C
	ER_USER_INTERFACE = -101,
	#�t�ο��~�A��l���~�C
	ER_INITIAL = -102,
    #�t�ο��~�A�䤣��˸m�C
    ER_NO_DEVICE = -103,
    #�t�ο��~�A�ϥΪ̤������~�C
    ER_NOT_EXIST = -104,
    #  Procedure Error
    #�{�ǿ��~�C
	ER_PROCEDURE = -1000,
    #�{�ǿ��~�A�Ѽƿ��~�C
    ER_PARAMETER = -1001,
    #�{�ǿ��~�A�ɮפ��s�b�C
    ER_FILE_NOT_EXIST = -1002,
    #�{�ǿ��~�A�O�ɡC
    ER_TIMEOUT = -1001,
	#Motion Error
	#�B�ʥd���~�A��l���`�C
	ER_MOTION_INIT = -2000,
	#�B�ʥd���~�A�氱���`�C
	ER_MOTION_ESTOP = -2001,
	#�B�ʥd���~�A�˸m�d���`�C
	ER_MOTION_CARD = -2002,
	#�B�ʥd���~�A�O�ɡC
	ER_MOTION_TIMEOUT = -2003,
	#�B�ʥd���~�AAdlink 8164 �d���~�X�A�n�O�d�� -2100~-2142 �C
	ER_MOTION_8164_NO_ERROR = -2100,	#�n�O -2100~-2142 �� Adlink 8164 �d�����~�X�C
	#�B�ʥd���~�A�S���o�ӥ\��C
	ER_MOTION_NO_FUNCTION = -2007,
	#�B�ʥd���~�A�˸m�d���`�C
	ER_MOTION_KINEMATICS = -2008,
	#�B�ʥd���~�A�w�g�B�@�F�A�L�k���йB�@�C
	ER_MOTION_OPERATED = -2009,
	#�B�ʥd���~�A�w�g�B�@�F�A���A�����C
	ER_MOTION_SERVO_OFF = -2010,
	# Vision Error
	#��ı�������~�A eVision ���~�C
	ER_EVISION = -3010,
	#��ı�������~�AeVision �t��k���~�C
	ER_VISION_ALGORITHM = -3011,
    #VixionX Error
    #��ı�������~�AXVision ���~�C
	ER_VISIONX = -3020,    
	#��ı�������~�A�۾����~�C
	ER_CAMERA = -3040,
	#��ı�������~�A�۾���l���~�C
	ER_CAMERA_INIT = -3041,
	#��ı�������~�A�۾��w����~�C
	ER_CAMERA_HARDWARE = -3043,
	#��ı�������~�A�۾��]�m���~�C
	ER_CAMERA_OPERATION = -3044,
	#��ı�������~�A�۾��Ѽƿ��~�C
	ER_CAMERA_PARAMETER = -3046,
	#Communication
	#�q�T���~�C
	ER_COMMUNICATION = -3500,
	#�q�T���~�A�q�T���A���s���C
	ER_COMM_NOT_CONNECT = -3501,
	#�q�T���~�A�q�T�O�ɡC
	ER_COMM_TIMEOUT = -3502,
	#IO Error
	#IO���~�A��l���~�C
	ER_IO_INIT = -4000,
	#IO���~�A�]�m�s������~�C
	ER_IO_SET_PORT = -4001,
	#IO���~�A���o�s������~�C
	ER_IO_GET_PORT = -4002,
	#IO���~�A�O�ɡC
	ER_IO_TIMEOUT = -4003,
	#IO���~�AAdlink 7230 �d���~�A���~�X�d�� -4201~-4217�C
	ER_IO_7230_NO_ERROR = -4100,	#�n�O -4100~-4167 �� Adlink 7230 �d�����~�X, -4201~-4217��Adlink 7230 �d�X�ʵ{�������~�X�C
    ER_IO_7250_NO_ERROR = -4100,	#��� Adlink 7230 �A�N���~�X�n�O�� Adlink 7250 
    #Classification Error
	#���������~�C
    ER_CLASSIFICATION_DATA_DIMENTION = -5000,
	#���������~�A�W�h���~�C
    ER_CLASSIFICATION_RULE = -5001,
	#���������~�A�S�x�^�����`�C
    ER_CLASSIFICATION_FEATURE_GENERATION = -5002,
    #Robot Error
	#�������u���~�C
    ER_ROBOT = -6000,
	#�������u���~�A�ѼƲ��`�C
    ER_ROBOT_PARAMETER = -6001,
    #PLC Error
    #PLC���~�C
    ER_PLC = -7000,
    #PLC���~�A�s�u���~�C
    ER_PLC_COMMUNICATION = -7001,
    #PLC���~�AMX Component ���~�X�d�� -7100~-7099�C
    ER_PLC_MX_COMPONENT_NO_ERROR = -7100,
	#Barcode Reader
	#Barcode Reader���~�C
    ER_BarcodeRead = -8000,
	#Barcode ReaderŪ�����~�C
    ER_BarcodeRead_NoReader = -8001,
	#=====================================================
	#Warning Definition
	#���ݩ��Y�����~�������w�q���A�C
	#=====================================================
	#Interface
	#ĵ�i�AInterface�L����k�C
    WN_INTERFACE_NO_FUNCTION = 20001,
	#Initialization
	#ĵ�i�A�������P�C
    WN_VERSION_DIFFERENT = 20002,
	#General
	#ĵ�i�A�O�ɡC
    WN_TIMEOUT = 20003,
	#Vision
	#ĵ�i�AeVision ���`�C
    WN_EVISION = 20010,
	# Procedure Error
    WN_PROCEDURE = 20005,
	# region " Motion Card - ���~�X��Ķ�� "
	# Adlink 8164 ��ƩҦ^�Ǫ����~�X�p�U: 

class Error_8164(Enum):
    ERR_NoError = 0,						#0
	ERR_BoardNoInit = 1,					#1
	ERR_InvalidBoardNumber = 2,			#2
	ERR_InitializedBoardNumber = 3,			#3
	ERR_BaseAddressError = 4,				#4
	ERR_BaseAddressConflict = 5,			#5
	ERR_DuplicateBoardSetting = 6,			#6
	ERR_DuplicateIrqSetting = 7,			#7
	ERR_PCIBiosNotExist = 8,				#8
	ERR_PCIIrqNotExist = 9,				#9
	ERR_PCICardNotExist = 10,				#10
	ERR_SpeedError = 11,   				#11
	ERR_MoveRatioError = 12,				#12
	ERR_PosOutOfRange = 13,				#13
	ERR_AxisAlreadyStop = 14,				#14
	ERR_AxisArrayError = 15,				#15
	ERR_SlowDownPointError = 16,			#16
	ERR_CompareMethodError = 17,			#17
	ERR_CompareNoError = 18,				#18
	ERR_CompareAxisError = 19,				#19
	ERR_CompareTableSizeError = 20,			#20
	ERR_CompareFunctionError = 21,			#21
	ERR_CompareTableNotReady = 22,			#22
	ERR_CompareLineNotReady = 23,			#23
	ERR_NoCardFound = 24,					#24
	ERR_LatchNoError = 25,					#25
	ERR_AxisRangeError = 26,				#26
	ERR_DioNoError = 27,					#27
	ERR_PChangeSlowDownPointError = 28,		#28
	ERR_SpeedChangeError = 29,				#29
	ERR_CardNoError = 30,					#30
	ERR_LinkIntError = 31,					#31
	ERR_HardwareCompareAxisWrong = 32,		#32
	ERR_AutoCompareSourceWrong = 33,		#33
	ERR_CompareDeviceTypeError = 34,		#34
	ERR_PulserHomeTypeError = 35,			#35
	ERR_EventAlreadyEnable = 36,			#36
	ERR_EventNotEnableYet = 37,			#37
	ERR_ConfigFileOpenError = 39,			#39
	ERR_CompareFIFONotReady = 40,			#40
	ERR_EventInitError = 41,				#41
	ERR_MemAllocError = 42,				#42 

	#region " IO Card - ���~�X��Ķ��"

	# Adlink 7230 ���~�N�X�C
class Error_7230(Enum):	
	NoError = 0,
	ErrorUnknownCardType = -1,
	ErrorInvalidCardNumber = -2,
	ErrorTooManyCardRegistered = -3,
	ErrorCardNotRegistered = -4,
	ErrorFuncNotSupport = -5,
	ErrorInvalidIoChannel = -6,
	ErrorInvalidAdRange = -7,
	ErrorContIoNotAllowed = -8,
	ErrorDiffRangeNotSupport = -9,
	ErrorLastChannelNotZero = -10,
	ErrorChannelNotDescending = -11,
	ErrorChannelNotAscending = -12,
	ErrorOpenDriverFailed = -13,
	ErrorOpenEventFailed = -14,
	ErrorTransferCountTooLarge = -15,
	ErrorNotDoubleBufferMode = -16,
	ErrorInvalidSampleRate = -17,
	ErrorInvalidCounterMode = -18,
	ErrorInvalidCounter = -19,
	ErrorInvalidCounterState = -20,
	ErrorInvalidBinBcdParam = -21,
	ErrorBadCardType = -22,
	ErrorInvalidDaRefVoltage = -23,
	ErrorAdTimeOut = -24,
	ErrorNoAsyncAI = -25,
	ErrorNoAsyncAO = -26,
	ErrorNoAsyncDI = -27,
	ErrorNoAsyncDO = -28,
	ErrorNotInputPort = -29,
	ErrorNotOutputPort = -30,
	ErrorInvalidDioPort = -31,
	ErrorInvalidDioLine = -32,
	ErrorContIoActive = -33,
	ErrorDblBufModeNotAllowed = -34,
	ErrorConfigFailed = -35,
	ErrorInvalidPortDirection = -36,
	ErrorBeginThreadError = -37,
	ErrorInvalidPortWidth = -38,
	ErrorInvalidCtrSource = -39,
	ErrorOpenFile = -40,
	ErrorAllocateMemory = -41,
	ErrorDaVoltageOutOfRange = -42,
	ErrorDaExtRefNotAllowed = -43,
	ErrorDIODataWidthError = -44,
	ErrorTaskCodeError = -45,
	ErrortriggercountError = -46,
	ErrorInvalidTriggerMode = -47,
	ErrorInvalidTriggerType = -48,
	ErrorInvalidCounterValue = -50,
	ErrorInvalidEventHandle = -60,
	ErrorNoMessageAvailable = -61,
	ErrorEventMessgaeNotAdded = -62,
	ErrorCalibrationTimeOut = -63,
	ErrorUndefinedParameter = -64,
	ErrorInvalidBufferID = -65,
	ErrorInvalidSampledClock = -66,
	ErrorInvalisOperationMode = -67,


		#Error code number for driver API
	ErrorConfigIoctl = -201,
	ErrorAsyncSetIoctl = -202,
	ErrorDBSetIoctl = -203,
	ErrorDBHalfReadyIoctl = -204,
	ErrorContOPIoctl = -205,
	ErrorContStatusIoctl = -206,
	ErrorPIOIoctl = -207,
	ErrorDIntSetIoctl = -208,
	ErrorWaitEvtIoctl = -209,
	ErrorOpenEvtIoctl = -210,
	ErrorCOSIntSetIoctl = -211,
	ErrorMemMapIoctl = -212,
	ErrorMemUMapSetIoctl = -213,
	ErrorCTRIoctl = -214,
	ErrorGetResIoctl = -215,
	ErrorCalIoctl = -216,
	ErrorPMIntSetIoctl = -217,	

class Error_7250(Enum):    
    NoError = 0,
    ErrorUnknownCardType = -1,
    ErrorInvalidCardNumber = -2,
    ErrorTooManyCardRegistered = -3,
    ErrorCardNotRegistered = -4,
    ErrorFuncNotSupport = -5,
    ErrorInvalidIoChannel = -6,
    ErrorInvalidAdRange = -7,
    ErrorContIoNotAllowed = -8,
    ErrorDiffRangeNotSupport = -9,
    ErrorLastChannelNotZero = -10,
    ErrorChannelNotDescending = -11,
    ErrorChannelNotAscending = -12,
    ErrorOpenDriverFailed = -13,
    ErrorOpenEventFailed = -14,
    ErrorTransferCountTooLarge = -15,
    ErrorNotDoubleBufferMode = -16,
    ErrorInvalidSampleRate = -17,
    ErrorInvalidCounterMode = -18,
    ErrorInvalidCounter = -19,
    ErrorInvalidCounterState = -20,
    ErrorInvalidBinBcdParam = -21,
    ErrorBadCardType = -22,
    ErrorInvalidDaRefVoltage = -23,
    ErrorAdTimeOut = -24,
    ErrorNoAsyncAI = -25,
    ErrorNoAsyncAO = -26,
    ErrorNoAsyncDI = -27,
    ErrorNoAsyncDO = -28,
    ErrorNotInputPort = -29,
    ErrorNotOutputPort = -30,
    ErrorInvalidDioPort = -31,
    ErrorInvalidDioLine = -32,
     = -33,
    ErrorDblBufModeNotAllowed = -34,
    ErrorConfigFailed = -35,
    ErrorInvalidPortDirection = -36,
    ErrorBeginThreadError = -37,
    ErrorInvalidPortWidth = -38,
    ErrorInvalidCtrSource = -39,
    ErrorOpenFile = -40,
    ErrorAllocateMemory = -41,
    ErrorDaVoltageOutOfRange = -42,
    ErrorDaExtRefNotAllowed = -43,
    ErrorDIODataWidthError = -44,
    ErrorTaskCodeError = -45,
    ErrortriggercountError = -46,
    ErrorInvalidTriggerMode = -47,
    ErrorInvalidTriggerType = -48,
    ErrorInvalidCounterValue = -50,
    ErrorInvalidEventHandle = -60,
    ErrorNoMessageAvailable = -61,
    ErrorEventMessgaeNotAdded = -62,
    ErrorCalibrationTimeOut = -63,
    ErrorUndefinedParameter = -64,
    ErrorInvalidBufferID = -65,
    ErrorInvalidSampledClock = -66,
    ErrorInvalisOperationMode = -67,


    #Error code number for driver API
    ErrorConfigIoctl = -201,
    ErrorAsyncSetIoctl = -202,
    ErrorDBSetIoctl = -203,
    ErrorDBHalfReadyIoctl = -204,
    ErrorContOPIoctl = -205,
    ErrorContStatusIoctl = -206,
    ErrorPIOIoctl = -207,
    ErrorDIntSetIoctl = -208,
    ErrorWaitEvtIoctl = -209,
    ErrorOpenEvtIoctl = -210,
    ErrorCOSIntSetIoctl = -211,
    ErrorMemMapIoctl = -212,
    ErrorMemUMapSetIoctl = -213,
    ErrorCTRIoctl = -214,
    ErrorGetResIoctl = -215,
    ErrorCalIoctl = -216,
    ErrorPMIntSetIoctl = -217,

    #region " PLC - ���~�X��Ķ�� "
    #MX Component ���~��C
class ZComponent(Enum):    
    NoError = 0,
    Timeout = -1,
    SendError = -2,
    ReceiveError = -3,
    ConnectError = -4,
    ElseError = -5,
    
    

#�˸m���O�C
class ZDeviceType(Enum):
    #DIO�d ADLink PCI-7230�C
    ADLINK_7230 = "PCI_7230",
    #DIO�d ADLink PCI-7250�C
    ADLINK_7250 = "PCI_7250",
    #DIO�d ADLink PCI-7440�C
    ADLINK_7442 = "PCI_7442",
    #���� Digital Input �d�C
    VIRTUAL_DI = "Virtual_DI",
    #���� Digital Output �d�C
    VIRTUAL_DO = "Virtual_DO",
	#���� Digital Input/Output �d�C
    VIRTUAL_DIO = "Virtual_DIO",
	#DIO�d ADLink PCI-7440�C
    ADLINK_8164 = "Adlink_8164",
	#DIO�d ADLink PCI-7440�C
    FESTO_CVE = "Festo",
	#���� Motion �d�C
    VIRTUAL_MOTION = "Virtual Motion",
    #LogRecoder�W�١C
    LOG_RECODER = "�T�������� / ������"

