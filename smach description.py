#!/usr/bin/env python

import rospy

##################################################################################################################

class getPoseOfTheObject(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded', 'aborted'],
                                    output_keys=['output_object_pose'])

        self.namespace = rospy.get_param("~robot_name")
        self.marker_pose_sub = rospy.Subscriber(self.namespace + '/ar_pose_marker', AlvarMarkers, self.arMarkerMsgCallback)

        self.OFFSET_FOR_GOAL_HEIGHT = 0.150

    def arMarkerMsgCallback(self, ar_marker_pose_msg):
        if len(ar_marker_pose_msg.markers) == 0:
            self.ar_marker_pose = False
        else:            
            self.ar_marker_pose = AlvarMarker()
            self.ar_marker_pose = ar_marker_pose_msg.markers[0]

    def execute(self, userdata):
        if self.ar_marker_pose == False:
            rospy.logwarn('Failed to get pose of the marker')
            return 'aborted'
        else:
            object_pose = Pose()
            object_pose.position = self.ar_marker_pose.pose.pose.position
 
            object_pose.position.x += 0.0
            object_pose.position.y  = 0.0
            object_pose.position.z += self.OFFSET_FOR_GOAL_HEIGHT

            dist = math.sqrt((self.ar_marker_pose.pose.pose.position.x * self.ar_marker_pose.pose.pose.position.x) +
                        (self.ar_marker_pose.pose.pose.position.y * self.ar_marker_pose.pose.pose.position.y))

            if self.ar_marker_pose.pose.pose.position.y > 0:
                yaw = math.acos(self.ar_marker_pose.pose.pose.position.x / dist)
            else:
                yaw = (-1) * math.acos(self.ar_marker_pose.pose.pose.position.x / dist)

            roll = 0.0
            pitch = 0.0

            cy = math.cos(yaw * 0.5)
            sy = math.sin(yaw * 0.5)
            cr = math.cos(roll * 0.5)
            sr = math.sin(roll * 0.5)
            cp = math.cos(pitch * 0.5)
            sp = math.sin(pitch * 0.5)

            object_pose.orientation.w = cy * cr * cp + sy * sr * sp
            object_pose.orientation.x = cy * sr * cp - sy * cr * sp
            object_pose.orientation.y = cy * cr * sp + sy * sr * cp
            object_pose.orientation.z = sy * cr * cp - cy * sr * sp

            userdata.output_object_pose = object_pose
            rospy.loginfo('Succeeded to get pose of the object')
            return 'succeeded'

        self.marker_pose_sub

##################################################################################################################

def main():
    rospy.init_node('pick_and_place_state_machine2')
    namespace = rospy.get_param("~robot_name")
    planning_group = rospy.get_param("~planning_group")

##################################################################################################################
        # Create the sub SMACH state machine
        pick_center = smach.StateMachine(outcomes=['succeeded','aborted','preempted'])

        with pick_center:
            pick_center.userdata.planning_group = planning_group

            def eef_pose_request_cb(userdata, request):
                eef = KinematicsPose()
                eef.pose = userdata.input_pose
                rospy.loginfo('eef.position.x : %f', eef.pose.position.x)
                rospy.loginfo('eef.position.y : %f', eef.pose.position.y)
                rospy.loginfo('eef.position.z : %f', eef.pose.position.z)
                eef.max_velocity_scaling_factor = 1.0
                eef.max_accelerations_scaling_factor = 1.0
                eef.tolerance = userdata.input_tolerance

                request.planning_group = userdata.input_planning_group
                request.kinematics_pose = eef
                return request

            def align_arm_with_object_response_cb(userdata, response):
                if response.is_planned == False:
                    pick_center.userdata.align_arm_with_object_tolerance += 0.005
                    rospy.logwarn('Set more tolerance[%f]', pick_center.userdata.align_arm_with_object_tolerance)
                    return 'aborted'
                else:
                    OFFSET_FOR_STRETCH = 0.030
                    pick_center.userdata.object_pose.position.x += OFFSET_FOR_STRETCH
                    rospy.sleep(3.)
                    return 'succeeded'

##################################################################################################################

            pick_center.userdata.object_pose = Pose()
            ## 1. getPoseOfTheObject Class 에서 AR Marker 좌표를 받아 outputkey로 설정된 output_object_pose 에 넣어 돌려줌. 
            ##    해당 값을 pick_center.userdata.object_pos 에 remap 함.  
            smach.StateMachine.add('GET_POSE_OF_THE_OBJECT', getPoseOfTheObject(),
                                    transitions={'succeeded':'ALIGN_ARM_WITH_OBJECT',
                                                'aborted':'aborted'},
                                    remapping={'output_object_pose':'object_pose'})
            ## 2. eef_pose_request_cb 함수에  object_pos를 input_pose로 remap 하여 대입 하면  eef_pose_request_cb 함수에서 input_pose로 해당 값으로 팔을 움직임. 
            ## 결과가 성공이면 CLOSE_TO_OBJECT state로 실패면 align_arm_with_object_response_cb 함수를 거쳐 align_arm_with_object_tolerance 값을 변경하여 다시 
            ## request 실행  
            pick_center.userdata.align_arm_with_object_tolerance = 0.01
            smach.StateMachine.add('ALIGN_ARM_WITH_OBJECT',
                                    ServiceState(planning_group + '/moveit/set_kinematics_pose',
                                                    SetKinematicsPose,
                                                    request_cb=eef_pose_request_cb,
                                                    response_cb=align_arm_with_object_response_cb,
                                                    input_keys=['input_planning_group',
                                                                'input_pose',
                                                                'input_tolerance']),                                                    
                                   transitions={'succeeded':'CLOSE_TO_OBJECT',
                                                'aborted':'ALIGN_ARM_WITH_OBJECT'},
                                   remapping={'input_planning_group':'planning_group',
                                            'input_pose':'object_pose',
                                            'input_tolerance':'align_arm_with_object_tolerance'})

            pick_center.userdata.close_to_object_tolerance = 0.01
            smach.StateMachine.add('CLOSE_TO_OBJECT',
                                    ServiceState(planning_group + '/moveit/set_kinematics_pose',
                                                    SetKinematicsPose,
                                                    request_cb=eef_pose_request_cb,
                                                    response_cb=close_to_object_response_cb,
                                                    input_keys=['input_planning_group',
                                                                'input_pose',
                                                                'input_tolerance']),                                                    
                                   transitions={'succeeded':'GRIP_OBJECT',
                                                'aborted':'CLOSE_TO_OBJECT'},
                                   remapping={'input_planning_group':'planning_group',
                                            'input_pose':'object_pose',
                                            'input_tolerance':'close_to_object_tolerance'})

##################################################################################################################

    sis = smach_ros.IntrospectionServer('server_name', task_center, '/TASKS_CENTER')
    sis.start()

    # Execute SMACH plan
    outcome = task_center.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
