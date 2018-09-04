# Description: Face and Eye Recognition

A simple python script utilizing the OpenCV framework and Haar Cascades to detect the users face and eyes from their webcam. So far the program only utilizes the Haar Cascade XML files from source. 


## Getting Started

This program is best run on the command line/terminal interface, and ensuring you have OpenCV and at least Python version 2.7 installed on your system. See the link below for information on installing OpenCV for Python. 

* [Source](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)


### Compilation

Make the following call from command line while in the source (src) folder. 

```
python main.py <first_name>
```

Ideally, this will be further built to take the detected images, filter out any unsatisfactory images, and learn the user's name, and facial characteristics over prolonged use of the program. 

### Terminating Webcam

In order end the recording of your webcam face and image detection, make sure you are actively on the webcam video and press the 'q' key on your keyboard. This will terminate the webcam session. 

### Limitations

Image processing is a CPU intensive process, and there are chances you will see labeling of incorrect images at times. 

## Built With

* [OpenCV](https://docs.opencv.org/3.0-beta/index.html#) - For image recognition software

## Author

* **Peter Dorsaneo** - *University of Central Florida* 

## License

This project is Free Open Source Software (FOSS), feel free to distribute with correct accreditation to the author. 

## Acknowledgments

* [Real Python Tutorial](https://realpython.com/face-recognition-with-python/) - For implementing Webcam class source code
* [Source Cascade Files](https://github.com/opencv/opencv/tree/master/data/haarcascades) - For sourcing cascade files
* [OpenCV w/ Python Docs](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html) - For documentation reference

