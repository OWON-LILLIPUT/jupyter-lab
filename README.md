# jupyter-lab

## 一、安装jupyter和jupyter-lab库

1、将示波器连接到以太网。

2、打开 `Pydroid3 App` ，点击左上角菜单按钮，在弹出的菜单中点击Pip。

3、在Pip界面中点击 `QUICK INSTALL` ，在下方列表中分别找到如下的库并点击右侧的 `install` 进行安装。

```
jupyter    matplotlib    scipy
```

4、安装完成后点击左上角返回按钮返回主界面，然后再点击左上角菜单按钮，在弹出的菜单中点击 `Terminal` 。

5、在 `Terminal` 中输入以下命令来安装 `jupyter-lab` 相关库。

```sh
./Python/lib_installer.sh
```



## 二、配置jupyter-lab登录密码

1、返回App主页面，点击左上角菜单按钮，在弹出的菜单中点击 `Terminal` 。

2、在 `Terminal` 中输入以下命令来设置登录密码。

```sh
jupyter-lab password
```



## 三、浏览器访问jupyter-lab

1、使用如下命令启动jupyter-lab，ip设置为本机的ip，ip可自动选择，也可手动设置（wifi和以太网同时连接时），端口自选一个可用的即可。

- 自动选择ip

  ```
  ./Python/start_jupyterlab.sh 端口
  ```

- 手动设置ip

  ```
  ./Python/start_jupyterlab.sh ip地址 端口
  ```

2、示波器本地访问，在浏览器输入如下网址

```sh
http://127.0.0.1:端口/lab
```

3、局域网下电脑浏览器访问，输入如下网址

```sh
http://示波器ip:端口/lab 
```



## 四、运行示例脚本

1、使用浏览器进入 `jupyter-lab` ，点击左侧 `Github` 图标，在上方的 `GITHUB USER` 框中按 `用户名/仓库名` 的格式输入存放代码的仓库，例如 `OWON-LILIPUT/jupyter-lab` 。

2、在文件列表中选择你要运行的脚本双击打开即可运行。



## 五、保存.py文件

1、使用浏览器进入 `jupyter-lab` ，在主页的Launcher底部即可看见创建py文件的按钮。

2、点击创建py文件后将调试好的代码复制粘贴进去保存即可。
