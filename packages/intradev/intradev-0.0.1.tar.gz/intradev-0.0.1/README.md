# IntraDev Library

IntraDev is a package intended to accelerate Python GUI creation.

- **Website:** https://intradev.com
- **Documentation:** https://intradev.com/doc
- **Mailing list:** https://mail.intradev.com/mailman
- **Source code:** https://github.com/asm3002/intradev
- **Bug reports:** https://github.com/asm3002/intradev/issues

It provides:

- a powerful GUI builder with minimal code
- customization of the GUI appearance
- a method to input / output files to a function

How To Use
----------------------
1. Install the IntraDev Library
For detailed tutorials on the use of the IntraDev Library, check out our YouTube channel.
If you have questions, post them **here** and we will make a YouTube tutorial if required.

```bash
pip install intradev
```
2. Import the Library
```python
import intradev as id
```
3. Create a GUI Data Model
```python
data = id.DataModel()
```
4. Add Functions, Inputs, and Outputs to the Data Model
```python
data.addInput("Input Filepath", id="0")
data.addFunction(functionName, "Button Label", inputMap={"inputFilePath": "0"})
data.addOutput("Output File", id="filepath")
```
5. Build GUI Using Data Model
```python
id.buildUI(data, title="GUI Application Title")
```

Code of Conduct
----------------------

IntraDev is a privately owned open source project developed by Aiden McDougal to support
the IntraDev Professional Tools. This package is open source to promote Python GUI development
in both professional and academic environments. The IntraDev leadership has made a strong
commitment to creating an easy to use, powerful tool to accelerate Python tool creation. 

