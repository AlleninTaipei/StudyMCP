--- 
marp: true
theme: gaia
backgroundColor: #181818
color: #EEF8F7
paginate: false
---

# Introduction to Agents

ASRock AI Center
Allen Sun 

---

<!--_class: lead  -->

# Agent Tools & Interoperability with Model Context Protocol (MCP)
5-Day AI Agents Intensive Course with Google - Day 1

---

## 核心轉變：從被動 AI 到自主 AI Agent (1/8)

|傳統 AI|AI Agent|
|:-|:-|
|被動回應（問答、翻譯）|具備目標導向<br>能規劃、行動、觀察<br>可在多步驟中自主完成任務|
|PoC|MVP|

---

## AI Agent 的三大核心組成 (2/8)

|AI Agent |思考 + 行動 + 指揮|
|:-|:-|
|**Model**<br>大腦|LLM 推理引擎<br>管理 Context（任務、記憶、工具結果）|
|**Tools**<br>雙手|API、資料庫、RAG、程式碼執行<br>|讓 Agent 能「做事」|
|**Orchestration Layer**<br>指揮|控制流程、狀態、策略<br>負責執行整個 Agent Loop|

---

## AI Agent 的基本運作循環 (3/8)

Agentic Loop = Think → Act → Observe → Think

1. 接收任務目標
2. 評估工具與記憶
3. 規劃下一步
4. 呼叫工具執行
5. 觀察結果並更新 Context，🔁 持續循環直到任務完成

---

### AI Agent 能力分級 (4/8)

|Level|關鍵能力|
|:-|:-|
 0：純 LLM|無工具、無即時資訊|
|1：連網問題解決者|可使用工具查詢即時資料|
|2：策略型問題解決者|Context Engineering（用前一步結果精準塑造下一步輸入）|
|3：多 Agent 協作系統|Agent 彼此視為工具，可進行「目標委派」，各自執行完整計畫後回傳結果|
|4：自我演化系統（前沿）|能識別自身能力缺口，可動態建立新 Agent 或工具來補足能力|

---

#### 走向生產環境的關鍵工程實務 (5/8)

|工程實務||
|:-|:-|
|模型選擇與 Routing|複雜規劃 → 高階模型<br>簡單高頻任務 → 快速低成本模型|
|工具可靠性|使用 RAG、向量資料庫、NL2SQL 進行資料檢索<br>透過 Function Calling（結構化工具描述），確保模型能正確呼叫與解析結果|
|記憶管理|短期記憶：當前任務的思考與行動紀錄<br>長期記憶：跨任務的偏好、知識與經驗（常用向量資料庫實作）

---

## AgentOps：測試、除錯與觀測 (6/8)

### 測試方式改變：不驗證固定輸出，而是驗證「品質」

* LLM as Judge（用 AI 評估 AI）
* Golden Dataset（標準測試情境）
* 使用 trace 記錄完整推理與工具呼叫流程（像飛行紀錄器）
* 人類回饋真實錯誤會轉為永久測試案例，防止重複發生

---

## 安全、治理與規模化 (7/8)

### 採用 Defense in Depth（多層防禦）

* 程式層 guardrails（硬規則）
* AI Guard Models（風險行為偵測）

### Agent 身分識別

* Agent 擁有獨立身分與最小權限（非使用者代言）

### Agent Governance

* 透過中央 Gateway 控制 agent、工具、agent-to-agent 通訊

---

## 持續學習與模擬 (8/8)

Agent 需透過執行紀錄、使用者回饋、政策更新持續優化

Agent Gym（模擬環境）

在非正式環境中壓力測試多 Agent 協作與新情境

---

## 總結關鍵觀點

成功的 AI Agent 不只靠模型聰明，而是取決於：
* 架構設計
* 工具與編排
* 測試、觀測、安全與治理

開發者角色正在轉變：
從寫程式的人 → 設計、指揮、治理自主 AI 系統的架構師。

----

<!--_class: lead  -->

# FastMCP Cloud
[🔗](https://fastmcp.cloud) 部署 MCP Server 的最快方法

---

<style scoped>section{font-size:28px;}</style>

## 觀念確認 (1/2)

### 🔲 Model Context Protocol (MCP)

可以把它理解成一種 **API（Application Programming Interface）**，這個 **應用程式介面** 是專門為 LLM 互動所設計的。用來將 LLM 連接到工具與資料；而 FastMCP 則透過乾淨、符合 Python 風格的程式碼，讓它具備可用於正式環境的能力。

---

<style scoped>section{font-size:28px;}</style>

## 觀念確認 (2/2)

### 🔲 Python main guard ( entry point pattern)

```python
if __name__ == "__main__"
```
讓同一個 .py 檔案既能當模組被導入，又能當獨立程式執行

### 🔲 Python docstring (documentation string)

```python
 """將兩個數字相加"""
```

```python
"""搜尋資料庫中的資料""" 
```

用來描述函數、類別或模組的功能說明。
當 AI Chatbot 使用你的 MCP 工具時，會讀取這個 docstring 來了解工具的功能，所以寫清楚的說明很重要!

---

<style scoped>section{font-size:28px;}</style>

## 部署準備

```bash
pip install fastmcp
```

## 開發測試

```python
from fastmcp import FastMCP

mcp = FastMCP("我的 MCP 服務器")

@mcp.tool()
def add_numbers(a: int， b: int) -> int:
    """Add Two Nimbers"""
    return a + b
```

```bash
fastmcp run mcp.py:mcp --transport http --port 8000
```
啟動 FastMCP Server，讓 `mcp.py` 的 `mcp` 這個工具透過 HTTP 協議在 port 8000 運行。

---

<style scoped>section{font-size:28px;}</style>

按 `CTRL-C` 關閉服務

![bg contain](assets/mymcp.jpg)

---

<style scoped>section{font-size:28px;}</style>

建立 `git` 專案並 `commit mcp.py`
登入 FastMCP Cloud
關閉 Authentication 後 Deploy Server

![bg contain](assets/deploymymcp.jpg)

---

<style scoped>section{font-size:28px;}</style>

![bg contain](assets/deployed.jpg)

<br><br><br><br><br><br><br><br><br><br>

$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 等待狀態從 Building → Production

---

# 🙏🏻 感謝 FastMCP 團隊

* 使用 FastMCP Cloud 的 ChatMCP 可以 進行測試
* 每次修改 `mcp.py` 再 `commit` 後 ，FastMCP 會自動重新 deploy
* MCP Server 的 Status、Log，都可以查詢






