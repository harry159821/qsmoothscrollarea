@echo off
set DestPath=%~dp0
set DestExt=*.exp
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.ilk
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.obj
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.pch
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.tlog
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.idb
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.lastbuildstate
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.CppClean.log
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.tlb
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.tds
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.map
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.res
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.tds
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.ipch
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.obj
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.pch
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.intermediate.manifest
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.embed.manifest
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.vcxprojResolveAssemblyReference.cache
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.unsuccessfulbuild
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)
set DestExt=*.sdf
for /f "delims=" %%i   in ('dir  /b/a-d/s  %DestPath%\%DestExt%')  do (
echo %%i
del %%i
)

del %DestPath%\Win32\Debug\AlgDesigner.pdb
del %DestPath%\Win32\Release\AlgDesigner.pdb
