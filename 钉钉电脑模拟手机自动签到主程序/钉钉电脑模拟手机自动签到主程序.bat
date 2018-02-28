rem @echo off
title 钉钉电脑模拟手机自动签到主程序
set script_bat=C:\Users\zhangqi\Desktop\dingding
echo %date% %time%  钉钉电脑模拟手机自动签到主程序开始工作 > %script_bat%\qiweb_auto_log.txt
rem:::::::::::::::::::::::::::::::::::::::::::第一步产生随机36分钟内延迟执行::::::::::
rem @echo off   ::关闭命令回显
echo 8点45执行 定时任务
@REM 产生[0,36]间的随机数 
rem @echo off 
REM 启用延迟环境变量扩展 
setlocal enabledelayedexpansion 
REM 设置随机数的最小和最大值以及求模用的变量 
set min=0 
set max=2
set /a mod=!max!-!min!+1 
set /a r=!random!%%!mod!+!min! 
echo %r%
rem 上面产生随机分钟数 范围在8:45至9:21
set /a waitTime=%r%*60

ping 127.0.0.1 -n %waitTime% >nul

echo %date% %time%  第一步产生随机36分钟 完成 >> %script_bat%\qiweb_auto_log.txt


rem:::::::::::::::::::::::::::::::::::::::::::第二步调用鼠标点击软件 点击模拟器指定位置，Ctrl+F4启动签到脚本::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  生成vbs语句输出到temp.vbs
echo object.sendkeys "^{F4}">>temp.vbs
rem 生成第二条vba语句附加到temp.vbs,^{F4}表示发送ctrl+F4快捷键，可根据需求修改
temp.vbs
rem 执行temp.vbs
del /q temp.vbs
rem 删除调用完成的temp.vbs



echo %date% %time%  第二步调用鼠标点击软件 点击模拟器指定位置，Ctrl+F4启动签到脚本 完成 >> %script_bat%\qiweb_auto_log.txt

rem 这是签到后在足迹界面截图 耗时1分钟20秒
ping 127.0.0.1 -n 80 >nul

rem:::::::::::::::::::::::::::::::::::::::::::第三步调用截图软件Ctrl+Shift+F1截图::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  生成vbs语句输出到temp.vbs
echo object.sendkeys "^+{F1}">>temp.vbs
rem 生成第二条vba语句附加到temp.vbs,^+{F1}表示发送Ctrl+Shift+F1快捷键，可根据需求修改
temp.vbs
rem 执行temp.vbs
del /q temp.vbs
rem 删除调用完成的temp.vbs


echo %date% %time%  第三步调用截图软件Ctrl+Shift+F1截图 完成 >> %script_bat%\qiweb_auto_log.txt


rem 这是签到后在足迹界面返回到首页 耗时1分钟20秒
ping 127.0.0.1 -n 80 >nul

rem:::::::::::::::::::::::::::::::::::::::::::第四步调用鼠标点击软件 Ctrl+F7把签到足迹返回到钉钉首页::::::::::

echo set object^=createobject("wscript.shell")>temp.vbs
rem  生成vbs语句输出到temp.vbs
echo object.sendkeys "^{F7}">>temp.vbs
rem 生成第二条vba语句附加到temp.vbs,^{F7}表示发送Ctrl+F7快捷键，可根据需求修改
temp.vbs
rem 执行temp.vbs
del /q temp.vbs
rem 删除调用完成的temp.vbs


echo %date% %time%  第四步调用鼠标点击软件 Ctrl+F7把签到足迹返回到钉钉首页 完成 >> %script_bat%\qiweb_auto_log.txt
ping 127.0.0.1 -n 80 >nul

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

