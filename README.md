
# Labelme to Icdar format and vice versa converter


The various text detection algorithms like Dbnet, Craft, East, and many more
uses icdar dataset. But a popular annotation tool called Labelme outputs labels in JSON format, so in order to use Labelme as an annotation tool,
to train these models Labelme's .json file should be converted to ICDAR .txt format.  


Additionally, in order to view the result in Labelme as well as the correct output given by the above-mentioned algorithms for retraining or incremental training. Output's .txt should be converted to  Labelme's .json file. 



## Deployment

For .json to .txt conversion run json2txt.py --json_dir=directory containing json files --text_dir=directory where text is to be saved

```bash
  python json2txt.py --json_dir=C:/json/ --text_dir=C:/text/
```
For .txt to .json conversion run txt2json.py --img_dir=directory containing images --text_dir=directory conatining text images/--json_dir=directory where json is to be saved

```bash
  python txt2json.py --img_dir=C:/images/ --text_dir=C:/text/ --json_dir=C:/json/
```


## If this repository helps you，please star it. Thanks.



