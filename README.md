# 프로젝트를 설정하는 방법

### Windows

1. PowerShell을 통해 pyenv-win을 설치한다.

    Install pyenv-win in PowerShell.
     ```pwsh
     Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
     ```

2. PowerShell을 껏다가 킨다.

3. pyenv --version 을 실행하여 설치가 제대로 완료되었는지 확인한다.

    Run pyenv --version to check if the installation was successful.
    
    ```pwsh
    pyenv --version

    > pyenv {설치된 pyenv의 버전}
    ```
    

4. pyenv의 사용방법은 [pyenv-win](https://github.com/pyenv-win/pyenv-win) 공식 레포지토리를 참고한다.

5. 프로젝트 폴더를 vscode로 연다.

6. pyenv local 커맨드를 사용하여 프로젝트에 알맞는 파이썬 버전이 몇인지 확인한다.

    ```pwsh
    pyenv local

    > 3.12.5
    ```

7. pyenv를 통해서 프로젝트에 알맞는 파이썬 버전을 다운로드한다.

    ```pwsh
    pyenv install 3.12.5
    ```

8. 다운로드가 제대로 되었는지 확인한다.

    ```pwsh
    pyenv versions

    > 
      system
    * 3.7.9 ( set by /~~~)
      3.12.5
    ```

9. 프로젝트 폴더에서 다운로드받은 파이썬 버전을 사용하도록 설정한다.

    ```pwsh
    pyenv local 3.12.5

    > 
      system
      3.7.9
    * 3.12.5 ( set by /~~~ )
    ```

10. 파이썬 버전이 제대로 적용되었는지 확인하다.

    ```pwsh
    python --version

    > Python 3.12.5
    ```

11. 파이썬 가상환경을 만들다.

    ```pwsh
    python -m venv {가상환경의 이름}

    가상환경의 이름은 venv로 하도록 한다.
    python -m venv venv
    ```

12. 가상환경을 활성화한다. 

    ```pwsh
    venv/Scripts/activate
    ```

13. 가상환경에 프로젝트에 필요한 패키지를 다운로드한다.

    ```pwsh
    pip install -r requirement.txt
    ```