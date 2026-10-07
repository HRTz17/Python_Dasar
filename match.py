hari    =   "sabtu"

match	hari:
    case "sabtu"|"minggu":
      print("Libur!") 
    case    "senin":
      print("Semangat!")
    case	_:
      print("Hari	kerja")