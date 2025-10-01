# PRD — **awsui**（Python 3.13 + Textual + uv）

## 1. 產品目標

提供一個跨平台 TUI（終端介面）工具，讓使用者可以**搜尋／檢視／切換** AWS Profiles（含 SSO），過期時自動補 `aws sso login`，並在介面中直接查看驗證結果。

## 2. 背景與依據

* **Python 3.13** 為穩定版，帶來互動介面更新與（可選）free-threaded/JIT 等新能力；本專案僅使用穩定面向。 ([Python documentation][1])
* **Textual** 是 Python 的 TUI 開發框架，可從 PyPI 安裝；如需文字語法高亮可用 `textual[syntax]`。 ([Textual Documentation][2])
* **uv** 提供快速的套件／工具執行與安裝，`uvx` 可臨時執行工具，`uv tool install` 可永久安裝。 ([docs.astral.sh][3])
* **AWS CLI（IAM Identity Center/SSO）** 的 `sso-session` 與 named profiles 為設定基礎。 ([AWS 文件][4])

## 3. 範圍（Scope）

### 3.1 MVP 必做

1. 讀取並解析 `~/.aws/config`、`~/.aws/credentials`（含 `sso-session`、`sso_account_id`、`sso_role_name`、傳統 `source_profile/role_arn`）。 ([AWS 文件][4])
2. TUI：關鍵字搜尋（對 name/account/role/region）、清單選取、側欄詳情、狀態列。
3. 認證流程：先呼叫 `aws sts get-caller-identity` 驗證；失敗自動執行 `aws sso login --profile <name>` 後重試一次（含進度與錯誤提示）。
4. 互動式 TUI：在單一畫面內完成搜尋、選擇、認證與狀態檢視。
5. WhoAmI 面板：顯示 Account/ARN/User 與（可讀快取的）Token TTL。

### 3.2 可選（次要）

* LRU 最近使用排序／Pin 常用項。
* Region 快速覆寫（臨時 `AWS_DEFAULT_REGION`）。
* 雙語介面（預設繁中，可切英文）。

### 3.3 非目標（MVP 外）

* 不修改 `~/.aws/config`（僅讀）。
* 不自建憑證保管或替代 aws-vault。
* 不自動開 Console（後續版本考慮）。

## 4. 使用者故事

* 雲端工程師：在數十個 SSO profiles 中模糊搜尋 `prod admin`，Enter 後即完成切換並顯示 whoami。
* 值班 SRE：Token 過期時，程式自動 `sso login` 再重試，無需手動補登。
* 數據工程師：能一眼看到目前 `AWS_PROFILE`、Region、Account/ARN，避免誤操作生產帳號。

## 5. 介面契約（CLI／I/O）

```
awsui [--profile <name>] [--region <code>] [--lang zh-TW|en] [--log-level INFO|DEBUG]
```

* **預設行為**：啟動 TUI → 選取 → 驗證／（必要時）登入 → 返回面板。

## 6. TUI 規格（Textual）

* 版面：上方搜尋框、左側清單、右側詳情、底部狀態列。
* 快捷鍵：`/` 搜尋、`Enter` 套用、`l` 強制登入、`w` WhoAmI、`r` Region、`?` 說明、`q` 離開。
* 空狀態：未偵測到 profiles → 引導使用者執行 `aws configure sso-session`／`aws configure sso`。 ([AWS 文件][5])

## 7. 資料模型

```python
class Profile(TypedDict):
    name: str
    kind: Literal["sso","assume","basic"]
    account: str | None
    role: str | None
    region: str | None
    session: str | None        # sso-session 名稱（若有）
    source: str                # 來源檔路徑
```

## 8. 非功能需求（NFR）

* **平台**：Linux/macOS/Windows（Windows 以 PowerShell 驗證）。
* **相容**：Python `>=3.13,<3.14`；Textual 取用穩定版；AWS CLI v2。 ([Python documentation][1])
* **效能**：啟動 ≤ 300ms；搜尋 ≤ 50ms；切換成功（含一次登入）≤ 5s。
* **可靠**：登入成功率 > 98%；Crash 率 < 0.1%。
* **可觀測**：結構化日誌（JSON 行）輸出 STDERR：`ts, level, action, duration_ms, profile, result`。

## 9. 安全與隱私

* 只透過 `aws` 子行程取得臨時憑證／登入，不落地長期憑證。
* 僅讀取 `~/.aws/config`／`~/.aws/credentials`，尊重 `AWS_CONFIG_FILE`／`AWS_SHARED_CREDENTIALS_FILE`。 ([AWS 文件][6])
* 日誌避免輸出完整 ARN／帳號，可做雜湊或遮罩。

## 10. 錯誤處理

| Code          | 情境             | 使用者訊息（摘要）       | 建議行動                                                |
| ------------- | -------------- | --------------- | --------------------------------------------------- |
| E_NO_AWS      | 找不到 `aws` 可執行檔 | 未偵測到 AWS CLI v2 | 依官方 Quickstart 安裝／設定。 ([AWS 文件][7])                 |
| E_NO_PROFILES | 無可用 profiles   | 掃描不到任何 Profile  | 依指引執行 `aws configure sso-session` 建立。 ([AWS 文件][5]) |
| E_LOGIN_FAIL  | `sso login` 失敗 | 可能網路/MFA 問題     | 提供重試與錯誤細節。                                          |
| E_STS_FAIL    | `sts` 仍失敗      | 認證或權限問題         | 檢查帳號/角色/region 與 SSO 狀態。                            |

## 11. 成功衡量（驗收）

**關鍵用例（Given/When/Then）**

1. **自動補登**

   * Given：選擇 `acctA-admin` 且 SSO token 過期
   * When：按 Enter
   * Then：自動執行 `aws sso login --profile acctA-admin`，再 `sts get-caller-identity` 成功並顯示於 TUI。
2. **雙平台輸出**

3. **搜尋體驗**

   * Given：輸入 `prod admin`
   * Then：能匹配 name/role 含關鍵字之 profiles，並以最近使用排序在前。
4. **錯誤可恢復**

   * When：登入失敗（如網路中斷）
   * Then：顯示具體行動建議並允許重試，程式不中斷。

## 12. 架構與模組

```
awsui/
  ├─ awsui/app.py          # Textual App / UI 與快捷鍵
  ├─ awsui/models.py       # Profile 掃描與解析
  ├─ awsui/aws_cli.py      # 呼叫 aws（sts / sso login / 讀快取）
  ├─ awsui/config.py       # 偏好設定（~/.config/awsui/config.toml）
  ├─ awsui/logging.py      # 結構化日誌（stderr）
  ├─ pyproject.toml
  └─ README.md
```

## 13. 相依與版本

* Python `>=3.13,<3.14`；Textual、Rich 為主要依賴。 ([Python documentation][1])
* 使用者需預先安裝 AWS CLI v2。 ([AWS 文件][7])

**`pyproject.toml` 重點**

```toml
[project]
name = "awsui"
version = "0.1.0"
description = "AWS Profile/SSO 切換 TUI（Textual + uv）"
requires-python = ">=3.13,<3.14"
dependencies = ["textual>=6.1.0"]
[project.scripts]
awsui = "awsui.app:main"
```

## 14. 建置與執行（uv）

* 安裝與釘選 Python 3.13：`uv python install 3.13 && uv python pin 3.13`。
* 本地執行：`uv sync && uv run awsui`。
* 零安裝執行：`uvx --python 3.13 awsui`；永久安裝工具：`uv tool install --python 3.13 awsui`。 ([docs.astral.sh][8])

## 15. 測試計畫

* **單元**：設定檔解析、搜尋索引、shell 指令輸出組裝。
* **整合**：以假 `aws` wrapper 模擬 `whoami/login`；驗證失敗→補登→重試流程。
* **端到端**：

  * POSIX：`uvx --python 3.13 awsui` → 透過 TUI 選取 profile 後 `aws sts get-caller-identity` 成功。
  * Windows：`uvx --python 3.13 awsui`（PowerShell）→ 同上。
* **CI Matrix**：Ubuntu/macOS/Windows + Python 3.13.x；覆蓋率 ≥ 80%。

## 16. 風險與對策（前瞻）

* **企業 SSO 差異**（自簽憑證／瀏覽器限制）→ 完全依賴 AWS CLI 官方登入流程，提供重試與明確錯誤說明。 ([AWS 文件][4])
* **Textual 版本差異** → 鎖用穩定版；若 `textual[syntax]` 相依衝突，文件建議僅裝核心包。 ([Textual Documentation][2])
* **Python 小版更新** → CI 追隨 3.13 最新維護版以獲得修補與穩定。 ([Python documentation][9])

## 17. 附錄

### 17.1 AWS 設定檔示例

```ini
[sso-session corp]
sso_start_url = https://your-company.awsapps.com/start
sso_region = ap-northeast-1

[profile acctA-admin]
sso_session = corp
sso_account_id = 111111111111
sso_role_name = AdministratorAccess
region = ap-northeast-1
output = json
```

（`sso-session` 與 named profile 欄位說明見官方文件。） ([AWS 文件][4])

### 17.2 安裝備忘（Textual / uv）

* `pip install textual` 或 `pip install "textual[syntax]"`（若需語法高亮）。 ([Textual Documentation][2])
* `curl -LsSf https://astral.sh/uv/install.sh | sh` 安裝 uv（也可用套件管理器）。 ([docs.astral.sh][8])

[1]: https://docs.python.org/?utm_source=chatgpt.com "3.13.7 Documentation"
[2]: https://textual.textualize.io/getting_started/?utm_source=chatgpt.com "Getting started - Textual"
[3]: https://docs.astral.sh/uv/guides/tools/?utm_source=chatgpt.com "Using tools | uv - Astral Docs"
[4]: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html?utm_source=chatgpt.com "Configuring IAM Identity Center authentication with the ..."
[5]: https://docs.aws.amazon.com/cli/latest/reference/configure/sso-session.html?utm_source=chatgpt.com "sso-session — AWS CLI 2.31.3 Command Reference"
[6]: https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html?utm_source=chatgpt.com "Configuration and credential file settings in the AWS CLI"
[7]: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html?utm_source=chatgpt.com "Setting up the AWS CLI - AWS Command Line Interface"
[8]: https://docs.astral.sh/uv/getting-started/installation/?utm_source=chatgpt.com "Installation | uv - Astral Docs"
[9]: https://docs.python.org/3/download.html?utm_source=chatgpt.com "Download — Python 3.13.7 documentation"
