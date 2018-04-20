### Crear imagen ISO a partir de un CD
Crear imagen ISO.
~~~
root@debian:~# dd if=/dev/sr0 of=iso_prueba.iso
430080+0 registros leídos
430080+0 registros escritos
220200960 bytes (220 MB, 210 MiB) copied, 9,61777 s, 22,9 MB/s
root@debian:~#
~~~


Montaje de la ISO y comprobación del contenido.
~~~
root@debian:~# mount iso_prueba.iso /mnt
mount: /dev/loop0 está protegido contra escritura; se monta como sólo lectura
root@debian:~# ls /mnt
boot  Clonezilla-Live-Version  EFI  GPL  live  syslinux  utils
root@debian:~# 
~~~


### Crear imagen ISO a partir de un directorio
Crear imagen ISO.
~~~
root@debian:~# genisoimage -r -J -o iso_carpeta.iso iso_carpeta
I: -input-charset not specified, using utf-8 (detected in locale settings)
Using K01MD000.;1 for  iso_carpeta/etc/rc0.d/K01mdadm (K01mdadm-waitidle)
Using K01LV000.;1 for  iso_carpeta/etc/rc0.d/K01lvm2-lvmpolld (K01lvm2-lvmetad)
Using S01LV000.;1 for  iso_carpeta/etc/rc4.d/S01lvm2-lvmetad (S01lvm2-lvmpolld)
Using S01LV000.;1 for  iso_carpeta/etc/rc2.d/S01lvm2-lvmetad (S01lvm2-lvmpolld)
Using S01LV000.;1 for  iso_carpeta/etc/rc5.d/S01lvm2-lvmetad (S01lvm2-lvmpolld)
Using APT_D000.TIM;1 for  iso_carpeta/etc/systemd/system/timers.target.wants/apt-daily-upgrade.timer (apt-daily.timer)
.
.
.
.
.
Total translation table size: 0
Total rockridge attributes bytes: 169977
Total directory bytes: 460800
Path table size(bytes): 2384
Max brk space used 12a000
1672 extents written (3 MB)
root@debian:~#
~~~


Montaje de la ISO y comprobación del contenido.
~~~
root@debian:~# mount iso_carpeta.iso /mnt
mount: /dev/loop0 está protegido contra escritura; se monta como sólo lectura
root@debian:~# ls /mnt/
etc
root@debian:~# ls /mnt/etc/
adduser.conf		dbus-1			gss		 locale.alias	 mysql		rc2.d		staff-group-for-usr-local
aliases			debconf.conf		hdparm.conf	 locale.gen	 nanorc		rc3.d		subgid
alternatives		debian_version		host.conf	 localtime	 network	rc4.d		subgid-
anacrontab		default			hostname	 logcheck	 networks	rc5.d		subuid
apm			deluser.conf		hosts		 login.defs	 newt		rc6.d		subuid-
apt			dhcp			hosts.allow	 logrotate.conf  nsswitch.conf	rcS.d		sysctl.conf
avahi			dictionaries-common	hosts.deny	 logrotate.d	 opt		reportbug.conf	sysctl.d
bash.bashrc		discover.conf.d		ifplugd		 lvm		 os-release	resolv.conf	systemd
bash_completion		discover-modprobe.conf	init		 machine-id	 pam.conf	rmt		terminfo
bash_completion.d	dpkg			init.d		 magic		 pam.d		rpc		timezone
bindresvport.blacklist	emacs			initramfs-tools  magic.mime	 passwd		rsyslog.conf	tmpfiles.d
binfmt.d		email-addresses		inputrc		 mailcap	 passwd-	rsyslog.d	ucf.conf
bluetooth		environment		iproute2	 mailcap.order	 perl		securetty	udev
ca-certificates		exim4			issue		 mailname	 ppp		security	ufw
ca-certificates.conf	fstab			issue.net	 manpath.config  profile	selinux		update-motd.d
calendar		fuse.conf		kernel		 mdadm		 profile.d	services	vim
console-setup		gai.conf		kernel-img.conf  mime.types	 protocols	sgml		wgetrc
cron.d			groff			ldap		 mke2fs.conf	 python		shadow		wpa_supplicant
cron.daily		group			ld.so.cache	 modprobe.d	 python2.7	shadow-		X11
cron.hourly		group-			ld.so.conf	 modules	 python3	shells		xdg
cron.monthly		grub.d			ld.so.conf.d	 modules-load.d  python3.5	skel		xml
crontab			gshadow			libaudit.conf	 motd		 rc0.d		ssh
cron.weekly		gshadow-		libnl-3		 mtab		 rc1.d		ssl
root@debian:~# 
~~~


~~~
root@debian:~# debootstrap \
> --arch=i386 \
> --variant=minbase \
> jessie iso_live/chroot \
>  http://ftp.es.debian.org/debian/
I: Retrieving InRelease 
I: Retrieving Release 
I: Retrieving Release.gpg 
.
.
.
.
.
I: Base system installed successfully.
root@debian:~# 
~~~

~~~
root@debian:~# chroot iso_live/chroot
root@debian:/# echo "debian-live" > /etc/hostname 
root@debian:/# apt-cache search linux-image
linux-image-3.16.0-4-586 - Linux 3.16 for older PCs
linux-image-3.16.0-4-686-pae - Linux 3.16 for modern PCs
linux-image-3.16.0-4-686-pae-dbg - Debugging symbols for Linux 3.16.0-4-686-pae
linux-image-3.16.0-4-amd64 - Linux 3.16 for 64-bit PCs
linux-image-486 - Linux for older PCs (dummy package)
linux-image-586 - Linux for older PCs (meta-package)
linux-image-686-pae - Linux for modern PCs (meta-package)
linux-image-686-pae-dbg - Debugging symbols for Linux 686-pae configuration (meta-package)
linux-image-amd64 - Linux for 64-bit PCs (meta-package)
root@debian:/#
~~~

~~~
root@debian:/# apt-get update && \
> apt-get install --no-install-recommends \
> linux-image-3.16.0-4-686-pae \
> live-boot \
> systemd-sysv
Ign http://ftp.es.debian.org jessie InRelease
Hit http://ftp.es.debian.org jessie Release.gpg
Hit http://ftp.es.debian.org jessie Release
Hit http://ftp.es.debian.org jessie/main i386 Packages
Get:1 http://ftp.es.debian.org jessie/main Translation-en [4583 kB]
Fetched 4583 kB in 4s (1134 kB/s)                              
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
systemd-sysv is already the newest version.
The following extra packages will be installed:
  busybox cpio initramfs-tools klibc-utils kmod libklibc libuuid-perl linux-base live-boot-initramfs-tools
Suggested packages:
  libarchive1 bash-completion linux-doc-3.16 debian-kernel-handbook grub-pc extlinux curlftpfs cryptsetup httpfs2 unionfs-fuse wget
Recommended packages:
  firmware-linux-free irqbalance libc6-i686 live-boot-doc live-tools rsync uuid-runtime
The following NEW packages will be installed:
  busybox cpio initramfs-tools klibc-utils kmod libklibc libuuid-perl linux-base linux-image-3.16.0-4-686-pae live-boot live-boot-initramfs-tools
0 upgraded, 11 newly installed, 0 to remove and 0 not upgraded.
Need to get 34.6 MB of archives.
After this operation, 124 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://ftp.es.debian.org/debian/ jessie/main kmod i386 18-3 [93.5 kB]
Get:2 http://ftp.es.debian.org/debian/ jessie/main libuuid-perl i386 0.05-1+b1 [10.7 kB]
Get:3 http://ftp.es.debian.org/debian/ jessie/main linux-base all 3.5 [34.3 kB]
Get:4 http://ftp.es.debian.org/debian/ jessie/main libklibc i386 2.0.4-2 [52.8 kB]
Get:5 http://ftp.es.debian.org/debian/ jessie/main klibc-utils i386 2.0.4-2 [108 kB]
Get:6 http://ftp.es.debian.org/debian/ jessie/main cpio i386 2.11+dfsg-4.1+deb8u1 [181 kB]
Get:7 http://ftp.es.debian.org/debian/ jessie/main busybox i386 1:1.22.0-9+deb8u1 [367 kB]
Get:8 http://ftp.es.debian.org/debian/ jessie/main initramfs-tools all 0.120+deb8u3 [96.7 kB]
Get:9 http://ftp.es.debian.org/debian/ jessie/main linux-image-3.16.0-4-686-pae i386 3.16.51-2 [33.5 MB]
Get:10 http://ftp.es.debian.org/debian/ jessie/main live-boot-initramfs-tools all 4.0.2-1 [29.3 kB]
Get:11 http://ftp.es.debian.org/debian/ jessie/main live-boot all 4.0.2-1 [51.9 kB]
Fetched 34.6 MB in 2s (15.3 MB/s) 
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LANG = "es_ES.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
debconf: delaying package configuration, since apt-utils is not installed
E: Can not write log (Is /dev/pts mounted?) - posix_openpt (19: No such device)
Selecting previously unselected package kmod.
(Reading database ... 7449 files and directories currently installed.)
Preparing to unpack .../archives/kmod_18-3_i386.deb ...
Unpacking kmod (18-3) ...
Selecting previously unselected package libuuid-perl.
Preparing to unpack .../libuuid-perl_0.05-1+b1_i386.deb ...
Unpacking libuuid-perl (0.05-1+b1) ...
Selecting previously unselected package linux-base.
Preparing to unpack .../linux-base_3.5_all.deb ...
Unpacking linux-base (3.5) ...
Selecting previously unselected package libklibc.
Preparing to unpack .../libklibc_2.0.4-2_i386.deb ...
Unpacking libklibc (2.0.4-2) ...
Selecting previously unselected package klibc-utils.
Preparing to unpack .../klibc-utils_2.0.4-2_i386.deb ...
Unpacking klibc-utils (2.0.4-2) ...
Selecting previously unselected package cpio.
Preparing to unpack .../cpio_2.11+dfsg-4.1+deb8u1_i386.deb ...
Unpacking cpio (2.11+dfsg-4.1+deb8u1) ...
Selecting previously unselected package busybox.
Preparing to unpack .../busybox_1%3a1.22.0-9+deb8u1_i386.deb ...
Unpacking busybox (1:1.22.0-9+deb8u1) ...
Selecting previously unselected package initramfs-tools.
Preparing to unpack .../initramfs-tools_0.120+deb8u3_all.deb ...
Unpacking initramfs-tools (0.120+deb8u3) ...
Selecting previously unselected package linux-image-3.16.0-4-686-pae.
Preparing to unpack .../linux-image-3.16.0-4-686-pae_3.16.51-2_i386.deb ...
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/i386-linux-gnu/perl/5.20.2 /usr/local/share/perl/5.20.2 /usr/lib/i386-linux-gnu/perl5/5.20 /usr/share/perl5 /usr/lib/i386-linux-gnu/perl/5.20 /usr/share/perl/5.20 /usr/local/lib/site_perl .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Unpacking linux-image-3.16.0-4-686-pae (3.16.51-2) ...
Selecting previously unselected package live-boot-initramfs-tools.
Preparing to unpack .../live-boot-initramfs-tools_4.0.2-1_all.deb ...
Unpacking live-boot-initramfs-tools (4.0.2-1) ...
Selecting previously unselected package live-boot.
Preparing to unpack .../live-boot_4.0.2-1_all.deb ...
Unpacking live-boot (4.0.2-1) ...
Processing triggers for systemd (215-17+deb8u7) ...
Setting up kmod (18-3) ...
Setting up libuuid-perl (0.05-1+b1) ...
Setting up linux-base (3.5) ...
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/i386-linux-gnu/perl/5.20.2 /usr/local/share/perl/5.20.2 /usr/lib/i386-linux-gnu/perl5/5.20 /usr/share/perl5 /usr/lib/i386-linux-gnu/perl/5.20 /usr/share/perl/5.20 /usr/local/lib/site_perl .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Setting up libklibc (2.0.4-2) ...
Setting up klibc-utils (2.0.4-2) ...
Setting up cpio (2.11+dfsg-4.1+deb8u1) ...
update-alternatives: using /bin/mt-gnu to provide /bin/mt (mt) in auto mode
Setting up busybox (1:1.22.0-9+deb8u1) ...
Setting up initramfs-tools (0.120+deb8u3) ...
update-initramfs: deferring update (trigger activated)
Setting up linux-image-3.16.0-4-686-pae (3.16.51-2) ...
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/i386-linux-gnu/perl/5.20.2 /usr/local/share/perl/5.20.2 /usr/lib/i386-linux-gnu/perl5/5.20 /usr/share/perl5 /usr/lib/i386-linux-gnu/perl/5.20 /usr/share/perl/5.20 /usr/local/lib/site_perl .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-3.16.0-4-686-pae
live-boot: core filesystems devices utils udev blockdev.
Setting up live-boot-initramfs-tools (4.0.2-1) ...
update-initramfs: deferring update (trigger activated)
Setting up live-boot (4.0.2-1) ...
Processing triggers for systemd (215-17+deb8u7) ...
Processing triggers for initramfs-tools (0.120+deb8u3) ...
update-initramfs: Generating /boot/initrd.img-3.16.0-4-686-pae
live-boot: core filesystems devices utils udev blockdev.
root@debian:/# 
~~~

~~~
root@debian:/# passwd root
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
root@debian:/# 
~~~

~~~
root@debian:~# mkdir -p iso_live/image/{live,boot/grub}
~~~

~~~
root@debian:~# mksquashfs \
> iso_live/chroot \
> iso_live/image/live/filesystem.squashfs \
> -e boot
Parallel mksquashfs: Using 1 processor
Creating 4.0 filesystem on iso_live/image/live/filesystem.squashfs, block size 131072.
[=================================================================================================================================/] 11468/11468 100%

Exportable Squashfs 4.0 filesystem, gzip compressed, data block size 131072
	compressed data, compressed metadata, compressed fragments, compressed xattrs
	duplicates are removed
Filesystem size 190807.47 Kbytes (186.34 Mbytes)
	47.07% of uncompressed filesystem size (405395.03 Kbytes)
Inode table size 130631 bytes (127.57 Kbytes)
	30.75% of uncompressed inode table size (424777 bytes)
Directory table size 120872 bytes (118.04 Kbytes)
	46.60% of uncompressed directory table size (259401 bytes)
Xattr table size 37 bytes (0.04 Kbytes)
	92.50% of uncompressed xattr table size (40 bytes)
Number of duplicate files found 249
Number of inodes 12562
Number of files 9427
Number of fragments 1125
Number of symbolic links  1532
Number of device nodes 7
Number of fifo nodes 0
Number of socket nodes 0
Number of directories 1596
Number of ids (unique uids + gids) 7
Number of uids 1
	root (0)
Number of gids 7
	root (0)
	shadow (42)
	utmp (43)
	tty (5)
	staff (50)
	adm (4)
	mail (8)
root@debian:~# 
~~~

~~~
root@debian:~# cp iso_live/chroot/boot/vmlinuz-3.16.0-4-686-pae iso_live/image/live/vmlinuz
root@debian:~# cp iso_live/chroot/boot/initrd.img-3.16.0-4-686-pae iso_live/image/live/initrd
root@debian:~# 
~~~

~~~
root@debian:~# (cd /usr/lib/grub/i386-pc && \
>     grub-mkimage \
>         --format=i386-pc \
>         --prefix="/boot/grub" \
>         --output=/root/iso_live/image/boot/grub/core.img \
>         linux \
>         normal \
>         iso9660 \
>         biosdisk
> )
root@debian:~# 
~~~

~~~
root@debian:~# (cd iso_live/image/boot/grub && \
>     cat \
>         /usr/lib/grub/i386-pc/cdboot.img \
>         core.img \
>     > bios.img
> )
root@debian:~# 
~~~

~~~
root@debian:~# xorriso \
>     -as mkisofs \
>     -iso-level 3 \
>     -full-iso9660-filenames \
>     -volid "DEBIAN_CUSTOM" \
>     -eltorito-boot \
>         boot/grub/bios.img \
>         -no-emul-boot -boot-load-size 4 -boot-info-table \
>         --eltorito-catalog boot/grub/boot.cat \
>     -output "iso_live/debian-custom.iso" \
>     "iso_live/image"
xorriso 1.4.6 : RockRidge filesystem manipulator, libburnia project.

Drive current: -outdev 'stdio:iso_live/debian-custom.iso'
Media current: stdio file, overwriteable
Media status : is blank
Media summary: 0 sessions, 0 data blocks, 0 data, 3173m free
Added to ISO image: directory '/'='/root/iso_live/image'
xorriso : UPDATE : 9 files added in 1 seconds
xorriso : UPDATE : 9 files added in 1 seconds
xorriso : UPDATE :  1.66% done
xorriso : UPDATE :  16.67% done
xorriso : UPDATE :  33.95% done
xorriso : UPDATE :  47.36% done, estimate finish Fri Apr 20 14:53:34 2018
xorriso : UPDATE :  60.73% done, estimate finish Fri Apr 20 14:53:34 2018
xorriso : UPDATE :  70.34% done, estimate finish Fri Apr 20 14:53:35 2018
xorriso : UPDATE :  80.11% done, estimate finish Fri Apr 20 14:53:35 2018
xorriso : UPDATE :  92.93% done
ISO image produced: 104460 sectors
Written to medium : 104460 sectors at LBA 0
Writing to 'stdio:iso_live/debian-custom.iso' completed successfully.

root@debian:~# 
~~~


### Referencias
[Will Haley](https://willhaley.com/blog/custom-debian-live-environment/)