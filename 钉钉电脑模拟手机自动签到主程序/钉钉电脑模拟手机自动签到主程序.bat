rem @echo off
title ��������ģ���ֻ��Զ�ǩ��������
set script_bat=C:\Users\zhangqi\Desktop\dingding
echo %date% %time%  ��������ģ���ֻ��Զ�ǩ��������ʼ���� > %script_bat%\qiweb_auto_log.txt
rem:::::::::::::::::::::::::::::::::::::::::::��һ���������36�������ӳ�ִ��::::::::::
rem @echo off   ::�ر��������
echo 8��45ִ�� ��ʱ����
@REM ����[0,36]�������� 
rem @echo off 
REM �����ӳٻ���������չ 
setlocal enabledelayedexpansion 
REM �������������С�����ֵ�Լ���ģ�õı��� 
set min=0 
set max=2
set /a mod=!max!-!min!+1 
set /a r=!random!%%!mod!+!min! 
echo %r%
rem ���������������� ��Χ��8:45��9:21
set /a waitTime=%r%*60

ping 127.0.0.1 -n %waitTime% >nul

echo %date% %time%  ��һ���������36���� ��� >> %script_bat%\qiweb_auto_log.txt


rem:::::::::::::::::::::::::::::::::::::::::::�ڶ��������������� ���ģ����ָ��λ�ã�Ctrl+F4����ǩ���ű�::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  ����vbs��������temp.vbs
echo object.sendkeys "^{F4}">>temp.vbs
rem ���ɵڶ���vba��丽�ӵ�temp.vbs,^{F4}��ʾ����ctrl+F4��ݼ����ɸ��������޸�
temp.vbs
rem ִ��temp.vbs
del /q temp.vbs
rem ɾ��������ɵ�temp.vbs



echo %date% %time%  �ڶ��������������� ���ģ����ָ��λ�ã�Ctrl+F4����ǩ���ű� ��� >> %script_bat%\qiweb_auto_log.txt

rem ����ǩ�������㼣�����ͼ ��ʱ1����20��
ping 127.0.0.1 -n 80 >nul

rem:::::::::::::::::::::::::::::::::::::::::::���������ý�ͼ���Ctrl+Shift+F1��ͼ::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  ����vbs��������temp.vbs
echo object.sendkeys "^+{F1}">>temp.vbs
rem ���ɵڶ���vba��丽�ӵ�temp.vbs,^+{F1}��ʾ����Ctrl+Shift+F1��ݼ����ɸ��������޸�
temp.vbs
rem ִ��temp.vbs
del /q temp.vbs
rem ɾ��������ɵ�temp.vbs


echo %date% %time%  ���������ý�ͼ���Ctrl+Shift+F1��ͼ ��� >> %script_bat%\qiweb_auto_log.txt


rem ����ǩ�������㼣���淵�ص���ҳ ��ʱ1����20��
ping 127.0.0.1 -n 80 >nul

rem:::::::::::::::::::::::::::::::::::::::::::���Ĳ������������� Ctrl+F7��ǩ���㼣���ص�������ҳ::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  ����vbs��������temp.vbs
echo object.sendkeys "^{F7}">>temp.vbs
rem ���ɵڶ���vba��丽�ӵ�temp.vbs,^{F7}��ʾ����Ctrl+F7��ݼ����ɸ��������޸�
temp.vbs
rem ִ��temp.vbs
del /q temp.vbs
rem ɾ��������ɵ�temp.vbs


echo %date% %time%  ���Ĳ������������� Ctrl+F7��ǩ���㼣���ص�������ҳ ��� >> %script_bat%\qiweb_auto_log.txt
ping 127.0.0.1 -n 80 >nul

rem:::::::::::::::::::::::::::::::::::::::::::���岽����blat���ʼ�::::::::::



:::::::::::::: ��������::::::::::::::
rem �ʼ�����
set from=ccccccccccccc.cn
set user=ccccccccc.cn
set pass=ccccc
set to=ccccccccccn
rem ,�����䶺�Ÿ���
set subj=������ʱǩ���ɹ�֪ͨ
set mail=%script_bat%\qiweb_auto_log.txt
rem ���� �������κ�*.jpg *.txt
set attach=%script_bat%\*.png
set server=smtp.qiye.163.com
set debug=-debug -log %script_bat%\blat.log -timestamp

rem ����blat���ʼ����ߵ�Ŀ¼
set blat_home=%script_bat%

echo %date% %time% ��ʼ���ʼ�>> %script_bat%\qiweb_auto_log.txt
::::::::::::::::: ����blat �����ʼ�:::::::::::::::::
%blat_home%\blat %mail% -to %to% -base64 -charset Gb2312 -subject %subj% -attach %attach% -server %server% -f %from% -u %user% -pw %pass% %debug%

