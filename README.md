# jupyter-lab

English | [简体中文](README_zh.md)

[**SCPI_WiKi**](https://github.com/OWON-LILIPUT/jupyter-lab/wiki/SCPI)

## 1、Download Pydroid3 offline library

- Access the  [GoogleDrive](https://drive.google.com/file/d/1LjAXf11ubn4tivQE7K1kL6wfOIgLjqmN/view?usp=sharing) or [BaiduNetDisk](https://pan.baidu.com/s/1aID5IbcW23gGj2UfjrBmFQ) download `Pyroid3` offline library.
- After downloading, open the file management `App` of the machine. Enter the `Android` folder and create a new `obb` folder. Then enter the `obb` folder and create a new `ru.iiec.pythoid3.quickinstallrepo` folder.
- Put the downloaded offline library into the `ru.iiec.pythoid3.quickinstallrepo` folder.

## 2、Install jupyter libraries and jupyter-lab libraries

- Connect the oscilloscope to the Internet.

- Open the `Pydroid3` application. Click the menu button in the upper left corner and click `Pip` in the pop-up menu.

- Click `QUICK INSTALL` in the `Pip` interface. Find the following libraries in the list below and click `install`  button on the right to install.

  ```
  jupyter    PyQt5    matplotlib    scipy
  ```

- After installation, click the return button in the upper left corner to return to the main interface. Then click the menu button in the upper left corner and click `Terminal` in the pop-up menu.

- Enter the following command in Terminal to install the `jupyter-lab` related libraries.

  ```
  ./Python/lib_installer.sh
  ```



## 3、Configure login password for  jupyter-lab

- Back to main application interface. Click the menu button in the upper left corner and click `terminal`in the pop-up menu.

- Enter the following command in `Terminal` to set the login password.

  ```
  jupyter-lab password
  ```

  

## 4、Access jupyter-lab via browser

- Use the following command to start `jupyter lab`. `IP` need by this machine's ip. `IP` can be automatically selected or manually set (when the `WiFi` and `Ethernet` are connected at the same time). You can select one of the available ports.

  - Auto select `IP`

    ```
    ./Python/start_jupyterlab.sh port
    ```

    ![Screenshot_3-1](./resources/Screenshot_3-1.png)

  - Manual settings `IP`

    ```
    ./Python/start_jupyterlab.sh ip port
    ```

    ![Screenshot_3-2](./resources/Screenshot_3-2.png)

- Oscilloscope local access. Enter the following URL in the oscilloscope's browser.

  ```
  http://Oscilloscope's ip:port/lab
  ```

  ![Screenshot_3-3](./resources/Screenshot_3-3.png)

- Computer access in LAN. Enter the following URL in the browser.

  ```
  http://Oscilloscope's ip:port/lab
  ```

  ![Screenshot_3-4](./resources/Screenshot_3-4.png)



## 5、Run example code

- Run `GitHub` Code
  - Enter the `jupyter-lab` via browser. Click the `GitHub` icon on the left and input the repository name in the `GITHUB USER` box. Such as `OWON-LILIPUT/jupyter-lab`.
  
  - Select the code you want to run in the file list and double-click to run it.
  
    ![Screenshot_4-1](./resources/Screenshot_4-1.png)


- Run `Local` Code
  - Enter the `jupyter-lab` via browser.   Click the `Directory` icon on the left and find `Python directory` . We prepared some code in advance.
  
  - Select the code you want to run in the file list and double-click to run it.
  
    ![Screenshot_4-2](./resources/Screenshot_4-2.png)



## 6、Save .py file

- Enter the `jupyter-lab` via browser. The button to create a `py` file can be seen at the bottom of the `Launcher` on the home page.

  ![Screenshot_5-1](./resources/Screenshot_5-1.png)

- Click to create a `py` file. Then copy the code into the editor and save it.

  ![Screenshot_5-2](./resources/Screenshot_5-2.png)



## 7、Run .py code

- Open the `Pydroid3` application. Click the folder icon in the upper right corner of the home page and click `Open` in the pop-up options.

  ![Screenshot_6-1](./resources/Screenshot_6-1.png)

- Click `InternalStorage` in the pop-up interface to enter internal storage.

  ![Screenshot_6-2](./resources/Screenshot_6-2.png)

- Find the `py` file you saved in the internal storage and click to open it. Take the sample code as an example. Entering the internal storage and click the `Python` folder. After entering the `Python` folder, click `get_scope_wave.py` and it will be opened.

  ![Screenshot_6-3](./resources/Screenshot_6-3.png)

  ![Screenshot_6-4](./resources/Screenshot_6-4.png)

- Click the run button in the lower right corner to run the code.

![Screenshot_6-5](./resources/Screenshot_6-5.png)

![Screenshot_6-6](./resources/Screenshot_6-6.png)



## 8、Use PyCharm to develop PyQt

1、Pycharm is an excellent python IDE developed by jetbrains. Like all other JetBrains integrated development environments. PyCharm has an intelligent code editor that can understand Python's features and provide excellent productivity promotion tools: **automatic code formatting**, **code completion**, **refactoring**, **automatic import** and **one click code navigation**. Supported by advanced code analysis programs, these functions make PyCharm a powerful tool for Python professional developers and beginners.

2、To facilitate development, code can be written and debugged on PyCharm and then transferred to the machine for running.

3、PyQt Demo running example

![Screenshot_7-1](./resources/Screenshot_7-1.png)