cmake_minimum_required(VERSION 3.5)
project(vicon_receiver)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -g)
endif()

include_directories(
  include
  ${Boost_INCLUDE_DIRS}
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclcpp REQUIRED)
find_package(Boost REQUIRED COMPONENTS thread)
find_package(geometry_msgs REQUIRED)

# Grab all message files
file(GLOB msg_files RELATIVE ${PROJECT_SOURCE_DIR} msg/*.msg)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  DEPENDENCIES geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime)

# Get typesupport target
rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} rosidl_typesupport_cpp)

add_executable(vicon_client src/vicon_receiver/communicator.cpp src/vicon_receiver/publisher.cpp)
target_link_libraries(vicon_client ViconDataStreamSDK_CPP ${Boost_LIBRARIES})
ament_target_dependencies(vicon_client rclcpp rosidl_default_runtime)

# Link the typesupport target
target_link_libraries(vicon_client ${cpp_typesupport_target})

install(TARGETS vicon_client DESTINATION lib/${PROJECT_NAME})

# Install launch file
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
