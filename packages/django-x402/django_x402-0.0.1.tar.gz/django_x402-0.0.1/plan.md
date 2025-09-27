Totally doable. Here’s a concrete, end-to-end plan to add x402 to a Django app, with pointers to the relevant docs/spec.

# Implementation plan

## 0) Prereqs & packages

* **Install Django 5.2+** (we’ll rely on new-style/async-aware middleware patterns). ([Django Project][1])
* **Install the x402 Python package** (gives types, helpers like base64 decoding, requirement matching, and a facilitator client).

  ```bash
  pip install x402
  ```

  If you prefer to inspect/track the reference implementation, the canonical repo is here. ([PyPI][2])

## 1) Choose where to enforce payment

* Identify the URL prefixes you want to monetize (e.g., `/api/premium/`, `/v1/infer/`).
* Put the x402 middleware **after** auth/session middleware (if you need user info) and **before** things that might mutate the body/headers you care about. Order matters in Django. ([Django Project][3])

## 2) New-style Django middleware skeleton

* Use **new-style** middleware (`__init__(get_response)`, `__call__(request)`), not `MiddlewareMixin`.
* If you plan to call networked services (facilitator), decide if you want a **sync** or **async** path and mark `async_capable` accordingly to avoid unnecessary adaptation overhead. ([Django Project][3])

**Docs:** *How to write middleware* & *async support*. ([Django Project][3])

## 3) Config in `settings.py`

Add a block the middleware can read at startup:

```python
X402 = {
  "paths": ["/api/premium/"],        # prefixes to protect
  "network": "base-sepolia",         # start on testnet
  "price": "$0.01",                  # or a tokenAmount object supported by x402
  "pay_to_address": "0xYourAddress",
  "mime_type": "application/json",
  "description": "Premium API call",
  "max_deadline_seconds": 60,
  "discoverable": True,              # browser HTML paywall support
  "output_schema": {"type": "json"}, # optional response hints in 402 body
  # Optional: custom facilitator; otherwise default hosted facilitator is used
  # "facilitator_config": {"base_url": "https://<your-facilitator>"}
}
```

The **x402 Python package** provides helpers to turn a human price into atomic units + asset metadata for the chosen network. ([PyPI][2])

## 4) Build the **Payment Requirements** per request

For each protected request:

* Construct an `accepts` array with one (or more) **paymentRequirements** objects, setting:

  * `scheme: "exact"`
  * `network` (e.g., `base-sepolia` for test)
  * `asset` & `max_amount_required` (derived from your configured `price`)
  * `resource` = `request.build_absolute_uri()` (the exact URL being purchased)
  * `description`, `mime_type`, `pay_to`, `max_timeout_seconds`
  * Optional: `output_schema` (input/output hints) and `extra` for EIP-712/domain data
* The shape and field names are defined by the x402 spec and mirrored in the Python SDK types. ([GitHub][4])

## 5) Inbound flow

1. **Detect coverage**: if `request.path` matches a protected prefix and the request lacks `X-PAYMENT` → return **HTTP 402** with the **x402 Payment Required** body.

   * For **API clients**, return JSON: `{ x402Version, accepts, error }`.
   * For **browsers**, you may return an HTML paywall (SDK helpers exist).
     The status/body shape is in the protocol and seller quickstart. ([Coinbase Developer Docs][5])
2. **If `X-PAYMENT` present**:

   * Base64-decode JSON to a `PaymentPayload` (SDK includes a safe decoder).
   * Ensure the payload matches one of your `paymentRequirements` (SDK function provided).
   * **Verify** by calling the facilitator `/verify` with `{ x402Version, paymentHeader, paymentRequirements }`.
   * If invalid → return 402 again with `error` populated.
     The **facilitator contract** for `/verify` (and later `/settle`) is documented here. ([GitHub][4])

## 6) Outbound flow (after view runs)

* Call **`/settle`** on the facilitator **only when** your view returns a 2xx.
* If settlement succeeds, attach **`X-PAYMENT-RESPONSE`** header to your outgoing response; the value is **base64-encoded JSON** of the facilitator settle result.
* If your view returns a **streaming** response, avoid touching `response.content`; just set the header. ([GitHub][4])

**Protocol flow overview** (verify → fulfill → settle) is described in Coinbase docs. ([Coinbase Developer Docs][6])

## 7) Sync vs Async (performance)

* If your app runs under ASGI and your facilitator client supports **async**, implement an async `__call__` and mark `async_capable = True`.
* Otherwise, keep calls sync; Django will adapt, but at a small performance cost. ([Django Project][7])

## 8) Error handling & edge cases

* **Invalid/missing header** → 402 with `error`.
* **Verify failed** → 402 with `invalidReason` surfaced in `error`.
* **Settle failed** → you can either (a) log and still return 2xx (non-blocking), or (b) convert to 402/5xx based on your business rule.
* **Streaming responses** → don’t read/modify body.
* **Middleware exceptions** → let them bubble; Django will format downstream unless you implement `process_exception`. ([Django Project][3])

## 9) Security & correctness check-list

* **Network/asset pinning**: reject payments on unexpected networks/assets for your SKU. ([GitHub][4])
* **Amount bound**: enforce `max_amount_required` (protocol allows you to define exact/upto schemes). ([GitHub][4])
* **Deadline/timeout**: honor `max_timeout_seconds` to limit payment windows. ([GitHub][4])
* **Replay protection**: cache a hash of validated `X-PAYMENT` for a short TTL to avoid double-settles on retries. (Best practice; protocol-compatible.)
* **Idempotency**: if your view is not idempotent, consider settling before side-effects or wrap with your own idempotency key.

## 10) Local/testnet setup

* Start on **Base Sepolia** (testnet). Coinbase’s quickstart walks through end-to-end test configuration and moving to mainnet later. ([Coinbase Developer Docs][5])
* If you don’t want to run infra, use a **hosted facilitator** (documented purpose/contract). ([Coinbase Developer Docs][8])

## 11) Observability

* Log: request path, payment hash (not full payload), verify/settle durations, decisions (402 vs 2xx), settle tx hash.
* Consider metrics for verify/settle success rates & latencies.

## 12) Tests

* **Unit tests**:

  * Missing header → 402 JSON body with correct `accepts`.
  * Bad header (bad base64, wrong network/asset) → 402 with `error`.
  * Valid header → view executes; on 2xx, `X-PAYMENT-RESPONSE` set.
* **Integration tests**: stub facilitator `/verify` and `/settle` (or use the hosted test endpoints) and assert full flow.
* Use Django’s test client + responses/httpretty or httpx mocks for facilitator calls. (General guidance: Django testing docs; facilitator contract in x402 docs.) ([Django Project][3])

## 13) Reference code to crib from

* **Official repo** – protocol, facilitator endpoints, and example middleware logic (FastAPI) that you can port 1:1 to Django. ([GitHub][4])
* **FastAPI middleware tutorial** (for understanding their flow you’re porting). ([FastAPI][9])
* **Third-party examples** (FastAPI one-liner, community SDKs) if you want to compare shapes. ([GitHub][10])

# Minimal task breakdown

1. **Wire config** (`X402` in `settings.py`) and add middleware class to `MIDDLEWARE`. ([Django Project][3])
2. **Implement middleware**:

   * Match protected paths.
   * Build `paymentRequirements` per request.
   * If no/invalid `X-PAYMENT` → 402 (`x402Version`, `accepts`, `error`), JSON or HTML.
   * If present → decode, match, **/verify**; on success stash context.
   * Call view → on 2xx, **/settle** and set `X-PAYMENT-RESPONSE`. ([GitHub][4])
3. **Add async capability** if your stack is ASGI and facilitator client supports it. ([Django Project][7])
4. **Tests**: unit + integration as above.
5. **Rollout**: start with one endpoint on **Base Sepolia**, monitor, then expand and flip to mainnet. ([Coinbase Developer Docs][5])

---

## Core references (keep handy)

* **Django 5.2 – Middleware (how to write/use):** middleware guide & async support. ([Django Project][3])
* **x402 protocol + repo:** spec, `/verify` & `/settle` shape, examples. ([GitHub][4])
* **x402 Python package (SDK):** helpers, types, facilitator client. ([PyPI][2])
* **Coinbase docs – “How x402 works” + Facilitator + Seller quickstart:** end-to-end flow, responsibilities, testnet→mainnet. ([Coinbase Developer Docs][6])

If you want, I can drop in a production-ready `X402Middleware` (new-style) with sync/async paths and a tiny test module you can paste into your repo.

[1]: https://docs.djangoproject.com/en/5.2/releases/5.2/?utm_source=chatgpt.com "Django 5.2 release notes"
[2]: https://pypi.org/project/x402/?utm_source=chatgpt.com "x402 Python"
[3]: https://docs.djangoproject.com/en/5.2/topics/http/middleware/?utm_source=chatgpt.com "Middleware | Django documentation"
[4]: https://github.com/coinbase/x402?utm_source=chatgpt.com "coinbase/x402: A payments protocol for the internet. Built on HTTP."
[5]: https://docs.cdp.coinbase.com/x402/quickstart-for-sellers?utm_source=chatgpt.com "Quickstart for Sellers - Coinbase Developer Documentation"
[6]: https://docs.cdp.coinbase.com/x402/core-concepts/how-it-works?utm_source=chatgpt.com "How x402 Works - Coinbase Developer Documentation"
[7]: https://docs.djangoproject.com/en/5.2/topics/async/?utm_source=chatgpt.com "Asynchronous support | Django documentation"
[8]: https://docs.cdp.coinbase.com/x402/core-concepts/facilitator?utm_source=chatgpt.com "Facilitator - Coinbase Developer Documentation"
[9]: https://fastapi.tiangolo.com/tutorial/middleware/?utm_source=chatgpt.com "Middleware"
[10]: https://github.com/jordo1138/fastapi-x402/?utm_source=chatgpt.com "jordo1138/fastapi-x402: One-liner cryptocurrency ..."
