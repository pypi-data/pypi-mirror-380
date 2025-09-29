
import src.intradev as id


def flipFileLines(inputFilePath, outputFilePath="outputTestFile.txt"):
    # Read whole file and strip existing newlines safely (works even if last line has no newline)
    with open(inputFilePath, "r", encoding="utf-8", newline="") as f:
        lines = f.read().splitlines()
    # Reverse in place
    lines.reverse()
    # Write back, adding exactly one '\n' per line
    with open(outputFilePath, "w", encoding="utf-8", newline="\n") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"Flipped data written to {outputFilePath}")
    return {"filepath": outputFilePath}
    
data = id.DataModel()
data.addInput("Input Filepath", id="0")
data.addFunction(flipFileLines, "Flip Lines", inputMap={"inputFilePath": "0"})
data.addOutput("Output Text File", id="filepath")

id.buildUI(data, title="Test GUI Application", 
           description="This is a demo description for an IntraDev generated GUI!",
           directions=["1. Open a file using the file input.",
                       "2. Run the filter on the input file by clicking the button.",
                       "3. To use output data, click open to view file or locate path in file explorer."])