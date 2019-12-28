
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# GCPCsvHunt 

#### what is GCPCsvHunt  ?
* GCP Csv Hunt is a open Source Python Modules that allows you to download all the Files from the GCP bucket with 2 lines of
python code check ouyt the example on How to use it 



## Dependencies 

```bash
pip install google-cloud-storage
pip install pandas

```


## Installation

```bash
pip install GCPCsvHunt
```
## Usage


```python

from gcpcsvhunt.gcpcsvhunt import GCPCsvHunt


pathToJsonFile = 'PATH TO YOUR JSON FILE '
BucketName = 'BUCKET NAME GOES HERE '
prefix = ''             # Searches in Outer Directory

obj = GCPCsvHunt(path=pathToJsonFile, bucketName=BucketName)

data = obj.getAllCSV(prefix=prefix)         # Return list of Objects

df1 = data.pop()                            # Pop the First Pandas Object
print(df1.data)                             # Print Pandas Data Frame

```

---------------------------------------------------
<img width="680" alt="Screen Shot 2019-12-28 at 11 45 22 AM" src="https://user-images.githubusercontent.com/39345855/71546736-9700be00-2967-11ea-9ddb-bdeb76de9fd5.png">


### Youtube Links to Tutorials 
* Tutorial : https://www.youtube.com/watch?v=Cd7v8UtyFpw


## Authors

## Soumil Nitin Shah 
Bachelor in Electronic Engineering |
Masters in Electrical Engineering | 
Master in Computer Engineering |

* Website : https://soumilshah.herokuapp.com
* Github: https://github.com/soumilshah1995
* Linkedin: https://www.linkedin.com/in/shah-soumil/
* Blog: https://soumilshah1995.blogspot.com/
* Youtube : https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber
* Facebook Page : https://www.facebook.com/soumilshah1995/
* Email : shahsoumil519@gmail.com



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


