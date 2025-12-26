import ctypes
from ctypes import byref, sizeof, pointer, cast, POINTER, create_string_buffer, memset, addressof
from ctypes.wintypes import HANDLE, ULONG, DWORD
from drivers.native import get_libs
from drivers.helpers import RtlInitUnicodeString
from drivers.structs.unicode import UNICODE_STRING
from drivers.structs.attributes import OBJECT_ATTRIBUTES
from drivers.structs.dir_info import OBJECT_DIRECTORY_INFORMATION
from drivers.defines.flags import *
from drivers.defines.ntstatus import *
import sys
import logging

ntdll, _ = get_libs()
INVALID_HANDLE_VALUE = HANDLE(-1).value if sys.platform == 'win32' else -1

def InitializeObjectAttributes(InitializedAttributes, ObjectName, Attributes, RootDirectory, SecurityDescriptor):
    try:
        memset(addressof(InitializedAttributes), 0, sizeof(InitializedAttributes))
        InitializedAttributes.Length = sizeof(InitializedAttributes)
        InitializedAttributes.ObjectName = ObjectName
        InitializedAttributes.Attributes = Attributes
        InitializedAttributes.RootDirectory = RootDirectory
        InitializedAttributes.SecurityDescriptor = SecurityDescriptor
        InitializedAttributes.SecurityQualityOfService = None
    except Exception:
        pass

def open_directory(root_handle, dir_path, desired_access):
    if not ntdll:
        return None
    status = STATUS_UNSUCCESSFUL
    dir_handle = HANDLE()
    us_dir = UNICODE_STRING()
    p_us_dir = None
    if dir_path:
        status = RtlInitUnicodeString(us_dir, dir_path)
        if status != STATUS_SUCCESS:
            return None
        p_us_dir = pointer(us_dir)
    obj_attr = OBJECT_ATTRIBUTES()
    InitializeObjectAttributes(obj_attr, p_us_dir, OBJ_CASE_INSENSITIVE, root_handle, None)
    try:
        status = ntdll.NtOpenDirectoryObject(byref(dir_handle), desired_access, byref(obj_attr))
    except Exception as e:
        logging.error(f"NtOpenDirectoryObject failed: {e}")
        return None
    if status != STATUS_SUCCESS:
        return None
    return dir_handle

def find_sym_link(dir_root_path, name_contains):
    """
    Searches the Windows object namespace for a symlink containing the given name.
    This is the PROPER implementation that actually iterates through entries.
    """
    if not ntdll:
        logging.warning("ntdll not available - cannot search for driver")
        return False, None
    
    dir_handle = open_directory(None, dir_root_path, DIRECTORY_QUERY)
    if not dir_handle or dir_handle.value == INVALID_HANDLE_VALUE:
        logging.warning(f"Failed to open directory: {dir_root_path}")
        return False, None
    
    status = STATUS_UNSUCCESSFUL
    query_context = ULONG(0)
    length = ULONG(0)
    buffer_size = 1024
    buffer = create_string_buffer(buffer_size)
    found = False
    found_name = None
    first_entry = True
    
    try:
        while True:
            status = ntdll.NtQueryDirectoryObject(
                dir_handle, buffer, buffer_size, 
                True,  # ReturnSingleEntry
                first_entry,  # RestartScan
                byref(query_context), 
                byref(length)
            )
            first_entry = False
            
            if status == STATUS_SUCCESS:
                current_objinf = cast(buffer, POINTER(OBJECT_DIRECTORY_INFORMATION)).contents
                obj_name = "N/A"
                type_name = "N/A"
                
                if current_objinf.Name.Buffer and current_objinf.Name.Length > 0:
                    try:
                        obj_name = current_objinf.Name.Buffer[:current_objinf.Name.Length // 2]
                    except Exception:
                        obj_name = "[Read Error]"
                        
                if current_objinf.TypeName.Buffer and current_objinf.TypeName.Length > 0:
                    try:
                        type_name = current_objinf.TypeName.Buffer[:current_objinf.TypeName.Length // 2]
                    except Exception:
                        type_name = "[Read Error]"
                
                # Check if this entry contains our target name
                if name_contains in obj_name:
                    logging.info(f"Found driver symlink: {obj_name} (Type: {type_name})")
                    found = True
                    found_name = obj_name
                    break
                continue
                
            elif status == STATUS_BUFFER_TOO_SMALL:
                if length.value <= buffer_size:
                    break
                buffer_size = length.value
                buffer = create_string_buffer(buffer_size)
                continue
                
            elif status == STATUS_NO_MORE_ENTRIES:
                logging.info(f"Finished scanning {dir_root_path} - no match for '{name_contains}'")
                break
            else:
                logging.warning(f"NtQueryDirectoryObject returned status: {status:#x}")
                break
                
    except Exception as e:
        logging.error(f"Error scanning directory: {e}")
        found = False
    finally:
        if dir_handle and dir_handle.value != INVALID_HANDLE_VALUE:
            ntdll.NtClose(dir_handle)
    
    return found, found_name