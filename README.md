# git 명령어

</br>

## 1. Initializing a repository
```
git init
```
Git으로 프로젝트 관리를 시작하려면 원하는 디렉토리로 이동하여 명령어를 입력한다
해당 장소에 `.git` 디렉토리를 생성하고 해당 저장소에 대한 모든 변경사항을 추적/관리한다

</br>

## 2. Checking the status (상태 확인)
```
git status
```
어떤 파일이 변경되었는지, 어떤 파일이 추가되었는지 등을 전부 보여준다

</br>

## 3. Staging files (Staging area에 파일 추가하기)
```
git add .
```
우리가 원하는 파일들을 `staging area` 로 추가하고 커밋을 남길 수 있게 해준다
`.` 은 모든 파일/폴더를 의미한다
`.`이 아닌 파일 이름을 사용해서 특정 파일만 추가할 수 있다

</br>

## 4. Making commits (커밋 남기기)
```
git commit -m "Commit message"
```
특정 시간의 코드 스냅샷의 형태로 해당 repository의 커밋 기록에 남게된다
새 커밋을 남기려면 `staging area`에 파일을 추가 한 다음 커밋을 남기는 프로세스를 반복해야 한다

</br>

## 5. Commit history
```
git log
```
프로젝트의 모든 커밋 내역을 볼 수 있다
`log`는 각 커밋에 대한 자세한 정보를 담고 있습니다. (작성자, hash 값, 날짜와 시간, 그리고 커밋 메세지)
```
git checkout <commit-hash>
```
위 명령어를 통해 특정 커밋 시점의 코드로 되돌아 갈 수 있다