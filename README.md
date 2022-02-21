# MacToManufacturer

#### A simple python library to find the manufacturer of a device by using macaddress.

### How to use:
<b>Example:</b>
```
from MacToManufacturer import MacToMan

macToManObj = MacToMan()
results = macToManObj.search("A8-93-4A-DA-6F-19")
print(results)

macToManObj.close()
```
You can also pass the macaddress seprated by ":"
```
from MacToManufacturer import MacToMan

macToManObj = MacToMan()
results = macToManObj.search("A8:93:4A:DA:6F:19")
print(results)

macToManObj.close()
```
<b>Note:</b> MacToManufacturer uses a csv file and searches through it so please call the close function as soon as you are done using MacToMan.
