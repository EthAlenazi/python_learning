Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> child=[436,437,438,439,431,432,433,434,435]
>>> for x in child:
	print(x)

	
436
437
438
439
431
432
433
434
435
>>> child.append(430)
>>> for x in child:
	print(x)

	
436
437
438
439
431
432
433
434
435
430
>>> child.pop(8)
435
>>> child.remove(430)
>>> print(child)
[436, 437, 438, 439, 431, 432, 433, 434]
>>> 
