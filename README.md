# Facebook Information Metadata Update
Script to update the metadata of all downloaded images and files you've shared and received on facebook
By default all of the images and files have the created and modified date of when FB completed the compilation of data for you. Not helpful if you want to group images by date.

This script scrapes the message_#.html files for images, gets the timestamp when the image was sent and then updates the image metadata with that timestamp.
It's not going to be 100% accurate of when the image was actually created, but it's close enough.

Firstly have python3 installed
Secondly install the following packages

```
pip install win32-setctime
pip install python-dateutil
pip install bs4
pip install pillow
```
Once you've downloaded all of your facebook data and extracted all of the folders, download the python file and put it in the same location like this.

![image](https://github.com/Kharliah/facebook-information-metadata-update/assets/105899626/ec0fcbd7-bc7a-4017-aa4b-4724814f146c)

Open the file in IDLE and run it.

Took about 10 minutes to process 22GB/68,000 files and now everything is good with the world once more

![image](https://github.com/Kharliah/facebook-information-metadata-update/assets/105899626/9aa24d33-a65f-4fe4-9ed1-93c59fa68d53)
