rem @echo off
title 钉钉电脑模拟手机自动签到主程序
set script_bat=C:\Users\zhangqi\Desktop\dingding

rem:::::::::::::::::::::::::::::::::::::::::::第五步调用blat发邮件::::::::::



:::::::::::::: 参数设置::::::::::::::
rem 邮件设置
set from=ccccccccccccc.cn
set user=ccccccccc.cn
set pass=ccccc
set to=ccccccccccn
rem ,多邮箱逗号隔开
set subj=钉钉定时签到成功通知
set mail=%script_bat%\qiweb_auto_log.txt
rem 附件 可以是任何*.jpg *.txt
set attach=%script_bat%\*.png
set server=smtp.qiye.163.com
set debug=-debug -log %script_bat%\blat.log -timestamp

rem 就是blat发邮件工具的目录
set blat_home=%script_bat%

echo %date% %time% 开始发邮件>> %script_bat%\qiweb_auto_log.txt
::::::::::::::::: 运行blat 发送邮件:::::::::::::::::
%blat_home%\blat %mail% -to %to% -base64 -charset Gb2312 -subject %subj% -attach %attach% -server %server% -f %from% -u %user% -pw %pass% %debug%

