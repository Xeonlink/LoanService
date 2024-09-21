# 개발환경 설정

### vscode 확장프로그램

1. [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

   파일을 저장할 때 파이썬 코드를 포맷팅해주는 확장프로그램. js의 prettier와 같은 철학을 가지고 만들어졌다고 함. 설치후 해야될 설정들은 .vscode/.settings.json을 통해서 되어있으므로, 설치하고 사용하기만 하면 된다.

2. [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)

   csv파일을 볼때, 각 열을 기준으로 서로 다른 색으로 표시해주는 확장프로그램. csv를 사용하여 작업할 때, 실수의 가능성을 줄여준다.

3. [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)

   sqlite의 \*.db 파일을 gui로 볼 수 있도록 하는 확장프로그램

4. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

   코드블럭 위에, 이 코드가 언제 누구에 의해서 작성되었는지 깃내역을 분석하여 작게 적어준다. 디버깅할 때 누가 짠 코드인지 쉽게 파악하여 수정해야될 사람이 누구인지 판단할 때 도움이 된다.

5. [Edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)

   CSV파일을 GUI에서 편집할 수 있도록 해주는 확장프로그램. 마치 액셀의 스프레드시트를 다루는 것처럼 CSV파일을 vscode안에서 수정할 수 있다.

6. [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

   컴퓨터 사양이 가능한 경우에 프로젝트 전역분석 및 코드 입력패턴을 분석하여 다음에 입력할 코드를 추천해주는 확장프로그램

7. [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

   IntelliCode를 파이썬에서 사용하려면 설치해야된다고 IntelliCode설정 가이드에 나와있지만, IntelliCode를 설치하면 자동으로 설치됨.
   관련 설정방법은 IntelliCode QuickGuide의 파이썬 설정을 참조

8. [Pyright](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)

   MS에서 지원하는 파이썬의 정적 타입체크 도구, 파이썬은 기본적으로 타입이 없는 언어이지만 typing 패키지를 사용하면, 마치 typescript처럼 런타임에는 영향을 끼치지 않는 정적 타이핑만을 지원한다.

9. [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg)

   vscode안에서 SVG파일의 Preview를 볼 수 있게 해주고, svg파일을 png로 변환하는 기능을 지원한다.

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

# 빌드 과정

### 빌드과정

1. constants.py에서 DEBUG를 False로, 변경

   ```python
   DEBUG=False
   ```

2. pyinstaller가 설치되어 있지 않다면, 설치

   설치되어 있다면, 다음 단계로 넘어감.
   ```pwsh
   pip install -r requirement.txt
   또는
   pip install pyinstaller
   ```

3. 터미널에 다음의 명령어를 입력하여, 빌드

   ```pwsh
   pyinstaller -w -F --add-data "./assets/*:assets" --add-data "./assets/themes/*:assets/themes" --add-data "./data:data" ./src/main.py
   ```
   -w : 빌드결과를 실행했을 때, 터미널창이 실행되지 않고 윈도우창만 나오도록 함

   -F : 빌드결과가 디렉토리 + .exe 형태가 아닌, 하나의 .exe파일로 나오도록 함

   --add-data "{src}:{des}" : {src}에 해당하는 파일을 빌드결과 {des}에 옮기도록 함. 수행하지 않을 경우 빌드결과물을 실행했을 때, 해당 리소스를 찾을 수 없다며 에러를 일으킴.

### 주의사항

1. data.db 파일의 제거 또는 초기화

   테스트할 때 사용했던 db파일이 그대로 빌드결과에 들어가기 때문에, 이를 방지하기 위해서 db파일을 삭제하거나 백업한 후에 빌드를 하는 것이 좋음.

2. DEBUG=False

   변경하지 않을 경우, AddDialog와 EditDialog에서 🔥 테스트용으로 채우기가 빌드결과에 반영됨.

   DEBUG=False 를 하는 것만으로도 🔥 테스트용으로 채우기 가 사라지도록 코드를 짜두었기 때문에 수동으로 제거할 필요 없음.


# Tips

### 필요한 아이콘을 가져오는 방법 (deprecated : 해봤는데 아이콘 깨짐)

1. https://fontawesome.com/ 사이트로 이동한다.

2. 무료로 제공되는 svg 아이콘중 적절한 아이콘을 다운받는다.

3. assets/svg 폴더에 다운받은 파일을 넣는다.

4. svg를 png로 변환

   - src/svg_converter.py 를 실행시킨다.

     ```pwsh
     python ./src/svg_converter.py
     ```

     꼭 위와 같이 실행시킬 필요는 없고, 터미널이 프로젝트 폴더에 있는 상태에서 svg_converter.py를 실행시킬 수 있으면 된다.

     실행이 완료되면, svg폴더에 있는 파일과 똑같은 png파일이 assets.png폴더에 생성될 것이다.

     예를 들어 book.svg를 svg폴더에 넣었다면, book.png가 png폴더에 생성된다.

   - [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg)를 사용한다.

     [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg) 확장프로그램을 설치했다면 SVG Preview를 열고, |-> 버튼을 눌러 svg파일을 png파일로 변환시킨다.

5. 변환된 png파일을 프로젝트에서 사용한다.
