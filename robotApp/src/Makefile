TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = robotApp

# robotApp.dbd will be created and installed
DBD += robotApp.dbd

# test.dbd will include these files:
robotApp_DBD += base.dbd
robotApp_DBD += busySupport.dbd
robotApp_DBD += asSupport.dbd

# robotApp_registerRecordDeviceDriver.cpp derives from test.dbd
robotApp_SRCS += robotApp_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
robotApp_SRCS_DEFAULT += robotMain.cpp
robotApp_SRCS_vxWorks += -nil-

robotApp_LIBS += autosave
robotApp_LIBS += busy
#robotApp_LIBS += asyn

# Finally link IOC to the EPICS Base libraries
robotApp_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE
