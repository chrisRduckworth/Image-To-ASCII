# Image-To-ASCII
Image-To-ASCII is a python program to convert any image to a string of ASCII characters. When you run the command in your terminal, it will print a copy of the string and create a `txt` file in directory.

```
                           ._..r"+`f`"-^e=-.                                    
                     _.~O-f` ``            `r~w-                                
                   ._Y`                         ^<-                             
                 xp`                       -      `c>                           
               _`/     ||..-_ .--          -. _   !  \>                         
         - }> '!h        ^  `                  `       .                        
   xh_:<>   J? `                                        ~.                      
  (` |!!+=z]t!-                                          |.                     
  [..-c_}xy  . ?R_        . ---.            _.   ++-. _   w                     
  n`  j"hh`  J    .. +       .  _   -+_  >  `_ ..-.._  `  ' |                   
  ! 7 .\L|Wr ~`>-_      - `       -_   `   . `       '.   . |                   
  v!  |(^A|_  h`,|`\   7'              {  r           2  !  r                   
  y   |!/, *3(l=<(                  !. !              7  `  '                   
 /    |T'    `=[x'  \  .            ' /\  L           ` _   h                   
 |    !yj   ..s'     X  +        _.q%, '\  !       .r  '`   h                   
<^    b-<Srf`         '. `^--  .  /_<    '.  '    ' _<`    .|                   
k~` s;!k`[              '~.      >c`       ` -...- " -r.   !|                   
  ` 'f" jr       (_7-+-_.._ _```           __ .-.}j`<` '   HL       ,=_~        
         |       `   8x !`F r `FFFFFF+'F``z` -` -gy`      -V        T   !       
         \'            `(~__l-_______$  ..[--x'*7x       zC`        hx-=!       
          G              4>_]_  "C  `!````.   L/'        D)          | J!       
          `                '*{   !   !    L .0 '        zW         !H-`-\       
           \_                 '' w---!--=-P``  .y'     (7          /  }==)-__   
            ' ,            _ _              _..'      fx`         U /`[L     '. 
             `' _           "?>__        .-'``     _ 3'          nc`w.'      .| 
               '.T              `   ++   `       .?`             |!`Y  `.`` -J  
                 T.<                          ___>               |L \ .{r     M 
                   `>C-5.                 ,+:5>'`                ` \.!.C-._r 3( 
                       '^-e5_       .._ts !``                      `|'!    ~O   
                             `````````                              'm_.____U   
                                                                       `````    

```

The above art was generated with 
```
python main.py sunglasses.png C:\\Windows\\Fonts\\consola.ttf font_size=8 min_val=50 max_val=175
```

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
