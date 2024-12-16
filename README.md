# Quest2PyLoader
A tiny sideloader for the Quest2. Most sideloader applications come with alot of bloat and usually an app marketplace. Quest2PyLoader removes this 
and just creates an easy way to use the ADB commands to install your homebrew applications to your Quest device.
</br>
</br>
<b>1.) Setup Developer Mode on you Oculus Device:</b>
</br>
https://developer.oculus.com/documentation/native/android/mobile-device-setup/
</br>
</br>
<b>2.) Install ADB Platform tools by:</b>
</br></br>
<b>Windows:</b>
</br>
Download: https://developer.android.com/tools/releases/platform-tools
</br>
Extract to C: so it's C:\platform-tools
</br>
Run Powershell as Admin type: setx PATH "%PATH%;C:\platform-tools"
</br></br>
<b>Mac:</b>
</br>
brew install --cask android-platform-tools
</br></br>
<b>Linux via APT:</b>
</br>
sudo apt-get install android-tools-adb -y
</br>

<b>3.) Drivers for Windows</b>
</br>
https://developer.oculus.com/downloads/package/oculus-adb-drivers/
</br>
</br>
<b>4.) Run </b>
<b>Run Quest2PyLoader by:</b>
</br>
<i>python Quest2PyLoader.py</i> or with <i>python3 Quest2PyLoader.py</i>
</br>
</br>
<img src="https://raw.githubusercontent.com/MitchellKopczyk/Quest2PyLoader/main/quest2py.png" width="500" height="350"> 
