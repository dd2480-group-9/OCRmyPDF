# Report for assignment 4

## Project

**Name**: OCRmyPDF

**URL**: [https://github.com/ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)

OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched or copy-pasted.

## Onboarding experience

#### Did you choose a new project or continue on the previous one?  
We chose a new project to work on.

#### If you changed the project, how did your experience differ from before?  
We changed projects twice: first to Zulip, and then to the final project, i.e. OCRmyPDF.

For Zulip, the experience was similar, although the setup and onboarding were far more complex due to the need for a virtual machine. These descriptions were not perfect and contained some errors (mostly due to being outdated), at least for Fedora, which made the setup take longer than necessary.

For OCRmyPDF, the onboarding experience was far worse. The complexity of the project and its dependencies is fairly small, making it fairly easy anyway, but some dependencies were not mentioned at all in the contribution guide, and that guide also did not include any instructions on the setup or how to get started.

## Effort spent

For each team member, how much time was spent in each of the categories.

For setting up tools and libraries (step 4), enumerate all dependencies
you took care of and where you spent your time, if that time exceeds
30 minutes.

### Alexandra Ejnervall
1. plenary discussions/meetings;  
**1,5h**

2. discussions within parts of the group;  
**1h**

3. reading documentation;  
***1,5h**
zulip: 0,5h  
OCRmyPDF: 1h

4. configuration and setup;  
**2,5h**
zulip: 1,5h setting up a vm and running tests  
OCRmyPDF: 2h running tests, installing dependencies and so on

5. analyzing code/output;  
**3h**
zulip: 0,5h
OCRmyPDF: 2,5h

6. writing documentation;  
**0,5h**
OCRmyPDF: 0,5h

7. writing code;  
**2,5h**
OCRmyPDF: 2,5h 

8. running code?  
**0,5h**
OCRmyPDF: 0,5h


### Eren Özogul
1. plenary discussions/meetings;  

2. discussions within parts of the group;  

3. reading documentation;  

4. configuration and setup;  

5. analyzing code/output;  

6. writing documentation;  

7. writing code;  

8. running code?  

### Ryll Åman
1. plenary discussions/meetings;  
**1,5h**

2. discussions within parts of the group;  

3. reading documentation;  
**2h**  
zulip: 1h  
OCRmyPDF: 1h

4. configuration and setup;  
**2h**  
zulip: 0.5h setting up pre-commit, vagrant and docker  
zulip: 0.5h setting up and running dev server environment and running tests  
OCRmyPDF: 0.5h trying to figure out structure of project, installing uv and syncing dependencies  
OCRmyPDF: 0.5h running tests and fixing extra missing dependencies (ocrmypdf, tesseract)

5. analyzing code/output;  
**2h**  
zulip: 1h  
OCRmyPDF: 1h

6. writing documentation;  
**2.5h**  
1h setting up issues and github structure  
0.5h summarizing onboarding experience and structuring report  
1h analyzing issue and specifying requirements

7. writing code;  

8. running code?  

### Sebastian Kristoffersson
1. plenary discussions/meetings;  

2. discussions within parts of the group;  

3. reading documentation;  

4. configuration and setup;  

5. analyzing code/output;  

6. writing documentation;  

7. writing code;  

8. running code?  

### Youngbin Pyo
1. plenary discussions/meetings;  

2. discussions within parts of the group;  

3. reading documentation;  

4. configuration and setup;  

5. analyzing code/output;  

6. writing documentation;  

7. writing code;  

8. running code?  


## Overview of issue(s) and work done.

**Title**: Auto-assign ASN using a barcode label

**URL**: [https://github.com/ocrmypdf/OCRmyPDF/issues/959](https://github.com/ocrmypdf/OCRmyPDF/issues/959)

This issue proposes automatically assigning an Archive Serial Number (ASN) to a document, replacing manual entry and enhancing the connection between physical and archived documents.

The feature integrates into the OCRmyPDF processing pipeline by embedding a barcode (or similar identifier) into the PDF; however, it is designed as a standalone enhancement that should not impact existing code or functionality.


## Requirements for the new feature

### Barcode Generation (REQ001)
A barcode should be created from given input data. The barcode should follow a standard format so that it can be easily recognized later for testing.

### Insert Barcode into PDF (REQ002)
The generated barcode should be added into a PDF file without changing or harming any of the existing content. The barcode should appear in a designated area that does not interfere with the original text or images.

### Read Barcode for Testing (REQ003)
The program should be able to read the barcode from the PDF to confirm that it was inserted correctly. This feature is used to test and verify that the barcode generation and insertion processes are working as expected.

### PDF Integrity Preservation (REQ004)
It should be ensured that the original layout, formatting, and content of the PDF remain unchanged after the barcode is added. The insertion process should not affect any of the existing document elements.

### Error Handling and User Alerts (REQ005)
Errors should be detected and handled during barcode generation, insertion, and reading. If something goes wrong, the program should provide clear error messages and instructions for the user to resolve the issue.

### User Settings for Barcode Appearance (REQ006)
Users should be allowed to set options for the barcode such as size, position, and style. These settings should be simple and user-friendly so that the barcode can be customized easily.

### Command-Line Interface (CLI) Support (REQ007)
The feature should include a simple command-line interface that allows users to easily run barcode generation and insertion when using the application. The CLI should provide clear instructions, options, and feedback for a smooth testing and usage experience.


## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).

## UML class diagram and its description

### Key changes/classes affected

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?
