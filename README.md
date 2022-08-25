# jupyter-lab

English | [简体中文](README_zh.md)

[**SCPI_WiKi**](https://github.com/OWON-LILIPUT/jupyter-lab/wiki/SCPI)

## 1、Install jupyter libraries and jupyter-lab libraries

- Connect the oscilloscope to the Internet.

- Open the `Pydroid3` application. Click the menu button in the upper left corner and click `Pip` in the pop-up menu.

- Click `QUICK INSTALL` in the `Pip` interface. Find the following libraries in the list below and click `install`  button on the right to install.

  ```
  jupyter    matplotlib    scipy
  ```

- After installation, click the return button in the upper left corner to return to the main interface. Then click the menu button in the upper left corner and click `Terminal` in the pop-up menu.

- Enter the following command in Terminal to install the `jupyter-lab` related libraries.

  ```
  ./Python/lib_installer.sh
  ```



## 2、Configure login password for  jupyter-lab

- Back to main application interface. Click the menu button in the upper left corner and click `terminal`in the pop-up menu.

- Enter the following command in `Terminal` to set the login password.

  ```
  jupyter-lab password
  ```

  

## 3、Access jupyter-lab via browser

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



## 4、Run example code

- Run `GitHub` Code
  - Enter the `jupyter-lab` via browser. Click the `GitHub` icon on the left and input the repository name in the `GITHUB USER` box. Such as `OWON-LILIPUT/jupyter-lab`.
  
  - Select the code you want to run in the file list and double-click to run it.
  
    ![Screenshot_4-1](./resources/Screenshot_4-1.png)


- Run `Local` Code
  - Enter the `jupyter-lab` via browser.   Click the `Directory` icon on the left and find `Python directory` . We prepared some code in advance.
  
  - Select the code you want to run in the file list and double-click to run it.
  
    ![Screenshot_4-2](./resources/Screenshot_4-2.png)



## 5、Save .py file

- Enter the `jupyter-lab` via browser. The button to create a `py` file can be seen at the bottom of the `Launcher` on the home page.

  ![Screenshot_5-1](./resources/Screenshot_5-1.png)

- Click to create a `py` file. Then copy the code into the editor and save it.

  ![Screenshot_5-2](./resources/Screenshot_5-2.png)



## 6、Run .py code

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