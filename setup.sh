RS="\033[0;31m"
YS="\033[1;33m"
CE="\033[0m"


#color end
CE="\033[0m"
#red start
RS="\033[0;31m"
#green start
GN="\033[0;32m"
#white start
WHS="\033[0m"

echo -e ""$GN"["$RS"+"$GN"]"$CE" Installing requirments"$C""
{
pkg update
pkg -y install git
pkg -y install python
pkg -y install android-tools
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install adb
apk update
apk add git
apk add python3
apk add android-tools
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm android-tools
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y android-tools
yum -y install git
yum -y install python3
yum -y install android-tools
dnf -y install git
dnf -y install python3
dnf -y install android-tools
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install android-tools
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y android-tools
} &> /dev/null

}
sleep 1
echo -e ""$GN"["$RS"+"$GN"]"$CE" Requierments successfully installed!"$C""
sleep 1