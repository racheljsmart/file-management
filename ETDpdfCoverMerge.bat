setlocal enabledelayedexpansion
for %%# in (*_coverpage.pdf) do (
    set n=%%~n#
    set n=!n:~0,-10!
    pdftk A=!n!.pdf B=%%# cat B A output C:\PDF_test\!n!.pdf
)
PAUSE