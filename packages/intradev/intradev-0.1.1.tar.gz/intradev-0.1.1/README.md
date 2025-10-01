# IntraDev Library

IntraDev is a free to use package intended to accelerate Python GUI creation. Whether a GUI needed to quickly share a internal Tool in industry, acadamia, or personal projects, Intradev provides a Python GUI solution in as little as 4 lines of code.  This can reduce development time significantly and make tools easier to distribute and maintain.  Although this library can be used for any project, it is designed to be used with the IntraDev Distribution Suite to efficiently create, share, and manage Python tools with colleagues and friends.  For more information, check out the links below!

- **Website:** https://intradev.com
- **Documentation:** https://intradev.com/doc
- **Mailing list:** https://mail.intradev.com/mailman
- **Source code:** https://github.com/asm3002/intradev
- **Bug reports:** https://github.com/asm3002/intradev/issues

This open-source library provides:

- a powerful GUI builder with minimal code
- customization of the GUI appearance
- an effective method to input / output files to functions

How To Use
----------------------
For detailed tutorials on the use of the IntraDev Library, check out our YouTube channel.
If you have questions, post them **here** and we will make a YouTube tutorial if required.

1. Install the IntraDev Library
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
4. Input GUI Metadata
```python
data.title("Test GUI Application")
data.description("This is a demo description for an IntraDev generated GUI!")
data.directions(["1. First direction step.",
                 "2. Second direction step.",])
```
5. Add Functions, Inputs, and Outputs to the Data Model
```python
data.addInput("Input Filepath", id="0")
data.addFunction(functionName, "Button Label", inputMap={"inputFilePath": "0"}, outputIDs=["filepath"])
data.addOutput("Output File", id="filepath")
```
6. Build GUI Using Data Model
```python
data.buildUI()
```

Code of Conduct
----------------------

IntraDev is a privately-owned open source project developed by Aiden McDougal to support
the IntraDev Professional Tools. This package is open source to promote Python GUI development
in both professional and academic environments. The IntraDev leadership has made a strong
commitment to creating an easy to use, powerful tool to accelerate Python tool creation. 

