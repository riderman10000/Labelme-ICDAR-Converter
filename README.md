
# Labelme to Icdar format and vice versa converter

The various text detection algorithms like Dbnet, Craft, East, and many more
uses icdar dataset. But a popular annotation tool called Labelme outputs labels in JSON format, so in order to use Labelme as an annotation tool,
to train these models Labelme's .json file should be converted to ICDAR .txt format.  


Additionally, in order to view the result in Labelme as well as the correct output given by the above-mentioned algorithms for retraining or incremental training. Output's .txt should be converted to  Labelme's .json file. 


## Deployment

For .json to .txt conversion run json2txt.py 

--json-dir=directory containing json files 

--text-dir=directory where text is to be saved

```bash
  python json2txt.py --json-dir C:/json/ --text-dir C:/text/
```
or 
```bash
  python json2txt.py -j C:/json/ -t C:/text/
```
For .txt to .json conversion run txt2json.py 

--img-dir=directory containing images 

--text-dir=directory conatining text images/

--json-dir=directory where json is to be saved

```bash
  python txt2json.py --img_dir=C:/images/ --text-dir C:/text/ --json-dir C:/json/
```
or 
```bash
  python txt2json.py -i C:/images/ -t C:/text/ -j C:/json/
```
