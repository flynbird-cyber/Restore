# Restore

[English](README.md) | 한국어

**더 좋은 확장 기능을 개발하기 위해 별(Star)이 필요합니다. 별을 주세요.**

별을 주시면 복원의 신이 당신의 시스템을 보호해 줍니다. 반대로 별을 주지 않으면 당신의 시스템이 복원될 가능성이 낮아질 수도 있습니다.

물론 농담입니다. 잊지 말고 꼭 별을 주세요.

---

AUTOMATIC1111 Stable Diffusion WebUI용 txt2img 갤러리 복원 확장 프로그램입니다.

## 시연 영상 (Demo)

저장된 PNG 이미지 100장을 복원하고, 이미지를 선택하여 Hires. fix 및 ADetailer로 후속 작업을 진행합니다.

https://github.com/user-attachments/assets/8f29bc15-23d5-4b40-ad38-addeec152114

## 1. 개발 목적

WebUI 재시작, 브라우저 종료 또는 오류 발생 시 txt2img 출력 갤러리가 초기화될 수 있습니다.

Restore는 저장된 PNG 이미지와 내장 생성정보를 기존 txt2img 출력 갤러리에 직접 복원하여 중단된 작업을 재개할 수 있도록 합니다.

## 2. 기능

- 최대 2,000장의 이미지 일괄 복원.
- 기존 txt2img 출력 갤러리에 직접 복원.
- PNG 내장 생성정보 복원.
- 별도의 갤러리 탭 불필요.
- 기본 이미지 출력 경로 자동 감지.
- 지정 폴더 및 하위 폴더 검색.
- 원본 PNG 파일 참조 방식.
- 원본 이미지 재생성, 수정 및 삭제 없음.
- 지원 환경에서 추가 종속 프로그램 불필요.
- 무료 사용.

## 3. 설치

1. AUTOMATIC1111 WebUI 실행.
2. **Extensions** 탭 선택.
3. **Install from URL** 선택.
4. **URL for extension's git repository** 입력란에 `https://github.com/flynbird-cyber/Restore.git` 입력. 나머지 입력란은 공란으로 유지.
5. **Install** 버튼 클릭.
6. 설치 완료 후 **Installed** 탭 선택.
7. Restore가 설치되어 있고 활성화 체크박스가 선택되어 있는지 확인.
8. **Apply and restart UI** 버튼 클릭. WebUI가 자동으로 재시작됨.
9. **txt2img** 탭에서 **Restore saved txt2img gallery (PNG)** 메뉴 확인.

## 4. 사용법

1. **txt2img** 탭 선택.
2. **Restore saved txt2img gallery (PNG)** 메뉴 열기.
3. **Image directory**에서 이미지 저장 경로 확인.
4. **Last N images**에서 복원 수량 지정.
   - 범위: 1~2,000장
   - 기본값: 1,000장
5. **Restore PNGs to txt2img gallery** 버튼 클릭.
6. 복원된 갤러리에서 이미지 선택 및 후속 작업 진행.

## 5. 갤러리 복원 후 활용

txt2img 출력 갤러리는 이미지 열람 외에도 생성정보 확인, 이미지 전송, 고해상도 업스케일 및 후속 보정에 사용됩니다.

갤러리에서 이미지를 선택하고 하단의 **Upscale selected image (✨)** 버튼을 클릭하면 최초 이미지 생성 단계를 반복하지 않고 선택한 이미지에 Hires. fix를 실행할 수 있습니다.

다음은 해당 기능을 모르는 사용자를 위한 안내입니다. Restore의 필요성과 갤러리 복원 이후 기존 기능을 활용하는 방법을 설명합니다.

### 5.1. 기본 갤러리 기능

- 이미지 열람 및 선택 (Image Preview)
- 생성정보 확인 (Generation Parameters)
- 이미지 변환 전송 (Send to img2img)
- 부분 수정 전송 (Send to Inpaint)
- 추가 후처리 전송 (Send to Extras)
- 이미지 저장 (Save)
- ZIP 압축 저장 (Save ZIP)
- 다운로드 (Download)
- 저장 폴더 열기 (Open Folder)

### 5.2. Hires. fix

- 고해상도 업스케일 (Upscaler)
- 프롬프트 지정 (Hires Prompt)
- 네거티브 프롬프트 지정 (Hires Negative Prompt)
- 체크포인트 지정 (Hires Checkpoint)
- 샘플러 지정 (Hires Sampler)
- 스케줄러 지정 (Hires Scheduler)
- 디노이징 강도 조절 (Denoising Strength)
- 업스케일 배율 조절 (Upscale by)
- 목표 해상도 지정 (Resize Width/Height)
- 고해상도 생성 스텝 조절 (Hires Steps)
- 추가 네트워크 적용 (LoRA)
- 원본 시드 자동 재사용 (Seed)

### 5.3. Hires. fix 조건부 연동 기능

| 기능 | 적용 조건 및 설정 |
| --- | --- |
| Variation Seed | 원본 이미지에 변형 시드가 기록되어 있고 Variation Strength가 0보다 큰 경우 적용. |
| Variation Strength | 현재 UI에서 변형 강도 지정. |
| Seed Resize | 현재 UI에서 시드 기준 해상도 지정. |
| Refiner | 리파이너 모델 및 전환 시점 지정. 적용 단계를 Second pass 또는 Both passes로 설정. |
| ADetailer | 확장 프로그램 활성화. 검출 모델, 보정 프롬프트 및 디노이징 강도 지정. 검출된 영역에 보정 적용. |
| ControlNet | 확장 프로그램 활성화. 제어 이미지, 전처리기 및 호환 모델 지정. 적용 단계를 High res only 또는 Both로 설정. |
| FreeU | 확장 프로그램 활성화. 호환 모델, Backbone Scale, Skip Scale 및 적용 스텝 범위 지정. |
| Dynamic Prompts | 확장 프로그램 활성화. 기본 프롬프트에 가변 구문 또는 와일드카드 입력. Hires Prompt를 비워 두거나 기본 프롬프트와 동일하게 설정. |

필요한 기능과 파라미터를 설정하고 복원된 갤러리에서 이미지를 선택한 후 **✨ 버튼**을 클릭합니다.

추가 생성 및 보정 기능은 현재 WebUI 설정값을 사용합니다.

## 6. 지원 범위

제5항의 기능은 AUTOMATIC1111 및 관련 확장 프로그램에서 제공하는 기능이며, Restore가 자체적으로 구현하거나 제어하는 기능이 아닙니다.

해당 내용은 Restore의 필요성과 갤러리 복원 이후의 활용 방법을 설명하기 위한 사용 안내입니다.

개별 기능의 작동 여부는 AUTOMATIC1111 및 해당 확장 프로그램의 버전, 설정, 모델 및 호환성에 따릅니다. Restore는 해당 기능의 정상 작동을 보장하지 않습니다.

Restore는 과거 확장 프로그램의 모든 설정값을 자동으로 복원하지 않습니다.

## 7. 호환성 및 제한사항

- AUTOMATIC1111 v1.10.x 및 Gradio 3.41.x 기준으로 설계.
- 다른 버전의 호환성은 확인되지 않음.
- 생성 파라미터가 내장된 PNG 파일 지원.
- 생성 파라미터가 없는 PNG 파일은 복원 대상에서 제외.
- 파일의 최종 수정시간을 기준으로 최근 이미지 선정.
- 삭제되거나 저장되지 않은 이미지 복구 기능은 지원하지 않음.
- WebUI 전체 설정 복원 기능은 지원하지 않음.
- 원본 이미지 파일 수정 및 삭제 없음.
- 신뢰할 수 있는 로컬 사용자를 대상으로 설계.
- 신뢰할 수 없는 원격 사용자에게 노출하지 말 것.

## 8. Issues

Restore 자체에 관한 오류 및 기능 개선 요청은 GitHub Issues를 통해 접수합니다.

## 9. 개발자

- 개발자: FOR_000 (Reddit: u/FOR_000)
- 지역: 대한민국 서울 (Seoul, Republic of Korea)
- 소스코드: Python, 132줄

## 10. 라이선스

GNU Affero General Public License v3.0 (AGPL-3.0).

라이선스 조건에 따라 자유롭게 사용, 수정 및 재배포할 수 있습니다.

자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

Copyright © 2026 FOR_000
