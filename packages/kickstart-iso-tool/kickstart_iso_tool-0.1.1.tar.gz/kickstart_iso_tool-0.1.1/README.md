Kickstart iso (kiso)
=========================================================

requirements for debian:
 apt install -y syslinux-utils isomd5sum genisoimage

creating deb package:
 clone source code
 bash setup-env.sh
 make build_deb
 copy deb_dist/python3-kiso_{version}-1_all.deb to destination and install

minimal config required:
 [DEFAULT]
 storage = <-- Where to store created iso
 kcfg_location = <-- where to look for kickstart files

 [rocky-9]
 url = <-- from where to download iso image
 kcfg = <-- path to kickstart.cfg file


How to use:
 kiso -b {varian-name}
