# pr-comment-cli

A CLI tool to review GitHub PR comments from your terminal.

[![PyPI version](https://badge.fury.io/py/pr-comment-cli.svg)](https://pypi.org/project/pr-comment-cli/)
![License](https://img.shields.io/pypi/l/pr-comment-cli)
![Python](https://img.shields.io/pypi/pyversions/pr-comment-cli)

---

**pr-comment-cli**는 GitHub Pull Request에 달린 코드 리뷰와 토론을 터미널에서 벗어나지 않고도 빠르고 직관적으로 확인할 수 있게 해주는 커맨드 라인 인터페이스 도구입니다. 복잡한 PR의 히스토리를 추적하고, 내가 작업했던 파일에 대한 피드백만 필터링하여 리뷰 효율을 극대화하세요.

## ✨ 주요 기능 (Key Features)

- 코멘트 뷰어: 코드 컨텍스트, 대댓글 구조, 사용자별 색상으로 가독성있는 UI

- 필터링: `--about` 옵션으로 관련 파일의 피드백만 선별적으로 조회

- PR 목록 조회: 상태별, 브랜치별 PR 목록 조회

---

## 🚀 설치 및 설정 (Installation & Setup)

### 1. 설치

pip을 통해 간단하게 설치할 수 있습니다.

```
pip install pr-comment-cli
```

### 2. GitHub 토큰 인증

설치 후, 가장 먼저 GitHub Personal Access Token을 설정해야 합니다. 아래 명령어를 실행하고 자신의 토큰을 붙여넣으세요. 이 과정은 최초 한 번만 필요합니다.

```
pr-comment-cli --auth <YOUR_GITHUB_PERSONAL_ACCESS_TOKEN>
```

### 3. 대상 저장소 설정

코멘트를 가져올 기본 저장소를 설정합니다. 이 정보는 홈 디렉터리에 저장되어 매번 입력할 필요가 없습니다.

```
pr-comment-cli --set-owner <OWNER> --set-repo <REPO>
```

예시:

```
pr-comment-cli --set-owner facebook --set-repo react
```

---

## 💻 사용법 (Usage)

### 코멘트 상세 조회 (--pr)

특정 PR의 코멘트를 조회하는 핵심 기능입니다. 항상 --pr <PR번호>가 필요합니다.

```
pr-comment-cli --pr 12345
```

#### Options:

- --about <PR번호...>: 지정한 PR들에서 변경된 파일과 관련된 코멘트만 필터링합니다.

- --files <키워드...>: 파일 경로에 특정 키워드가 포함된 코멘트만 추가 필터링합니다.

- --context <숫자>: 코멘트 주변에 보여줄 코드 라인 수를 조절합니다. (기본값: 3)

### PR 목록 조회 (--list-prs)

저장소의 PR 목록을 다양한 조건으로 조회합니다.

```
# 모든 브랜치의 열려있는 PR 목록 보기 (첫 페이지만)
pr-comment-cli --list-prs
```

#### Keyword:

all: pr-comment-cli --list-prs all과 같이 명령어 뒤에 붙이면 모든 PR 목록을 가져옵니다.

#### Options:

- --state <open|closed|all>: 조회할 PR의 상태를 지정합니다. (기본값: open)

- --base <브랜치명>: 특정 브랜치를 타겟으로 하는 PR만 필터링합니다. (미지정 시: 모든 브랜치)

### 내 PR 목록 조회 (--my-prs)

자신이 생성한 PR 목록을 최신순으로 조회합니다.

```
# 내가 생성한 PR 목록 보기 (첫 페이지만)
pr-comment-cli --my-prs
```

#### Keyword:

- all: pr-comment-cli --my-prs all과 같이 명령어 뒤에 붙이면 모든 페이지를 가져옵니다.

---

## 💡 주요 사용 예시 (Key Usage Examples)

### 내가 작업한 파일에 대한 코멘트만 모아보기 (개발자 추천)

PR #12345에서, 내가 이전에 작업했던 #12300, #12310 PR과 관련된 파일의 코멘트만 필터링하여 조회합니다.

```
pr-comment-cli --pr 12345 --about 12300 12310
```

### 모든 브랜치의 닫힌 PR 전체 목록 확인하기

저장소에 있는 모든 브랜치를 대상으로, 닫히거나 병합된 모든 PR을 모두 조회합니다.

```
pr-comment-cli --list-prs all --state closed
```

### 특정 키워드가 들어간 파일에 대한 코멘트만 모아보기

```
pr-comment-cli --pr 38 --files "controller" "service"
```

---

### 코멘트 조회 (기본 기능)

- 특정 PR의 모든 코멘트 보기:

  ```
  pr-comment-cli --pr 12345
  ```

- 관련 파일 코멘트만 필터링해서 보기 (핵심 기능):

  PR #12345에서, 내가 이전에 작업했던 #12300, #12310 PR과 관련된 파일의 코멘트만 조회

  ```
  pr-comment-cli --pr 12345 --about 12300 12310
  ```

- 파일 경로 키워드로 추가 필터링:
  ```
  pr-comment-cli --pr 12345 --files "service"
  ```

#### PR 목록 조회

- 내가 생성한 PR 목록 보기 (최신 50개):

  ```
  pr-comment-cli --my-prs
  ```

- 내가 생성한 모든 PR 보기 (전체 페이지):

  ```
  pr-comment-cli --my-prs all
  ```

- 저장소의 main 브랜치를 대상으로 하는 closed 상태의 PR 목록 보기:
  ```
  pr-comment-cli --list-prs --state closed --base main
  ```

#### 출력 및 연동 옵션

- 코드 컨텍스트 라인 수 조절:
  ```
  pr-comment-cli --pr 12345 --context 5
  ```

---

## PR-COMMENT-CLI 기능 명령어 목록

### 1. 설정 (Configuration)

최초 1회만 실행하거나 설정을 바꿀 때 사용합니다.

#### 명령어 1: 저장소 설정

```
pr-comment-cli --set-owner <OWNER> --set-repo <REPO>
```

### 2. PR 목록 조회 (--list-prs)

PR 목록을 다양한 조건으로 조회하는 기능입니다.

#### 명령어 2-1: PR 목록 조회 (첫 페이지)

```
pr-comment-cli --list-prs
```

- 확인 사항: 모든 브랜치를 대상으로 open 상태인 PR이 최대 50개까지 테이블로 출력됩니다.

#### 명령어 2-2: PR 목록 조회 - 모든 페이지 조회

```
pr-comment-cli --list-prs all
```

- 확인 사항: Fetching next page... 메시지가 뜨면서 50개가 넘는 모든 open 상태의 PR이 출력됩니다.

#### 명령어 2-3: state 필터링

```
pr-comment-cli --list-prs --state [open|closed|all]
```

예시:

```
pr-comment-cli --list-prs --state closed
```

- 확인 사항: closed 상태인 PR 목록이 출력됩니다.

#### 명령어 2-4: base 브랜치 필터링

```
pr-comment-cli --list-prs --base <branch name>
```

예시:

```
pr-comment-cli --list-prs --base main
```

- 확인 사항: main 브랜치를 타겟으로 하는 PR 목록만 출력됩니다.

#### 명령어 2-5: 모든 조건 조합 (가장 강력한 목록 조회)

```
pr-comment-cli --list-prs all --state all --base main
```

- 확인 사항: main 브랜치를 타겟으로 하는, 모든 상태(open/closed)의, 모든 페이지의 PR이 전부 출력됩니다.

### 3. 내 PR 목록 조회 (--my-prs)

자신이 생성한 PR 목록을 조회하는 기능입니다.

#### 명령어 3-1: 기본 PR 목록 조회

```
pr-comment-cli --my-prs
```

- 확인 사항: 현재 GitHub 토큰 주인의 PR 목록이 최신순으로 최대 50개까지 출력됩니다.

#### 명령어 3-2: 내 모든 PR 목록 조회

```
pr-comment-cli --my-prs all
```

- 확인 사항: 50개가 넘는 자신의 모든 PR이 출력됩니다.

### 4. 코멘트 상세 조회 및 필터링 (--pr)

가장 핵심적인 코멘트 조회와 다양한 옵션 조합입니다.

#### 명령어 4-1: 단일 PR 코멘트 조회

```
pr-comment-cli --pr <PR번호>
```

- 확인 사항: 해당 PR의 모든 코멘트와 대댓글이 출력됩니다.

#### 명령어 4-2: --about 파일 필터링

```
pr-comment-cli --pr <PR번호> --about <내 PR번호 1> <내 PR번호 2>
```

- 확인 사항: 메인 PR의 코멘트 중, --about PR들에서 변경됐던 파일에 달린 코멘트만 필터링되어 출력됩니다.

#### 명령어 4-3: --files 키워드 필터링

```
pr-comment-cli --pr <PR번호> --files "service"
```

- 확인 사항: 해당 PR에서 파일 경로에 service가 포함된 코멘트만 필터링되어 출력됩니다.

#### 명령어 4-4: --about 과 --files 조합

```
pr-comment-cli --pr <PR번호> --about <PR번호> --files "controller"
```

- 확인 사항: --about으로 1차 필터링된 결과에 --files 키워드로 2차 필터링이 잘 적용됩니다.

#### 명령어 4-5: --context 옵션

```
pr-comment-cli --pr <PR번호> --context 10
```

- 확인 사항: 코멘트가 달린 코드 라인을 포함한 코드블럭이 기본 3줄이 아닌 10줄로 늘어나서 보입니다.
