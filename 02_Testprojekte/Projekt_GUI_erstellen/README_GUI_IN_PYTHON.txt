PyQt5 Designer um GUI zu erstellen


Folgender Code wandelt erstellte GUI von .ui zu .py um.

>> pyuic5 –x "filename".ui –o "filename".py

Alternativer Code falls obiger bei Batch nicht funktioniert https://stackoverflow.com/questions/13551316/error-converting-ui-file-to-py-file
>> pyuic5 -x filename.ui > filename.py