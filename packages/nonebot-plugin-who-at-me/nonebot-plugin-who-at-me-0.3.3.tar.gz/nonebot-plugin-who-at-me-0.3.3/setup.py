# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_who_at_me']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.8.0,<23.0.0',
 'nonebot-adapter-onebot>=2.1.1,<3.0.0',
 'nonebot2>=2.0.0-beta.4,<3.0.0',
 'peewee>=3.14.4',
 'pydantic==2.10.6']

setup_kwargs = {
    'name': 'nonebot-plugin-who-at-me',
    'version': '0.3.3',
    'description': 'Find who on earth has ated you',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-who-at-me\n\n_✨ 看看是谁又在艾特我 ✨_\n</div>\n  \n # 说明\n 你是否遇到过这种情景：你点进一个99+的QQ群，发现有人艾特/回复过你，你满心期待地去查看，结果腾讯告诉你消息过多无法定义到上下文。现在你只需要部署一个机器人卧底即可找出到底是谁艾特了你。\n # 安装\n通过`pip`或`nb`安装；\n需要协议端支持转发合并消息。\n\n命令：\n```shell\npip install nonebot-plugin-who-at-me\n```\n```shell\nnb plugin install nonebot-plugin-who-at-me\n```\n# 配置\n记得配置SUPERUSERS\n```shell\nreminder_expire_time 合并转发消息记录的超时时间, 单位为天\n```\n# 使用\n<div align="center">\n\n（这里默认COMMAND_START为"/"）\n| 命令              | 描述              |\n| ------------------ | --------------- |\n|谁艾特我 | 查看到底是谁艾特了你       |\n|/clear_db     | 清理当前用户的消息记录 |\n|/clear_all     | 清理全部消息记录     |\n\n结果将以合并转发形式发送\n',
    'author': 'SEAFHMC',
    'author_email': 'soku_ritsuki@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SEAFHMC/nonebot-plugin-who-at-me',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
