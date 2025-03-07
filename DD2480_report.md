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
**3h**

3. reading documentation;  
***1,5h**
zulip: 0,5h  
OCRmyPDF: 1h

4. configuration and setup;  
**4,5h**
zulip: 1,5h setting up a vm and running tests  
OCRmyPDF: 3h running tests, installing dependencies and so on

5. analyzing code/output;  
**3h**
zulip: 0,5h
OCRmyPDF: 2,5h

6. writing documentation;  
**0,5h**
OCRmyPDF: 0,5h

7. writing code;  
**4h**
OCRmyPDF: 4h 

8. running code?  
**2h**
OCRmyPDF: 2h


### Eren Özogul
1. plenary discussions/meetings;  
**1.5h**

2. discussions within parts of the group;  
**3h**

3. reading documentation;  
***2h**
zulip: 0,5h  
OCRmyPDF: 1,5h

4. configuration and setup;  
**4h**
zulip: 1h setting up a vm  
OCRmyPDF: 3h running tests, installing dependencies

5. analyzing code/output; 
**3h**
OCRmyPDF: 3h 

6. writing documentation;  
**0,5h**
OCRmyPDF: 0,5h

7. writing code; 
**5h** 

8. running code?  
**2h** 

### Ryll Åman
1. plenary discussions/meetings;  
**1,5h**

2. discussions within parts of the group;  
**1h**

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
**6h**  
zulip: 1h  
OCRmyPDF: 5h

6. writing documentation;  
**4h**

7. writing code;  
**1h**

8. running code?  
**6h**  
zulip: 1h  
OCRmyPDF: 5h

### Sebastian Kristoffersson
1. plenary discussions/meetings;  
   **1,5h**
2. discussions within parts of the group;  
    **3.5h** (Youngbin Pyo)
        1,5h  planning and dividing work and starting
        2h integrating parts of work and finalizing implementation

3. reading documentation;  
    **2h**  
    zulip: 1h  
    OCRmyPDF: 1h
        
4. configuration and setup;  
    **2h**  
    zulip: 0.5h setting up environment on vm and running tests
    OCRmyPDF: 1h understanding project, installing and using on vm (not sucessful) 
    OCRmyPDF: 0.5h installing project and dependencies for windows (tesseract, ghostscript) and running tests

5. analyzing code/output;  
    **3h**
    zulip: 0.5h
    OCRmyPDF: 2.5h 

6. writing documentation; 
    **1h**

7. writing code;
    **6h**
    4h : barcode implementation 
    2h: integration and finilazing with codebase 

8. running code?  
    **2h**


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

Our experience with documentation on contributing and engaging with the community varied significantly across different projects. While all communities were welcoming, not all provided clear guidelines on how to contribute effectively. Specifically, our final project (`OCRmyPDF`) lacked information on dependency management and the tools used. This created unnecessary hurdles when setting up the environment. The differences in onboarding were quite noticeable, each team member encountered different issues with `OCRmyPDF`, many of which could have been easily avoided with just a few paragraphs outlining setup instructions and dependencies.

Working with a larger codebase presented challenges in adding functionality. Even minor changes to one part of the code often led to unintended test failures elsewhere, highlighting the complexity of maintaining and expanding an existing project.

Problems with our inital project selections required us to change projects twice, forcing us to work under a much tighter deadline. To manage this, we divided our group into sub-teams: two members focused on implementation, two on writing tests, and the fifth took on coordination, documentation, and reviewing code to ensure coherence. This structure significantly improved our teamwork and communication, allowing us to work efficiently under time constraints.

Additionally, we have enhanced our proficiency in Git, improved our ability to collaborate on larger projects, and become more adept at managing dependencies across different environments.

In terms of the Essence framework, we are still currently at the In-Place stage, meaning the entire team is involved in evaluating and adapting our way of working. However, there is still room for improvement. One key area we identified is early-stage communication. Our project selection took longer than necessary due to other commitments, which delayed our ability to establish a clear plan from the beginning. If we had set up a structured project plan earlier, it would have likely streamlined our workflow and improved overall collaboration.