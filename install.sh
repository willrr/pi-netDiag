#!/bin/sh
#install.sh

cd /home/pi
sudo apt-get -y install python3-tk fping vim unzip
wget https://github.com/willrr/pi-networkDiagnostics/archive/master.zip
unzip ./master.zip
cp -r ./pi-networkDiagnostics-master/ ./pi-networkDiagnostics/
rm -r ./pi-networkDiagnostics-master/
cd ./pi-networkDiagnostics/
cat > launcher.sh
echo "#!/#!/bin/sh" >> launcher.sh
echo "# launcher.sh" >> launcher.sh
echo "cd /" >> launcher.sh
echo "cd home/pi/pi-networkDiagnostics" >> launcher.sh
echo "python3 willrr.py" >> launcher.sh
echo "cd /" >> launcher.sh
sudo sed '3i@/home/pi/pi-networkDiagnostics/launcher.sh' /home/pi/.config/lxsession/LXDE-pi/autostart
echo "Installed"
