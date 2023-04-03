import os
 import time
# Set up variables for the installation
hostname = "arch"
username = "user"
password = "123"
device = "/dev/sda"
print("user - user ")
print("password - 123 ")

 time.sleep(5)
# Prepare the disk
os.system("sgdisk -Z " + device)
os.system("parted " + device + " -- mklabel gpt")
os.system("parted " + device + " -- mkpart primary ext4 1MiB -8GiB")
os.system("parted " + device + " -- mkpart primary linux-swap -8GiB 100%")
os.system("mkfs.ext4 " + device + "1")
os.system("mkswap " + device + "2")
os.system("swapon " + device + "2")
 
# Mount the root file system
os.system("mount " + device + "1 /mnt")
 
# Install Arch Linux base system
os.system("pacstrap /mnt base base-devel")
 
# Generate the fstab file
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
 
# Set up the locale
os.system("arch-chroot /mnt ln -sf /usr/share/zoneinfo/Europe/London /etc/localtime")
os.system("arch-chroot /mnt hwclock --systohc")
os.system("echo en_GB.UTF-8 UTF-8 > /mnt/etc/locale.gen")
os.system("arch-chroot /mnt locale-gen")
os.system("echo LANG=en_GB.UTF-8 > /mnt/etc/locale.conf")
 
# Set the hostname
os.system("echo " + hostname + " > /mnt/etc/hostname")
 
# Set up the network
os.system("echo 127.0.0.1 localhost >> /mnt/etc/hosts")
os.system("echo ::1 localhost >> /mnt/etc/hosts")
os.system("echo 127.0.1.1 " + hostname + " >> /mnt/etc/hosts")
 
# Install GRUB bootloader
os.system("arch-chroot /mnt pacman -Sy grub")
os.system("arch-chroot /mnt grub-install --target=i386-pc --recheck " + device)
os.system("arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg")
 
# Set up the root password
os.system("arch-chroot /mnt sh -c 'echo -n \"root:" + password +
