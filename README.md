# Image-To-ASCII
Image-To-ASCII is a python program to convert any image to a string of ASCII characters. When you run the command in your terminal, it will print a copy of the string and create a `txt` file in directory.

```
               _,gggg@@@@@@@@@ggg,_                
              g@@@@@@@@@@@@@@@@@@@@@_              
             j@@@"`"&@@@@@@@@@@@@@@@@              
             &@@[   J@@@@@@@@@@@@@@@@[             
             &@@@g,g@@@@@@@@@@@@@@@@@[             
             &@@@@@@@@@@@@@@@@@@@@@@@[             
             ************%@@@@@@@@@@@[             
    _,ggggggggggggggggggg@@@@@@@@@@@@[ ggggggg,    
  _g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[ @@@@@@@@@_  
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[ @@@@@@@@@@  
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[ @@@@@@@@@@@ 
j@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"J@@@@@@@@@@@ 
g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"_@@@@@@@@@@@@[
&@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&P"_g@@@@@@@@@@@@@@
&@@@@@@@@@@@@@#"__,,,,,,,,,,,,,,ggg@@@@@@@@@@@@@@@@
&@@@@@@@@@@@@"_g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
l@@@@@@@@@@@`_@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P
 @@@@@@@@@@@ g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
 &@@@@@@@@@@ &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@` 
  %@@@@@@@@@ &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"  
   "%&@@@@@@ &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P"   
             &@@@@@@@@@@@[____________             
             &@@@@@@@@@@@@@@@@@@@@@@@[             
             &@@@@@@@@@@@@@@@@@&&&@@@[             
             &@@@@@@@@@@@@@@@@`   %@@[             
             &@@@@@@@@@@@@@@@@_  _g@@C             
              *&@@@@@@@@@@@@@@@@g@@@"              
                "&&@@@@@@@@@@@@@&P"                
                    `""*****""`                    
                                                   
                 ___,,,,,,,,,,____                 
            _ggg@@@@@@@@@@@@@@@@@@@ggg_            
            &@@@@@@@@@@@@@@@@@@@@@@@@@@            
             ""M&&&&@@@@@@@@@@@&&&&P*"             
                        ```                        

```

The above art was generated with 
```
python main.py Python.png C:\Windows\Fonts\consola.ttf edge_detection=false threshold=50 char_limit=2000
```

I'm pretty pleased with the result of this project. It's not as fast as I'd hoped but it's much more cleanly written than my previous version and it was my first time using pytest.

## Requirements
Earlier versions may work but have not been tested.
 - Python 3.11
 - NumPy
 - Pillow
 - fontTools
 - OpenCV

## Usage
To run Image-To-ASCII:
```
python main.py image_path font_path
```

## Optional Arguments
Image-To-ASCII accepts the following keyword arguments:

 - Font size (in [ems](https://en.wikipedia.org/wiki/Em_(typography))) - Default 8:
```
font_size=integer
```

 - Character limit - Maximum number of characters of the output string. Many websites have a maximum of 2000 (eg Discord). If 0 or less, there is not limit on the length. Overrides font size. Default 0
```
char_limit=integer
```

 - Trim Whitespace - Enable or disable the trimming of whitespace around the edge of the image. Default true:
```
trim_whitespace=boolean
```

 - Threshold - The minimum pixel value to be considered a black pixel in the conversion. Default 127:
```
threshold=boolean
```

 - Inverse - Inverts the image so black pixels become white and vice versa. Default false:
```
inverse=boolean
```

 - Edge detection - Enable or disable edge detection on the input image. Uses [OpenCV Canny Edge Detection](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html). Default true:
 ```
 edge_detection=boolean
 ```

 - Minimum value - The minimum threshold used in the edge detection algorithm. Default 100:
```
min_val=integer
```

 - Maximum value - The maximum threshold use in the edge detection algorithm. Default 150:
```
max_val=integer
```

 - DPI - Used in calculating the font size in pixels. You probably don't want to change this. Default 96:
```
dpi=integer
```
