HUMAN_UNITS = ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]
SPEED_UNITS = ["bps", "Kbps", "Mbps", "Gbps", "Tbps"]
CHUNK_SIZE = 1024
ISOINFO_BIN = "/usr/bin/isoinfo"
XORRISO = "/usr/bin/xorriso"
grub_cfg_template = """
set default="0"
function load_video {
  insmod all_video
}
load_video
set gfxpayload=keep
insmod gzio
insmod part_gpt
insmod ext2
insmod chain
set timeout=5
search --no-floppy --set=root -l '{{ iso_name }}'
menuentry 'Kickstarted install of {{ name }}' --class fedora --class gnu-linux --class gnu --class os {
	linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL={{ iso_name }} inst.ks=hd:LABEL={{ iso_name }} net.ifnames=0 biosdevname=0 mitigations=off inst.text
	initrd /images/pxeboot/initrd.img
}
"""
isolinux_cfg_template = """
default vesamenu.c32
timeout 100
display boot.msg
menu clear
menu background splash.png
menu title Rocky Linux 9.5
menu vshift 8
menu rows 18
menu margin 8
menu helpmsgrow 15
menu tabmsgrow 13
menu color border * #00000000 #00000000 none
menu color sel 0 #ffffffff #00000000 none
menu color title 0 #ff7ba3d0 #00000000 none
menu color tabmsg 0 #ff3a6496 #00000000 none
menu color unsel 0 #84b8ffff #00000000 none
menu color hotsel 0 #84b8ffff #00000000 none
menu color hotkey 0 #ffffffff #00000000 none
menu color help 0 #ffffffff #00000000 none
menu color scrollbar 0 #ffffffff #ff355594 none
menu color timeout 0 #ffffffff #00000000 none
menu color timeout_msg 0 #ffffffff #00000000 none
menu color cmdmark 0 #84b8ffff #00000000 none
menu color cmdline 0 #ffffffff #00000000 none
menu tabmsg Press Tab for full configuration options on menu items.
menu separator # insert an empty line
menu separator # insert an empty line
label linux
  menu label ^Kickstarted install of Rocky Linux {{ name }}
  menu default
  kernel vmlinuz
  append initrd=initrd.img inst.stage2=hd:LABEL={{ iso_name }} inst.ks=hd:LABEL={{ iso_name }} net.ifnames=0 biosdevname=0 mitigations=off inst.text
"""