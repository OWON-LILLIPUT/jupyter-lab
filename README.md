# jupyter-lab

English | [简体中文](README.md)

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

  - Manual settings `IP`

    ```
    ./Python/start_jupyterlab.sh ip port
    ```

- Oscilloscope local access. Enter the following URL in the browser.

  ```
  http://127.0.0.1:port/lab
  ```

- Computer access in LAN. Enter the following URL in the browser.

  ```
  http://Oscilloscope's ip:port/lab
  ```

  

## 4、Run example code

- Enter the `jupyter-lab` via browser. Click the `GitHub` icon on the left and input the repository name in the `GITHUB USER` box. Such as `OWON-LILIPUT/jupyter-lab`.
- Select the script you want to run in the file list and double-click to run it.



## 5、Save .py file

- Enter the `jupyter-lab` via browser. The button to create a `py` file can be seen at the bottom of the `Launcher` on the home page.
- Click to create a `py` file and then copy and paste the code to save it.



## 6、Run .py code

- Open the `Pydroid3` application. Click the folder icon in the upper right corner of the home page and click `Open` in the pop-up options.
- Click `InternalStorage` in the pop-up interface to enter internal storage.
- Find the `py` file you saved in the internal storage and click to open it. Take the sample code as an example. Entering the internal storage and click the `Python` folder. After entering the `Python` folder, click `get_scope_wave.py` and it will be opened.
- Open the `py` file and click the run button in the lower right corner to run the code.