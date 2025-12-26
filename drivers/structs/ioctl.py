from ctypes import Structure, c_int32

class RZCONTROL_IOCTL_STRUCT(Structure):
    _fields_ = [("unk0", c_int32), ("unk1", c_int32), 
                ("max_val_or_scan_code", c_int32), ("click_mask", c_int32), 
                ("unk3", c_int32), ("x", c_int32), ("y", c_int32), ("unk4", c_int32)]