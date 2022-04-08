# File-management
Standalone scripts for automating tasks.

## ETDpdfCoverMerge.bat (Windows)
The purpose of this batch script is to merge hundreds of ETD PDFs to their Coverpages. In the current ETDs workflow they are delivered to me separately for the file management stage of the ETDs workflow. The filenames are similar except Coverpages have a `_coverpage.pdf` at the end of the filename. This naming convention makes a simple pattern that is easy to be followed programatically.

Make sure to run this batch file in the same directory as the PDFs you want to merge together. You can choose whatever output path you want HOWEVER make sure the output file already exists or the outout will result in an error. Or you can add lines of code to the program to check for the output file and make if if it doesn't exist... If your PDF directory isn't in the same directory as pdftk then [create an environmental variable for pdftk](https://ourcodeworld.com/articles/read/240/how-to-edit-and-add-environment-variables-in-windows-for-easy-command-line-access).

Tools needed: PDFtk Server

## pullRecords.py

## remove_identifier.py

## splitPidsFile.py

## tabReplace.py
