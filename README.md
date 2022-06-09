# webp-auto-convert
Automatically convert .webp to .png, .jpg on download

# How to use
**This requires <a href="https://ffmpeg.org/">ffmpeg</a> to be installed and set as a enviroment variable**
After you install the newest release find a webp file on your pc and open it with the exe.

**Don't to forget check: "Always use this app to open .webp files"**

<img src="https://user-images.githubusercontent.com/73427833/172900812-d8e52995-5749-4845-9958-6d349853899a.png" width="250"></img>


# Example

https://user-images.githubusercontent.com/73427833/172898885-019fc6c9-3a38-4e4d-905b-09e9de182dc3.mp4


# Configuration

~~~json
{
    "remove-on-completion": false,
    "open-on-completion": true
}
~~~
remove-on-completion - Remove webp file after completion <br>
open-on-completion - Open output file with default image viewer


