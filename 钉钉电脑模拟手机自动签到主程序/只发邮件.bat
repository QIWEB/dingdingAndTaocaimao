rem @echo off
title ��������ģ���ֻ��Զ�ǩ��������
set script_bat=C:\Users\zhangqi\Desktop\dingding

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

