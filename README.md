# UMOOC-Auto-Sign
这不是给超星平台用的！！！！这是给优慕课用的！！！（只在重庆医科大学的平台进行过半可行性测试，签到部分未经过测试，建议不要YOLO）

只需把配置信息填写好，就可以把它部署在你的服务器上半自动运行了（需要每次发布签到二维码后更改脚本内的内容）

自启推荐使用crontab

依赖环境：Python3，requests库

你需要填写的内容有
学号，密码的MD5值（请务必用小写），签到二维码扫描后的addStudentSign.do?等等整串内容，并使用抓包软件获取签到时的parentID（我不知道每次会不会变动，建议各位也多试一试）

本脚本未提供多门课签到支持，有多门课需求的可以考虑多开达到多门签到效果

进一步地，你可以去https://sc.ftqq.com/ 配置你的自动签到后微信推送——每天早上服务器自动签到之后会向你推送签到后的内容，如果你看到{"datas":{"id":xxxxx,"signTime":"xxxx-xx-xx xx:xx:xx","userId":xxxxxx,"seq":xxx},"status":1,"sessionid":"xxxxxxxxxxxxxxxxxxxxxxxxxxxx"}则说明签到成功

Enjoy your sleep! 不要忘记回头继续上课哦！
