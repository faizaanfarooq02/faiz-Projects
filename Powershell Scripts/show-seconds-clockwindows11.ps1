@echo off
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced' -Name 'ShowSecondsInSystemClock' -Value 1 -Type DWord"
powershell -Command "Stop-Process -Name explorer -Force"
powershell -Command "Start-Process explorer.exe"
