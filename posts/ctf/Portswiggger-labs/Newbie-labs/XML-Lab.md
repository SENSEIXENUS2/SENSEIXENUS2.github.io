### XML-INJECTION (Portswigger labs)


### <u>Meaning of XML injection </u>
   XML means extensible markup language.It is a form of language designed for storing data and transporting data.It uses a tree-like structure for data storage.
It does not use predefined tags like html.Data can be given to describe the data.Xml applies important elements like xml entities,xml elements and
document type definition(DTD).The document type definition allows custom entities to declared within the declaration.
### Custom entities
For example

     <!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>
The value "my entity value" can be called with &myentity;
### Custom External entities
  External entities will lead us to the first portswigger challenge.This form of custom entities are declared outside the dtd.
For example

     <!DOCTYPE foo [ <!ENTITY ext SYSTEM "file:///path/to/file" > ]>
The file url can be used to read files like /etc/passwd etc

1st Challenge

Challenge description: Read /etc/passwd by XXE(XML External Entity)

![2023-10-18_14-29](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ab0f3280-ed81-4eb6-9059-916666c14bc2)