# OASIS-SDK

## 1. Concept

OASIS-LLM-PROXY-CLIENT는 OpenAI와 Azure OpenAI를 **통합된 단일 클라이언트**로 제공하는 Python 라이브러리입니다. 공식 SDK 및 LangChain을 얇게 wrapping하여 사내 규칙에 맞는 필드 입력과 프록시 서버를 통한 키 주입을 지원합니다.

**주요 특징:**

- 🔄 **통합 클라이언트**: 하나의 `OasisOpenAI` 클라이언트로 OpenAI와 Azure OpenAI 모두 사용
- 🎯 **자동 프로바이더 선택**: 모델 ID만으로 적절한 프로바이더 자동 선택
- 🔗 **완전한 호환성**: 원본 라이브러리의 모든 기능을 그대로 사용 가능
- 🛡️ **통합 인증**: 프록시 서버를 통한 안전한 키 관리

## 2. Usage

### 2.1 설치

```bash
pip install oasis-sdk
```

### 2.2 환경 설정

프록시 서버 URL을 환경변수로 설정할 수 있습니다

- 기본값은 이미 설정되어있음

```bash
export OASIS_PROXY_URL="https://your-proxy-server.com"
```

또는 클라이언트 생성시 직접 지정:

```python
client = OasisOpenAI(
    proxy_url="https://your-proxy-server.com",
    # ... 기타 매개변수
)
```

### 2.3 사용 예시

**client parameters**

[required]

- account_id: 계정 ID
- user_uuid: 사용자 UUID
- workspace_uuid: 워크스페이스 UUID
- tenant_uuid: 테넌트 UUID
- plugin_name: 호출한 시스템 명 (ex: chatbot, mcp1, rag-mcp 등)

[optional]

- proxy_url: LLM 프록시 서버 URL (환경변수 `OASIS_PROXY_URL`에서 자동 로드)
- user_ip: 사용자 IP (기본값: 127.0.0.1)

[auto]

- root_id: 클라이언트 생성시 발급
- req_id: 요청시마다 발급

📍 **주의**

- 1번의 연속적인 수행에서 root_id는 고정되어야 함
- 연계되는 시스템에서는 클라이언트 생성시 초기 발급된 root_id를 주입하여 사용

#### 2.3.1 SDK (통합된 OpenAI 클라이언트)

**통합된 OpenAI/Azure SDK 래퍼**

> 📍 **중요**: 이제 OpenAI와 Azure OpenAI 모두 동일한 `OasisOpenAI` 클라이언트를 사용합니다. 모델 ID만으로 자동으로 적절한 프로바이더를 선택합니다.

```python
import oasis
# 또는
from oasis.sdk.openai import OasisOpenAI, OasisAsyncOpenAI

# 동기 클라이언트
with OasisOpenAI(
    account_id="your_account_id",
    user_uuid="your_uuid",
    workspace_uuid="your_workspace_uuid",
    tenant_uuid="your_tenant_uuid",
    plugin_name="your_system"
) as client:
    print(f"Client base URL: {client.base_url}")

    # OpenAI 모델 사용 예시
    openai_resp = client.chat.completions.create(
        model="your_openai_model_uuid",  # OpenAI 모델 UUID
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
    )
    print("OpenAI Response:", openai_resp.choices[0].message.content)

    # Azure OpenAI 모델 사용 예시 (동일한 클라이언트로!)
    azure_resp = client.chat.completions.create(
        model="your_azure_model_uuid",  # Azure deployment UUID
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello from Azure!"}
        ],
        max_tokens=100,  # Azure 모델 사용시 토큰 제한
    )
    print("Azure Response:", azure_resp.choices[0].message.content)

    # 스트리밍 (OpenAI 모델)
    stream = client.chat.completions.create(
        model="your_openai_model_uuid",
        messages=[{"role": "user", "content": "Tell me a short story"}],
        stream=True,
    )
    print("OpenAI Stream:")
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # 스트리밍 (Azure 모델)
    azure_stream = client.chat.completions.create(
        model="your_azure_model_uuid",
        messages=[{"role": "user", "content": "Count to 3"}],
        max_tokens=50,
        stream=True,
    )
    print("Azure Stream:")
    for chunk in azure_stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # 임베딩 (동일한 모델 ID가 OpenAI/Azure 모두 지원)
    embedding_resp = client.embeddings.create(
        model="your_embedding_uuid",  # 임베딩 모델 UUID
        input=["This sentence will be embedded.", "Another test sentence."],
    )
    print(f"Embedding vector dimension: {len(embedding_resp.data[0].embedding)}")

# 비동기 클라이언트 (동일한 방식으로 OpenAI/Azure 모두 지원)
import asyncio

async def async_example():
    async with OasisAsyncOpenAI(
        account_id="your_account_id",
        user_uuid="your_uuid",
        workspace_uuid="your_workspace_uuid",
        tenant_uuid="your_tenant_uuid",
        plugin_name="your_system"
    ) as client:
        # 비동기 채팅 완성 (OpenAI)
        openai_resp = await client.chat.completions.create(
            model="model_uuid",
            messages=[{"role": "user", "content": "Hello OpenAI!"}],
        )
        print("Async OpenAI:", openai_resp.choices[0].message.content)

        # 비동기 채팅 완성 (Azure)
        azure_resp = await client.chat.completions.create(
            model="model_uuid",
            messages=[{"role": "user", "content": "Hello Azure!"}],
            max_tokens=50,
        )
        print("Async Azure:", azure_resp.choices[0].message.content)

        # 비동기 스트리밍
        stream = await client.chat.completions.create(
            model="model_uuid",
            messages=[{"role": "user", "content": "Count to 5"}],
            stream=True,
        )
        print("Async Stream:")
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print("\n")

        # 비동기 임베딩
        embedding_resp = await client.embeddings.create(
            model="your_model_uuid",
            input=["Async embedding test"],
        )
        print(f"Async embedding vector: {embedding_resp.data[0].embedding[:5]}...")

# 비동기 함수 실행
asyncio.run(async_example())
```

#### 2.3.2 LangChain (통합된 OpenAI 래퍼)

> 📍 **중요**: LangChain도 통합된 `OasisChatOpenAI`와 `OasisOpenAIEmbedding`을 사용합니다. 모델 ID로 OpenAI/Azure를 자동 구분합니다.

```python
from oasis.langchain.openai import OasisChatOpenAI, OasisOpenAIEmbedding

# OpenAI 모델을 사용하는 채팅 예시
openai_llm = OasisChatOpenAI(
    account_id="your_account_id",
    user_uuid="your_uuid",
    workspace_uuid="your_workspace_uuid",
    tenant_uuid="your_tenant_uuid",
    model_name="model_uuid",  # OpenAI 모델 UUID
    plugin_name="langchain_openai_test"
)

# Azure 모델을 사용하는 채팅 예시 (동일한 클래스!)
azure_llm = OasisChatOpenAI(
    account_id="your_account_id",
    user_uuid="your_uuid",
    workspace_uuid="your_workspace_uuid",
    tenant_uuid="your_tenant_uuid",
    model_name="model_uuid",  # Azure deployment UUID
    plugin_name="langchain_azure_test"
)

try:
    # OpenAI 모델 호출
    openai_resp = openai_llm.invoke("Hello from OpenAI via LangChain!")
    print("OpenAI Response:", openai_resp.content)

    # Azure 모델 호출 (동일한 인터페이스!)
    azure_resp = azure_llm.invoke("Hello from Azure via LangChain!")
    print("Azure Response:", azure_resp.content)

    # OpenAI 스트리밍
    print("OpenAI Stream:")
    for chunk in openai_llm.stream("Tell me a short story"):
        if chunk.content:
            print(chunk.content, end="", flush=True)
    print("\n")

    # Azure 스트리밍
    print("Azure Stream:")
    for chunk in azure_llm.stream("Count to 3"):
        if chunk.content:
            print(chunk.content, end="", flush=True)
    print("\n")

    # 비동기 호출 예시
    async def async_langchain_example():
        # 비동기 OpenAI 호출
        openai_async_resp = await openai_llm.ainvoke("Async OpenAI LangChain!")
        print("Async OpenAI:", openai_async_resp.content)

        # 비동기 Azure 호출
        azure_async_resp = await azure_llm.ainvoke("Async Azure LangChain!")
        print("Async Azure:", azure_async_resp.content)

        # 비동기 스트리밍
        print("Async OpenAI Stream:")
        async for chunk in openai_llm.astream("Async streaming test"):
            if chunk.content:
                print(chunk.content, end="", flush=True)
        print("\n")

    # 비동기 함수 실행
    import asyncio
    asyncio.run(async_langchain_example())

finally:
    # 리소스 정리
    openai_llm.close()
    azure_llm.close()

# 임베딩 예시 (OpenAI/Azure 모두 동일한 클래스 사용)
openai_embedding = OasisOpenAIEmbedding(
    account_id="your_account_id",
    user_uuid="your_uuid",
    workspace_uuid="your_workspace_uuid",
    tenant_uuid="your_tenant_uuid",
    model_name="model_uuid",  # 임베딩 모델 UUID (OpenAI/Azure 공통)
    plugin_name="langchain_embedding_test"
)

try:
    # 동기 임베딩 (여러 문서)
    vectors = openai_embedding.embed_documents([
        "First document for embedding",
        "Second document for embedding",
        "Third document with different content"
    ])
    print(f"Embedded {len(vectors)} documents, vector dimension: {len(vectors[0])}")

    # 동기 임베딩 (단일 쿼리)
    query_vector = openai_embedding.embed_query("What was the main topic?")
    print(f"Query vector dimension: {len(query_vector)}")

    # 비동기 임베딩
    async def async_embedding_example():
        async_vectors = await openai_embedding.aembed_documents([
            "Async embedding test document"
        ])
        print(f"Async embedded vector dimension: {len(async_vectors[0])}")

    asyncio.run(async_embedding_example())

finally:
    # 리소스 정리
    await openai_embedding.aclose()
```

## 3. 모범 사례

### 3.1 리소스 관리

**권장: Context Manager 사용**

```python
# 동기 클라이언트
with OasisOpenAI(...) as client:
    # 작업 수행
    resp = client.chat.completions.create(...)

# 비동기 클라이언트
async with OasisAsyncOpenAI(...) as client:
    # 작업 수행
    resp = await client.chat.completions.create(...)
```

**수동 리소스 관리**

```python
# 동기
client = OasisOpenAI(...)
try:
    # 작업 수행
    resp = client.chat.completions.create(...)
finally:
    client.close()

# 비동기
client = OasisAsyncOpenAI(...)
try:
    # 작업 수행
    resp = await client.chat.completions.create(...)
finally:
    await client.aclose()
```

### 3.2 스트리밍 처리

```python
# 동기 스트리밍
with OasisOpenAI(...) as client:
    stream = client.chat.completions.create(
        model="model_id",
        messages=[...],
        stream=True
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

# 비동기 스트리밍
async with OasisAsyncOpenAI(...) as client:
    stream = await client.chat.completions.create(
        model="model_id",
        messages=[...],
        stream=True
    )
    async for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
```

### 3.3 에러 핸들링

```python
from oasis.sdk.openai import OasisOpenAI
from openai import OpenAIError

with OasisOpenAI(...) as client:
    try:
        resp = client.chat.completions.create(
            model="model_id",
            messages=[{"role": "user", "content": "Hello"}]
        )
    except OpenAIError as e:
        print(f"OpenAI API 에러: {e}")
    except Exception as e:
        print(f"기타 에러: {e}")
```

## 4. 의존성

- Python 3.11.x
- openai 1.97.0
- langchain-openai 0.3.28

## 5. 테스트

```bash
# 테스트 실행
python -m pytest tests/

# 특정 테스트만 실행
python -m pytest tests/test_oasis_openai.py
python -m pytest tests/test_oasis_azure.py
python -m pytest tests/test_oasis_lc_openai.py
python -m pytest tests/test_oasis_lc_azure.py
```

**노트북 예시**

실제 사용 예시는 `tests/notebooks/` 디렉토리의 Jupyter 노트북을 참고하세요:

- `openai.ipynb`: 통합 SDK 래퍼를 사용한 OpenAI 모델 예시
- `azure.ipynb`: 통합 SDK 래퍼를 사용한 Azure OpenAI 모델 예시
- `api.ipynb`: API 레벨 사용 예시
