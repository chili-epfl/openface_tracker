cmake_minimum_required(VERSION 2.8.3)
project(features_face)

set(CMAKE_POSITION_INDEPENDENT_CODE True)
add_definitions(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  tf
  visualization_msgs
  sensor_msgs
  cv_bridge
  image_transport
  image_geometry
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_package()

add_executable(estimate_focus2 nodes/estimate_focus.cpp)
target_link_libraries(estimate_focus2 ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

install(TARGETS estimate_focus2
ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(PROGRAMS nodes/withmeness.py
DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES
    launch/features_face.launch
    share/targets.json
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
