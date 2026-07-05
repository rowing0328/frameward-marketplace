# 로컬 플러그인 설치

이 문서는 Frameward를 Codex에 로컬 플러그인으로 연결하는 방법을 설명합니다.

현재 Frameward 저장소는 플러그인 루트입니다. Codex는 플러그인을 직접 저장소 경로에서 설치하기보다, 설정된 마켓플레이스 안의 플러그인 항목으로 설치합니다. 그래서 로컬 개발 중에는 작은 로컬 마켓플레이스 래퍼를 하나 만들고, 그 안에서 Frameward 저장소를 가리키게 하면 됩니다.

## 구조

권장 구조는 다음과 같습니다.

```text
frameward-marketplace/
  .agents/
    plugins/
      marketplace.json
  plugins/
    frameward/
      .codex-plugin/
        plugin.json
      skills/
      hooks/
      core/
      docs/
      providers/
      workflows/
      schemas/
      templates/
      assets/
```

개발 중에는 `plugins/frameward`를 현재 Frameward 저장소로 심볼릭 링크해도 됩니다. 배포 전 검증을 할 때는 실제 폴더를 복사해서 테스트하는 편이 더 명확합니다.

## 마켓플레이스 파일

`frameward-marketplace/.agents/plugins/marketplace.json` 파일을 다음처럼 만듭니다.

```json
{
  "name": "local-frameward",
  "interface": {
    "displayName": "Local Frameward"
  },
  "plugins": [
    {
      "name": "frameward",
      "source": {
        "source": "local",
        "path": "./plugins/frameward"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

중요한 점은 `path`가 마켓플레이스 루트 기준으로 Frameward 플러그인 폴더를 가리켜야 한다는 것입니다. 위 예시는 `frameward-marketplace/plugins/frameward`를 가리킵니다.

## 설치 명령

로컬 마켓플레이스를 Codex에 등록합니다.

```bash
codex plugin marketplace add /path/to/frameward-marketplace
```

등록된 마켓플레이스를 확인합니다.

```bash
codex plugin marketplace list
```

설치 가능한 플러그인 목록에 Frameward가 보이는지 확인합니다.

```bash
codex plugin list --available
```

Frameward를 설치합니다.

```bash
codex plugin add frameward@local-frameward
```

설치 후 목록을 확인합니다.

```bash
codex plugin list
```

## 사용 예시

새 Codex 세션에서 UI 작업을 요청할 때 Frameward를 언급하면 됩니다.

```text
Frameward를 사용해서 이 화면을 더 깔끔하게 개선해주세요.
```

```text
Frameward 기준으로 새 프로젝트의 첫 화면을 만들어주세요. 기존 디자인 시스템이 없으면 작은 UI 기준부터 잡아주세요.
```

```text
Frameward를 사용하되 Astryx는 설치하거나 MCP를 켜지 마세요.
```

## 알아둘 점

- 플러그인 설치 후 새 Codex 세션을 열어야 스킬과 훅이 안정적으로 반영될 수 있습니다.
- 훅이 처음 실행될 때 신뢰 확인이 필요할 수 있습니다.
- Astryx는 선택 제공자입니다. Frameward 설치만으로 Astryx 설치나 MCP 활성화가 자동으로 일어나면 안 됩니다.
- 공개 배포나 팀 전체 사용이 필요해질 때 마켓플레이스 등록을 검토하면 됩니다. 로컬 개발과 검증에는 위 방식이면 충분합니다.

## 문제가 있을 때

Frameward가 설치 가능 목록에 보이지 않으면 다음을 확인합니다.

- `marketplace.json`이 `.agents/plugins/marketplace.json` 위치에 있는지 확인합니다.
- `marketplace.json`의 `name`이 설치 명령의 `@local-frameward`와 일치하는지 확인합니다.
- `source.path`가 실제 Frameward 플러그인 폴더를 가리키는지 확인합니다.
- Frameward 폴더 안에 `.codex-plugin/plugin.json`이 있는지 확인합니다.

스킬이 보이지 않거나 훅이 실행되지 않으면 새 세션을 열고, 필요한 경우 플러그인을 다시 설치합니다.
