
from configurator.models import Device, DeviceTypeSetting, DeviceSetting
print "Cobbler"
#Cobbler Device
device = Device.objects.get(dtype=DeviceTypeSetting.COBBLER_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='compute-host(host-name;')
DeviceSetting(device=device, device_type_setting=setting, value="crhel1; 19.19.150.10;08:80; Eth1/1;eno16777736;profile1").save()
#DeviceSetting(device=device, device_type_setting=setting, value="crhel2; 192.168.211.88;00:56:34:87:34:55; Eth1/1;eno16777736;profile2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='network-host(host-name')
DeviceSetting(device=device, device_type_setting=setting, value="nrhel1; 192.168.150.11;08:80; Eth1/1 ;eno16777736; profile3").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='profile(profile-name; distro)')
DeviceSetting(device=device, device_type_setting=setting, value="profile1;RHEL-7x86_64").save()
DeviceSetting(device=device, device_type_setting=setting, value="profile2;RHEL-7x86_64").save()
#DeviceSetting(device=device, device_type_setting=setting, value="profile3;RHEL-7x86_64").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='distro')
DeviceSetting(device=device, device_type_setting=setting, value="RHEL-7x86_64").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-interface')
DeviceSetting(device=device, device_type_setting=setting, value="eno16777736").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-server')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.178").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-next-server')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.178").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-subnet')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.0").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-netmask')
DeviceSetting(device=device, device_type_setting=setting, value="255.255.255.0").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-option-router')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-DNS')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='cobbler-hostname')
DeviceSetting(device=device, device_type_setting=setting, value="buildserver").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='cobbler-web(')
DeviceSetting(device=device, device_type_setting=setting, value="cobbler; cobbler").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='redhat-info(')
DeviceSetting(device=device, device_type_setting=setting, value="rahuupad2;iso*help123;8a85f98444de1da50144e5c4aeae67d0").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='proxy(http-')
DeviceSetting(device=device, device_type_setting=setting, value=";;").save()

print "general"
#GENERAL
device = Device.objects.get(dtype=DeviceTypeSetting.GENERAL_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='name-server')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='enable-fi')
DeviceSetting(device=device, device_type_setting=setting, value="True").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='host-ip-address')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.178").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='host-password')
DeviceSetting(device=device, device_type_setting=setting, value="root").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='life-cycle-manager')
DeviceSetting(device=device, device_type_setting=setting, value="Foreman").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='openstack-provisioner')
DeviceSetting(device=device, device_type_setting=setting, value="Packstack").save()

print "Foreman"
#Foreman
device = Device.objects.get(dtype=DeviceTypeSetting.FOREMAN_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='compute-host(h')
DeviceSetting(device=device, device_type_setting=setting, value="crhel1; 192.168.211.87;00:56:34:87:34:44").save()
DeviceSetting(device=device, device_type_setting=setting, value="crhel2; 192.168.211.87;00:56:34:87:34:46").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='foreman-ip-address')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.178").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='foreman-hostname')
DeviceSetting(device=device, device_type_setting=setting, value="buildserver").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='domain-name')
DeviceSetting(device=device, device_type_setting=setting, value="domain.name").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='DNS')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='option-router')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.2").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='netmask')
DeviceSetting(device=device, device_type_setting=setting, value="255.255.255.0").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='subnet')
DeviceSetting(device=device, device_type_setting=setting, value="192.168.211.0").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='proxy(http-proxy-')
DeviceSetting(device=device, device_type_setting=setting, value="19.19.0.253;19.19.0.253;80").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='redhat-info(')
DeviceSetting(device=device, device_type_setting=setting, value="rahuupad2;iso*help123;8a85f98444de1da50144e5c4aeae67d0").save()

print "FI"
#FI
device = Device.objects.get(dtype=DeviceTypeSetting.FI_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-mgmt-native-vlan')
DeviceSetting(device=device, device_type_setting=setting, value="True").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-cluster-ip-address')
DeviceSetting(device=device, device_type_setting=setting, value="19.19.102.10").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-cluster-username')
DeviceSetting(device=device, device_type_setting=setting, value="admin").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-cluster-password')
DeviceSetting(device=device, device_type_setting=setting, value="Cisco12345").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-server-ports')
DeviceSetting(device=device, device_type_setting=setting, value="3,4,9,10").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-uplink-ports')
DeviceSetting(device=device, device_type_setting=setting, value="20").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='fi-slot(s')
DeviceSetting(device=device, device_type_setting=setting, value="1; 3,4,9,10").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='fi-uuid-pool(')
DeviceSetting(device=device, device_type_setting=setting, value="UUID-Test; 0000-000000000050; 0000-000000000100").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='fi-mac-pool(f')
DeviceSetting(device=device, device_type_setting=setting, value="MAC_A; 00:35:B5:6A:00:00; 00:35:B5:6A:03:E7").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='fi-vnic(')
#DeviceSetting(device=device, device_type_setting=setting, value="tenant; 1000; 1010").save()
#DeviceSetting(device=device, device_type_setting=setting, value="internal; 172; 172").save()
DeviceSetting(device=device, device_type_setting=setting, value="Management; 19; 20").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-service-profile-name')
DeviceSetting(device=device, device_type_setting=setting, value="demoLS").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-boot-vnic')
DeviceSetting(device=device, device_type_setting=setting, value="Management").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='fi-boot-policy-name')
DeviceSetting(device=device, device_type_setting=setting, value="Boot_policy_1").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='fi-ip-pool')
DeviceSetting(device=device, device_type_setting=setting, value="ip_pool1; 19.19.117.10; 19.19.117.20; 19.19.0.100; 19.19.0.0").save()

print "Packstack"
#Packstack
device = Device.objects.get(dtype=DeviceTypeSetting.PACKSTACK_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='enable-openvswitch')
DeviceSetting(device=device, device_type_setting=setting, value="True").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='enable-cisconexus')
DeviceSetting(device=device, device_type_setting=setting, value="True").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='vlan-mapping-ranges')
DeviceSetting(device=device, device_type_setting=setting, value="physnet:1000:1500").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='keystone-admin-pw')
DeviceSetting(device=device, device_type_setting=setting, value="Cisco12345").save()

print "Switch"
#Switch

device = Device.objects.get(dtype=DeviceTypeSetting.SWITCH_TYPE)
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='switch-type')
DeviceSetting(device=device, device_type_setting=setting, value="9k").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='ip-address')
DeviceSetting(device=device, device_type_setting=setting, value="19.19.0.3").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='hostname')
DeviceSetting(device=device, device_type_setting=setting, value="sdu-n9396").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='username')
DeviceSetting(device=device, device_type_setting=setting, value="admin").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label='password')
DeviceSetting(device=device, device_type_setting=setting, value="Cisco123").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='vlan(id;')
DeviceSetting(device=device, device_type_setting=setting, value="19;;").save()
DeviceSetting(device=device, device_type_setting=setting, value="50-100;;").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='interface(name')
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/1;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/2;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/3;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/4;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/5;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/6;trunk;;1-4094").save()
DeviceSetting(device=device, device_type_setting=setting, value="ethernet1/7;trunk;;1-4094").save()
setting = DeviceTypeSetting.objects.get(dtype=device.dtype,  standard_label__startswith='port-channel(')
DeviceSetting(device=device, device_type_setting=setting, value="1; ethernet1/8,ethernet1/9").save()

