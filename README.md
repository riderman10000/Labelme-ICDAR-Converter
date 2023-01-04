
# Labelme to Icdar format and vice versa converter


The various text detection algorithms like Dbnet, Craft, East, and many more
uses icdar dataset. But a popular annotation tool called Labelme outputs labels in JSON format, so in order to use Labelme as an annotation tool,
to train these models Labelme's .json file should be converted to ICDAR .txt format.  


Additionally, in order to view the result in Labelme as well as the correct output given by the above-mentioned algorithms for retraining or incremental training. Output's .txt should be converted to  Labelme's .json file. 



## Deployment

For .json to .txt conversion put .json file in json directory,
the output will be saved in txt directory.

```bash
  python json2txt.py
```
For .txt to .json conversion put image and text file in img+txt directory, the output will be saved in same directory.

```bash
  python txt2json.py
```


## If this repository helps you，please star it. Thanks.



