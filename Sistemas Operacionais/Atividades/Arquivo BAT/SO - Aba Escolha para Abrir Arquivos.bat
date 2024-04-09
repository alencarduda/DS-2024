@echo off
chcp 65001 >nul ::BIBLIOTECA (DIC.) UTF-8

echo Escolha uma opção
echo 1 - Abrir Claculadora
echo 2 - Abrir Blaco de Notas
echo 3 - Abrir Paint

::CRIAR UMA VARIÁVEL E ATRIBUIR UM VALOR
set /p opcao="Digite sua opção:"

if "%opcao%"=="1" (
    start calc.exe
	)
	
	if "%opcao%"=="2" (
    start notepad.exe
	)
	
	if "%opcao%"=="3" (
    start mspaint.exe
	)

::EXIBIR VARIÁVEL
echo %opcao%
echo %username%
echo %computername%

pause