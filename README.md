# pygoogle_image

### Pygoogle_image extracts images from google image, allowing you to download as many images as you like with just one keyword. Let's exemplify how to download images from google images for you.</br>

### To use this updated branch, download the code locally and use (for now)</br>
```
pip install -e .
```

### first import the package</br>
```
pip install pygoogle-image
```

### in the example below we will pass on the keyword 'cat' and we will limit the number of images to be downloaded to only 10</br>
```
from pygoogle_image import image as pi

pi.download(keywords='gatos', limit=10)
````
### if you don't specify a directory, pygoogle_image will create a folder called image at the root of the project. if you wish you can save it in a specific directory</br>
```
pi.download(keywords='gatos', limit=10, directory='c:\image')
```

