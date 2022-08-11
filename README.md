# jupyter-lab

## 一、安装jupyter和jupyter-lab库

1、打开 `Pydroid3 App` ，点击左上角菜单按钮，在弹出的菜单中点击Pip。

2、在Pip界面中点击 `QUICK INSTALL` ，在下方列表中找到 `jupyter` 并点击右侧的 `install` 进行安装。

3、安装完成后点击左上角返回按钮返回主界面，然后再点击左上角菜单按钮，在弹出的菜单中点击 `Terminal` 。

4、在 `Terminal` 中输入以下命令来安装 `jupyter-lab` 相关库。

```python
pip3 install jupyter-lsp jupyter-server jupyterlab jupyterlab-lsp jupyterlab-github
```



## 二、配置jupyter-lab登录密码

1、返回App主页面，点击左上角菜单按钮，在弹出的菜单中点击 `Terminal` 。

2、在 `Terminal` 中输入以下命令来设置登录密码。

```
jupyter-lab password
```

## 三、浏览器访问jupyter-lab

1、使用如下命令启动jupyter-lab，ip设置为本机的ip，端口自选一个可用的即可。

```
jupyter-lab --ip=示波器ip --port=xxxx
```

2、示波器本地访问，在浏览器输入如下网址

```
http://127.0.0.1:xxxx/lab
```

3、局域网下电脑浏览器访问，输入如下网址

```
http://示波器ip:xxxx/lab 
```
