# webp-auto-convert
Automatically convert .webp to .png, .jpg on download

# How to use
**This requires <a href="https://ffmpeg.org/">ffmpeg</a> to be installed and set as an enviroment variable**
After you install the <a href="https://github.com/Vito510/webp-auto-convert/releases">newest release</a> find a webp file on your pc and open it with the exe.

<h2>Automatic conversion</h2>
<b>check "Always use this app to open .webp files"</b>

<img src="https://user-images.githubusercontent.com/73427833/172900812-d8e52995-5749-4845-9958-6d349853899a.png" width="250"></img>

In your web browser set the file type to automatically open<br>
![image](https://user-images.githubusercontent.com/73427833/172930443-fe28fb9b-8229-464e-bbf6-60a8c3dae312.png) <br>
<i>This is in chrome, it may be different in your web browser</i>


# Example

https://user-images.githubusercontent.com/73427833/172898885-019fc6c9-3a38-4e4d-905b-09e9de182dc3.mp4

**The console is hidden by default*

# Configuration

~~~json
{
    "remove-on-completion": false,
    "open-on-completion": true
    "hideconsole": true,
    "output-format": "png"
}
~~~
remove-on-completion - Remove webp file after completion <br>
open-on-completion - Open output file with default image viewer <br>
hideconsole - Don't show a console when converting a file <br>
output-format - Conversion output file format (Should support anything ffmpeg supports)


